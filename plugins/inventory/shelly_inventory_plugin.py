from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.plugins.inventory import AnsibleError
import requests
import re

DOCUMENTATION = r'''
        name: denismaggior8.shelly_collection.shelly_inventory_plugin
        plugin_type: inventory
        short_description: Returns a dynamic host inventory from Shelly Cloud
        description: Returns a dynamic host inventory using Shelly Cloud REST API
        options:
            plugin:
                description: Name of the plugin
                required: true
                choices: ['denismaggior8.shelly_collection.shelly_inventory_plugin']
            auth_key:
                description: Shelly Cloud auth key
                required: true
            url_prefix:
                description: The REST API URL prefix to be prepended to '.shelly.cloud' (i.e. shelly-6-eu)
                required: true
    '''

class InventoryModule(BaseInventoryPlugin):

    NAME = 'denismaggior8.shelly_collection.shelly_inventory_plugin'

    def __init__(self):
        super(InventoryModule, self).__init__()
        self.plugin = None
        self.auth_key = None
        self.url_prefix = None

    def verify_file(self, path: str):
        if super(InventoryModule, self).verify_file(path):
            return path.endswith('yaml') or path.endswith('yml')
        return False

    def parse(self, inventory, loader, path, cache):
        # Initialize base class
        super(InventoryModule, self).parse(inventory, loader, path, cache)

        # Read the inventory YAML file
        self._read_config_data(path)

        try:
           # Store the options from the YAML file
           self.auth_key = self.get_option('auth_key')
           self.url_prefix = self.get_option('url_prefix')
           self.api_url = "https://{}.shelly.cloud/interface/device/list?auth_key={}".format(self.url_prefix,self.auth_key)
        except KeyError as e:
            raise AnsibleParserError('All correct options required: {}'.format(e))
        
        try:
            response = requests.get(self.api_url)
        except Exception as e:
            raise AnsibleError('An error occured invoking Shelly Cloud REST API: {}'.format(e))
        
        response = response.json()

        if response['isok'] == True and response['data']['devices'] != None:
            devices = response['data']['devices']
            for key in devices.keys():
                # Creating groups
                self.inventory.add_group(re.sub(r"[-.]", "", "type_{}".format(devices[key]['type']).lower()))
                self.inventory.add_group(re.sub(r"[-.]", "", "gen_{}".format(devices[key]['gen'])))
                self.inventory.add_group(re.sub(r"[-.]", "", "category_{}".format(devices[key]['category'])))
                self.inventory.add_group("cloud_online_{}".format(devices[key].get('cloud_online', 'na')).lower())
                self.inventory.add_group(re.sub(r"[-.]", "", "room_id_{}".format(devices[key]['room_id']).lower()))

                # Assigning hosts to groups
                if(isinstance(devices[key].get('ip'), str)):
                    self.inventory.add_host(host=devices[key]['ip'],group=re.sub(r"[-.]", "","type_{}".format(devices[key]['type']).lower()))
                    self.inventory.add_host(host=devices[key]['ip'],group=re.sub(r"[-.]", "","gen_{}".format(devices[key]['gen'])))
                    self.inventory.add_host(host=devices[key]['ip'],group="cloud_online_{}".format(devices[key].get('cloud_online', 'na')).lower())
                    self.inventory.add_host(host=devices[key]['ip'],group=re.sub(r"[-.]", "","room_id_{}".format(devices[key]['room_id']).lower()))
                else:
                    AnsibleError("The entry '{}' does not have an ip".format(key))
        else:
            raise AnsibleError('The response from Shelly Cloud is not ok, unable to add hosts into inventory...')

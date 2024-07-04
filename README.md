# Ansible Collection - denismaggior8.shelly_collection

To install collection from this git repo:

```console
$ git clone https://github.com/denismaggior8/shelly_collection
$ ansible-galaxy collection install shelly_collection
```

To uninstall the collection:

```console
$ rm -rf ~/.ansible/collections/ansible_collections/denismaggior8/shelly_collection/
```

## Inventorty plugin 

Verify if the inventory plugin is installed:

```console
$ ansible-doc -t inventory -l 2> /dev/null | grep shelly
```

Create the plugin configuration file (make sure you substitute the placeholders marked with \<\> with actual values):

```console
$ cat << 'EOF' > shelly_inventory_plugin.yaml
---
plugin: shelly_inventory_plugin
auth_key: <YOUR SHELLY CLOUD AUTHENTICATION KEY>
url_prefix: <YOUR SHELLY CLOUD REST API PREFIX (i.e. shelly-6-eu)>
EOF 
```

Test the inventory plugin:

```console
$ ansible-inventory --inventory $PWD/shelly_inventory_plugin.yaml --list -v -v -v
```

An inventory JSON file containing all your Shelly devices should appear.
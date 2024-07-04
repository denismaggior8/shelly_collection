# Ansible Collection - denismaggior8.shelly_collection

## Prerequisites

- ansible core 2.17.0
- python 3.11.0

# Installation and removal

To install this collection from its GitHub repo:

```console
$ git clone https://github.com/denismaggior8/shelly_collection
$ ansible-galaxy collection install shelly_collection
```

To uninstall this collection:

```console
$ rm -rf ~/.ansible/collections/ansible_collections/denismaggior8/shelly_collection/
```

## Inventory plugin 

Verify if the inventory plugin is installed:

```console
$ ansible-doc -t inventory -l 2> /dev/null | grep shelly
```

Create the plugin configuration file (make sure you substitute the placeholders marked with \<\> with actual values):

```console
$ cat << 'EOF' > shelly_inventory_plugin.yaml
---
plugin: denismaggior8.shelly_collection.shelly_inventory_plugin
auth_key: <YOUR SHELLY CLOUD AUTHENTICATION KEY>
url_prefix: <YOUR SHELLY CLOUD REST API PREFIX (i.e. shelly-6-eu)>
EOF 
```

Test the inventory plugin:

```console
$ ansible-inventory --inventory $PWD/shelly_inventory_plugin.yaml --list -v -v -v
```

An inventory JSON file containing all your Shelly devices (grouped by category, type, room_id, etc) should appear.
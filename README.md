# Ansible Collection - denismaggior8.shelly_collection

Documentation for the collection.



## Inventorty plugin 


```console
$ export ANSIBLE_INVENTORY_PLUGINS=$DEFAULT_INVENTORY_PLUGIN_PATH:$(pwd)
```

```console
$ ansible-doc -t inventory -l 2> /dev/null | grep shelly
```

```console
$ ansible-inventory --inventory $PWD/shelly_inventory_plugin.yaml --list -v -v -v
```

```console
$ cat << 'EOF' > shelly_inventory_plugin.yaml
---
plugin: shelly_inventory_plugin
auth_key: <YOUR SHELLY CLOUD AUTHENTICATION KEY>
url_prefix: <YOUR SHELLY CLOUD REST API PREFIX (i.e. shelly-6-eu)>
EOF 
```
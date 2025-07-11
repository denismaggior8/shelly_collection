from ansible.module_utils.basic import to_text
from ansible.errors import AnsibleConnectionFailure
from ansible.plugins.httpapi import HttpApiBase
from ansible.module_utils.connection import ConnectionError


class HttpApi(HttpApiBase):
    def set_become(self, become_context):
        """As this is an http rpc call there is no elevation available
        """
        pass

    def update_auth(self, response, response_text):
        return None

    def login(self, username, password):
        pass

    def logout(self):
        pass

    def api_version(self):
        pass

    def send_request(self, data=None, request_method="POST", path="/api_jsonrpc.php"):
        print(data)
from evolution_api_sdk.models import InstanceConfig, PresenceConfig, PresenceStatus
from typing import Union, Dict, Any


class InstanceService:
    def __init__(self, client):
        self.client = client

    def fetch_instances(self, instance_name: str = None):
        if instance_name:
            param = {'instanceName': instance_name}
        else:
            param = None
        url = 'instance/fetchInstances/'
        return self.client.get(url, params=param)

    def remove_instance(self, instance_name: str):
        url = f'instance/delete/{instance_name}'
        return self.client.delete(url)

    def create_instance(self, config: Union[InstanceConfig, Dict[str, Any]]):
        if hasattr(config, 'to_dict'):
            data = config.to_dict()
        else:
            data = config
        return self.client.post('instance/create', data=data)

    def connect_instance(self, instance_name: str):
        return self.client.get(f'instance/connect/{instance_name}')

    def status_instance(self, instance_name: str):
        return self.client.get(f'instance/connectionState/{instance_name}')

    def logout_instance(self, instance_name: str):
        return self.client.delete(f'instance/logout/{instance_name}')

    def set_presence(self, instance_name: str, presence: PresenceStatus):
        config = PresenceConfig(presence)
        return self.client.post(
            f'instance/setPresence/{instance_name}',
            data=config.__dict__,
        )

    def restart_instance(self, instance_name: str):
        return self.client.post(f'instance/restart/{instance_name}')

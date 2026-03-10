import pytest
from evolution_api_sdk.client import EvolutionClient
from evolution_api_sdk.models.instance import InstanceConfig, WebhookConfig


# =====================
# Fixtures
# =====================


@pytest.fixture
def evolution_client(evolution_api_mock_server):
    return EvolutionClient(base_url=evolution_api_mock_server.base_url, api_token='mock-token')


# =====================
# Testes de Integração
# =====================


def test_create_instance_basic(evolution_client, evolution_api_mock_server):
    instance_name = 'test_instance_basic'

    config = InstanceConfig(instanceName=instance_name, qrcode=True, integration='WHATSAPP-BAILEYS')

    response = evolution_client.instance.create_instance(config)

    assert response['instance']['instanceName'] == instance_name
    assert response['instance']['integration'] == 'WHATSAPP-BAILEYS'
    assert response['hash'] == f'mock-hash-{instance_name}'
    assert response['qrcode'] == 'mock-qrcode'
    assert evolution_api_mock_server.created_instances[instance_name]['instanceName'] == instance_name

    delete_response = evolution_client.instance.remove_instance(instance_name)
    assert delete_response['status'] == 'deleted'
    assert delete_response['instanceName'] == instance_name
    assert instance_name in evolution_api_mock_server.deleted_instances
    assert instance_name not in evolution_api_mock_server.created_instances


def test_create_instance_with_webhook(evolution_client, evolution_api_mock_server):
    instance_name = 'test_instance_webhook'

    webhook = WebhookConfig(
        url='https://webhook.site/unique-id',
        byEvents=True,
        base64=False,
        events=['MESSAGES_UPSERT', 'CONNECTION_UPDATE'],
    )

    config = InstanceConfig(instanceName=instance_name, qrcode=True, integration='WHATSAPP-BAILEYS', webhook=webhook)

    response = evolution_client.instance.create_instance(config)

    assert response['instance']['instanceName'] == instance_name
    assert response['instance']['webhook'] == {
        'url': 'https://webhook.site/unique-id',
        'byEvents': True,
        'base64': False,
        'events': ['MESSAGES_UPSERT', 'CONNECTION_UPDATE'],
    }

    delete_response = evolution_client.instance.remove_instance(instance_name)
    assert delete_response['status'] == 'deleted'
    assert instance_name in evolution_api_mock_server.deleted_instances


def test_create_instance_with_settings(evolution_client, evolution_api_mock_server):
    instance_name = 'test_instance_advanced'

    config = InstanceConfig(
        instanceName=instance_name, qrcode=True, integration='WHATSAPP-BAILEYS', alwaysOnline=True, readMessages=True
    )

    response = evolution_client.instance.create_instance(config)

    assert response['instance']['instanceName'] == instance_name
    assert response['instance']['alwaysOnline'] is True
    assert response['instance']['readMessages'] is True

    delete_response = evolution_client.instance.remove_instance(instance_name)
    assert delete_response['status'] == 'deleted'
    assert instance_name in evolution_api_mock_server.deleted_instances


def test_create_instance_dict_format(evolution_client, evolution_api_mock_server):
    instance_name = 'test_instance_dict'

    config_dict = {'instanceName': instance_name, 'qrcode': True, 'integration': 'WHATSAPP-BAILEYS'}

    response = evolution_client.instance.create_instance(config_dict)

    assert response['instance'] == config_dict
    assert evolution_api_mock_server.created_instances[instance_name] == config_dict

    delete_response = evolution_client.instance.remove_instance(instance_name)
    assert delete_response['status'] == 'deleted'
    assert instance_name in evolution_api_mock_server.deleted_instances

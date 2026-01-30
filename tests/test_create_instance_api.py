import pytest
from evolution_api_sdk.client import EvolutionClient
from evolution_api_sdk.models.instance import InstanceConfig, WebhookConfig


# =====================
# Configs
# =====================

EVOLUTION_API_URL = ''
EVOLUTION_API_KEY = ''


# =====================
# Fixtures
# =====================

@pytest.fixture
def evolution_client():
    """Cria um cliente Evolution API para testes de integração"""
    return EvolutionClient(base_url=EVOLUTION_API_URL, api_token=EVOLUTION_API_KEY)


# =====================
# Testes de Integração
# =====================

def test_create_instance_basic(evolution_client):
    """Testa criação de instância básica sem webhook"""
    instance_name = "test_instance_basic"
    
    config = InstanceConfig(
        instanceName=instance_name,
        qrcode=True,
        integration="WHATSAPP-BAILEYS"
    )
    
    try:
        response = evolution_client.instance.create_instance(config)
        
        assert response is not None
        assert "instance" in response or "hash" in response or "qrcode" in response
        print(f"\n✅ Instância criada com sucesso: {instance_name}")
        print(f"Resposta: {response}")
        
    except Exception as e:
        print(f"\n❌ Erro ao criar instância: {e}")
        raise
    finally:
        try:
            evolution_client.instance.remove_instance(instance_name)
            print(f"🗑️  Instância {instance_name} removida após teste")
        except:
            pass


def test_create_instance_with_webhook(evolution_client):
    """Testa criação de instância com configuração de webhook"""
    instance_name = "test_instance_webhook"
    
    webhook = WebhookConfig(
        url="https://webhook.site/unique-id",
        byEvents=True,
        base64=False,
        events=["MESSAGES_UPSERT", "CONNECTION_UPDATE"]
    )
    
    config = InstanceConfig(
        instanceName=instance_name,
        qrcode=True,
        integration="WHATSAPP-BAILEYS",
        webhook=webhook
    )
    
    try:
        response = evolution_client.instance.create_instance(config)
        
        assert response is not None
        print(f"\n✅ Instância com webhook criada: {instance_name}")
        print(f"Resposta: {response}")
        
    except Exception as e:
        print(f"\n❌ Erro ao criar instância com webhook: {e}")
        raise
    finally:
        try:
            evolution_client.instance.remove_instance(instance_name)
            print(f"🗑️  Instância {instance_name} removida após teste")
        except:
            pass


def test_create_instance_with_settings(evolution_client):
    """Testa criação de instância com configurações avançadas"""
    instance_name = "test_instance_advanced"
    
    config = InstanceConfig(
        instanceName=instance_name,
        qrcode=True,
        integration="WHATSAPP-BAILEYS",
        alwaysOnline=True,
        readMessages=True
    )
    
    try:
        response = evolution_client.instance.create_instance(config)
        
        assert response is not None
        print(f"\n✅ Instância avançada criada: {instance_name}")
        print(f"Resposta: {response}")
        
    except Exception as e:
        print(f"\n❌ Erro ao criar instância avançada: {e}")
        raise
    finally:
        try:
            evolution_client.instance.remove_instance(instance_name)
            print(f"🗑️  Instância {instance_name} removida após teste")
        except:
            pass


def test_create_instance_dict_format(evolution_client):
    """Testa criação de instância usando dicionário ao invés de objeto"""
    instance_name = "test_instance_dict"
    
    config_dict = {
        "instanceName": instance_name,
        "qrcode": True,
        "integration": "WHATSAPP-BAILEYS"
    }
    
    try:
        response = evolution_client.instance.create_instance(config_dict)
        
        assert response is not None
        print(f"\n✅ Instância criada via dict: {instance_name}")
        print(f"Resposta: {response}")
        
    except Exception as e:
        print(f"\n❌ Erro ao criar instância via dict: {e}")
        raise
    finally:
        try:
            evolution_client.instance.remove_instance(instance_name)
            print(f"🗑️  Instância {instance_name} removida após teste")
        except:
            pass

# Evolution API SDK

<p align="center">
  <strong>SDK Python para integracao com a Evolution API (WhatsApp API)</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/license-Apache%202.0-green.svg" alt="Apache 2.0 License">
  <img src="https://img.shields.io/badge/version-0.1.0-orange.svg" alt="Version 0.1.0">
</p>

## Sobre

O **Evolution API SDK** facilita a integracao com a [Evolution API](https://doc.evolution-api.com/) em Python.
Com ele, voce consegue gerenciar instancias, configurar webhook na criacao da instancia e enviar mensagens (texto, midia por URL, PTV e audio narrado) com payloads tipados.

## Funcionalidades

- Autenticacao por token via `EvolutionClient`
- Gerenciamento de instancias (`fetch`, `create`, `connect`, `status`, `restart`, `logout`, `remove`)
- Controle de presenca (`available` e `unavailable`)
- Suporte a webhook no `InstanceConfig` com `WebhookConfig`
- Servico de mensagens com `MessageService`
  - envio de texto (`send_text`)
  - envio de midia por URL (`send_media_url`)
  - envio de PTV/video (`send_ptv`)
  - envio de audio narrado (`send_narrated_audio`)
- Modelos de mensagem com suporte a quoted/reply (`QuotedMessageConfig`)
- Excecoes de dominio (`EvolutionAPIError`, `EvolutionAuthenticationError`, `EvolutionNotFoundError`)

## Requisitos

- Python 3.9+
- [uv](https://github.com/astral-sh/uv) (recomendado)

## Instalacao

```bash
git clone https://github.com/juniorcarvalho/evolution-api-sdk.git
cd evolution-api-sdk
uv sync --dev
```

## Uso rapido

### Cliente

```python
from evolution_api_sdk import EvolutionClient

client = EvolutionClient(
    base_url='https://sua-evolution-api.com',
    api_token='seu_token_aqui',
)
```

### Instancias

```python
from evolution_api_sdk.models import InstanceConfig, WebhookConfig

# Listar todas as instancias
instances = client.instance.fetch_instances()

# Buscar instancia especifica
one = client.instance.fetch_instances(instance_name='minha_instancia')

# Criar instancia com webhook
config = InstanceConfig(
    instanceName='nova_instancia',
    integration='WHATSAPP-BAILEYS',
    qrcode=True,
    webhook=WebhookConfig(
        url='https://meu-sistema.com/webhook',
        byEvents=True,
        events=['MESSAGES_UPSERT'],
    ),
)
created = client.instance.create_instance(config)

# Conectar e verificar status
qrcode = client.instance.connect_instance('nova_instancia')
status = client.instance.status_instance('nova_instancia')

# Reiniciar, deslogar e remover
client.instance.restart_instance('nova_instancia')
client.instance.logout_instance('nova_instancia')
client.instance.remove_instance('nova_instancia')
```

### Presenca

```python
from evolution_api_sdk.models import PresenceStatus

client.instance.set_presence('minha_instancia', PresenceStatus.AVAILABLE)
client.instance.set_presence('minha_instancia', PresenceStatus.UNAVAILABLE)
```

### Mensagens

```python
from evolution_api_sdk.models import (
    QuotedContentConfig,
    QuotedKeyConfig,
    QuotedMessageConfig,
    SendMediaUrlMessageConfig,
    SendNarratedAudioMessageConfig,
    SendPtvMessageConfig,
    SendTextMessageConfig,
)

instance_name = 'minha_instancia'

# 1) Texto
text_payload = SendTextMessageConfig(
    number='5511999999999@s.whatsapp.net',
    text='Ola! Esta e uma mensagem de teste.',
)
client.message.send_text(instance_name, text_payload)

# 2) Texto com quoted/reply
quoted_payload = SendTextMessageConfig(
    number='5511999999999@s.whatsapp.net',
    text='Respondendo sua mensagem.',
    quoted=QuotedMessageConfig(
        key=QuotedKeyConfig(id='MESSAGE_ID'),
        message=QuotedContentConfig(conversation='Mensagem original'),
    ),
)
client.message.send_text(instance_name, quoted_payload)

# 3) Midia por URL
media_payload = SendMediaUrlMessageConfig(
    number='5511999999999',
    mediatype='image',
    media='https://s3.amazonaws.com/bucket/image.png',
    caption='Legenda da imagem',
)
client.message.send_media_url(instance_name, media_payload)

# 4) PTV
ptv_payload = SendPtvMessageConfig(
    number='5511999999999',
    video='https://evolution-api.com/files/video.mp4',
)
client.message.send_ptv(instance_name, ptv_payload)

# 5) Audio narrado
audio_payload = SendNarratedAudioMessageConfig(
    number='5511999999999',
    audio='https://evolution-api.com/files/narratedaudio.mp3',
    encoding=True,
)
client.message.send_narrated_audio(instance_name, audio_payload)
```

## Referencia rapida

### `InstanceService`

| Metodo | Descricao |
|---|---|
| `fetch_instances(instance_name=None)` | Lista todas as instancias ou uma instancia especifica |
| `create_instance(config)` | Cria nova instancia (dict ou `InstanceConfig`) |
| `connect_instance(instance_name)` | Conecta instancia e retorna dados do QR Code |
| `status_instance(instance_name)` | Retorna estado da conexao |
| `restart_instance(instance_name)` | Reinicia a instancia |
| `logout_instance(instance_name)` | Desloga a instancia |
| `remove_instance(instance_name)` | Remove a instancia |
| `set_presence(instance_name, presence)` | Define presenca (`PresenceStatus`) |

### `MessageService`

| Metodo | Endpoint Evolution API |
|---|---|
| `send_text(instance_name, payload)` | `message/sendText/{instance_name}` |
| `send_media_url(instance_name, payload)` | `message/sendMedia/{instance_name}` |
| `send_ptv(instance_name, payload)` | `message/sendPtv/{instance_name}` |
| `send_narrated_audio(instance_name, payload)` | `message/sendWhatsAppAudio/{instance_name}` |

> Os metodos aceitam payload como `dict` ou como modelos tipados em `evolution_api_sdk.models`.

## Tratamento de erros

```python
from evolution_api_sdk.exception import (
    EvolutionAPIError,
    EvolutionAuthenticationError,
    EvolutionNotFoundError,
)

try:
    client.instance.fetch_instances()
except EvolutionAuthenticationError:
    print('Falha de autenticacao: verifique seu token')
except EvolutionNotFoundError:
    print('Recurso nao encontrado')
except EvolutionAPIError as exc:
    print(f'Erro na API: {exc}')
```

## Testes e qualidade

```bash
uv run ruff format .
uv run ruff check .
uv run mypy evolution_api_sdk
uv run pytest
```

## Estrutura do projeto

```text
evolution_api_sdk/
├── evolution_api_sdk/
│   ├── client.py
│   ├── exception.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── instance.py
│   │   └── message.py
│   └── service/
│       ├── __init__.py
│       ├── instance.py
│       ├── message.py
│       └── webhook.py
├── tests/
├── pyproject.toml
├── README.md
└── LICENSE
```

## Licenca

Este projeto esta licenciado sob a **Apache License 2.0**.
Consulte o arquivo [LICENSE](LICENSE).

## Links uteis

- [Evolution API - Documentacao](https://doc.evolution-api.com/)
- [Evolution API - GitHub](https://github.com/EvolutionAPI/evolution-api)

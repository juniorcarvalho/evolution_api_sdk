# Evolution API SDK

<p align="center">
  <strong>SDK Python para integração com a Evolution API - WhatsApp API</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/version-0.1.0-orange.svg" alt="Version 0.1.0">
  <img src="https://img.shields.io/badge/tests-9%20passed-brightgreen.svg" alt="Tests Passed">
  <img src="https://img.shields.io/badge/coverage-54%25-yellow.svg" alt="Coverage 54%">
</p>

## 📋 Sobre

O **Evolution API SDK** é uma biblioteca Python que facilita a integração com a [Evolution API](https://doc.evolution-api.com/), uma API poderosa para automação e gerenciamento do WhatsApp. Com este SDK, você pode facilmente criar instâncias, enviar mensagens, gerenciar webhooks e muito mais, tudo de forma programática.

## ✨ Funcionalidades

- 🔐 **Autenticação simples** - Configuração rápida com token de API
- 📱 **Gerenciamento de instâncias** - Criar, conectar, desconectar e remover instâncias
- 🔄 **Status de conexão** - Verificar estado da conexão em tempo real
- 🟢 **Gerenciamento de presença** - Configurar status online/offline
- 🔗 **Webhooks** - Configuração de webhooks para receber eventos
- ⚠️ **Tratamento de erros** - Exceções personalizadas para diferentes cenários

## 📋 Requisitos

- Python 3.9 ou superior
- [UV](https://github.com/astral-sh/uv) (recomendado) ou pip

## 📦 Instalação

### Usando UV (Recomendado)

```bash
# Clonar o repositório
git clone https://github.com/juniorcarvalho/evolution-api-sdk.git
cd evolution-api-sdk

# Instalar dependências com UV
uv sync

# Instalar com dependências de desenvolvimento
uv sync --dev
```


### Instalação para Desenvolvimento

```bash
# Clonar o repositório
git clone https://github.com/juniorcarvalho/evolution-api-sdk.git
cd evolution-api-sdk

# Criar ambiente virtual com UV
uv venv

# Ativar ambiente virtual
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate     # Windows

# Instalar dependências de desenvolvimento
uv sync --dev
```

## 🚀 Uso Rápido

### Configuração Inicial

```python
from evolution_api_sdk import EvolutionClient

# Inicializar o cliente
client = EvolutionClient(
    base_url="https://sua-evolution-api.com",
    api_token="seu_token_aqui"
)
```

### Gerenciamento de Instâncias

```python
# Listar todas as instâncias
instances = client.instance.fetch_instances()
print(instances)

# Buscar instância específica
instance = client.instance.fetch_instances(instance_name="minha_instancia")

# Criar nova instância
config = {
    "instanceName": "nova_instancia",
    "qrcode": True,
    "integration": "WHATSAPP-BAILEYS"
}
nova_instancia = client.instance.create_instance(config)

# Conectar instância (gera QR Code)
qrcode = client.instance.connect_instance("nova_instancia")

# Verificar status da conexão
status = client.instance.status_instance("nova_instancia")
print(status)

# Reiniciar instância
client.instance.restart_instance("nova_instancia")

# Desconectar instância
client.instance.logout_instance("nova_instancia")

# Remover instância
client.instance.remove_instance("nova_instancia")
```

### Gerenciamento de Presença

```python
from evolution_api_sdk.models import PresenceStatus

# Definir como disponível
client.instance.set_presence("minha_instancia", PresenceStatus.AVAILABLE)

# Definir como indisponível
client.instance.set_presence("minha_instancia", PresenceStatus.UNAVAILABLE)
```

## 📖 Documentação

### Classes Principais

#### `EvolutionClient`

Cliente principal para interação com a Evolution API.

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `base_url` | `str` | URL base da Evolution API |
| `api_token` | `str` | Token de autenticação da API |

#### `InstanceService`

Serviço para gerenciamento de instâncias.

| Método | Descrição |
|--------|-----------|
| `fetch_instances(instance_name=None)` | Lista instâncias (todas ou específica) |
| `create_instance(config)` | Cria nova instância |
| `connect_instance(instance_name)` | Conecta instância e retorna QR Code |
| `status_instance(instance_name)` | Retorna status da conexão |
| `logout_instance(instance_name)` | Desconecta instância |
| `remove_instance(instance_name)` | Remove instância |
| `restart_instance(instance_name)` | Reinicia instância |
| `set_presence(instance_name, presence)` | Define status de presença |

### Modelos

#### `InstanceConfig`

Configuração para criação de instâncias.

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `instanceName` | `str` | Nome da instância (obrigatório) |
| `integration` | `str` | Tipo de integração (ex: "WHATSAPP-BAILEYS") |
| `businessId` | `str` | ID do negócio |
| `token` | `str` | Token personalizado |
| `number` | `str` | Número de telefone |
| `qrcode` | `bool` | Gerar QR Code automaticamente |
| `rejectCall` | `bool` | Rejeitar chamadas recebidas |
| `msgCall` | `str` | Mensagem ao rejeitar chamadas |
| `groupsIgnore` | `bool` | Ignorar grupos |
| `alwaysOnline` | `bool` | Manter sempre online |
| `readMessages` | `bool` | Marcar mensagens como lidas |
| `readStatus` | `bool` | Visualizar status |
| `syncFullHistory` | `bool` | Sincronizar histórico completo |

```python
from evolution_api_sdk.models import InstanceConfig

config = InstanceConfig(
    instanceName="minha_instancia",
    integration="WHATSAPP-BAILEYS",
    qrcode=True,
    rejectCall=False,
    alwaysOnline=True
)
```

#### `PresenceStatus`

Enum para status de presença.

```python
from evolution_api_sdk.models import PresenceStatus

PresenceStatus.AVAILABLE    # Disponível
PresenceStatus.UNAVAILABLE  # Indisponível
```

### Tratamento de Erros

O SDK possui exceções personalizadas para diferentes cenários:

```python
from evolution_api_sdk.exception import (
    EvolutionAPIError,
    EvolutionAuthenticationError,
    EvolutionNotFoundError
)

try:
    client.instance.fetch_instances()
except EvolutionAuthenticationError:
    print("Erro de autenticação - verifique seu token")
except EvolutionNotFoundError:
    print("Recurso não encontrado")
except EvolutionAPIError as e:
    print(f"Erro na API: {e}")
```

## 🧪 Testes

O SDK possui testes unitários abrangentes utilizando pytest e mocks.

### Executando os Testes

```bash
# Rodar todos os testes
uv run pytest

# Rodar com cobertura
uv run pytest --cov=src

# Rodar com cobertura detalhada
uv run pytest --cov=src --cov-report=term-missing

# Rodar testes específicos
uv run pytest tests/test_client.py -v
```

### Verificação de Código

```bash
# Linting com Ruff
uv run ruff check .

# Formatação com Ruff
uv run ruff format .

# Verificação de tipos com MyPy
uv run mypy src
```

## 📁 Estrutura do Projeto

```
evolution-api-sdk/
├── src/                         # Código fonte principal
│   ├── __init__.py              # Exportações principais
│   ├── client.py                # Cliente principal da API
│   ├── exception.py             # Exceções personalizadas
│   ├── models/
│   │   ├── __init__.py          # Exportações dos modelos
│   │   └── instance.py          # Modelos de instância e presença
│   └── service/
│       ├── __init__.py
│       ├── instance.py          # Serviço de instâncias
│       └── webhook.py           # Serviço de webhooks
├── tests/                       # Testes unitários
│   ├── __init__.py
│   ├── test_client.py           # Testes do cliente HTTP
│   └── test_service_instance.py # Testes do serviço de instâncias
├── pyproject.toml               # Configuração do projeto
├── README.md                    # Documentação
└── LICENSE                      # Licença MIT
```

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova feature'`)
4. Envie para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

### Padrões de Código

- Use `ruff` para linting e formatação
- Escreva testes para novas funcionalidades
- Mantenha a documentação atualizada
- Siga as convenções de código Python (PEP 8)

## 📄 Licença
Este projeto é licenciado sob a Apache License, Version 2.0.

Copyright 2026 Júnior Carvalho

Você pode usar, modificar e distribuir este software, inclusive para fins comerciais, desde que cumpra os termos da licença.

O software é fornecido "AS IS", sem garantias de qualquer tipo.

https://www.apache.org/licenses/LICENSE-2.0

O texto completo da licença está disponível no arquivo [LICENSE](LICENSE).

## 🔗 Links Úteis

- [Evolution API Documentação](https://doc.evolution-api.com/)
- [Evolution API GitHub](https://github.com/EvolutionAPI/evolution-api)

---

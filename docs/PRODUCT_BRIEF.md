# Product Brief: Evolution API SDK

## 1. Project overview
Evolution API SDK is a Python library that streamlines integration with Evolution API (WhatsApp API). It provides a simple, typed client for managing WhatsApp instances, sending messages, and handling webhooks without requiring teams to build low-level HTTP integrations from scratch.

## 2. Target audience
- Python developers building WhatsApp automation workflows
- Backend teams integrating WhatsApp messaging into products or internal tools
- Technical teams that need reliable instance lifecycle and webhook management

## 3. Primary benefits / features
- Fast setup with token-based authentication and a centralized `EvolutionClient`
- Instance lifecycle operations: create, connect, status, restart, logout, remove
- Messaging and presence management to support operational workflows
- Webhook configuration for event-driven integrations
- Clear SDK-specific exceptions and test-backed behavior for predictable integration

## 4. High-level tech/architecture
- Python 3.9+ package distributed via `pyproject.toml` (hatchling)
- Layered SDK design: client transport (`EvolutionClient`) + service modules + typed models
- Payload-centric models with API-compatible key names for Evolution endpoints
- Quality gates via `ruff` (format/lint), `mypy` (typing), and `pytest` (unit tests)

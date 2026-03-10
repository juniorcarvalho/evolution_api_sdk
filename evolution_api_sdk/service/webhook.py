class WebhookService:
    def __init__(self, client, token: str = None):
        self.client = client
        self.token = token

    def _get_headers_webhook(self) -> dict:
        result = {
            'Content-Type': 'application/json',
        }
        if self.token:
            result['Authorization'] = f'Bearer {self.token}'
        return result

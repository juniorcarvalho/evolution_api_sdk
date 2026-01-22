class EvolutionAPIError(Exception):
    pass

class EvolutionAuthenticationError(EvolutionAPIError):
    pass

class EvolutionNotFoundError(EvolutionAPIError):
    pass
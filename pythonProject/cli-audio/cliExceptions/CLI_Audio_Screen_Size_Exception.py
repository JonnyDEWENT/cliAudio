class CLI_Audio_Screen_Size_Exception(CLI_Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

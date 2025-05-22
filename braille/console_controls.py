class ConsoleOutputControls:
    @staticmethod
    def save_position():
        print("\033[s",end="")
    @staticmethod
    def load_position():
        print("\033[u",end="")
    @staticmethod
    def clear_terminal():
        print("\033[2J",end="")
    @classmethod
    def keep_position(cls):
        return cls._KeepPositionContext()
    
    class _KeepPositionContext:
        def __enter__(self):
            ConsoleOutputControls.save_position()
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            ConsoleOutputControls.load_position()
            return False

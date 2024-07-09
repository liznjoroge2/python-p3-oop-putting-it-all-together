class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
        self._condition = "Used"  # Initialize condition with a default value
    
    @property
    def size(self):
        """Get the size of the shoe."""
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else: 
            print('size must be an integer')

    def cobble(self):
        print('Your shoe is as good as new!')
        self._condition = "New"

    @property
    def condition(self):
        """Get the condition of the shoe."""
        return self._condition

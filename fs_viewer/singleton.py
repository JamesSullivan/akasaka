from sec import query
class GlobalObject:
    def __init__(self):
        # Initialize your object here
        print("GlobalObject is being instantiated!")
        self.query = query.Query()

# This will hold the single instance of GlobalObject
global_instance = None

def get_global_object():
    """
    Provides access to the global object instance.
    Instantiates it if it doesn't exist (though ready() should handle this).
    """
    global global_instance
    if global_instance is None:
        global_instance = GlobalObject()
    return global_instance


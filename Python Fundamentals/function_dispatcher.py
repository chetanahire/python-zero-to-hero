from typing import Callable, Any, Dict
class FunctionDispatcher:

    def __init__(self):
        self._registry : Dict[str, Callable] = {}
    
    def register(self, name : str, func: Callable):
        
        if not Callable:
            raise TypeError(f'Function register under {name} is not Callable')
        
        if not isinstance(name, str) or name.strip == "":
            raise NameError(f'Function name must not be empty')
                
        self._registry[name] = func
    
    def dispatch(self , name: str, *args, **kwargs):
        if name not in self._registry:
            raise KeyError(f'Function is not register under {name}')
        
        return self._registry[name](*args, **kwargs)

    def list_functions(self) -> Dict[str, Callable]:
        """Return a copy of the registry."""
        return dict(self._registry)
    
    def unregister(self, name):

        if name not in self._registry:
            raise KeyError(f'Function is not register under {name}')
        
        del self._registry[name]

    

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b


if __name__ == "__main__":

    dispatcher = FunctionDispatcher()

    dispatcher.register("addition", add)
    dispatcher.register("sub", sub)
    dispatcher.register("multiplication", mul)

    print(dispatcher.list_functions())

    print(dispatcher.dispatch("addition",2,4))
    print(dispatcher.dispatch("sub",5,1))
    print(dispatcher.dispatch("multiplication",5,5))
    
    # dispatcher.unregister("addition")

    print(dispatcher.list_functions())
from abc import ABC, abstractmethod 
from gym import Env 

class BaseEnvironment(Env, ABC):
    metadata = {"render.modes": ['human']}
    
    
    
    
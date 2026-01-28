# projgen/engine/plugin.py
from abc import ABC, abstractmethod

class FeaturePlugin(ABC):
    name: str = None

    def __init__(self):
        if not self.name:
            raise ValueError("FeaturePlugin must define a name")

    def register(self, context):
        pass

    @abstractmethod
    def apply(self, context):
        raise NotImplementedError

    def after(self, context):
        pass

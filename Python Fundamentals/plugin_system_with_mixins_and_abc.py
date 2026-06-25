from abc import ABC, abstractmethod
from typing import List, Type


# ---------------------------
# Base Plugin Interface (ABC)
# ---------------------------
class PluginBase(ABC):
    """Abstract base class for all plugins."""

    @abstractmethod
    def name(self) -> str:
        """Return the plugin's name."""
        pass

    @abstractmethod
    def run(self, data: str) -> str:
        """Process input data and return output."""
        pass


# ---------------------------
# Mixins for Reusable Features
# ---------------------------
class LoggingMixin:
    """Provides logging capability to plugins."""
    def log(self, message: str):
        print(f"[{self.name()}] {message}")


class UpperCaseMixin:
    """Provides a helper to convert text to uppercase."""
    def to_upper(self, text: str) -> str:
        return text.upper()


# ---------------------------
# Example Plugins
# ---------------------------
class UpperCasePlugin(LoggingMixin, UpperCaseMixin, PluginBase):
    """Plugin that converts text to uppercase."""
    def name(self) -> str:
        return "UpperCasePlugin"

    def run(self, data: str) -> str:
        self.log("Converting text to uppercase.")
        return self.to_upper(data)


class ReversePlugin(LoggingMixin, PluginBase):
    """Plugin that reverses text."""
    def name(self) -> str:
        return "ReversePlugin"

    def run(self, data: str) -> str:
        self.log("Reversing text.")
        return data[::-1]


# ---------------------------
# Plugin Manager
# ---------------------------
class PluginManager:
    """Manages plugin registration and execution."""
    def __init__(self):
        self.plugins: List[PluginBase] = []

    def register_plugin(self, plugin_cls: Type[PluginBase]):
        """Register a plugin class."""
        if not issubclass(plugin_cls, PluginBase):
            raise TypeError(f"{plugin_cls.__name__} is not a PluginBase subclass.")
        self.plugins.append(plugin_cls())
        print(f"Registered plugin: {plugin_cls.__name__}")

    def run_all(self, data: str):
        """Run all registered plugins on the given data."""
        results = {}
        for plugin in self.plugins:
            try:
                results[plugin.name()] = plugin.run(data)
            except Exception as e:
                results[plugin.name()] = f"Error: {e}"
        return results


# ---------------------------
# Example Usage
# ---------------------------
if __name__ == "__main__":
    manager = PluginManager()

    # Register plugins
    manager.register_plugin(UpperCasePlugin)
    manager.register_plugin(ReversePlugin)

    # Run all plugins
    input_text = "Hello Plugins"
    print(f"Input: {input_text}")
    output = manager.run_all(input_text)

    # Display results
    for plugin_name, result in output.items():
        print(f"{plugin_name} output: {result}")

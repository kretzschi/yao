# -*- coding: utf-8 -*-
import os
import organizer
from yapsy.PluginManager import PluginManager

PluginFolder = os.path.join("..", "plugins")


def main():
    # Create plugin manager
    manager = PluginManager()
    manager.setPluginPlaces([PluginFolder])
    # Collect plugins
    manager.collectPlugins()

    for plugin in manager.getAllPlugins():
        plugin.plugin_object.say_hello()


if __name__ == "__main__":
    main()

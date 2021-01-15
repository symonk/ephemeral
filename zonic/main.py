"""Console script for zonic."""
import argparse
import sys

from colorama import Fore
from pluggy import PluginManager

from zonic import Configuration
from zonic import plugin_manager


def main():
    welcome()
    parser = argparse.ArgumentParser()
    _register_core_plugins(plugin_manager)
    plugin_manager.hook.zonic_add_options(parser=parser)
    config = Configuration(
        options=vars(parser.parse_args()), plugin_manager=plugin_manager
    )
    plugin_manager.hook.zonic_setup(config=config)
    vulnerable_ports = plugin_manager.hook.zonic_execute(config=config)
    plugin_manager.hook.zonic_teardown(config=config, vulnerable_ports=vulnerable_ports)
    plugin_manager.hook.zonic_report(config=config, ports=vulnerable_ports)
    return 0


def _register_core_plugins(plugin_manager: PluginManager) -> None:
    from zonic.core.zonic_core import ZonicCorePlugin
    from zonic.core.zonic_csv import ZonicCSVPlugin

    core_plugin = ZonicCorePlugin(plugin_manager)
    csv_plugin = ZonicCSVPlugin(plugin_manager)
    plugin_manager.register(plugin=csv_plugin, name=csv_plugin.name)
    plugin_manager.register(plugin=core_plugin, name=core_plugin.name)


def welcome() -> None:
    print(
        fr"""
================================ {Fore.LIGHTBLUE_EX}
 ______     ______     __   __     __     ______    
/\___  \   /\  __ \   /\ "-.\ \   /\ \   /\  ___\   
\/_/  /__  \ \ \/\ \  \ \ \-.  \  \ \ \  \ \ \____  
  /\_____\  \ \_____\  \ \_\\"\_\  \ \_\  \ \_____\ 
  \/_____/   \/_____/   \/_/ \/_/   \/_/   \/_____/ 
                                                    

{Fore.RESET} =================== {Fore.WHITE}
  zonic: Powerful python port scanner, https://github.com/symonk/zonic
    """,
        Fore.RESET,
    )


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

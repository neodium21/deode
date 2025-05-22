# Copyright (c) 2025 devgagan : https://github.com/devgaganin.
# Licensed under the GNU General Public License v3.0.
# See LICENSE file in the repository root for full license text.

import asyncio
import importlib
import os
import signal
import sys

from shared_client import start_client

PLUGIN_DIR = "plugins"
PLUGIN_PREFIX = "run_"

async def load_and_run_plugins():
    await start_client()
    plugins = [f[:-3] for f in os.listdir(PLUGIN_DIR) if f.endswith(".py") and f != "__init__.py"]
    tasks = []

    for plugin in plugins:
        try:
            module = importlib.import_module(f"{PLUGIN_DIR}.{plugin}")
            func_name = f"{PLUGIN_PREFIX}{plugin}_plugin"
            if hasattr(module, func_name):
                print(f"Running {plugin} plugin...")
                task = asyncio.create_task(getattr(module, func_name)())
                tasks.append(task)
        except Exception as e:
            print(f"Error loading plugin {plugin}: {e}")

    return tasks

async def main():
    stop_event = asyncio.Event()

    def shutdown_signal(*args):
        print("Shutdown signal received.")
        stop_event.set()

    # Register shutdown signals
    for sig in (signal.SIGINT, signal.SIGTERM):
        signal.signal(sig, shutdown_signal)

    plugin_tasks = await load_and_run_plugins()

    await stop_event.wait()  # Wait until shutdown signal

    # Gracefully cancel plugins
    for task in plugin_tasks:
        task.cancel()
    await asyncio.gather(*plugin_tasks, return_exceptions=True)

    print("All plugins stopped. Exiting...")

if __name__ == "__main__":
    try:
        print("Starting clients ...")
        asyncio.run(main())
    except Exception as e:
        print(f"Unhandled error: {e}")
        sys.exit(1)

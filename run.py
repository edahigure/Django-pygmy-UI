#!/usr/bin/env python3
import os
import sys
import time
import signal
import traceback
import subprocess

PYGMYUI_ARGS = ['gunicorn', '-b 0.0.0.0:8000', '-w 1', 'pygmyui.wsgi']
process = []

def print_err(proc, timeout=2):
    try:
        print(proc.communicate(timeout=timeout))
    except subprocess.TimeoutExpired:
        pass

try:

    print("Starting development server at http://127.0.0.1:8000/")
    os.chdir('pygmyui')
    process.append(subprocess.Popen(PYGMYUI_ARGS, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE))
    print_err(process[-1])
    while True:
        time.sleep(1) 

except KeyboardInterrupt:
    pass
except Exception as e:
    traceback.print_exc()
finally:
    print("Terminating subprocesses...")
    for proc in process:
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
    print("Cleanup done.")


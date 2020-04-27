#!/usr/bin/env python3
"""skiis v0.01"""

import pynvim

@pynvim.plugin
class Skiis(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command("SkiiRun", sync=True)
    def exec_conf(self):
        """exec_conf"""
        try:
            with open(".skiiconf", "r") as f:
                conf_file = f.read()
        except FileNotFoundError:
            return
        self.nvim.funcs.execute(f"!{conf_file[:-1]}")

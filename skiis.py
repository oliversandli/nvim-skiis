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
        pwd = self.nvim.command_output("pwd")
        try:
            with open(f"{pwd}/.skiiconf", "r") as f:
                conf_contents = f.read()
        except FileNotFoundError:
            self.nvim.out_write("ERROR: could not find .skiiconf")
            return
        self.nvim.command("set splitright")
        self.nvim.command(f"vsplit | terminal {conf_contents}")
        self.nvim.command("startinsert")

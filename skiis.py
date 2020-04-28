#!/usr/bin/env python3
"""skiis v1.0.0"""

import pynvim

@pynvim.plugin
class Skiis(object):
    """Skiis"""
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command("SkiiRun", sync=True)
    def exec_conf(self):
        """run the command in conf_contents"""
        pwd = self.nvim.command_output("pwd")
        try:
            with open(f"{pwd}/.skiiconf", "r") as open_file:
                conf_contents = open_file.read()
        except FileNotFoundError:
            self.nvim.out_write("ERROR: could not find .skiiconf")
            return
        self.nvim.command("set splitright")
        self.nvim.command(f"vsplit | terminal {conf_contents}")
        self.nvim.command("startinsert")

# -*- coding: utf-8 -*-

import ConfigParser

def openCfg(cfgfilename):
        config = ConfigParser.ConfigParser()
        config.optionxform = str
        config.readfp(open(cfgfilename))
        return config

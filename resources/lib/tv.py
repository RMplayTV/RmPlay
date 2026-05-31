import os
import re
import xbmcaddon
from utils import load_m3u

addon = xbmcaddon.Addon()

class TV:
    def __init__(self):
        self.m3u_url = addon.getSetting('m3u_url')
        self.m3u_path = addon.getSetting('m3u_local_path')
        self.channels = []
        self.load_channels()
    
    def load_channels(self):
        try:
            if self.m3u_path and os.path.exists(self.m3u_path):
                self.channels = load_m3u(self.m3u_path)
        except Exception as e:
            print(f"Erro: {e}")
            self.channels = []
    
    def show_tv_list(self, addon_handle, add_item_callback):
        if not self.channels:
            self.channels = [{'name': 'Canal Exemplo', 'url': 'http://example.com/stream.m3u8', 'logo': '', 'fanart': ''}]
        
        for channel in self.channels:
            add_item_callback(nome=channel['name'], url=channel['url'], thumb=channel.get('logo', ''))

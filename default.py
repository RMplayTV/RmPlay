import sys
import os
from urllib.parse import parse_qsl

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'resources', 'lib'))

import xbmcplugin
import xbmcgui
from tv import TV
from filmes import Filmes
from series import Series
from desenhos import Desenhos
from pesquisa import Pesquisa

addon_handle = int(sys.argv[1])
params = dict(parse_qsl(sys.argv[2].replace('?', '')))

tv = TV()
filmes = Filmes()
series = Series()
desenhos = Desenhos()
pesquisa_obj = Pesquisa()

xbmcplugin.setContent(addon_handle, 'videos')

def show_main_menu():
    items = [
        ("📺 TV AO VIVO", "tv"),
        ("🎬 FILMES", "filmes"),
        ("📺 SÉRIES", "series"),
        ("🧸 DESENHOS", "desenhos"),
        ("🔍 PESQUISA", "pesquisa"),
    ]
    
    for nome, action in items:
        url = f"plugin://plugin.video.rmtv/?action={action}"
        item = xbmcgui.ListItem(nome)
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=item, isFolder=True)
    
    xbmcplugin.endOfDirectory(addon_handle)

def add_video_item(nome, url, thumb='', fanart='', info=None):
    item = xbmcgui.ListItem(nome)
    item.setProperty('IsPlayable', 'true')
    if info:
        item.setInfo('video', info)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=item, isFolder=False)

action = params.get('action')

if action is None:
    show_main_menu()
elif action == 'tv':
    tv.show_tv_list(addon_handle, add_video_item)
    xbmcplugin.endOfDirectory(addon_handle)
elif action == 'filmes':
    filmes.show_filmes_list(addon_handle, add_video_item)
    xbmcplugin.endOfDirectory(addon_handle)
elif action == 'series':
    series.show_series_list(addon_handle, add_video_item)
    xbmcplugin.endOfDirectory(addon_handle)
elif action == 'desenhos':
    desenhos.show_desenhos_list(addon_handle, add_video_item)
    xbmcplugin.endOfDirectory(addon_handle)
elif action == 'pesquisa':
    pesquisa_obj.show_pesquisa(addon_handle, add_video_item)
    xbmcplugin.endOfDirectory(addon_handle)
else:
    xbmcplugin.endOfDirectory(addon_handle)

import sys
import os

# Add resources/lib to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'resources', 'lib'))

import xbmcplugin
import xbmcgui
import xbmcaddon

addon_handle = int(sys.argv[1])

# Menu principal simples
def main_menu():
    items = [
        ("📺 TV AO VIVO", "tv"),
        ("🎬 FILMES", "filmes"),
        ("📺 SÉRIES", "series"),
        ("🧸 DESENHOS", "desenhos"),
        ("🔍 PESQUISA", "pesquisa"),
    ]
    
    for label, action in items:
        li = xbmcgui.ListItem(label)
        url = f"plugin://plugin.video.rmtv/?action={action}"
        xbmcplugin.addDirectoryItem(addon_handle, url, li, isFolder=True)
    
    xbmcplugin.endOfDirectory(addon_handle)

# Menu de TV
def tv_menu():
    items = [
        ("Canal 1", "http://example.com/stream1.m3u8"),
        ("Canal 2", "http://example.com/stream2.m3u8"),
    ]
    
    for label, url in items:
        li = xbmcgui.ListItem(label)
        li.setProperty('IsPlayable', 'true')
        xbmcplugin.addDirectoryItem(addon_handle, url, li, isFolder=False)
    
    xbmcplugin.endOfDirectory(addon_handle)

# Menu de Filmes
def filmes_menu():
    items = [
        ("Filme 1", "http://example.com/filme1.mp4"),
        ("Filme 2", "http://example.com/filme2.mp4"),
    ]
    
    for label, url in items:
        li = xbmcgui.ListItem(label)
        li.setProperty('IsPlayable', 'true')
        xbmcplugin.addDirectoryItem(addon_handle, url, li, isFolder=False)
    
    xbmcplugin.endOfDirectory(addon_handle)

# Menu de Séries
def series_menu():
    items = [
        ("Série 1", "http://example.com/serie1-ep1.mp4"),
        ("Série 2", "http://example.com/serie2-ep1.mp4"),
    ]
    
    for label, url in items:
        li = xbmcgui.ListItem(label)
        li.setProperty('IsPlayable', 'true')
        xbmcplugin.addDirectoryItem(addon_handle, url, li, isFolder=False)
    
    xbmcplugin.endOfDirectory(addon_handle)

# Menu de Desenhos
def desenhos_menu():
    items = [
        ("Desenho 1", "http://example.com/desenho1.mp4"),
        ("Desenho 2", "http://example.com/desenho2.mp4"),
    ]
    
    for label, url in items:
        li = xbmcgui.ListItem(label)
        li.setProperty('IsPlayable', 'true')
        xbmcplugin.addDirectoryItem(addon_handle, url, li, isFolder=False)
    
    xbmcplugin.endOfDirectory(addon_handle)

# Pesquisa
def pesquisa_menu():
    keyboard = xbmcgui.Keyboard('', 'Pesquisar')
    keyboard.doModal()
    
    if keyboard.isConfirmed():
        query = keyboard.getText()
        li = xbmcgui.ListItem(f"Resultados para: {query}")
        xbmcplugin.addDirectoryItem(addon_handle, "", li, isFolder=False)
    
    xbmcplugin.endOfDirectory(addon_handle)

# Roteamento
if len(sys.argv) > 2:
    params = sys.argv[2]
    if '?action=tv' in params:
        tv_menu()
    elif '?action=filmes' in params:
        filmes_menu()
    elif '?action=series' in params:
        series_menu()
    elif '?action=desenhos' in params:
        desenhos_menu()
    elif '?action=pesquisa' in params:
        pesquisa_menu()
    else:
        main_menu()
else:
    main_menu()

# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/GoProCamera
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------
import os
import sys
import time
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.novelasclassicas'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=resfolder+"entrada.mp4"

YOUTUBE_PLAYLIST_ID1 = "PLpRC9CpcCCqi-ezNiwZjTlT8YfXZqGnoW"
YOUTUBE_PLAYLIST_ID3 = "PLpRC9CpcCCqigNisHFPBXhhG-olL8X8xI"
YOUTUBE_PLAYLIST_ID2 = "PLpRC9CpcCCqiao9C6adIg3e4A79bhNLty"
YOUTUBE_PLAYLIST_ID4 = "PLpRC9CpcCCqiY0OZ8fQG2GFXS7SWeoWeq"

# Ponto de Entrada
def run():
	# Pega Parâmetros
	params = plugintools.get_params()
	
	if params.get("action") is None:
		xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(entryurl)
		
		while xbmc.Player().isPlaying():
			time.sleep(1)

		main_list(params)
	else:
		action = params.get("action")
		exec action+"(params)"

	plugintools.close_item_list()


	# Menu Principal
def main_list(params):

#YOUTUBE_PLAYLIST_ID1 = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	plugintools.log("PLpRC9CpcCCqi-ezNiwZjTlT8YfXZqGnoW.main_list "+repr(params))
	plugintools.log("PLpRC9CpcCCqi-ezNiwZjTlT8YfXZqGnoW.run")
	plugintools.add_item(
		title = "Roque Santeiro Parte 1",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_PLAYLIST_ID1+"/",
		thumbnail = 'http://xmbcrios.esy.es/novelas/roqsanteiro.png',
		fanart = 'http://xmbcrios.esy.es/novelas/fanartrosant.jpg',
		folder = True )
#YOUTUBE_PLAYLIST_ID3 = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	plugintools.log("PLpRC9CpcCCqigNisHFPBXhhG-olL8X8xI.main_list "+repr(params))
	plugintools.log("PLpRC9CpcCCqigNisHFPBXhhG-olL8X8xI.run")
	plugintools.add_item(
		title = "Roque Santeiro Parte 2",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_PLAYLIST_ID3+"/",
		thumbnail = 'http://xmbcrios.esy.es/novelas/roqsanteiro.png',
		fanart = 'http://xmbcrios.esy.es/novelas/fanartrosant.jpg',
		folder = True )		
#YOUTUBE_PLAYLIST_ID2 = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"		
	plugintools.log("PLpRC9CpcCCqiao9C6adIg3e4A79bhNLty.main_list "+repr(params))
	plugintools.log("PLpRC9CpcCCqiao9C6adIg3e4A79bhNLty.run")
	plugintools.add_item(
		title = "Tieta",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_PLAYLIST_ID2+"/",
		thumbnail = 'http://xmbcrios.esy.es/novelas/tieta.png',
		fanart = 'http://xmbcrios.esy.es/novelas/tieta.png',
		folder = True )
#YOUTUBE_PLAYLIST_ID2 = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"		
	plugintools.log("PLpRC9CpcCCqiY0OZ8fQG2GFXS7SWeoWeq.main_list "+repr(params))
	plugintools.log("PLpRC9CpcCCqiY0OZ8fQG2GFXS7SWeoWeq.run")
	plugintools.add_item(
		title = "Renascer",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_PLAYLIST_ID4+"/",
		thumbnail = 'http://zip.net/bcr84F',
		fanart = 'http://zip.net/bcr84F',
		folder = True )			

run()
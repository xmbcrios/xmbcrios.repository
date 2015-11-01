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

addonID = 'plugin.video.bryoutubers'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=resfolder+"entrada.mp4"

YOUTUBE_CHANNEL_ID1 = "moshipery"
YOUTUBE_CHANNEL_ID2 = "canalvocenaosabia"
YOUTUBE_CHANNEL_ID3 = "tokudoc"
YOUTUBE_CHANNEL_ID4 = "BrazilinSoccer"
YOUTUBE_CHANNEL_ID5 = "Desimpedidos"
YOUTUBE_CHANNEL_ID6 = "cangaianerd"
YOUTUBE_CHANNEL_ID7 = "TheClaudiojp"
YOUTUBE_CHANNEL_ID8 = "iberethenorio"
YOUTUBE_CHANNEL_ID9 = "Boomoficial"
YOUTUBE_CHANNEL_ID10 = "endorfinanet"
YOUTUBE_CHANNEL_ID11 = "laliga"
YOUTUBE_CHANNEL_ID12 = "fecastanhari"
YOUTUBE_CHANNEL_ID13 = "UCwxu7-JP0zrHqccjEzrSW6g"
YOUTUBE_CHANNEL_ID14 = "vcsabiavideos"
YOUTUBE_CHANNEL_ID15 = "baixaki"
YOUTUBE_CHANNEL_ID16 = "canalmegacurioso"
YOUTUBE_CHANNEL_ID17= "eldiadespuesplus"


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
# Canal 01
	plugintools.log("moshipery.main_list "+repr(params))
	plugintools.log("moshipery.run")
	plugintools.add_item(
	title="Olhar Digital",
	url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID1+"/",
	thumbnail= 'http://zip.net/bmsfKt',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
# Canal 02
	plugintools.log("baixaki.main_list "+repr(params))
	plugintools.log("baixaki.run")
	plugintools.add_item(
	title="TecMundo",
	url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID15+"/",
	thumbnail= 'http://zip.net/bdsgY2',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
	# Canal 03
	plugintools.log("canalmegacurioso.main_list "+repr(params))
	plugintools.log("canalmegacurioso.run")
	plugintools.add_item(
	title="Mega Curioso",
	url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID16+"/",
	thumbnail= 'http://zip.net/bqshv9',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
# Canal 04
	plugintools.log("canalvocenaosabia.main_list "+repr(params))
	plugintools.log("canalvocenaosabia.run")
	plugintools.add_item(
	title="Você Não Sabia",
	url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID2+"/",
    thumbnail= 'http://zip.net/bysjRL',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
# Canal 05
	plugintools.log("vcsabiavideos.main_list "+repr(params))
	plugintools.log("vcsabiavideos.run")
	plugintools.add_item(
	title="Você Sabia?",
	url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID14+"/",
    thumbnail= 'http://zip.net/bdsgYq',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
# Canal 06
	plugintools.log("cangaianerd.main_list "+repr(params))
	plugintools.log("cangaianerd.run")
	plugintools.add_item(
	title="Cangaia Nerd",
	url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID6+"/",
    thumbnail= 'http://zip.net/bksfGS',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
# Canal 07
	plugintools.log("tokudoc.main_list "+repr(params))
	plugintools.log("tokudoc.run")
	plugintools.add_item(
	title="Tokudoc",
	url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID3+"/",
	thumbnail= 'http://zip.net/bxskqs',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
# Canal 08
	plugintools.log("UCwxu7-JP0zrHqccjEzrSW6g.main_list "+repr(params))
	plugintools.log("UCwxu7-JP0zrHqccjEzrSW6g.run")
	plugintools.add_item(
	title="Futebol Vídeos HD",
	url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID13+"/",
    thumbnail= 'http://zip.net/bksfLK',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
	# Canal 09
	plugintools.log("BrazilinSoccer.main_list "+repr(params))
	plugintools.log("BrazilinSoccer.run")
	plugintools.add_item(
	title="Brazil in Soccer",
	url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID4+"/",
    thumbnail= 'http://zip.net/bgsfsc',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
# Canal 10
	plugintools.log("Desimpedidos.main_list "+repr(params))
	plugintools.log("Desimpedidos.run")
	plugintools.add_item(
	title="Desimpedidos",
	url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID5+"/",
    thumbnail= 'http://zip.net/bdsf7m',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
# Canal 11
	plugintools.log("TheClaudiojp.main_list "+repr(params))
	plugintools.log("TheClaudiojp.run")
	plugintools.add_item(
	title="Sinta meu estylo!",
	url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID7+"/",
    thumbnail= 'http://zip.net/bnsfPJ',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
# Canal 15
	plugintools.log("laliga.main_list "+repr(params))
	plugintools.log("laliga.run")
	plugintools.add_item(
	title="Canal Laliga Espanhola",
	url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID11+"/",
    thumbnail= 'http://zip.net/bwshZx',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
	# Canal 15
	plugintools.log("eldiadespuesplus.main_list "+repr(params))
	plugintools.log("eldiadespuesplus.run")
	plugintools.add_item(
	title="El Día Después",
	url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID17+"/",
    thumbnail= 'http://zip.net/bksjlt',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
		
	# Canal 12
	plugintools.log("iberethenorio.main_list "+repr(params))
	plugintools.log("iberethenorio.run")
	plugintools.add_item(
	title="Manual do Mundo",
	url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID8+"/",
    thumbnail= 'http://zip.net/bxsgPQ',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
# Canal 13
	plugintools.log("Boomoficial.main_list "+repr(params))
	plugintools.log("Boomoficial.run")
	plugintools.add_item(
	title="Canal BOOM [COLOR greenyellow](Pegadinhas)[/COLOR]",
	url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID9+"/",
    thumbnail= 'http://zip.net/bnsfQw',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
# Canal 14
	plugintools.log("endorfinanet.main_list "+repr(params))
	plugintools.log("endorfinanet.run")
	plugintools.add_item(
	title="David Mafra [COLOR greenyellow](Pegadinhas)[/COLOR]",
	url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID10+"/",
    thumbnail= 'http://zip.net/bysgh2',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
# Canal 15
	plugintools.log("WebTvSomzoom.main_list "+repr(params))
	plugintools.log("WebTvSomzoom.run")
	plugintools.add_item(
	title="TV Somzoom",
	url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID11+"/",
    thumbnail= 'http://zip.net/bxsgQQ',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
# Canal 16
	plugintools.log("fecastanhari.main_list "+repr(params))
	plugintools.log("fecastanhari.run")
	plugintools.add_item(
	title="Canal Nostalgia",
	url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID12+"/",
    thumbnail= 'http://zip.net/bmsfPt',
    fanart= 'http://zip.net/bxsgND',
	folder = True )
	
	
		

run()
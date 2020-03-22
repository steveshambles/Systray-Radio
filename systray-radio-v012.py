"""
Systray Radio V0.12

Just a quick demo to show how icons work in a systray menu.
stevepython.wordpress.com

Requirements:
pip install infi.systray

menu icons in 'icons' folder in same dir as main prg.
Will still work without them, though look odd.

radio.ico in main dir. If not found system default icon is used.

I found most of the streams here:
http://www.suppertime.co.uk/blogmywiki/2015/04/updated-list-of-bbc-network-radio-urls/
"""
import ctypes
import webbrowser
from PIL import ImageGrab
from infi.systray import SysTrayIcon as stray

def visit_blog(stray):
    """Open webbrowser and go to my Python blog site."""
    webbrowser.open('https://stevepython.wordpress.com/2020/03/16/how-to-create-a-systray-app')

def sr_about(stray):
    """Popup box showing info about this program."""
    ctypes.windll.user32.MessageBoxW(None,
                                     u'\nSystray Radio V0.12.\n'
                                     'Freeware by Steve Shambles March 2020.\n\n'
                                     'This is Just a quick demo to show how icons\n'
                                     'work in a systray menu.\n\n'
                                     'Over time the radio streams may need updating\n'
                                     'to keep them working.',
                                     u'Systray Radio V0.12', 0)

def exit_prg(stray):
    """When quit is clicked, thread should close and icon in systray destroyed."""
    pass

def radio_4(stray):
    """Radio 4 stream."""
    webbrowser.open('http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio4fm_mf_p')

def radio_4xtra(stray):
    """Radio 4 Extra stream."""
    webbrowser.open('http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio4extra_mf_p')

def radio_5live(stray):
    """Radio 5 Live stream."""
    webbrowser.open('http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio5live_mf_p')

def world_service(stray):
    """BBC World Service stream."""
    webbrowser.open('http://bbcwssc.ic.llnwd.net/stream/bbcwssc_mp1_ws-eieuk')

def radio_london(stray):
    """Radio London stream."""
    webbrowser.open('http://bbcmedia.ic.llnwd.net/stream/bbcmedia_lrldn_mf_p')

def brit_com(stray):
    """British Comedy Radio stream."""
    webbrowser.open('http://149.255.59.164:8132/;stream/1')

def punk_fm(stray):
    """Punk FM stream"""
    webbrowser.open('http://94.23.26.22:8090/live.mp3')

def lbc(stray):
    """LBC stream."""
    webbrowser.open_new('http://media-ice.musicradio.com:80/LBCLondon')

def talk_sport(stray):
    """Talk Shite stream."""
    webbrowser.open('http://radio.talksport.com/stream-mobile?ref=rf')

def talk_sport2(stray):
    """Talk even more shite 2 stream."""
    webbrowser.open('http://radio.talksport.com/stream2-mobile?ref=rf')

def dud(stray):
    """I do not know if a seperator bar is possible using infi-systray,
       there is nothing mentioned in docs. So I used an item as a fake bar.
       This requires a callback, which is what this is for, to do nothing."""
    pass

# Program name displayed when mouse hovered over radio icon in systray.
hover_text = 'Systray Radio V0.12 Mar 2020'

# Use 'None' in place of icons if you want to remove menu icons,
# see visit blog line below.
menu_options = (('BBC Radio 4', r'icons/r4.ico', radio_4),
                ('BBC Radio 4 Xtra', r'icons/r4x.ico', radio_4xtra),
                ('BBC Radio 5 Live', r'icons/r5.ico', radio_5live),
                ('BBC Radio London', r'icons/rl.ico', radio_london),
                ('BBC World Service', r'icons/ws.ico', world_service),
                ('Punk FM', r'icons/punkfm.ico', punk_fm),
                ('LBC', r'icons/lbc.ico', lbc),
                ('Talk Sport', r'icons/talksport.ico', talk_sport),
                ('Talk Sport 2', r'icons/talksport2.ico', talk_sport2),
                ('Brit comedy radio', r'icons/britcom.ico', brit_com),
                ('_______________', None, dud),
                ('Options', None, (('About', None, sr_about),
                                   ('Visit my blog', None, visit_blog),))
               )
# radio.ico is the main program icon that will appear in the systray.
# If it is not found then the system default icon is used.
# Index=2 will play 3rd item (Radio5 Live) if radio icon is double-clicked.
stray = stray('radio.ico',
              hover_text, menu_options, on_quit=exit_prg,
              default_menu_index=2)
stray.start()

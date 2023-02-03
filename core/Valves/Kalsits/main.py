import os
import Ani
import Audio
import sys
sys.path.append(os.getcwd())
import core.petc as petc
import core.stray as stray
pet = petc.pet()
pet.setsits()
pet.init(850, 194)
pet.Audio(Audio.touch1, Audio.touch2, Audio.touch3, Audio.touch4, Audio.touch5, Audio.sleeps, Audio.rain, Audio.cold, Audio.hot)
pet.Animate(Ani.Anirelax, Ani.Aniinteract, Ani.Anisit, Ani.Anisleep, Ani.Animove, Ani.Anilrelax, Ani.Anilinteract, Ani.Anilsit, Ani.Anilsleep, Ani.Anilmove)
'''
pet.timeremind(230000)
pet.weather(230100, 230200, 140000)
'''
stray.stray(stray.stray_thread)
pet.main(3.5,60)
from pygame import mixer

mixer.init()  # Pygame Mixer初始化 Pygame Mixer initialization
# 语音相关设置 Voice-related settings
touch1 = mixer.Sound("./core/valves/Kalsits/Audio/Kal_touch1.mp3")
touch1.set_volume(0.2)
touch2 = mixer.Sound("./core/valves/Kalsits/Audio/Kal_touch2.mp3")
touch2.set_volume(0.2)
touch3 = mixer.Sound("./core/valves/Kalsits/Audio/Kal_touch3.mp3")
touch3.set_volume(0.2)
touch4 = mixer.Sound("./core/valves/Kalsits/Audio/Kal_touch4.mp3")
touch4.set_volume(0.2)
touch5 = mixer.Sound("./core/valves/Kalsits/Audio/Kal_touch5.mp3")
touch5.set_volume(0.2)
sleeps = mixer.Sound("./core/valves/Kalsits/Audio/Kal_sleep.mp3")
sleeps.set_volume(0.2)
rain = mixer.Sound("./core/valves/Kalsits/Audio/Kal_rain.mp3")
rain.set_volume(0.2)
hot = mixer.Sound("./core/valves/Kalsits/Audio/Kal_hot.mp3")
hot.set_volume(0.2)
cold = mixer.Sound("./core/valves/Kalsits/Audio/Kal_cold.mp3")
cold.set_volume(0.2)
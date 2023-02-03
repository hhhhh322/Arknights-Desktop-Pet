"""
用于导入所有动作的帧图并且镜像，只需要准备一份素材即可。
animTypes, aaniTypes, anniTypes: 动作类型，素材张数相同的放在同一个Types中
此种方法从pyganim的示例文件中获得，项目地址：https://github.com/asweigart/pyganim
"""
import pyganim

animTypes = 'interact sit sleep'.split()# 分解字符串
animObjs = {}# 动画列表
for animType in animTypes:
    imagesAndDurations = [('./core/valves/kalsits/%s/%s_%s.png' % (animType, animType, str(num).rjust(2, '0')), 65) for num in range(54)]# 动画序列，详见pyganim文档。
    animObjs[animType] = pyganim.PygAnimation(imagesAndDurations)# 将动画序列存入动作列表
animObjs['linteract'] = animObjs['interact'].getCopy()# 复制列表内容
animObjs['linteract'].flip(True, False)# 将列表中的动画序列翻转(垂直翻转)
animObjs['linteract'].makeTransformsPermanent()# 没查到
# 同上
animObjs['lsit'] = animObjs['sit'].getCopy()
animObjs['lsit'].flip(True, False)
animObjs['lsit'].makeTransformsPermanent()
animObjs['lsleep'] = animObjs['sleep'].getCopy()
animObjs['lsleep'].flip(True, False)
animObjs['lsleep'].makeTransformsPermanent()

# 同上，除列表名以及分割字符串改变外无改变(应该可以不改)
aaniTypes = 'move'.split()
aanimObjs = {}
for aanimType in aaniTypes:
    aimagesAndDurations = [('./core/valves/kalsits/%s/%s_%s.png' % (aanimType, aanimType, str(num1).rjust(2, '0')), 65) for num1 in range(80)]
    aanimObjs[aanimType] = pyganim.PygAnimation(aimagesAndDurations)
aanimObjs['lmove'] = aanimObjs['move'].getCopy()
aanimObjs['lmove'].flip(True, False)
aanimObjs['lmove'].makeTransformsPermanent()
# 同上
anniTypes = 'relax'.split()
anniObjs = {}
for anniType in anniTypes:
    aiimagesAndDurations = [('./core/valves/kalsits/%s/%s_%s.png' % (anniType, anniType, str(num2).rjust(3, '0')), 65) for num2 in range(134)]
    anniObjs[anniType] = pyganim.PygAnimation(aiimagesAndDurations)
anniObjs['lrelax'] = anniObjs['relax'].getCopy()
anniObjs['lrelax'].flip(True, False)
anniObjs['lrelax'].makeTransformsPermanent()

# 赋值给字符串便于调用
Anirelax = anniObjs['relax']
Anilrelax = anniObjs['lrelax']
Animove = aanimObjs['move']
Anilmove = aanimObjs['lmove']
Aniinteract = animObjs['interact']
Anilinteract = animObjs['linteract']
Anisit = animObjs['sit']
Anilsit = animObjs['lsit']
Anisleep = animObjs['sleep']
Anilsleep = animObjs['lsleep']

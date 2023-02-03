from pygame import mixer
from json import load
import os
import pyganim
from importlib import import_module
import stray
import petc


class MDF():
    def __init__(self):
        mixer.init()
    # 加载json文件用于配置
    def __loadJson(self,JsonFile):
        global data
        f = open(JsonFile,'r',encoding='utf-8')
        data = load(f)
        return data

    #根据json文件的动画名称在动画文件夹中寻找，并转为动画对象
    def __loadAnim(self,andata):
        Ani_Path = data["Animations"]["path"]
        path = os.listdir(Ani_Path)
        relax = []
        interact = []
        sit = []
        sleep = []
        move = []
        special=[]
        for files in path:
            if data["Animations"]["relax"] in files:
                r = (Ani_Path + '/' + files, 65)
                relax.append(r)
            if data["Animations"]["interact"] in files:
                i = (Ani_Path + '/' + files, 65)
                interact.append(i)
            if data["Animations"]["sit"] in files:
                si = (Ani_Path + '/' + files, 65)
                sit.append(si)
            if data["Animations"]["relax"] in files:
                sl = (Ani_Path + '/' + files, 65)
                sleep.append(sl)
            if data["Animations"]["move"] in files:
                m = (Ani_Path + '/' + files, 65)
                move.append(m)
            if data["Animations"]["special"] != None and data["Animations"]["special"] in files:
                s = (Ani_Path + '/' + files, 65)
                special.append(s)
        relaxr = pyganim.PygAnimation(relax)
        relaxl = relaxr.getCopy()
        relaxl.flip(True,False)
        relaxl.makeTransformsPermanent()
        interactr = pyganim.PygAnimation(interact)
        interactl = interactr.getCopy()
        interactl.flip(True, False)
        interactl.makeTransformsPermanent()
        sitr = pyganim.PygAnimation(sit)
        sitl = sitr.getCopy()
        sitl.flip(True, False)
        sitl.makeTransformsPermanent()
        sleepr = pyganim.PygAnimation(sleep)
        sleepl = sleepr.getCopy()
        sleepl.flip(True, False)
        sleepl.makeTransformsPermanent()
        mover = pyganim.PygAnimation(move)
        movel = mover.getCopy()
        movel.flip(True, False)
        movel.makeTransformsPermanent()
        if special != []:
            specialr = pyganim.PygAnimation(special)
            speciall = specialr.getCopy()
            speciall.flip(True, False)
            speciall.makeTransformsPermanent()
            return [relaxr,interactr,sitr,sleepr,mover,specialr,sitl,sleepl,relaxl,interactl,movel,speciall]
        else:
            return [relaxr, interactr, sitr, sleepr, mover, None,  sitl, sleepl,relaxl, interactl, movel, None]

    def __loadAudio(self,adata):
        Audio_Path=data["Audio"]["path"]
        path=os.listdir(Audio_Path)
        touch=[]
        sleep=[]
        rain=[]
        hot=[]
        cold=[]
        Audio_List=[]
        for files in path:
            if data["Audio"]["touch"] in files:
                files = mixer.Sound(Audio_Path+'/'+str(files))
                files.set_volume(0.2)
                touch.append(files)
            elif data["Audio"]["sleep"] in files:
                files = mixer.Sound(Audio_Path+'/'+str(files))
                files.set_volume(0.2)
                sleep.append(files)
            elif data["Audio"]["rain"] in files:
                files = mixer.Sound(Audio_Path+'/'+str(files))
                files.set_volume(0.2)
                rain.append(files)
            elif data["Audio"]["hot"] in files:
                files = mixer.Sound(Audio_Path+'/'+str(files))
                files.set_volume(0.2)
                hot.append(files)
            elif data["Audio"]["cold"] in files:
                files = mixer.Sound(Audio_Path+'/'+str(files))
                files.set_volume(0.2)
                cold.append(files)
        if len(touch) <5 and len(touch) != 5:
            n=5-len(touch)
            for i in range(n):
                touch.append('None')
        elif len(touch) >5:
            raise ValueError('信赖触摸语音超过5句,请减少')
        else:
            pass
        Audio_List.extend(touch)
        Audio_List.extend(sleep)
        Audio_List.extend(rain)
        Audio_List.extend(cold)
        Audio_List.extend(hot)
        return Audio_List

    def __loadStray(self,sdata):
        FuncNameList=[]
        FuncList=[]
        Stray_Func_Dict={"cpu":stray.cpu,"memo":stray.memos,"fileclean":stray.FileClean}
        Stray_Name_Dict={"cpu":"状态监测","memo":"备忘录","fileclean":"文件整理"}
        Stray_data=sdata["stray"]
        for functions in Stray_data:
            if functions in Stray_Func_Dict:
                FuncNameList.append(Stray_Name_Dict[functions])
                FuncList.append(Stray_Func_Dict[functions])
            else:
                try:
                    module=import_module(functions)
                    FuncNameList.append(module.name)
                    FuncList.append(module.run)
                except:
                    raise ImportError('no module name:'+functions)
        return [FuncNameList,FuncList]

    def run(self,Json_Path,name):
        data=self.__loadJson(Json_Path)
        petcl = petc.pet()
        petcl.init(data["settings"]["window_size"])
        petcl.Audio(self.__loadAudio(data))
        petcl.Animate(self.__loadAnim(data))
        petcl.name(name)
        petcl.timeremind(data["settings"]["sleeptime"])
        petcl.weather(data["settings"]["weather_time"],data["settings"]["low_temperture_warning"],data["settings"]["hot_warning"])
        stray.stray(self.__loadStray(data))
        petcl.default_main(data["settings"]["interact_stop"], data["settings"]["sit_time"])
    def Search(self,path):
        datanames = os.listdir(path)
        return datanames

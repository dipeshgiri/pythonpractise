from pygame import mixer
import time
def musicloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break

def log(msg):
    f=open("water.txt","a")
    loctime=time.asctime(time.localtime(time.time()))
    f.write(f"{msg} {loctime}\n")
    f.close()

if __name__ == '__main__':
    init_water=time.time()
    init_exe=time.time()
    init_eye=time.time()
    water=5
    exe=20
    eye=30

    while True:
        if time.time()-init_water > water:
            print("Drink Water.Enter Drank To Stop ")
            musicloop("water.wav","Drank")
            init_water=time.time()
            log("Water Drank At")
        if time.time()-init_exe > exe:
            print("Do Exercise. Enter Done To Stop")
            musicloop("water.wav","Done")
            init_exe=time.time()
            log("Exercise Done At")
        if time.time()-init_eye > eye:
            print("Do Eye exercise. Enter Done To Stop")
            musicloop("water.wav","Done")
            init_eye=time.time()
            log("Eye exercise Done At")
        


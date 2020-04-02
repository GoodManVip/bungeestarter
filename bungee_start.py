import threading import Thread
import os

def execute(path,j):
    if j=='y':
        os.system('cd '+path+' && chmod +x ./Start.sh')
    try:
        while True:
            os.system('cd '+path+' &&  ./Start.sh')
    except:
        print('An eror while start in '+path+' has ocured!')
        exit()

p1='./anarchy1'
p2='./anarchy2'
p3='./Auth'
p4='./bedwars'
p5='./buildbattle'
p6='./bungee'
p7='./eggwars'
p8='./hideandseek'
p9='./lobby'
p10='./skywars'
p11='./spleef'
p12='./survival1'
p13='./survival2'
p14='./tntrun'

print('Initing threads.....')
print('Thread #1 started ANARX #1')
t1=threading.Thread(target= execute, args=(p1,'y'))
t1.start()
print('Thread #2 started ANARX #2')
t2=threading.Thread(target= execute, args=(p2,'y'))
t2.start()
print('Thread #3 started Auth')
t3=threading.Thread(target= execute, args=(p3,'y'))
t3.start()
print('Thread #4 started bw')
t4=threading.Thread(target= execute, args=(p4,'y'))
t4.start()
print('Thread #5 started bb')
t5=threading.Thread(target= execute, args=(p5,'y'))
t5.start()
print('Thread #6 started bungee')
t6=threading.Thread(target= execute, args=(p6,'y'))
t6.start()
print('Thread #7 started eggwars')
t7=threading.Thread(target= execute, args=(p7,'y'))
t7.start()
print('Thread #8 started hide and seek')
t8=threading.Thread(target= execute, args=(p8,'y'))
t8.start()
print('Thread #9 started lobby')
t9=threading.Thread(target= execute, args=(p9,'y'))
t9.start()
print('Thread #10 started sw')
t10=threading.Thread(target= execute, args=(p10,'y'))
t10.start()
print('Thread #11 started spleef')
t11=threading.Thread(target= execute, args=(p11,'y'))
t11.start()
print('Thread #12 started SURVIVAL 1')
t12=threading.Thread(target= execute, args=(p12,'y'))
t12.start()
print('Thread #13 started SURVIVAL 2')
t13=threading.Thread(target= execute, args=(p13,'y'))
t13.start()
print('Thread #3 started tntrun')
t14=threading.Thread(target= execute, args=(p14,'y'))
t14.start()
print('Done!')




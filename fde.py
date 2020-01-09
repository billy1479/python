#this simulates the FDE

part = str(input("What part of the cycle do you want to see : "))
t = 0

while t==0:
    if part=="fetch":
        t = 1
    elif part=="decode":
        t = 1
    elif part=="execute":
        t = 1
    else:
        print("Please try again, that was wrong.")
        time.sleep(1)
        part = str(input("What part of the cycle do you want to see, please enter either 'fetch', 'decode', or 'execute' : "))
PC = 0
address = 10011001
import time
if part=="fetch":
    def fetch():
        time.sleep(1)
        print("Contents of PC is copied to the MAR")
        time.sleep(1)
        print("Address is accessed in the main memory by the CPU, using the address bus, and the data held here is returned to the MDR, via the data bus, meanwhile the PC is incremented to point towards the next instruction")
        time.sleep(1)
        print("The contents of the MDR are copied to the CIR")
    fetch()
elif part=="decode":
    def decode():
        time.sleep(1)
        print("The instruction stored in the CIR is decoded into the operand and opcode which shows what type of instruction it is and what hardware is needed")
        time.sleep(1)
        print("The operand stores either the address of data about to be used which is then copied to the MAR or the actual data that is about to be operated on and this is passed onto the accumulator")
    fecode()
elif part=="execute":
    def execute():
        time.sleep(1)
        print("The appropriate method of execution is carried out.")
    execute()
elif part=="whole":
    fetch()
    decode()
    execute()

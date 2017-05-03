import serial
import time
import datetime








def phWizard():
        print("\n\n\n")
        print("***********************************")
        print("Arduino Based PH Reader Interface")
        print("Developed by: Adam Musciano")
        print("***********************************\n")


        #Get inputs
        port = input("Enter port address (ex: COM11): ")                        
        baudrate=int(input("Enter buadrate(ex: 9600): "))                       
        delayTime=int(input("milliseconds of delay between samplings: "))
        duration=int(input("seconds of sampling duration: "))
        filename=str(datetime.datetime.now().strftime('%m-%d-%Y_%H-%M'))
        log= open(filename+"_log.csv","w")
        curMilliSecond=0
        
        print("[+] Connecting to Serial Port...")
        s=None
        try:
                s= serial.Serial(port,baudrate,timeout=5)

                if(s.is_open):
                        #We successsfully connected to the serial port...
                        print("[+] Connected!\n\n")
                        print("[+] Logging serial for: "+str(port)+":"+str(baudrate))
                        print("[+}\tDuration: "+str(duration)+"s\tSampling Rate: "+str(delayTime)+"ms")
                        while(s.is_open and curMilliSecond <= (int(duration)*1000)):
                                result= str(s.readline()).strip('\\b\'rn')  #sanitizes code of any escape characters or single quotes
                                print("T="+str(curMilliSecond)+"ms:\t"+result)
                                log.write(str(curMilliSecond)+";"+result+"\n")
                                time.sleep(int(delayTime)/1000)
                                curMilliSecond+=delayTime
                        print("[+] Closing Connections...")
                        log.close()
                        s.close()
                        print("[+] Closed and Ready to Exit")
                        print("[+] Log file is availabe as: "+filename+"_log.csv in current directory")
                                                
        except serial.serialutil.SerialException :
                print("[-] Connection Error, is deviced properly addressed and plugged in?")
        
                

                

        


phWizard()

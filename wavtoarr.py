import wave
import struct
import sys
#import shutil
import math

def wav_to_floats(wave_file):
    w = wave.open(wave_file)
    astr = w.readframes(w.getnframes())
    # convert binary chunks to short 
    a = struct.unpack("%ih" % (w.getnframes()* w.getnchannels()), astr)
    #a = [float(val) / pow(2, 15) for val in a]
    return a

def floats_to_wav(a,og):
    w = wave.open(og)
    #shutil.copy(og, "output.wav")
    rez=wave.open("output.wav",'w')
    rez.setparams(w.getparams())
    #print("%ih" % w.getnframes())
    da=struct.pack("%ih" % (w.getnframes()* w.getnchannels()),*a)
    rez.writeframes(da)
                       

nams=["sample","rouxl"]
#namm="sample"
#namm="rouxl"
for namm in nams:
    sourc=namm+".wav"

    signal = wav_to_floats(sourc)
    print ("read " + str(len(signal))+ " frames")
    f = open(namm+"song.csv", "w")
    i=0
    n=50
    for j in range (0,n):
        f.write('c')
        f.write(str(j))
        #f.write('"')
        if(j<n-1):
            f.write(';')
    f.write('\n')


    while i < (len(signal)-n):
        for j in range (0,n):
            #f.write('"')
            f.write(str(signal[i+j]))
            #f.write('"')
            if(j<n-1):
                 f.write(';')
        i=i+n
        f.write('\n')
    f.close()








if 1==0 :
    b = ()
    meen=0
    maex=0
    hl=0
    for i in range (0,len(signal)):
        #print(type(b[i]))
        hl=int(signal[i]+math.sin(i/10)*10000)
        if(hl>32767):
            hl=32766
        if(hl<-32768):
            hl=-32767
        #if(hl<meen):
        #    meen=hl
        #if(hl>maex):
        #    maex=hl
        b=b+(hl,)
    print(meen)
    print(maex)

    floats_to_wav(b,sourc)

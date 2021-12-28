
def hitrates(filename,tagbits,indexbits,offsetbits): 
    def hexadecimalToBinary(argument): #function to convert hexadecimal numbers to binary using switch
        switcher = {
            "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "a": "1010",
            "b": "1011",
            "c": "1100",
            "d": "1101",
            "e": "1110",
            "f": "1111",
        }
  
        return switcher.get(argument, "nothing")

    def checkIndex(dict,key):#function to check if a key is present in a dictionary
       
        if key in dict:
            return True
        else:
            return False

#a dictionary is kept whose key is the index and the value stored in it is a list of tag along with the valid bit.
    dict={}

    hit=0 #initializing hit to 0
    miss=0 #initalizing miss to 0
    f=open(filename,"r")  
    for line in f:  
        address=line[4:12] #extracting the address using string slicing
        ans=""#to store the final address in binary
        for i in address:
            ans+=hexadecimalToBinary(i)    
        tag=ans[0:tagbits] #storing the tagbits in binary form
        index=ans[tagbits:tagbits+indexbits] #storing the index in binary form
        byteoffset=ans[tagbits+indexbits:32] #storing the byteoffset in binary form
    
        if(checkIndex(dict,index) and dict[index]==[tag,1]): #checking if there exists a key equal to index and its value is equal to that of [tag,valid bit]
                                                             #if the valid bit is 1 and the value of the key matches,it is a cache hit
            hit+=1
        else:
            dict[index]=[tag,1]                             #the cache stores the new index along with tag and makes its valid bit equal to 1
            miss+=1                                         #it is a cache miss

    return (hit/(hit+miss))                                 #returing the hit rate
print("part A")    
# last 2 bits are byte offset as block size is 4(log4=2)
#(64*1024)/4=2^14 so 14 bits for the index
#Remaining 16 bits are for the tag
print("hit rate for gcc.trace =",hitrates("gcc.trace",16,14,2))
print("hit rate for gzip.trace =",hitrates("gzip.trace",16,14,2))
print("hit rate for mcf.trace =",hitrates("mcf.trace",16,14,2))
print("hit rate for swim.trace =",hitrates("swim.trace",16,14,2))
print("hit rate for twolf.trace =",hitrates("twolf.trace",16,14,2))
print()
print("part B")
# last 2 bits are byte offset as block size is 4(log4=2)
#(512*1024)/4=2^17 so 17 bits for the index
#Remaining 13 bits are for the tag
print("hit rate for gcc.trace =",hitrates("gcc.trace",13,17,2))
print("hit rate for gzip.trace =",hitrates("gzip.trace",13,17,2))
print("hit rate for mcf.trace =",hitrates("mcf.trace",13,17,2))
print("hit rate for swim.trace =",hitrates("swim.trace",13,17,2))
print("hit rate for twolf.trace =",hitrates("twolf.trace",13,17,2))
print()
print("part C")
print("block size = 1")
# Does not have any byte offset
#(64*1024)/1=2^16 so 16 bits for the index
#Remaining 16 bits are for the tag
print("hit rate for gcc.trace =",hitrates("gcc.trace",16,16,0))
print("hit rate for gzip.trace =",hitrates("gzip.trace",16,16,0))
print("hit rate for mcf.trace =",hitrates("mcf.trace",16,16,0))
print("hit rate for swim.trace =",hitrates("swim.trace",16,16,0))
print("hit rate for twolf.trace =",hitrates("twolf.trace",16,16,0))
print("block size = 4")
# last 2 bits are byte offset as block size is 4(log4=2)
#(64*1024)/4=2^14 so 14 bits for the index
#Remaining 16 bits are for the tag
print("hit rate for gcc.trace =",hitrates("gcc.trace",16,14,2))
print("hit rate for gzip.trace =",hitrates("gzip.trace",16,14,2))
print("hit rate for mcf.trace =",hitrates("mcf.trace",16,14,2))
print("hit rate for swim.trace =",hitrates("swim.trace",16,14,2))
print("hit rate for twolf.trace =",hitrates("twolf.trace",16,14,2))
print("block size = 8")
# last 3 bits are byte offset as block size is 8(log8=3)
#(64*1024)/8=2^13 so 13 bits for the index
#Remaining 16 bits are for the tag
print("hit rate for gcc.trace =",hitrates("gcc.trace",16,13,3))
print("hit rate for gzip.trace =",hitrates("gzip.trace",16,13,3))
print("hit rate for mcf.trace =",hitrates("mcf.trace",16,13,3))
print("hit rate for swim.trace =",hitrates("swim.trace",16,13,3))
print("hit rate for twolf.trace =",hitrates("twolf.trace",16,13,3))
print("block size = 16")
# last 4 bits are byte offset as block size is 16(log16=4)
#(64*1024)/16=2^12 so 12 bits for the index
#Remaining 16 bits are for the tag
print("hit rate for gcc.trace =",hitrates("gcc.trace",16,12,4))
print("hit rate for gzip.trace =",hitrates("gzip.trace",16,12,4))
print("hit rate for mcf.trace =",hitrates("mcf.trace",16,12,4))
print("hit rate for swim.trace =",hitrates("swim.trace",16,12,4))
print("hit rate for twolf.trace =",hitrates("twolf.trace",16,12,4))
print("block size = 32")
# last 5 bits are byte offset as block size is 32(log32=5)
#(64*1024)/32=2^11 so 11 bits for the index
#Remaining 16 bits are for the tag
print("hit rate for gcc.trace =",hitrates("gcc.trace",16,11,5))
print("hit rate for gzip.trace =",hitrates("gzip.trace",16,11,5))
print("hit rate for mcf.trace =",hitrates("mcf.trace",16,11,5))
print("hit rate for swim.trace =",hitrates("swim.trace",16,11,5))
print("hit rate for twolf.trace =",hitrates("twolf.trace",16,11,5))

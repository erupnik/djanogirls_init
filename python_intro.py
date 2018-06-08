import sys, getopt

def main(argv) :
    print(argv)   

     

    print(argv[1])    
    if len(argv)==2 :  
        hi(argv{1})    

def hi(name):
    if name=='ewelina' or name=='Ewelina' :
        print("Ewelina essai d'apprendre django et elle le fait bien!")
    else :
        print("no good name!")


    for i in range (1,6) :
        print(i)

    girls={"a","b","c"}
    for i in girls :
        print(i)

main(str(sys.argv))

#hi("Ewelina")

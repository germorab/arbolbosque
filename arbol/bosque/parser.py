thefile = open("category_labels_es.ttl", "r")


#fileinlist = thefile.readlines()
#print len(fileinlist)


y=0
listadecat = []
for i in thefile:
    
    i = i.strip()[i.find('"')+1:i.rfind('"')]
    
    print i
    

thefile.close()
#return fileinlist

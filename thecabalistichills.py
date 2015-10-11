def parse_input():
   T = int(raw_input())    
   cases = []
   for i in range(1, T + 1):
       dict_name = "dict_" + str(i)
       dict_name = {}
       case = raw_input().split()
       dict_name['N'] = int(case[0])
       dict_name['M'] = int(case[1])
       bridges = []
       for i in range(dict_name['M']):
           bridge = raw_input().strip()
           bridges.append(bridge)
           dict_name['bridges'] = bridges
       cases.append(dict_name)
   # print "T", T
   # print "LIST OF CASES", cases
   return cases

def check_trap(case):
    M = case['M'] #PATHS
    N = case['N'] #HILLS
    conn = case['bridges']
    safe = True
    get_lamp = False
    pass_bridge = 0
    start, end = (conn[0].split())
    start = int(start)
    #print 'start', start
    
    for i in conn:
        hill, to_hill = i.split()
        hill, to_hill = int(hill),int(to_hill)
        #print hill, to_hill
        #print start,to_hill,'and',hill,N
        if to_hill == hill+1:
            safe = True
            pass_bridge += 1
        else: 
            safe = False
        if (hill == N) and (to_hill == start):
            safe = True
            pass_bridge +=1
            
        #print safe
        
    if safe == True and pass_bridge == M:
        print "Go on get the Magical Lamp"
    else:
        print "Danger!! Lucifer will trap you"
    
    #print conn #CONNECTIONS
    
    
cases = parse_input()

#print cases

for case in cases:
   check_trap(case)
# search operation
def find_longest_match (searchWindow, lookaheadWindow):
    
    LWSize = len(lookaheadWindow)
    SWSize = len(searchWindow)
    bestLength = 0
    bestoffset = 0 

    for item in range(SWSize):
        length = 0
        if searchWindow[item] != lookaheadWindow[0]:
            if item == SWSize - 1:
                if bestLength < len(lookaheadWindow):
                    return [bestoffset, bestLength,lookaheadWindow[bestLength]]
            else: continue


        while item + length < SWSize and length < LWSize and searchWindow[item + length] == lookaheadWindow [length]:
            length += 1

        #redundancies handling -- aaaa -- abcabc
        
        overloading = 0 #NewCounter for redundancies 
        offset = SWSize - item  
        
        while length > 0 and length + overloading < LWSize:  #to insure the correct window.
            target_index = item + ((length + overloading) % offset)   #5%3=2 -- to make the correct compartion.
            
            if target_index < SWSize and searchWindow[target_index] == lookaheadWindow[length + overloading]: ## if the comparied letter == the one in the offset search window 
                overloading += 1 
            else:
                break
        length += overloading
        #----------------
        if length > bestLength:
            bestLength = length
            bestoffset = SWSize - item
        elif length == bestLength:
            if SWSize - item > bestLength:
                bestLength = length
                bestoffset = SWSize - item

        # overloading = 0
        # while bestLength > 0 and length + overloading < LWSize and searchWindow[(item + length + overloading) % bestLength ] == lookaheadWindow [length + overloading]:
        #     overloading += 1


    if len(lookaheadWindow) > bestLength:
        return [bestoffset,bestLength,  lookaheadWindow[bestLength] ] 
    return [bestoffset,bestLength,""]


def compress(originalData):

    # items initialization 
    pointer = 0
    searchWindow = []
    SWSize  = len(originalData) // 2
    LWSize = len(originalData) - SWSize
    lookaheadWindow = []

    # fill lookahead window first time
    for i in range(LWSize):
        lookaheadWindow.insert(i, originalData[i])

    # # DEBUGING
    # print("POINTER:",pointer)
    # print("SW:", searchWindow)
    # print("LW:", lookaheadWindow)

    tags = []
    while lookaheadWindow:
        tag = find_longest_match(searchWindow,lookaheadWindow) # [ offset , length, char ]
        updatorS = pointer
        updatorL = pointer

        if tag[0] == 0 and tag[1] == 0:

            # print("Pointer at 0 0 s", pointer)
            # update search window
            if searchWindow and len(searchWindow) == SWSize:
                searchWindow.pop(0)
            searchWindow.insert(len(searchWindow), originalData[updatorS])
        
            # update lookahead window
            # print("pointer at 0 0 l", pointer)
            pointer += tag[1] + 1

            updatorL = pointer
            lookaheadWindow.clear()
            for indx in range(LWSize):
                if updatorL + indx < len(originalData):
                    lookaheadWindow.insert(len(lookaheadWindow),originalData[updatorL + indx])
            
            tags.insert(len(tags),tag)
        
            #     # DEBUGING
            # print("TAG:", tag)
            # print("POINTER:", pointer)
            # print("SW:", searchWindow)
            # print("LW:", lookaheadWindow)
            # print("-------------------------------")
            continue

        # update search window 
        for indx in range(tag[1] + 1):
            if searchWindow and len(searchWindow) == SWSize:
                searchWindow.pop(0)
            if updatorS < len(originalData):
                searchWindow.insert(len(searchWindow), originalData[updatorS])
                updatorS += 1

        pointer += tag[1] + 1
        # update lookahead window 
        updatorL = pointer
        # print("P", pointer)
        lookaheadWindow.clear()
        for indx in range(LWSize): 
            if updatorL + indx < len(originalData):
                lookaheadWindow.insert(len(lookaheadWindow), originalData[updatorL + indx])
        
        tags.insert(len(tags),tag)

        # # DEBUGIN 
        # print("TAG:", tag)
        # print("POINTER:", pointer)
        # print("SW:", searchWindow)
        # print("LW:", lookaheadWindow)
        # print("-------------------------------")
    
    return tags



originalData = list(input("Enter your Text to compression:"))
tags = compress(originalData)

print(tags)





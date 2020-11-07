
def analyze(tree):
    chunk_chunk, chunk_token = relationship(tree)
    devided = analysing(chunk_chunk)
    return analysing2(chunk_chunk, chunk_token)
    '''
    print(chunk_token)
    for i in range(len(chunk_token)):
        for j in range(len(chunk_token[i])):
            print(i, j, chunk_token[i][j].text)
    '''
    #print_devided(devided, chunk_token)

    devided = delete_empty(devided)
    
    #print_devided(devided, chunk_token)

    #print(devided)
    flags = have_noun(devided, chunk_token)
    
    res = modeling_word(flags, tree, devided, chunk_token)
    #print(res)
    
    return res
    
    
def analysing(cc):
    devided = []
    add_list = []
    #add_after = {}
    link_list = [-1]
    
    for i in range(len(cc)): 
        #print('ini',i, link_list, add_list, link_list[-1])
        if cc[i] != None:            
            #print('i',i, 'chunk_id',cc[i].chunk_id)
            #print('link_list',int(link_list[-1]), 'i',i, 'add_list',add_list)
            #print('c1', cc[i].chunk_id, 'link:',link_list, 'add_list', add_list, 'af', add_after, 'dev', devided)
            if int(link_list[-1]) == i:
                #print('bunki1')
                if len(add_list) == 0:
                    add_list.append(i-1)
                add_list.append(i)
                link_list[-1] = cc[i].chunk_id
                link_list = sorted(set(link_list), key=link_list.index)
            elif len(add_list) != 0:
                #print('bunki2')
                devided.append(add_list)
                link_list.pop(-1)
                add_list = []

            #print('add', cc[i].chunk_id, link_list)
            if cc[i].chunk_id not in link_list:
            #if cc[i].chunk_id != link_list[-1]:
                link_list.append(cc[i].chunk_id)
                
            #print('end', cc[i].chunk_id, 'link:',link_list, 'add', add_list, 'af', add_after, 'dev', devided)
                    
        else:
            #print('None')
            devided.append(add_list)
            link_list.pop(-1)
            try:
                add_list = [link_list[-1]]
            except:
                pass
            
        #print()
    
    if len(add_list) != 0:
        devided.append(add_list)
        try:
            devided[-1].insert(0,0)
        except:
            pass

    #print(devided)
    return devided

#-----------------------------------------------------------
def analysing2(chunk_chunk, chunk_token):
    devided = []
    to = []
    to_stack = []
    hierurchy = []
    empty_stack = 0

    #--------------------------------------------#
    #                 stage1                     #
    #--------------------------------------------#
    for i, cc in enumerate(chunk_chunk):
        #if cc != None:
            #print("start  i: ", i, "id: ", cc.chunk_id, "devided: ", devided, "to: ", to, "stack: ", to_stack, "hie", hierurchy)
        #else:
            #print("None start  i: ", i, "devided: ", devided, "to: ", to, "stack: ", to_stack, "hie", hierurchy)
        try:
            if cc != None:
                if i in hierurchy:
                    hierurchy.remove(i)
                    
                if len(hierurchy) == 0:
                    empty_stack = 1
                else:
                    empty_stack = 0
                #print(empty_stack)
                    
                if cc.chunk_id > i+1:
                    if cc.chunk_id not in hierurchy:
                        hierurchy.append(cc.chunk_id)
                    
                if to.count(i) > 1:
                    #print("switch 1")
                    devided.append([i])
                    if (cc.chunk_id not in to) and (empty_stack != 1):
                        to.append(cc.chunk_id)
                        
                    to_stack.append(i-1)
                    to_stack.append(i)
                elif i == to[-1]:
                    #print("switch 2")
                    devided[-1].append(i)
                    if (cc.chunk_id not in to) and (empty_stack != 1):
                        to.append(cc.chunk_id)
                    if cc.chunk_id > i+1:
                        to_stack.append(i)
                        to_stack.append(i+1)
                else:
                    #print("switch 3")
                    devided.append([i])
                    to.append(cc.chunk_id)
                    if cc.chunk_id not in to:
                       to_stack.append(i)
            else:
                #print("else")
                if to.count(i) > 1:
                    devided.append([i])
                    to_stack.append(i-1)
                    to_stack.append(i)

                elif i == to[-1]:
                    devided[-1].append(i)
                    #if cc.chunk_id > i+1:
                    #    to_stack.append(i)
                    #    to_stack.append(i+1)
                else:
                    devided.append([i]) 
                    to_stack.append(i)               
        except:
            #import traceback
            #traceback.print_exc()
            
            #print("None")
            if i == 0:
                if cc == None:
                    #print("i == 0 and cc == None")
                    break
                    
            devided.append([i])
            to.append(cc.chunk_id)
            to_stack.append(i)
            to_stack.append(i+1)
                
        #if cc != None:
            #print("end  i: ", i, "id: ", cc.chunk_id, "devided: ", devided, "to: ", to, "stack: ", to_stack, "hie", hierurchy)
        #else:
            #print("end  i: ", i, "devided: ", devided, "to: ", to, "stack: ", to_stack, "hie", hierurchy)
        #print()

        
    #print("devided: ", devided)

    
    #--------------------------------------------#
    #                 stage2                     #
    #--------------------------------------------#
    ref_to = [[] for _ in range(len(devided))]
    ref_from = [[] for _ in range(len(devided))]
    #print(len(chunk_chunk))

    for i, dev in enumerate(devided):
        if len(dev) > 1:
            continue
        for j, search in enumerate(devided):
            if chunk_chunk[dev[0]] != None:
                if chunk_chunk[dev[0]].chunk_id in search:
                    ref_to[i].append(j)
                    ref_from[j].append(i)
            else:
                if len(chunk_chunk)-1 in search:
                    ref_to[i].append(j)
                    ref_from[j].append(i)

    #print("ref_to: ", ref_to, "ref_from: ", ref_from)

    
    #--------------------------------------------#
    #                 stage3                     #
    #--------------------------------------------#
    print_stack = []
    print_result = []
    print_add = ""
    joint_flag = 0
    print_hierurchy = []
    

    #print()
    #print("result_print")
    #print()
    for i in range(len(ref_to)):
                
        #print("hie", print_hierurchy)
        
        if len(ref_to[i]) > 0:
            if ref_to[i][0] not in print_stack:
                try:
                    #print("aaa", devided[ref_to[i][0]][-1],  print_hierurchy[-1])
                    if devided[ref_to[i][0]][-1] > print_hierurchy[-1]:
                        print_hierurchy.pop(-1)
                        #print("poped: ", print_hierurchy)
                except:
                    pass
            
                for chunk in ref_from[ref_to[i][0]]:
                    for dev in devided[chunk]:
                        for word in chunk_token[dev]:
                            print_add += word.text
                            #print(word.text, end='')
                    #print('', end='-')
                #print()
                #print(len(ref_from[ref_to[i][0]]), ref_from[ref_to[i][0]][0], i)
                if len(ref_from[ref_to[i][0]]) == 1 and ref_from[ref_to[i][0]][0] == i:
                    pass
                else:
                    #print("len: ", len(print_hierurchy))
                    if len(print_hierurchy) > 0:
                        print_add = len(print_hierurchy)*"___"+"・" + print_add
                    print_result.append(print_add)
                    print_add = ""
                
                if ref_to[i][0] not in print_stack:
                    print_stack.append(ref_to[i][0])
                if chunk_chunk[devided[ref_to[i][0]][-1]] != None:
                    if chunk_chunk[devided[ref_to[i][0]][-1]].chunk_id not in print_hierurchy:
                        print_hierurchy.append(chunk_chunk[devided[ref_to[i][0]][-1]].chunk_id)
                else:
                    if len(chunk_chunk)-1 not in print_hierurchy:
                        print_hierurchy.append(len(chunk_chunk)-1)
        else:
            try:
                #print("aa", devided[i][-1], print_hierurchy[-1])
                if devided[i][-1] > print_hierurchy[-1]:
                    print_hierurchy.pop(-1)
                    #print("poped: ", print_hierurchy)
            except:
                pass

            for dev in devided[i]:
                for word in chunk_token[dev]:
                    print_add += word.text
                    #print(word.text, end='')
                #print('', end='-')
            #print()
            if len(print_hierurchy) > 0:
                print_add = len(print_hierurchy)*"___"+"・" + print_add
            print_result.append(print_add)
            print_add = ""
            if chunk_chunk[devided[i][-1]] != None:
                if chunk_chunk[devided[i][-1]].chunk_id not in print_hierurchy:
                    print_hierurchy.append(chunk_chunk[devided[i][-1]].chunk_id)
            else:
                if len(chunk_chunk)-1 not in print_hierurchy:
                    print_hierurchy.append(len(chunk_chunk)-1)


        '''
        try:
            if ref_to[i][0] not in print_hierurchy:
                print_hierurchy.append(ref_to[i][0])
        except:
            pass
        '''

    #print()
    for word in print_result:
        print(word)
    return print_result


def print_devided(devided, chunk_token):
    print()
    for dev in devided:
            #print(dev)
            if dev != None:
                for dev_elem in dev:
                    #print('elem', dev_elem)
                    for token in chunk_token[dev_elem]:
                        print(token.text, end='')
                    print("", end='-')


def delete_empty(devided):
    res = []
    for i, area in enumerate(devided):
        if len(area) != 0:
            res.append(area)
            
    return res 

    
def have_noun(devided, chunk_token):
    res = []
    flag = False
    
    for area in devided:
        flag = False
        for i, word in enumerate(chunk_token[area[-1]]):
            #print(word.text, word.surface)
            if word.surface == '名詞':
                flag = True
        res.append([flag, i])
        #print('end')

    #print(res)
    return res

def modeling_word(flags, tr, devided, chunk_token):
    String = []
    add_chunk = ''
    add_str = ''
    
    for f, dev in zip(flags, devided):
        #print(f)
        if f[0] == True:
            add_chunk += '要素: '
        else:
            add_chunk += '動作: '
            
        for d in dev:
            for token in chunk_token[d]:
                add_str += token.text
                #print(token.text)
            add_chunk += add_str
            add_str = ''
        String.append(add_chunk)
        #print(add_str)
        #print(String)
        add_chunk = ''
    #print(add_str)
    return String
            
def relationship(tr): 
    chunk_num = len(tr.chunk_list)
    token_num = len(tr.token_list)
    #print(chunk_num, token_num)
    chunk_token, chunk_chunk = [], []

    
    #print(tr.chunk_list)
    for to_token in tr.chunk_list:
        #print(to_token.chunk_id)
        chunk_token.append([token for token in tr.token_list if token.chunk_id == to_token.chunk_id])
    #for ct in chunk_token:
    #    for token in ct:
    #        print(token.text)
    #    print()
         
    for to_chunk in tr.chunk_list:
        if to_chunk.link[0] != '-':
            chunk_chunk.append(tr.chunk_list[int(to_chunk.link)])
        else:
            chunk_chunk.append(None)
            #print(tr.chunk_list[int(to_chunk.link)].chunk_id)
    #for cc in chunk_chunk:
    #    if cc != None:
    #        print(cc.chunk_id)
    #    else:
    #        print(-1)
    
    return chunk_chunk, chunk_token

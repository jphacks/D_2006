
def analyze(tree):
    chunk_chunk, chunk_token = relationship(tree)

    devided = analysing(chunk_chunk)
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
    
    res = modeling_word(flags, tree, devided[0:-1], chunk_token)
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
            add_list = [link_list[-1]]
            
        #print()
    
    if len(add_list) != 0:
        devided.append(add_list)
    try:
        devided[-1].insert(0,0)
    except:
        return [[]]

    #print(devided)
    return devided

def print_devided(devided, chunk_token):
    print()
    for dev in devided:
            #print(dev)
            if dev != None:
                for dev_elem in dev:
                    #print('elem', dev_elem)
                    for token in chunk_token[dev_elem]:
                        print(token.text, end='')
                print()


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

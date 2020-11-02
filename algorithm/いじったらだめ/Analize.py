
def analyze(tree):
    chunk_chunk, chunk_token = relationship(tree)
    #layer = []
    
    f = open('parse_result2.txt')
    text = f.read().splitlines()
    f.close()
    print(text)

    analysing(chunk_chunk)
    
    #attributes = add_attribute(chunk_token)

def analysing(chunk_chunk):
    devided = []
    add_list = []
    link_list = []
    #link_list = chunk_chunk[0]
    old = 0
    
    for i, cc in enumerate(chunk_chunk):
        if cc != None:
            link_list.append(cc)
            if link_list[-1] == i:
                pass
                
    
def relationship(tr): 
    chunk_num = len(tr.chunk_list)
    token_num = len(tr.token_list)
    #print(chunk_num, token_num)
    chunk_token, chunk_chunk = [], []
    
    for to_token in tr.chunk_list:
        chunk_token.append([token for token in tr.token_list if token.chunk_id == to_token.chunk_id])
    #for ct in chunk_token:
    #    for token in ct:
    #        print(token.text)
    #    print()
         
    for to_chunk in tr.chunk_list:
        if to_chunk.link != '-':
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

def add_attribute(chunk_token):
    attributes = []
    for i, ct in enumerate(chunk_token):
        for j, ps in enumerate(ct):
            if ps.surface != '名詞':
                if ps.surface == '助詞':
                    if  ps.detail1 == '格助詞':
                        if   ps.detail2 == '連語':
                            attributes.append(["equal", i])
                            break
                        elif ps.detail2 == '一般':
                            attributes.append(["←target", i])
                            break
                        else:
                            attributes.append(["格助詞", i])
                            break
                    elif   ps.detail1 == '係助詞':
                        attributes.append(["is", i])
                        break
                    elif ps.detail1 == '連体化':
                        attributes.append(["of", i])
                        break
                    elif ps.detail1 == '連体化':
                        attributes.append(["of", i])
                        break
                    else:
                        attributes.append(["助詞", i])
                        break
                else:
                    attributes.append(["unknown", i])
                    break
                
    #print(attributes)
    
    return attributes
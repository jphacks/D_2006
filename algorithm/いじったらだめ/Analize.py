
def analyze(tree):
    chunk_chink, chunk_token = relationship(tree)

def relationship(tr): 
    chunk_num = len(tr.chunk_list)
    token_num = len(tr.token_list)
    #print(chunk_num, token_num)
    chunk_token, chunk_chunk = [], []
    
    for to_token in tr.chunk_list:
        chunk_token.append([token for token in tr.token_list if token.chunk_id == to_token.chunk_id])
    '''
    for ct in chunk_token:
        for token in ct:
            print(token.text)
        print()
    '''
         
    for to_chunk in tr.chunk_list:
        if to_chunk.link != '-':
            chunk_chunk.append(tr.chunk_list[int(to_chunk.link)])
        else:
            chunk_chunk.append(None)
            #print(tr.chunk_list[int(to_chunk.link)].chunk_id)

    """
    for cc in chunk_chunk:
        if cc != None:
            print(cc.chunk_id)
        else:
            print(-1)
    """
    
    return chunk_chunk, chunk_token
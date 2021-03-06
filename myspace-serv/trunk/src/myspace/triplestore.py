'''
Created on 1 Feb 2010

@author: kurtjx
'''

from config import ENDPOINT
from HTTP4Store import HTTP4Store

class TripleStore:
    '''
    Simple container for the interfacing with the triple store
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.store = HTTP4Store(ENDPOINT)
        
    def insert(self, content, graph, format="xml"):
        r = self.store.add_graph(uri=graph, content=content, content_type=format)
        if not (r.status == 201 or r.status == 200):
            raise TripleStoreInsertException(content)
        
    def query(self, query):
        return self.store.sparql(query)
    
    def delete_graph(self, graph):
        self.store.del_graph(graph)

class TripleStoreInsertException(Exception):
    '''Insertion error: '''
    def __init__(self, msg):
        self.msg = msg 
        
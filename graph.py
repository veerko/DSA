from collections import deque
# BFS

graph = {}
graph['you'] = ['Bob', 'Alice', 'Claire']
graph['Bob'] = ['Peggy', 'Anuj']
graph['Alice'] = ['Peggy']
graph['Claire'] = ['Johnny', 'Thonny']
graph['Anuj'] = []
graph['Peggy'] = []
graph['Johnny'] = []
graph['Thonny'] = []


search_queue = deque()
search_queue += graph['you']

def person_is_seller(person):
    if person == 'Peggy':
        return True


while search_queue:
    person = search_queue.popleft()
    if person_is_seller(person):
        print(f'This {person} is Mango Seller.')
        search_queue = False
    else:
        search_queue += graph[person]
        
    



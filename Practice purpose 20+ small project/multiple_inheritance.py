# Multiple inheritance

class Family:
    def __init__(self, address) -> None:
        self.address = address
        
class School:
    def __init__(self , id, level) -> None:
        self.id = id
        self.level = level
    
class Sports:
    def __init__(self , game) -> None:
        self.game = game
        
class Students(Family, School , Sports):
    def __init__(self, address , id, level, game) -> None:
        School.__init__(self, id, level)
        Family.__init__(self, address)
        Sports.__init__(self, game) 
            
        
# cnt = {}
# i = 1
# if  i not in cnt:
#     cnt[i] = 1
# else:
#     cnt[i] += 1

# print(cnt )
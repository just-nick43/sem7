class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight= weight
        
def fractionalKnapsack(Knapsack, arr):
    arr.sort(key = lambda x: (x.value/x.weight), reverse=True)
    finalvalue = 0.0
    weight = 0
    
    for item in arr:
        if weight + item.weight <= Knapsack:
            weight += item.weight
            finalvalue += item.value
        else:
            remaining_weight = Knapsack - weight
            finalvalue += item.value * remaining_weight / item.weight
            break
            
    return finalvalue

#Weight of Knapsack
Knapsack = 50
arr = [Item(60, 10), Item(100, 20), Item(120, 30)]

max_val = fractionalKnapsack(Knapsack, arr)
print ('Maximum value we can obtain = ',max_val)
toxic = ["anjing", "babi", "kampret", "monyet"]

def sensor(kata) :
    for huruf in toxic :  
        kata = kata.replace(huruf, "*" * len(huruf))
    
    return kata

# * говорит о перечислениях из списка(который был создан из последовательности x

def minimum(*x): 
    m = x[0] 
    for i in x:
        if i < m:  # Для максимума меняем на >
            m = i
    return m
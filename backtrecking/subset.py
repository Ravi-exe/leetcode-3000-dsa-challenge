


def sol():
    """
        [1 2 3 4]
        1 
            234  
        3 
            34
        4 

        1

    2     
     
    3
    
    4 
    """

    a=[1,2,3]
    result = [[]]

    for i in range(len(a)):
        ini = a[i]
        def recursion(ind, temp = []):
            if ind == len(a):
                return temp.append(a[ind])
            
            recursion(ind + 1, temp)
            

            
            
    return result
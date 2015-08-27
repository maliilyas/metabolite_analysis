'''
Created on Aug 27, 2015

@author: Ali Ilyas

we have two columns C1 and C2 like following;

C1  C2
1   a      
1   a
1   x  
1   z 
2   a
2   y 
3   x
3   x
3   x
3   z

and we have to get some thing like
1   a(2)      
    x(1)
    z(1)  
2   a(1)      
    y(1) 
3   x(3)      
    z(1)
'''

def counting_columns(C1 , C2):
    assert len(C1) == len(C2), "The lengths of both columns should be the same."; # asserting the lengths
    assert len(C1) > 0 , "The lengths of both columns should be greater than 0"; # The columns shldnt be empty
    C1_element = C1[0];
    start = 0;
    end   = 0;
    large_dick = {}
    for _ in range(0,len( C1)):
        element = C1[_]
        if(element != C1_element):
            start = end # previous end of the element change
            end = _;
            large_dick[C1_element] = count_unique_elements(C2, start, end)
            C1_element = element
    if(end < len(C1)): # means that last element has to be added in large_dick
        large_dick[C1_element] = count_unique_elements(C2, end, len(C1))

    
    return large_dick        
            
def count_unique_elements(C2 , start,end):
    dick = {}
    for _ in range(start,end):
        element = C2[_];
        if (dick.has_key(element)):
            val = dick.get(element);
            val = val + 1;
            dick[element] = val;
        else:
            dick[element] = 1;
    return dick;
            
              
if __name__ == '__main__':
    C1 = [1,1,1,1,2,2,3,3,3,3]
    C2 = ['a','a','x','z','a','y','x','x','x','z']
    print(counting_columns(C1, C2))


def hanoi(n,source,spare,target):
    '''
    objective:to solve problem of tower of hanoi using n discs and 3 poles
    input parameters:n,source,spare,target:numeric value
    return value:none
    '''

    assert n>0
    if n==1:
        print ('Move a disk from',source,'to',target)
    else:
        hanoi(n-1,source,target,spare)
        print('Move a disk from',source,'to',target)
        hanoi(n-1,spare,source,target)

hanoi(3,1,2,3)

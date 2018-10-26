

def lights(state,n,m,v,start_num,seq,print_seq=False):
    '''The base case for recursion. We've no more moves to try, to check if we are in a valid state'''
    if m==0:
        if success(state,v):
            if print_seq:
                print(seq)
            return 1
        else:
            return 0
    else:
        successes=0
        '''Test each move, each time we iterate through the loop we explore another branch
        keeping track of the current move in the recursion means we only try moves in increasing order
        thus don't need to worry about counting ordering of the same sets of moves.'''
        for i in range(start_num,2**n):
            new_seq=[]
            if print_seq:
                new_seq=seq.copy()
                new_seq.append(i)
            '''recursive call, advance the state, decrease moves and increment next move.
            the key here is the next state is just an XOR of the current move with the current state'''
            successes+=lights(state^i,n,m-1,v,i+1,new_seq,print_seq)
        return successes


'''test to see if we are in the goal state
using binary encoding. Eg. (2^2-1) = 3 = 0b011 if we have 3 lights, indicating first 2 lights are on only.'''
def success(state,v):
    return state == (2**v)-1

#Wrap the recursive function
def solve(n,m,v,print_seq=False):
    #start with no lights on, start move is do nothing, empty move sequence.
    return lights(0,n,m,v,0,[],print_seq)

def choose(n,r):
    from math import factorial as f
    return (f(n)//(f(r)*f(n-r)))

'''There is some closed form solution for odd m. I kind of know why, but mainly found it by tinkering
I'm not sure if I'll figure it out for even m. This is because there's a different number of moves for n=0 to n >1
which is not the case with odd m. Something to do with abelian groups? (I don't know maths...)'''
def solve_fast(n,m,v):
    if m % 2 ==1:
        return choose(2**n-1,m)//(2**n-m)
    else:
        return solve(n,m,v)




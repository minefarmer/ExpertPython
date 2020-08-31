# FACTORY FUNCTIONS OR CLOSURES

def maker(N):
    # nested function
    def action(X):
        return X**N
    return action
    
act1 = maker(2)
res1 = act1(4)
print('Square of 4',res1)  # Square of 4 16
act2 = maker(3)
res2 = act2(4)
print('cube of 4:',res2)  # cube of 4: 64

# for act1 value of N is still 2 because of state of retention
res3 = act1(3)
print('Square of 3:', res3)  # Square of 3: 9


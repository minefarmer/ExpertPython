# FACTORY FUNCTIONS OR CLOSURES

def maker(N):
    # nested function
    def action(X):
        return X**N
    return action
    
act1 = maker(2)
res1 = act1(4)
print('Square of 4',resl) # Traceback (most recent call last):
                            # File "c:\Users\pgold\MatHub\ExpertPython\ClassWork\ExpertGuide\FactoryClosures.py", line 11, in <module>
                        #     print('Square of 4',resl)
                        # NameError: name 'resl' is not defined
act2 = maker(3)
res2 = act2(4)
print('cube of 4:',res2)
# for act1 value of N is still 2 because of state of retention
res3 = act1(3)
print('Square of 3:', res3)


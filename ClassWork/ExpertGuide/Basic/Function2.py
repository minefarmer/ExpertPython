# Factory functions or clousers

def maker (N):
    # nested Function
    def action (X):
        return X**N
    return action

act1 = maker(2)
res1 = act1(4)
print('Square of 4:',res1)  # Square of 4: 16
act2 = maker(2)
res2 = act2(4)
print('cube of 4:',res2)  # cube of 4: 16
# for act1 value of N is still 2 because of state retention
res3 = act1(3)
print('Square of 3:',res3)  # Square of 3: 9

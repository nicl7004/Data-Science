from scipy import zeros

def swag(tl, tr, bl, br):
    obs = zeros((2,2))

    obs[0][0], obs[0][1], obs[1][0], obs[1][1] = tl, tr, bl, br


    obsTotal = obs[0][0] + obs[0][1] + obs[1][0] + obs[1][1]
    topRowSum = obs[0][0] + obs[0][1]
    bottomRowSum = obs[1][0] + obs[1][1]
    leftColSum = obs[0][0] + obs[1][0]
    rightColSum = obs[0][1] + obs[1][1]

    print("top row sum", topRowSum)
    print("right  col sum", rightColSum)

    ex = zeros((2, 2))
    ex[0][0] = leftColSum * topRowSum * 1/obsTotal
    ex[0][1] = rightColSum * topRowSum *1/obsTotal
    ex[1][0] = leftColSum * bottomRowSum *1/obsTotal
    ex[1][1] = rightColSum * bottomRowSum * 1/obsTotal

    return obs, ex
x = swag(8,4667, 15820, 14287181)
print("obs =", x[0])
print("ex =", x[1])

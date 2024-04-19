"""
Script to compute in a systematic manner the calibration coefficients for
gravitational model, transport demand.
"""

# number of travels as a matrix with produced travels on lines
# and attracted travels on columns

travs = [[40, 110, 150],
         [50, 20, 30],
         [110, 30, 10]]

# the matching friction factors, same arrangement

ffs = [[0.753, 1.597, 0.753],
       [0.987, 0.753, 0.765],
       [1.597, 0.765, 0.753]]

def gravmod(travs,ffs):
    """
    Function to compute gravitational model values in order to determine the
    calibration factors.
    Takes as input the travels and friction factors matrices.
    Returns a matrix with computed values.
    """
    
    # check if the matrices have the same shape
    if(len(travs) != len(ffs)):
        print("The matrices doesn't match. Please fix it.")
        exit()
    
    # transpose de matrices
    travs_tt = list(zip(*travs))
    ffs_tt = list(zip(*ffs))
    travs_t = [list(sublist) for sublist in travs_tt]
    ffs_t = [list(sublist) for sublist in ffs_tt]
    # print(travs_t)
    # print(ffs_t)
    
    # get attracted travels sums (cycling on transposes)
    s_Aj = []   # store the attracted sums

    for item in travs_tt:
        s_Aj.append(sum(item))

    # get produced travels sums
    s_Pi = []
    for item in travs:
        s_Pi.append(sum(item))
    
    # compute travels with gravitational model
    gvals = []    # store values
    for i in range(len(travs)):
        pdsum = 0
        for j1, j2 in zip(s_Aj, ffs[i]):
            pdsum = pdsum + j1 * j2
            print(pdsum)
            print(ffs[i])
        for k1 in range(len(ffs[i])):
            gvals.append((s_Pi[i] * ffs[k1] * s_Aj[k1] / pdsum))
            print(gvals)
    # list to store values
    cmb = []
    # zip transposed lines as separate variables
    for i in range(len(travs_t)):
        t = list(zip(travs_t[i], ffs_t[i]))
        # cmb.append(t)
        # print(t)
        s = 0
        for item in t:
            pd = item[0] * item[1]
            s = s + pd

        cmb.append(s)
    
    # print(cmb)
    """
    cmb2 = []
    for item in cmb:
        sm = 0
        for item in item:
            #print(item[0], item[1])
            pd = item[0] * item[1]
            # print(sm)
            # sm = sm + pd
        # cmb2.append(sm)
    """

                

    # print(travs[0])
    # print(len(travs))


gravmod(travs, ffs)

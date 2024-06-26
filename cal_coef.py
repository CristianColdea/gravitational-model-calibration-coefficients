"""
Script to compute in a systematic manner the calibration coefficients for
gravitational model, transport demand.
Also, the travels weights using LOGIT model are computed.
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

# neutral calibration coefficients
k_ij0 = [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]

# auto travels cost

tca = [[0.5, 1, 1.4],
       [1.2, 0.8, 1.2],
       [1.7, 1.5, 0.7]]

# transit travels cost
tct = [[1, 1.5, 2],
       [1.8, 1.2, 1.9],
       [1.7, 1.5, 0.7]]

# auto travels duration
tda = [[3, 12, 7],
       [13, 3, 19],
       [9, 16, 4]]

# transit travels duration
tdt = [[15, 5, 12],
       [15, 6, 26],
       [20, 21, 8]]

# the future friction factors
ffs_f = [[0.753, 0.987, 1.597],
         [0.987, 0.753, 0.765],
         [1.597, 0.765, 0.753]]

def gravmod(travs,ffs, k_ij):
    """
    Function to compute gravitational model values in order to determine the
    calibration factors.
    Takes as input the travels, calibration coefficients and friction factors matrices.
    Returns a matrix with calibration factors.
    """
    
    # check if the matrices have the same shape
    if(len(travs) != len(ffs) or (len(travs) != len(k_ij))):
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
    gvals = []    # to store computed values
    for i in range(len(travs)):
        pdsum = 0
        for j1, j2 in zip(s_Aj, ffs[i]):
            pdsum = pdsum + j1 * j2
            # print(pdsum)
            # print(ffs[i])
        for k1 in range(len(ffs[i])):
            gvals.append((s_Pi[i] * ffs[i][k1] * s_Aj[k1] * k_ij[i][k1] / pdsum))

    print("Travel obtained with gravitational model, ", gvals)

    # check raw produced travels
    gvals_m0 = [gvals[i:i + 3] for i in range(0, len(gvals), 3)]
    # print(gvals_m0)

    
    for p1, p2 in zip(travs, gvals_m0):
        print(round(sum(p1)) == round(sum(p2)))
        print(sum(p2))

    # round the number of travels
    gvalsr = []
    for item in gvals:
        gvalsr.append(round(item))
    
    print("Rounded number of travels, ", gvalsr)

    # group flatten list 'gvalsr' as a matrix
    gvals_m = [gvalsr[i:i + 3] for i in range(0, len(gvalsr), 3)]
    # print(gvals_m)
    # print("Matrix of rounded numbers, ", gvals_m)

    # check produced travels sum
    for p1, p2 in zip(travs, gvals_m):
        print(sum(p1) == sum(p2))

    # check attracted travels sum
    # transpose the matrix first
    gvals_m_tt = list(zip(*gvals_m))
    # print(gvals_m_tt, travs_tt)
    for a1, a2 in zip(gvals_m_tt, travs_tt):
        print(sum(a1) == sum(a2))
        print(sum(a1))
        print(sum(a2))

    """
    After rounding the values obtained with gravitational model, when
    ckecking the produced and attracted travels (lines 104-114),
    the travels sums on lines (i.e., produced travels) are equal to
    the historical data, but not on columns (i.e., attracted travels).
    Suggested approach: maintain the sums on lines and move from the exceeding
    sums on columns to the column with less travels.
    After rounding:
    [[82, 140, 78],
     [43, 26, 31],
     [82, 197, 146]].
    Sums on lines are okay, [300, 100, 150], but on columns are
    [207, 197, 146] instead of [200, 160, 190]. There is clearly and excedent
    on columns 1 and 2 and a lack of on column 3. Remove as much as possible
    from the exceeding columns and maintain the sums on lines, i.e. move 7 from
    column 1 to 3 on the line with the highest value (line 3), move 30 from
    column 2 to 3, on line 1 (highest value), and move 7 from column 2 to 3, on line 2.
    The final travels matrix will be:
    [[82, 110, 108],
     [43, 19, 38],
     [75, 31, 44]].
    """

    return gvalsr

# introduce flatten computed travels after rounding and adjustment
gvalsradj = [82, 110, 108, 43, 19, 38, 75, 31, 44]

def ccoeffs(gvalsradj, travs):
    # compute calibration coefficients
    ccoeffs = []
    # flatten the travels matrix
    unpck_travs = [value for row in travs for value in row]
    # print(unpck_travs)
    for c_obs, c_comp in zip(unpck_travs, gvalsradj):
        ccoeffs.append(round(c_obs / c_comp, 2))

    # print(ccoeffs)

    return ccoeffs

# function for modal option
def modopt(tca, tct, tda, tdt):
    """
    Function to compute modal option, i.e. auto and transit.
    Takes as inputs the matrices of travels cost, auto and transit, and
    duration, respectively.
    Returns the weights of auto and transit travels for each zone to zone
    combination.
    """
    # compute utilities for auto and transit modes
    u_a = []    # store auto utility results
    u_t = []    # store transit utility results

    for i in range(len(tca)):
        for ca, da in zip(tca[i], tda[i]):
            u_a.append(2.5 - 0.5 * ca - 0.01 * da)
        for ct, dt in zip(tct[i], tdt[i]):
            u_t.append(-0.4 * ct - 0.012 * dt)

    # print("Auto utilities, ", u_a)
    # print("Transit utilities, ", u_t)

    return (u_a, u_t)

# function to compute auto and transit weight, from to each zone
def logit(u_a, u_t):
    """
    Function to compute travels weights for each zone.
    Takes as inputs the utilities lists, auto and transit.
    Returns auto and transit weights for each zone to zone combination.
    """
    # import to get Euler number
    from math import e
    # print("e, ", e)

    w_a = []    # store auto weights
    w_t = []    # store transit weights
    for u_a, u_t in zip(u_a, u_t):
        w_i = e**u_a / (e**u_a + e**u_t)
        # print(w_i)
        w_i = round(w_i, 2)
        # print(w_i)
        # w_a.append(w_i)
        w_t.append(round(1-w_i, 2))

    # print("Auto travels weights, ", w_a)
    # print("Trasit travels weights, ", w_t)

    return (w_a, w_t)

gvalsr = gravmod(travs, ffs, k_ij0)

# print(gvalsr)

# print(gvalsradj)
ccoeffs = ccoeffs(gvalsradj, travs)

# print(ccoeffs)

ccoeffs_m = [ccoeffs[i:i + 3] for i in range(0, len(ccoeffs), 3)]


# print(ccoeffs_m)

u_a, u_t = modopt(tca, tct, tda, tdt)

w_a, w_t = logit(u_a, u_t)

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
    gvals = []    # to store computed values
    for i in range(len(travs)):
        pdsum = 0
        for j1, j2 in zip(s_Aj, ffs[i]):
            pdsum = pdsum + j1 * j2
            # print(pdsum)
            # print(ffs[i])
        for k1 in range(len(ffs[i])):
            gvals.append((s_Pi[i] * ffs[i][k1] * s_Aj[k1] / pdsum))

    print(gvals)
    # round the number of travels
    gvalsr = []
    for item in gvals:
        gvalsr.append(round(item))
    
    print(gvalsr)

    # group flatten as a matrix
    gvals_m = list(zip(*[iter(gvalsr)]*3))
    print(gvals_m)

    # check produced travels sum
    for p1, p2 in zip(travs, gvals_m):
        print(sum(p1) == sum(p2))

    # check attracted travels sum
    # transpose the matrix first
    gvals_m_tt = list(zip(*gvals_m))
    print(gvals_m_tt, travs_tt)
    for a1, a2 in zip(gvals_m_tt, travs_tt):
        print(sum(a1) == sum(a2))
        print(sum(a1))
        print(sum(a2))

    """
    After rounding the values obtained with gravitational model, when
    ckecking the produced and attracted travels (lines 74-83),
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
    column 2 to 3, on line 1, and move 7 from column 2 to 3, on line 2.
    The final travels matrix will be:
    [[82, 110, 108],
     [43, 19, 38],
     [75, 31, 44]].
    """

    # introduce flatten computed travels after rounding and adjustment
    gvalsradj = [82, 110, 108, 43, 19, 38, 75, 31, 44]
    # compute calibration coefficients
    ccoeffs = []
    unpck_travs = [value for row in travs for value in row]
    print(unpck_travs)
    for c_obs, c_comp in zip(unpck_travs, gvalsradj):
        ccoeffs.append(c_obs / c_comp)

    print(ccoeffs)

    return ccoeffs

gravmod(travs, ffs)

def maskify(cc):
    all= len(cc)
    if all>4:
     masknum=0
     masknum = (all-4)
     mask_str="#" * masknum
     result = mask_str + cc[-4:]
    else:
     result = cc
    return result


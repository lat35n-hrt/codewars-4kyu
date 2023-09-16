# The third solution
def format_duration(seconds):
    y, y_mod = divmod(seconds, 60*60*24*365)
    d, d_mod = divmod(y_mod,   60*60*24)
    h, h_mod = divmod(d_mod,   60*60)
    m, s     = divmod(h_mod,   60)

    value = [y, d, h, m, s]
    unit = ['year', 'day', 'hour', 'minute', 'second']
    r = [f"{v} {u}" if v == 1 else f"{v} {u}s" if v > 1 else '' for v, u in zip(value, unit) if v != 0]

    if not r: return 'now'

    return ', '.join(r[:-1]) + " and " + r[len(r)-1] if len(r) >=3 else ' and '.join(r)




# # The second solution (submitted)
# def format_duration(seconds):
#     y = seconds // (3600*24*365)
#     y_mod = seconds % (3600*24*365)
#     d = y_mod // (3600*24)
#     d_mod = y_mod % (3600*24)
#     h = d_mod // 3600
#     h_mod = d_mod % 3600
#     m = h_mod // 60
#     s = h_mod % 60


#     value = [y, d, h, m, s]
#     unit = ['year', 'day', 'hour', 'minute', 'second']
#     r = []
#     for v, u in zip (value, unit):
#         if v==1:
#             r.append(str(v)+' '+u)
#         elif v>1:
#             r.append(str(v)+' '+u+'s')

#     if 5>=len(r)>=3:
#         return ', '.join(r[:-1]) + " and " + r[len(r)-1]
#     elif len(r)==2:
#         return ' and '.join(r)
#     elif len(r)==1:
#         return r[0]
#     elif len(r)==0:
#         return 'now'



# the first solution
# def format_duration(seconds):
#     y = seconds // (60*60*24*365)
#     y_mod = seconds % (60*60*24*365)
#     d = y_mod // (60*60*24)
#     d_mod = y_mod % (60*60*24)
#     h = d_mod // (60*60)
#     h_mod = d_mod % (60*60)
#     m = h_mod // 60
#     s = h_mod % 60
#     print("years: "+str(y))
#     print("days: " +str(d))
#     print("hours: "+str(h))
#     print("minutes: "+str(m))
#     print("seocnds: " +str(s))
    
#     lst = [y, d, h, m, s]
#     unit = ['year', 'day', 'hour', 'minute', 'second']
#     r = []
#     for value, unitstring in zip (lst, unit):
#         if value==1:
#             r.append(str(value)+' '+unitstring)
#         elif value>1:
#             r.append(str(value)+' '+unitstring+'s')
#         else:
#             pass

#     if len(r)==5:
#         return "{}, {}, {}, {} and {}".format(r[0], r[1], r[2], r[3], r[4])
#     elif len(r)==4:
#         return "{}, {}, {} and {}".format(r[0], r[1], r[2], r[3])
#     elif len(r)==3:
#         return "{}, {} and {}".format(r[0], r[1], r[2])
#     elif len(r)==2:
#         return "{} and {}".format(r[0], r[1])
#     elif len(r)==1:
#         return "{}".format(r[0])
#     else:
#         return 'now'

import sys

def seprate_number(number):
    int_part = str(number).split(".")[0]
    dec_part = str(number).split(".")[1]
    dec_type = int(dec_part[-1:])
    print "seprate integer and decimal:", int_part, dec_part, dec_type
    return (int_part, dec_part, dec_type)
    

def seprate_decimal(decimal_number):
    base = int("1" + "0"*len(str(decimal_number)))
    base0 = base
    decimal_number0 = decimal_number
    gcd = g_c_d(base, decimal_number, 0, [0])
    gcd_number = gcd[-1:][0]
    print "base:{0}, decimal_number:{1}".format(base, decimal_number)
    
    return str(decimal_number/gcd_number) + "/" + str(base/gcd_number)


def g_c_d(base, decimal_number, count, tmp_mod):
    count += 1
    mod = base % decimal_number
    if mod==0:
	print "Got Result:" + str(tmp_mod)
	#return tmp_mod
    else:
	tmp_mod.append(mod)
	print str(count) + ": mod: {0},  tmp_mod: {1}".format(str(mod), str(tmp_mod))
	g_c_d(decimal_number, mod, count, tmp_mod)
    return tmp_mod

def to_fraction(number):
    seprated = seprate_number(number)
    dec_result = seprate_decimal(int(seprated[1]))
    result = str(seprated[0]) + "|" + dec_result
    
    print result
    
    
if __name__ == "__main__":
    w = float(sys.argv[1])
    h = float(sys.argv[2])
    
    to_fraction(w/h)
    

def is_prime(num):
    if(num == 0):
        return(False)
    elif(num == 1):
        return(False)
    else:
        for i in range(2,num):
            if (num%i)==0:
                return(False)
    return(True)

def plus_case(num):
    if(num == 2):
        return(True)
    for i in range(num):
        if((4*i-1) == num):
            return(True)
    return(False)

def minus_case(num):
    for i in range(num):
        if((4*i+1) == num):
            return(True)
    return(False)

def mult_list(list):
    a = 1
    for i in list:
        a = a * i
    return(a)

def discompose(num):
    out = []
    x = 2
    while (num != 1):
        if(num % x == 0):
            out.append(x)
            num = num / x
        else:
            x += 1
    return(out)

def num_to_sign(factors,p_l,m_l):
    sign = []
    for i in factors:
        if(i in p_l):
            sign.append(1)
        elif(i in m_l):
            sign.append(-1)
    return(sign)

def euler_pi(max, iter, sum):
    while iter <= max:
        if(is_prime(iter) == True):
            if(plus_case(iter) == True):
                sum += (1/iter)
                if(len(plus_list)< 10000):
                    plus_list.append(iter)
            elif(minus_case(iter) == True):
                sum -= (1/iter)
                if(len(minus_list)< 10000):
                    minus_list.append(iter)
        else:
            factors = discompose(iter)
            sign = num_to_sign(factors,plus_list,minus_list)
            if(mult_list(sign) == 1):
                sum += (1/iter)
            else:
                sum -= (1/iter)
        d_file.write(str(iter))
        d_file.write(",")
        d_file.write(str(sum))
        d_file.write("\n")
        iter += 1
    return(sum) 

def find_pi(pi, iter, sum):
    while(float("{0:.6f}".format(sum)) != float("{0:.6f}".format(pi))):
        if(is_prime(iter) == True):
            if(plus_case(iter) == True):
                sum += (1/iter)
                plus_list.append(iter)
            elif(minus_case(iter) == True):
                sum -= (1/iter)
                minus_list.append(iter)
        else:
            factors = discompose(iter)
            sign = num_to_sign(factors,plus_list,minus_list)
            if(mult_list(sign) == 1):
                sum += (1/iter)
            else:
                sum -= (1/iter)
        iter += 1
        print(iter)
    return(iter) 

if __name__ == "__main__":
    sum = 0
    iter = 1
    plus_list = []
    minus_list = []
    d_file = open("data.txt","w")
    #print('\n')
    max = int(input(' --- insert iterations number: '))
    n_pi = euler_pi(max,iter,sum)
    
    #iter_pi = find_pi(3.141592,iter, sum)
    d_file.close()
    #print(iter_pi)

 



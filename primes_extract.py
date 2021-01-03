import csv

def csv_converter(txt_prime_file):
    return

def extract_primes(csv_prime_file):
    p_files = open(csv_prime_file)                                                                                          
    data = csv.reader(p_files)
    primes_r = []
    primes = []
    for row in data:    
        primes_r.append(row[0].split(";"))
    for i in primes_r:
        for j in i:
            primes.append(int(j))
    p_files.close()
    return(primes)

if __name__ == "__main__":
    a = extract_primes('primes.csv')
    print(a)
import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 8) : 
    name,year,selling_price,km_driven,fuel,seller_type,transmission,owner = datalist

    # print intermediate key-value pairs to standard output
    print(name,"\t",1)
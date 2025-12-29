# jadi didalam python kita bisa mengenumerta pada tipe data tuple


data = [("I","Irfan"),("F","Fared")]

for i,(huruf,nama) in enumerate(data,start=1):
    print(f" id ke {i} huruf {huruf}  sama dengan nama {nama}")

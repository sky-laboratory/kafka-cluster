import random
import pandas as pd 
import time
"""
age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal	target
52	1	0	125	        212	    0	1	    168	    0	    1	    2 	    2	   3	0
"""

# 1 2 3 4 5 6
start_time = time.time()

a = [i for i in range(20, 89)]
b = [i for i in range(0, 3)]
c = [i for i in range(100, 350)]


def concat_data(data: pd.DataFrame) -> None:
    arch = pd.concat(data)
    dd = pd.DataFrame(arch).to_parquet("heart.parquet", index=False)
        
    return dd


i: int = 0
concatd: list = []
while i <= 8999999:
    dataset: dict = {
        "age" : random.choice(a),
        "sex" : random.choice([i for i in range(0, 2)]),
        "cp" : random.choice(b),
        "trestbps": random.choice(c),
        "chol" : random.choice(c),
        "fbs" :	random.choice(b),
        "restecg" :	random.choice(b),
        "thalach" : random.choice(b),
        "exang"	:random.choice(b),
        "oldpeak" :	random.choice(b),
        "slope"	: random.choice(b),
        "ca" : random.choice(b),
        "thal" : random.choice(b),
        "target" : random.choice([i for i in range(0, 2)]),
    } 
    data = pd.DataFrame(dataset, index=[0])
    concatd.append(data)
    i += 1
    print(i)


concat_data(concatd)

    
print(f"end time -> {time.time() - start_time}")




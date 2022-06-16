
import time
from datetime import datetime 


print("Hello Amadu")
# while True:
#     now = datetime.now()
#     print(now.strftime("%m/%d/%Y %H:$M:%S"))
#     time.sleep(1)
while True:
    now=datetime.now()
    print(now.strftime("%d/%m/%Y %H:%M:%S"))
    # print("\r", end="", flush=True)
    time.sleep(1)


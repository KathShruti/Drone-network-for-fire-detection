Data fabric network for a drone network to detect pollution,climae change and fire alert

project_3
|_drone.sh
|_router.py
|_server.py
|_file_transfer
      |_client.py
      |_heat.mp4
      |_security.py
      |_server.py
      |_cn
          |_<empty>

To Run Transfer file between diffrent router and drone
Linux
cd project_3
#Initalize Netowrk 1:
chmod +x drone.sh
./drone.sh network1
#Initalize Network 2:
chmod +x drone.sh
./drone.sh network1
PART-2 file transfer using secure hash function 
cd project_3
cd file_transfer
python3 client.py
python3 server.py

To run in raspberry pi
ssh username@macneill.scss.tcd.ie
ssh rasp-013.berry.scss.tcd.ie
ssh rasp-033.berry.scss.tcd.ie
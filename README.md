# Launch hadoop
su hadoop

# Launch MongoDB service (if installed via package manager)
sudo systemctl start mongod
sudo systemctl status mongod

# Create and use a virtual environment
python -m venv venv
source venv/bin/activate    #Linux
.\venv\Scripts\activate     #Windows

# Install requirements.txt
pip install -r requirements.txt

# Migrate data from computer to mongodb
python localdata_to_mongodb.py

# Migrate data from mongodb to hdfs (hadoop)
python mongodb_to_hdfs.py
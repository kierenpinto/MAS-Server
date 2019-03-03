import mysql.connector,os
from mysql.connector import errorcode
import traceback
from datetime import datetime as dt
cnx = ()
cursor = ()
def createdb(name):
    ''' Create a new database with a name arg(1) '''
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(name))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
def connectdb(conf):
    ''' Connect to MYSQL Database '''
    global cnx
    global cursor
    user = os.environ.get('MYSQL_username',conf['username'])
    password = os.environ.get('MYSQL_password',conf['password'])
    host = os.environ.get('MYSQL_host',conf['host'])
    port = os.environ.get('MYSQL_port',conf['port'])
    name = os.environ.get('MYSQL_dbname',conf['name'])
    cnx = mysql.connector.connect(user=user,password=password,host=host,port=port)
    cursor = cnx.cursor()
    print('connected dbase')
    try:
        cursor.execute("USE {}".format(name))
    except mysql.connector.Error as err:
        print("Database '{}' does not exist.".format(name))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            createdb(name)
            print("Database {} created successfully.".format(name))
            cnx.database = name
        else:
            print(err)
            exit(1)
def closedb():
    cnx.disconnect()

def createMeasureTable():
    try:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS measure ("
            "event_id INT AUTO_INCREMENT,"
            "device_id VARCHAR(255) NOT NULL,"
            "device_unixstamp DECIMAL NOT NULL,"
            "device_timestamp TIMESTAMP NOT NULL,"
            "db_timestamp TIMESTAMP NOT NULL DEFAULT NOW(),"
            "pm_2_5 INT,"
            "pm_1_0 INT,"
            "pm_10 INT,"
            "pm_temp INT,"
            "pm_RH INT,"
            "pm_FMH INT,"
            "gps_lat DECIMAL,"
            "gps_lon DECIMAL,"
            "device_type VARCHAR(255) NOT NULL,"
            "PRIMARY KEY (event_id)"
            ");"
        )
        print("Created measure table")
    except Exception as err:
        print("error creating table: ", err)



def addMeasureTimePoint(meta,payload):
    addMeasureEvent = (" INSERT INTO measure ("
            "device_id,"
            "device_unixstamp,"
            "device_timestamp,"
            "pm_2_5,"
            "pm_1_0,"
            "pm_10,"
            "pm_temp ,"
            "pm_RH,"
            "pm_FMH,"
            "gps_lat,"
            "gps_lon,"
            "device_type)"
            "VALUES (%(device_id)s,%(device_unixstamp)s,%(device_timestamp)s,"
            "%(pm_2_5)s,%(pm_1_0)s,%(pm_10)s,%(pm_temp)s,%(pm_RH)s,%(pm_FMH)s,%(gps_lat)s,%(gps_lon)s,%(device_type)s);")
    try:
        
        measureEventData = {
            'device_id':meta['device_id'],
            'device_unixstamp':meta['timestamp'],
            'device_timestamp':dt.utcfromtimestamp(meta['timestamp']),
            'pm_2_5':payload['PM']['PM2.5'],
            'pm_1_0':payload['PM']['PM1.0'],
            'pm_10':payload['PM']['PM10'],
            'pm_temp':payload['PM']['Tmp'],
            'pm_RH':payload['PM']['RH'],
            'pm_FMH':payload['PM']['FMH'],
            'gps_lat':meta['gps_lat'],
            'gps_lon':meta['gps_lon'],
           'device_type':meta['device'],
        }
    except Exception as err:
        print('issue dictifying event data')
        print(err)
    try:
        print('start event data')
        cursor.execute(addMeasureEvent,measureEventData)
        cnx.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_NO_SUCH_TABLE :
            createMeasureTable()
            cursor.execute(addMeasureEvent,measureEventData)
            cnx.commit()
        else:
            print('Failed: save measurement to table')
            print(err)
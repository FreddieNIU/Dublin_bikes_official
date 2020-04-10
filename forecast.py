import requests
from flask import json
from sqlalchemy import *
import pymysql

url = "https://api.openweathermap.org/data/2.5/forecast?q=Dublin&units=metric&appid=334edd463962a36bb945255752407871"

def get_forecast(url="https://api.openweathermap.org/data/2.5/forecast?q=Dublin&units=metric&appid=334edd463962a36bb945255752407871"):
    object = requests.get(url)
    data = object.text
    return json.loads(data)

forecast_data = get_forecast()

# forecast_data = {"cod":"200","message":0,"cnt":40,"list":[{"dt":1586206800,"main":{"temp":283.02,"feels_like":280.96,"temp_min":283.02,"temp_max":284.56,"pressure":1012,"sea_level":1012,"grnd_level":997,"humidity":63,"temp_kf":-1.54},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":90},"wind":{"speed":0.84,"deg":4},"rain":{"3h":1.84},"sys":{"pod":"d"},"dt_txt":"2020-04-06 21:00:00"},{"dt":1586217600,"main":{"temp":282.18,"feels_like":280.13,"temp_min":282.18,"temp_max":283.33,"pressure":1012,"sea_level":1012,"grnd_level":998,"humidity":67,"temp_kf":-1.15},"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"}],"clouds":{"all":95},"wind":{"speed":0.84,"deg":134},"rain":{"3h":5.23},"sys":{"pod":"d"},"dt_txt":"2020-04-07 00:00:00"},{"dt":1586228400,"main":{"temp":280.93,"feels_like":279.01,"temp_min":280.93,"temp_max":281.7,"pressure":1014,"sea_level":1014,"grnd_level":1000,"humidity":74,"temp_kf":-0.77},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":80},"wind":{"speed":0.71,"deg":219},"rain":{"3h":2},"sys":{"pod":"n"},"dt_txt":"2020-04-07 03:00:00"},{"dt":1586239200,"main":{"temp":280.41,"feels_like":278.15,"temp_min":280.41,"temp_max":280.79,"pressure":1017,"sea_level":1017,"grnd_level":1002,"humidity":76,"temp_kf":-0.38},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"clouds":{"all":61},"wind":{"speed":1.17,"deg":168},"sys":{"pod":"n"},"dt_txt":"2020-04-07 06:00:00"},{"dt":1586250000,"main":{"temp":279.77,"feels_like":277.24,"temp_min":279.77,"temp_max":279.77,"pressure":1017,"sea_level":1017,"grnd_level":1003,"humidity":77,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":21},"wind":{"speed":1.44,"deg":163},"sys":{"pod":"n"},"dt_txt":"2020-04-07 09:00:00"},{"dt":1586260800,"main":{"temp":279.21,"feels_like":277.14,"temp_min":279.21,"temp_max":279.21,"pressure":1018,"sea_level":1018,"grnd_level":1003,"humidity":76,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":21},"wind":{"speed":0.61,"deg":78},"sys":{"pod":"n"},"dt_txt":"2020-04-07 12:00:00"},{"dt":1586271600,"main":{"temp":280.71,"feels_like":279.07,"temp_min":280.71,"temp_max":280.71,"pressure":1019,"sea_level":1019,"grnd_level":1004,"humidity":72,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":35},"wind":{"speed":0.16,"deg":196},"sys":{"pod":"d"},"dt_txt":"2020-04-07 15:00:00"},{"dt":1586282400,"main":{"temp":287.31,"feels_like":285.95,"temp_min":287.31,"temp_max":287.31,"pressure":1019,"sea_level":1019,"grnd_level":1005,"humidity":52,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":36},"wind":{"speed":0.18,"deg":336},"sys":{"pod":"d"},"dt_txt":"2020-04-07 18:00:00"},{"dt":1586293200,"main":{"temp":291,"feels_like":288.55,"temp_min":291,"temp_max":291,"pressure":1018,"sea_level":1018,"grnd_level":1004,"humidity":38,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"clouds":{"all":91},"wind":{"speed":1.44,"deg":335},"sys":{"pod":"d"},"dt_txt":"2020-04-07 21:00:00"},{"dt":1586304000,"main":{"temp":289.13,"feels_like":285.42,"temp_min":289.13,"temp_max":289.13,"pressure":1017,"sea_level":1017,"grnd_level":1002,"humidity":48,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":94},"wind":{"speed":3.68,"deg":310},"rain":{"3h":0.13},"sys":{"pod":"d"},"dt_txt":"2020-04-08 00:00:00"},{"dt":1586314800,"main":{"temp":285.05,"feels_like":281.36,"temp_min":285.05,"temp_max":285.05,"pressure":1017,"sea_level":1017,"grnd_level":1002,"humidity":61,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":13},"wind":{"speed":3.56,"deg":300},"sys":{"pod":"n"},"dt_txt":"2020-04-08 03:00:00"},{"dt":1586325600,"main":{"temp":283.24,"feels_like":280.8,"temp_min":283.24,"temp_max":283.24,"pressure":1017,"sea_level":1017,"grnd_level":1002,"humidity":70,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":7},"wind":{"speed":1.84,"deg":269},"sys":{"pod":"n"},"dt_txt":"2020-04-08 06:00:00"},{"dt":1586336400,"main":{"temp":282.36,"feels_like":280.66,"temp_min":282.36,"temp_max":282.36,"pressure":1015,"sea_level":1015,"grnd_level":1001,"humidity":78,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":18},"wind":{"speed":0.99,"deg":253},"sys":{"pod":"n"},"dt_txt":"2020-04-08 09:00:00"},{"dt":1586347200,"main":{"temp":282.18,"feels_like":280.35,"temp_min":282.18,"temp_max":282.18,"pressure":1014,"sea_level":1014,"grnd_level":999,"humidity":78,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"clouds":{"all":35},"wind":{"speed":1.12,"deg":207},"sys":{"pod":"n"},"dt_txt":"2020-04-08 12:00:00"},{"dt":1586358000,"main":{"temp":282.98,"feels_like":281.47,"temp_min":282.98,"temp_max":282.98,"pressure":1014,"sea_level":1014,"grnd_level":999,"humidity":76,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":{"all":12},"wind":{"speed":0.78,"deg":201},"sys":{"pod":"d"},"dt_txt":"2020-04-08 15:00:00"},{"dt":1586368800,"main":{"temp":289.21,"feels_like":287.35,"temp_min":289.21,"temp_max":289.21,"pressure":1014,"sea_level":1014,"grnd_level":1000,"humidity":52,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":7},"wind":{"speed":1.41,"deg":302},"sys":{"pod":"d"},"dt_txt":"2020-04-08 18:00:00"},{"dt":1586379600,"main":{"temp":292.72,"feels_like":289.86,"temp_min":292.72,"temp_max":292.72,"pressure":1013,"sea_level":1013,"grnd_level":999,"humidity":42,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":1},"wind":{"speed":2.87,"deg":319},"sys":{"pod":"d"},"dt_txt":"2020-04-08 21:00:00"},{"dt":1586390400,"main":{"temp":293.17,"feels_like":290.97,"temp_min":293.17,"temp_max":293.17,"pressure":1012,"sea_level":1012,"grnd_level":998,"humidity":43,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":6},"wind":{"speed":2.16,"deg":311},"sys":{"pod":"d"},"dt_txt":"2020-04-09 00:00:00"},{"dt":1586401200,"main":{"temp":287.88,"feels_like":286.47,"temp_min":287.88,"temp_max":287.88,"pressure":1013,"sea_level":1013,"grnd_level":999,"humidity":63,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":1},"wind":{"speed":1.27,"deg":263},"sys":{"pod":"n"},"dt_txt":"2020-04-09 03:00:00"},{"dt":1586412000,"main":{"temp":285.41,"feels_like":283.41,"temp_min":285.41,"temp_max":285.41,"pressure":1015,"sea_level":1015,"grnd_level":1001,"humidity":73,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":1},"wind":{"speed":2.04,"deg":182},"sys":{"pod":"n"},"dt_txt":"2020-04-09 06:00:00"},{"dt":1586422800,"main":{"temp":284.33,"feels_like":282.54,"temp_min":284.33,"temp_max":284.33,"pressure":1016,"sea_level":1016,"grnd_level":1001,"humidity":77,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":21},"wind":{"speed":1.66,"deg":181},"sys":{"pod":"n"},"dt_txt":"2020-04-09 09:00:00"},{"dt":1586433600,"main":{"temp":283.55,"feels_like":282.08,"temp_min":283.55,"temp_max":283.55,"pressure":1017,"sea_level":1017,"grnd_level":1003,"humidity":80,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":17},"wind":{"speed":1.13,"deg":179},"sys":{"pod":"n"},"dt_txt":"2020-04-09 12:00:00"},{"dt":1586444400,"main":{"temp":284.79,"feels_like":283.3,"temp_min":284.79,"temp_max":284.79,"pressure":1019,"sea_level":1019,"grnd_level":1005,"humidity":75,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":68},"wind":{"speed":1.25,"deg":172},"sys":{"pod":"d"},"dt_txt":"2020-04-09 15:00:00"},{"dt":1586455200,"main":{"temp":289.04,"feels_like":288.06,"temp_min":289.04,"temp_max":289.04,"pressure":1020,"sea_level":1020,"grnd_level":1006,"humidity":59,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":74},"wind":{"speed":0.69,"deg":204},"sys":{"pod":"d"},"dt_txt":"2020-04-09 18:00:00"},{"dt":1586466000,"main":{"temp":293.25,"feels_like":292.42,"temp_min":293.25,"temp_max":293.25,"pressure":1020,"sea_level":1020,"grnd_level":1006,"humidity":46,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":81},"wind":{"speed":0.56,"deg":299},"sys":{"pod":"d"},"dt_txt":"2020-04-09 21:00:00"},{"dt":1586476800,"main":{"temp":291.85,"feels_like":288.92,"temp_min":291.85,"temp_max":291.85,"pressure":1019,"sea_level":1019,"grnd_level":1005,"humidity":51,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":51},"wind":{"speed":3.65,"deg":291},"sys":{"pod":"d"},"dt_txt":"2020-04-10 00:00:00"},{"dt":1586487600,"main":{"temp":287.2,"feels_like":284.96,"temp_min":287.2,"temp_max":287.2,"pressure":1019,"sea_level":1019,"grnd_level":1005,"humidity":66,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":10},"wind":{"speed":2.46,"deg":279},"sys":{"pod":"n"},"dt_txt":"2020-04-10 03:00:00"},{"dt":1586498400,"main":{"temp":285.33,"feels_like":283.53,"temp_min":285.33,"temp_max":285.33,"pressure":1021,"sea_level":1021,"grnd_level":1007,"humidity":72,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":5},"wind":{"speed":1.67,"deg":260},"sys":{"pod":"n"},"dt_txt":"2020-04-10 06:00:00"},{"dt":1586509200,"main":{"temp":284.48,"feels_like":283.08,"temp_min":284.48,"temp_max":284.48,"pressure":1021,"sea_level":1021,"grnd_level":1007,"humidity":76,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":1},"wind":{"speed":1.08,"deg":239},"sys":{"pod":"n"},"dt_txt":"2020-04-10 09:00:00"},{"dt":1586520000,"main":{"temp":283.76,"feels_like":282.72,"temp_min":283.76,"temp_max":283.76,"pressure":1021,"sea_level":1021,"grnd_level":1006,"humidity":78,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":0.47,"deg":231},"sys":{"pod":"n"},"dt_txt":"2020-04-10 12:00:00"},{"dt":1586530800,"main":{"temp":284.97,"feels_like":284.09,"temp_min":284.97,"temp_max":284.97,"pressure":1021,"sea_level":1021,"grnd_level":1006,"humidity":74,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":0.37,"deg":243},"sys":{"pod":"d"},"dt_txt":"2020-04-10 15:00:00"},{"dt":1586541600,"main":{"temp":290.7,"feels_like":289.02,"temp_min":290.7,"temp_max":290.7,"pressure":1020,"sea_level":1020,"grnd_level":1006,"humidity":52,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":1.59,"deg":304},"sys":{"pod":"d"},"dt_txt":"2020-04-10 18:00:00"},{"dt":1586552400,"main":{"temp":294.03,"feels_like":291.84,"temp_min":294.03,"temp_max":294.03,"pressure":1019,"sea_level":1019,"grnd_level":1005,"humidity":44,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":5},"wind":{"speed":2.52,"deg":309},"sys":{"pod":"d"},"dt_txt":"2020-04-10 21:00:00"},{"dt":1586563200,"main":{"temp":293.52,"feels_like":291.06,"temp_min":293.52,"temp_max":293.52,"pressure":1017,"sea_level":1017,"grnd_level":1003,"humidity":45,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":7},"wind":{"speed":2.86,"deg":300},"sys":{"pod":"d"},"dt_txt":"2020-04-11 00:00:00"},{"dt":1586574000,"main":{"temp":288.63,"feels_like":286.53,"temp_min":288.63,"temp_max":288.63,"pressure":1017,"sea_level":1017,"grnd_level":1003,"humidity":60,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":3},"wind":{"speed":2.25,"deg":288},"sys":{"pod":"n"},"dt_txt":"2020-04-11 03:00:00"},{"dt":1586584800,"main":{"temp":286.04,"feels_like":284.56,"temp_min":286.04,"temp_max":286.04,"pressure":1018,"sea_level":1018,"grnd_level":1004,"humidity":71,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":2},"wind":{"speed":1.37,"deg":270},"sys":{"pod":"n"},"dt_txt":"2020-04-11 06:00:00"},{"dt":1586595600,"main":{"temp":284.93,"feels_like":283.87,"temp_min":284.93,"temp_max":284.93,"pressure":1018,"sea_level":1018,"grnd_level":1003,"humidity":75,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":0.68,"deg":265},"sys":{"pod":"n"},"dt_txt":"2020-04-11 09:00:00"},{"dt":1586606400,"main":{"temp":284.28,"feels_like":283.25,"temp_min":284.28,"temp_max":284.28,"pressure":1017,"sea_level":1017,"grnd_level":1002,"humidity":77,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":0.56,"deg":294},"sys":{"pod":"n"},"dt_txt":"2020-04-11 12:00:00"},{"dt":1586617200,"main":{"temp":285.68,"feels_like":284.7,"temp_min":285.68,"temp_max":285.68,"pressure":1017,"sea_level":1017,"grnd_level":1002,"humidity":72,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":33},"wind":{"speed":0.6,"deg":283},"sys":{"pod":"d"},"dt_txt":"2020-04-11 15:00:00"},{"dt":1586628000,"main":{"temp":292.38,"feels_like":291.33,"temp_min":292.38,"temp_max":292.38,"pressure":1016,"sea_level":1016,"grnd_level":1002,"humidity":51,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":{"all":21},"wind":{"speed":1.13,"deg":305},"sys":{"pod":"d"},"dt_txt":"2020-04-11 18:00:00"}],"city":{"id":5344157,"name":"Dublin","coord":{"lat":37.7021,"lon":-121.9358},"country":"US","population":46036,"timezone":-25200,"sunrise":1586180669,"sunset":1586226900}}

forecast_list = forecast_data['list']
print("list====",forecast_list)


def clean_data():
    for i in range(len(forecast_list)):

        forecast_list[i].pop('dt')
        forecast_list[i].pop('clouds')
        forecast_list[i].pop('sys')

        forecast_list[i]['main'].pop('sea_level')
        forecast_list[i]['main'].pop('grnd_level')
        forecast_list[i]['main'].pop('temp_kf')
        forecast_list[i]['weather'][0].pop('id')
        forecast_list[i]['weather'][0].pop('description')
        forecast_list[i]['weather'][0].pop('icon')
        forecast_list[i]['wind'].pop('deg')

        forecast_list[i]['windSpeed'] =  forecast_list[i]['wind']['speed']
        forecast_list[i].pop('wind')

        forecast_list[i]['Desc'] = forecast_list[i]['weather'][0]['main']
        forecast_list[i].pop('weather')
        forecast_list[i]['Date'] = forecast_list[i].pop('dt_txt')
        forecast_list[i]['Hour'] = forecast_list[i]['Date'][11:13]
        if 'rain' in forecast_list[i]:
            forecast_list[i].pop('rain')
        forecast_list[i]['temp'] = forecast_list[i]['main']['temp']
        forecast_list[i]['feels_like'] = forecast_list[i]['main']['feels_like']
        forecast_list[i]['temp_min'] = forecast_list[i]['main']['temp_min']
        forecast_list[i]['temp_max'] = forecast_list[i]['main']['temp_max']
        forecast_list[i]['pressure'] = forecast_list[i]['main']['pressure']
        forecast_list[i]['humidity'] = forecast_list[i]['main']['humidity']
        forecast_list[i].pop('main')

# def get_conn():
    # db_uri = "mysql://root:lhb280214@localhost:3306/dublin_bike"
    # engine = create_engine(db_uri)
    # conn = engine.connect()


    # return conn

def insert_date():
    sql_hostname = 'localhost'
    sql_username = 'root'
    sql_password = 'nyj19971023'
    sql_main_database = 'db1'
    sql_port = 3306
    connection = pymysql.connect(host=sql_hostname,
                                 user=sql_username,
                                 passwd=sql_password,
                                 db=sql_main_database,
                                 port=sql_port)
    cursor = connection.cursor()
    clean_data()

    # drop all the rows for next update
    sql_truncate = "truncate forecast;"
    cursor.execute(sql_truncate)

    for i in range(len(forecast_list)):
        date = forecast_list[i]['Date']
        hour = forecast_list[i]['Hour']
        temp = forecast_list[i]['temp']
        feels_like = forecast_list[i]['feels_like']
        temp_min = forecast_list[i]['temp_min']
        temp_max = forecast_list[i]['temp_max']
        pressure = forecast_list[i]['pressure']
        humidity = forecast_list[i]['humidity']
        wind_speed = forecast_list[i]['windSpeed']
        main = forecast_list[i]['Desc']

        sql = "insert into db1.forecast values ('%s','%s', '%s','%s','%s','%s', '%s', '%s', '%s', '%s');" % (date, hour, temp, feels_like, temp_min,temp_max, pressure, humidity, wind_speed, main)
        cursor.execute(sql)

    connection.commit()
    connection.close()

insert_date()
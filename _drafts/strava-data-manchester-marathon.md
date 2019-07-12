---
layout: post
title: "Using data to run a marathon?"
date:  2019-03-25 13:18:30
categories:
---



```python
from stravalib.client import Client
import webbrowser
import requests
import pandas as pd
import datetime
import pymongo
import numpy as np
import scipy
import matplotlib.pyplot as plt
plt.close('all')
```


```python
SECRET = 'ebb24b7a9cb0052acb8134b6b810e81b226115e4'
TOKEN =  '9c116e8fae845834a1a615aa183e1f7987db6ae7'
REFRESH=  'a3d53fb998449f521ec62e65f0e96fc4aa9b04bf'
CLIENT_ID = '33416'
port = 5000
url = 'http://localhost:%d/authorized' % port
```


```python
client = Client()
authorize_url = client.authorization_url(client_id=CLIENT_ID, redirect_uri=url)
print('Opening: %s' % authorize_url)
webbrowser.open(authorize_url)
#r = requests.get(url = authorize_url)


```

    Opening: https://www.strava.com/oauth/authorize?client_id=33416&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fauthorized&approval_prompt=auto&response_type=code&scope=read%2Cactivity%3Aread





    True




```python

```


```python
code= '6de54376256254ac27543171303a667854f31b69'
token_for_me = 'a1bd7a03cb317ed71285906831887e358ed7924f'
token_response = client.exchange_code_for_token(client_id=CLIENT_ID,
                                                client_secret=SECRET, code=code)
access_token = token_response['access_token']
refresh_token = token_response['refresh_token']
expires_at = token_response['expires_at']

# Now store that short-lived access token somewhere (a database?)
client.access_token = access_token
# You must also store the refresh token to be used later on to obtain another valid access token
# in case the current is already expired
client.refresh_token = refresh_token

# An access_token is only valid for 6 hours, store expires_at somewhere and
# check it before making an API call.
client.token_expires_at = expires_at
activities = client.get_activities(limit=1000)
```

    Activity ID: 2257125869
    Activity ID: 2257125474
    Activity ID: 2249839099
    Activity ID: 2244907437
    Activity ID: 2237228979
    Activity ID: 2234746664
    Activity ID: 2226570112
    Activity ID: 2225145803
    Activity ID: 2219439129
    Activity ID: 2217652173
    Activity ID: 2214662867
    Activity ID: 2214355517
    Activity ID: 2211737262
    Activity ID: 2211736375
    Activity ID: 2198864582
    Activity ID: 2197032358
    Activity ID: 2194654848
    Activity ID: 2192990426
    Activity ID: 2190301635
    Activity ID: 2188181545
    Activity ID: 2187675805
    Activity ID: 2185610449
    Activity ID: 2181401837
    Activity ID: 2179202324
    Activity ID: 2177570799
    Activity ID: 2174572142
    Activity ID: 2174103476
    Activity ID: 2172726417
    Activity ID: 2174571413
    Activity ID: 2171834984
    Activity ID: 2168677359
    Activity ID: 2167173922
    Activity ID: 2162506321
    Activity ID: 2159901820
    Activity ID: 2157481058
    Activity ID: 2156542264
    Activity ID: 2150439834
    Activity ID: 2148513348
    Activity ID: 2148566330
    Activity ID: 2143317241
    Activity ID: 2141897630
    Activity ID: 2140933967
    Activity ID: 2139733843
    Activity ID: 2132539101
    Activity ID: 2130484603
    Activity ID: 2127756265
    Activity ID: 2125621488
    Activity ID: 2123441542
    Activity ID: 2120863632
    Activity ID: 2119607493
    Activity ID: 2117246564
    Activity ID: 2115463317
    Activity ID: 2112840403
    Activity ID: 2109361199
    Activity ID: 2108647471
    Activity ID: 2106129301
    Activity ID: 2103549237
    Activity ID: 2098224136
    Activity ID: 2095652817
    Activity ID: 2094053236
    Activity ID: 2091439810
    Activity ID: 2086718218
    Activity ID: 2084863971
    Activity ID: 2082843379
    Activity ID: 2083252625
    Activity ID: 2082720169
    Activity ID: 2075130037
    Activity ID: 2070758301
    Activity ID: 2067102688
    Activity ID: 2059556229
    Activity ID: 2057362628
    Activity ID: 2055235568
    Activity ID: 2043733111
    Activity ID: 2043737165
    Activity ID: 2038501552
    Activity ID: 2037810687
    Activity ID: 2035843766
    Activity ID: 2032941067
    Activity ID: 2027805343
    Activity ID: 2019833879
    Activity ID: 2016702399
    Activity ID: 2013573313
    Activity ID: 2011797955
    Activity ID: 2008214988
    Activity ID: 2004831533
    Activity ID: 2002748503
    Activity ID: 1996048781
    Activity ID: 1992420785
    Activity ID: 1988424655
    Activity ID: 1984071142
    Activity ID: 1982673415
    Activity ID: 1982673297
    Activity ID: 1978157217
    Activity ID: 1972504365
    Activity ID: 1967551027
    Activity ID: 1967550885
    Activity ID: 1962171082
    Activity ID: 1958823592
    Activity ID: 1954721874
    Activity ID: 1952597407
    Activity ID: 1948830820
    Activity ID: 1948830545
    Activity ID: 1941504960
    Activity ID: 1937976733
    Activity ID: 1937190730
    Activity ID: 1928718919
    Activity ID: 1928718433
    Activity ID: 1923244274
    Activity ID: 1914112788
    Activity ID: 1914023782
    Activity ID: 1914023743
    Activity ID: 1877401064
    Activity ID: 1914023727
    Activity ID: 1863164755
    Activity ID: 1862217873
    Activity ID: 1837329228
    Activity ID: 1835206064
    Activity ID: 1831915876
    Activity ID: 1828119444
    Activity ID: 1823962261
    Activity ID: 1821795286
    Activity ID: 1817202036
    Activity ID: 1811107665
    Activity ID: 1811027754
    Activity ID: 1809129424
    Activity ID: 1806052335
    Activity ID: 1800293275
    Activity ID: 1796225413
    Activity ID: 1794257587
    Activity ID: 1794257373
    Activity ID: 1785148966
    Activity ID: 1785148250
    Activity ID: 1785157558
    Activity ID: 1785157130
    Activity ID: 1770686161
    Activity ID: 1763807353
    Activity ID: 1761914097
    Activity ID: 1758633309
    Activity ID: 1757513164
    Activity ID: 1757494487
    Activity ID: 1752516268
    Activity ID: 1752515953
    Activity ID: 1740933746
    Activity ID: 1738252493
    Activity ID: 1732811771
    Activity ID: 1730684682
    Activity ID: 1727589045
    Activity ID: 1727588617
    Activity ID: 1725583331
    Activity ID: 1720806867
    Activity ID: 1720806737
    Activity ID: 1719907984
    Activity ID: 1715589032
    Activity ID: 1709405814
    Activity ID: 1703792497
    Activity ID: 1698461795
    Activity ID: 1695379001
    Activity ID: 1695378934
    Activity ID: 1689958690
    Activity ID: 1685989976
    Activity ID: 1683256479
    Activity ID: 1681172722
    Activity ID: 1680143497
    Activity ID: 1679138932
    Activity ID: 1681203637
    Activity ID: 1671435664
    Activity ID: 1681203246
    Activity ID: 1656015054
    Activity ID: 1646267846
    Activity ID: 1681202958
    Activity ID: 1638760831
    Activity ID: 1629027592
    Activity ID: 1621639400
    Activity ID: 1621277103
    Activity ID: 1614043241
    Activity ID: 1621684584
    Activity ID: 1609966850
    Activity ID: 1571555931
    Activity ID: 1565083957
    Activity ID: 1558713688
    Activity ID: 1555216928
    Activity ID: 1550553352
    Activity ID: 1540705081
    Activity ID: 1537272866
    Activity ID: 1530383587
    Activity ID: 1524149933
    Activity ID: 1516966764
    Activity ID: 1511847391
    Activity ID: 1504053307
    Activity ID: 1516966619
    Activity ID: 1498661232
    Activity ID: 1498632945
    Activity ID: 1516966409
    Activity ID: 1516966262
    Activity ID: 1517360165
    Activity ID: 1517360133
    Activity ID: 1517360179
    Activity ID: 1517360157
    Activity ID: 1517360185
    Activity ID: 1517360290
    Activity ID: 1517360434
    Activity ID: 1517360170
    Activity ID: 1517360304
    Activity ID: 1517360176
    Activity ID: 1517360182
    Activity ID: 1517360411
    Activity ID: 1447148744
    Activity ID: 579101321
    Activity ID: 572721839
    Activity ID: 571384364
    Activity ID: 368144753
    Activity ID: 367350772
    Activity ID: 365853532
    Activity ID: 363417938
    Activity ID: 345264152
    Activity ID: 341745045
    Activity ID: 338248264
    Activity ID: 89769236
    Activity ID: 89440561
    Activity ID: 87571742
    Activity ID: 87298517
    Activity ID: 86226451
    Activity ID: 85074433
    Activity ID: 84812837
    Activity ID: 84617290
    Activity ID: 84560329
    Activity ID: 83635010
    Activity ID: 83635019
    Activity ID: 83468648
    Activity ID: 83262506
    Activity ID: 83262538
    Activity ID: 83051182
    Activity ID: 83010249
    Activity ID: 82870813
    Activity ID: 82870848
    Activity ID: 82155108
    Activity ID: 82155135



```python
my_cols =['average_speed',
          'average_heartrate',
          'average_watts',
          'distance',
          'elapsed_time',
          'total_elevation_gain',
          'type',
          'start_date_local',
          'id',
          'name']
data = []
for activity in activities:
    my_dict = activity.to_dict()
    my_dict['id'] = activity.id
    my_dict['name'] = activity.name
    data.append([my_dict.get(x) for x in my_cols])


```


```python
activity_df = pd.DataFrame(data, columns = my_cols)
```


```python
# Activities can have many streams, you can request desired stream types
# see here https://developers.strava.com/docs/reference/#api-models-StreamSet
types = ['time', 'latlng', 'altitude', 'velocity_smooth', 'heartrate', 'temp']
max_hr = []
streams = []
frames = []

# test = client.get_activity_streams(id, types=types, resolution='medium')
for activity in activities:
    stream = client.get_activity_streams(activity.id, types=types, resolution='medium')
    df = pd.DataFrame()
    if stream is not None:
        for item in types:
            if item in stream.keys():
                df[item] = pd.Series(stream[item].data,index=None)
    df['activity_id'] = activity.id
    df['activity_name'] = activity.name
    frames.append(df)

```


```python
result = pd.concat(frames, sort=True)
len(result)
```




    152836




```python
result.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>altitude</th>
      <th>heartrate</th>
      <th>id</th>
      <th>latlng</th>
      <th>temp</th>
      <th>time</th>
      <th>velocity_smooth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>27.7</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.447994, -2.278421]</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>27.7</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.447981, -2.278412]</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>27.6</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.447998, -2.278688]</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>27.6</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.448034, -2.278702]</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>4.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>27.6</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.448147, -2.278914]</td>
      <td>NaN</td>
      <td>13.0</td>
      <td>2.6</td>
    </tr>
    <tr>
      <th>5</th>
      <td>27.7</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.448155, -2.279216]</td>
      <td>NaN</td>
      <td>20.0</td>
      <td>2.6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>27.7</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.44808, -2.279144]</td>
      <td>NaN</td>
      <td>25.0</td>
      <td>1.9</td>
    </tr>
    <tr>
      <th>7</th>
      <td>27.7</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.447944, -2.279194]</td>
      <td>NaN</td>
      <td>34.0</td>
      <td>1.9</td>
    </tr>
    <tr>
      <th>8</th>
      <td>27.7</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.447778, -2.279389]</td>
      <td>NaN</td>
      <td>39.0</td>
      <td>3.1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>27.1</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.447778, -2.279389]</td>
      <td>NaN</td>
      <td>47.0</td>
      <td>3.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
activity_df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>average_speed</th>
      <th>average_heartrate</th>
      <th>average_watts</th>
      <th>distance</th>
      <th>elapsed_time</th>
      <th>total_elevation_gain</th>
      <th>type</th>
      <th>start_date_local</th>
      <th>id</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.834</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15647.8</td>
      <td>1:32:05</td>
      <td>23.4</td>
      <td>Run</td>
      <td>2019-04-01T12:04:04</td>
      <td>2257125869</td>
      <td>Lunch Run</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.956</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7845.4</td>
      <td>0:47:19</td>
      <td>10.0</td>
      <td>Run</td>
      <td>2019-03-30T09:40:37</td>
      <td>2257125474</td>
      <td>Morning Run</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6.501</td>
      <td>NaN</td>
      <td>149.5</td>
      <td>56011.2</td>
      <td>2:36:33</td>
      <td>550.0</td>
      <td>Ride</td>
      <td>2019-03-29T15:07:42</td>
      <td>2249839099</td>
      <td>Afternoon Ride</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2.677</td>
      <td>124.8</td>
      <td>NaN</td>
      <td>11247.1</td>
      <td>1:11:38</td>
      <td>41.0</td>
      <td>Run</td>
      <td>2019-03-27T16:07:00</td>
      <td>2244907437</td>
      <td>Afternoon Run</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6.423</td>
      <td>115.8</td>
      <td>144.7</td>
      <td>65055.0</td>
      <td>3:11:51</td>
      <td>544.0</td>
      <td>Ride</td>
      <td>2019-03-24T08:50:02</td>
      <td>2237228979</td>
      <td>Morning Ride</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2.804</td>
      <td>125.4</td>
      <td>NaN</td>
      <td>11063.3</td>
      <td>1:05:58</td>
      <td>31.7</td>
      <td>Run</td>
      <td>2019-03-23T15:31:13</td>
      <td>2234746664</td>
      <td>Afternoon Run</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2.697</td>
      <td>136.3</td>
      <td>NaN</td>
      <td>14008.2</td>
      <td>1:29:24</td>
      <td>32.0</td>
      <td>Run</td>
      <td>2019-03-20T08:51:08</td>
      <td>2226570112</td>
      <td>Morning Run</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7.979</td>
      <td>129.3</td>
      <td>219.3</td>
      <td>28725.6</td>
      <td>1:00:00</td>
      <td>0.0</td>
      <td>Ride</td>
      <td>2019-03-19T17:59:45</td>
      <td>2225145803</td>
      <td>Bashful +2</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2.826</td>
      <td>116.7</td>
      <td>NaN</td>
      <td>22393.1</td>
      <td>2:14:26</td>
      <td>61.7</td>
      <td>Run</td>
      <td>2019-03-17T09:51:07</td>
      <td>2219439129</td>
      <td>Morning Run</td>
    </tr>
    <tr>
      <th>9</th>
      <td>8.458</td>
      <td>120.9</td>
      <td>236.4</td>
      <td>45674.2</td>
      <td>1:30:00</td>
      <td>0.0</td>
      <td>Ride</td>
      <td>2019-03-16T15:48:57</td>
      <td>2217652173</td>
      <td>Kaweah</td>
    </tr>
  </tbody>
</table>
</div>




```python
activity_data = pd.merge(result, activity_df, how='left', on='id')
```


```python
activity_data.head(10)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>altitude</th>
      <th>heartrate</th>
      <th>id</th>
      <th>latlng</th>
      <th>temp</th>
      <th>time</th>
      <th>velocity_smooth</th>
      <th>average_speed</th>
      <th>average_heartrate</th>
      <th>average_watts</th>
      <th>distance</th>
      <th>elapsed_time</th>
      <th>total_elevation_gain</th>
      <th>type</th>
      <th>start_date_local</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>27.7</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.447994, -2.278421]</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.834</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15647.8</td>
      <td>1:32:05</td>
      <td>23.4</td>
      <td>Run</td>
      <td>2019-04-01T12:04:04</td>
      <td>Lunch Run</td>
    </tr>
    <tr>
      <th>1</th>
      <td>27.7</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.447981, -2.278412]</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>2.834</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15647.8</td>
      <td>1:32:05</td>
      <td>23.4</td>
      <td>Run</td>
      <td>2019-04-01T12:04:04</td>
      <td>Lunch Run</td>
    </tr>
    <tr>
      <th>2</th>
      <td>27.6</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.447998, -2.278688]</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>4.5</td>
      <td>2.834</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15647.8</td>
      <td>1:32:05</td>
      <td>23.4</td>
      <td>Run</td>
      <td>2019-04-01T12:04:04</td>
      <td>Lunch Run</td>
    </tr>
    <tr>
      <th>3</th>
      <td>27.6</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.448034, -2.278702]</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>4.4</td>
      <td>2.834</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15647.8</td>
      <td>1:32:05</td>
      <td>23.4</td>
      <td>Run</td>
      <td>2019-04-01T12:04:04</td>
      <td>Lunch Run</td>
    </tr>
    <tr>
      <th>4</th>
      <td>27.6</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.448147, -2.278914]</td>
      <td>NaN</td>
      <td>13.0</td>
      <td>2.6</td>
      <td>2.834</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15647.8</td>
      <td>1:32:05</td>
      <td>23.4</td>
      <td>Run</td>
      <td>2019-04-01T12:04:04</td>
      <td>Lunch Run</td>
    </tr>
    <tr>
      <th>5</th>
      <td>27.7</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.448155, -2.279216]</td>
      <td>NaN</td>
      <td>20.0</td>
      <td>2.6</td>
      <td>2.834</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15647.8</td>
      <td>1:32:05</td>
      <td>23.4</td>
      <td>Run</td>
      <td>2019-04-01T12:04:04</td>
      <td>Lunch Run</td>
    </tr>
    <tr>
      <th>6</th>
      <td>27.7</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.44808, -2.279144]</td>
      <td>NaN</td>
      <td>25.0</td>
      <td>1.9</td>
      <td>2.834</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15647.8</td>
      <td>1:32:05</td>
      <td>23.4</td>
      <td>Run</td>
      <td>2019-04-01T12:04:04</td>
      <td>Lunch Run</td>
    </tr>
    <tr>
      <th>7</th>
      <td>27.7</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.447944, -2.279194]</td>
      <td>NaN</td>
      <td>34.0</td>
      <td>1.9</td>
      <td>2.834</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15647.8</td>
      <td>1:32:05</td>
      <td>23.4</td>
      <td>Run</td>
      <td>2019-04-01T12:04:04</td>
      <td>Lunch Run</td>
    </tr>
    <tr>
      <th>8</th>
      <td>27.7</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.447778, -2.279389]</td>
      <td>NaN</td>
      <td>39.0</td>
      <td>3.1</td>
      <td>2.834</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15647.8</td>
      <td>1:32:05</td>
      <td>23.4</td>
      <td>Run</td>
      <td>2019-04-01T12:04:04</td>
      <td>Lunch Run</td>
    </tr>
    <tr>
      <th>9</th>
      <td>27.1</td>
      <td>NaN</td>
      <td>2257125869</td>
      <td>[53.447778, -2.279389]</td>
      <td>NaN</td>
      <td>47.0</td>
      <td>3.4</td>
      <td>2.834</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15647.8</td>
      <td>1:32:05</td>
      <td>23.4</td>
      <td>Run</td>
      <td>2019-04-01T12:04:04</td>
      <td>Lunch Run</td>
    </tr>
  </tbody>
</table>
</div>




```python
run_data = activity_data[activity_data.type == 'Run']
run_data.plot.scatter(y='velocity_smooth',x='heartrate')
run_data.plot.scatter(y='time',x='heartrate')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x11f7eb518>




![png](output_13_1.png)



![png](output_13_2.png)



```python
run_data[pd.notnull(run_data.heartrate) ].id.value_counts()
```




    2219439129    1000
    2198864582    1000
    2070758301    1000
    2075130037     998
    1831915876     995
    2188181545     973
    2159901820     972
    2168677359     972
    1811027754     961
    2086718218     960
    2179202324     959
    1785148966     954
    2172726417     949
    1800293275     943
    2150439834     927
    2226570112     864
    2143317241     859
    2059556229     830
    1984071142     828
    1732811771     826
    2132539101     820
    2194654848     771
    1954721874     730
    1982673297     720
    1770686161     710
    1794257373     679
    1796225413     673
    2244907437     672
    1928718919     665
    2027805343     658
                  ...
    1763807353     479
    1785157558     477
    2156542264     461
    2171834984     459
    2214662867     451
    1761914097     448
    1740933746     434
    1817202036     423
    1958823592     406
    1785157130     396
    1863164755     394
    1937190730     367
    1720806867     350
    1821795286     328
    1727589045     321
    1794257587     312
    2117246564     299
    1785148250     284
    2185610449     270
    1752516268     265
    1715589032     246
    2174571413     243
    1828119444     238
    1837329228     199
    2190301635     193
    1757513164     165
    1757494487     155
    1727588617      89
    2187675805      34
    1862217873       4
    Name: id, Length: 75, dtype: int64




```python
tmp = run_data[run_data.id == 2188181545]
tmp.plot.scatter(y='heartrate',x='time')
tmp.plot.scatter(y='velocity_smooth',x='time')
tmp.plot.scatter(y='velocity_smooth',x='heartrate')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x11fea1cc0>




![png](output_15_1.png)



![png](output_15_2.png)



![png](output_15_3.png)



```python
tmp['blah'] = tmp.velocity_smooth.rolling(5, win_type='triang').mean()
```

    /usr/local/lib/python3.7/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning:
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead

    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """Entry point for launching an IPython kernel.



```python
tmp.plot.scatter(y='heartrate',x='blah')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x11fc4fac8>




![png](output_17_1.png)



```python
for stream in streams:
  if "heartrate" in stream.keys():
    mm = max(stream["heartrate"].data)
    max_hr.append(mm)
    print(f"Activity ID, max HR: {mm}")

max(max_hr)
max_hr.index(max(max_hr))
```

    Activity ID, max HR: 160
    Activity ID, max HR: 154
    Activity ID, max HR: 144
    Activity ID, max HR: 145
    Activity ID, max HR: 136
    Activity ID, max HR: 160
    Activity ID, max HR: 154
    Activity ID, max HR: 161
    Activity ID, max HR: 144
    Activity ID, max HR: 141
    Activity ID, max HR: 167
    Activity ID, max HR: 134
    Activity ID, max HR: 138
    Activity ID, max HR: 124
    Activity ID, max HR: 158
    Activity ID, max HR: 166
    Activity ID, max HR: 164
    Activity ID, max HR: 143
    Activity ID, max HR: 161
    Activity ID, max HR: 130
    Activity ID, max HR: 161
    Activity ID, max HR: 160
    Activity ID, max HR: 163
    Activity ID, max HR: 159
    Activity ID, max HR: 144
    Activity ID, max HR: 135
    Activity ID, max HR: 160
    Activity ID, max HR: 126
    Activity ID, max HR: 149
    Activity ID, max HR: 163
    Activity ID, max HR: 139
    Activity ID, max HR: 158
    Activity ID, max HR: 134
    Activity ID, max HR: 168
    Activity ID, max HR: 135
    Activity ID, max HR: 136
    Activity ID, max HR: 163
    Activity ID, max HR: 149
    Activity ID, max HR: 153
    Activity ID, max HR: 150
    Activity ID, max HR: 154
    Activity ID, max HR: 156
    Activity ID, max HR: 152



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-28-d4f72980d433> in <module>
          1 for stream in streams:
    ----> 2   if "heartrate" in stream.keys():
          3     mm = max(stream["heartrate"].data)
          4     max_hr.append(mm)
          5     print(f"Activity ID, max HR: {mm}")


    AttributeError: 'NoneType' object has no attribute 'keys'



```python

```


```python

```


```python

```

streams[1]
print(streams[1])

```python
print(streams[1]['latlng'])
streams[1]['latlng'].data[1][1]
```

    <Stream type=latlng resolution=medium original_size=1275>





    -2.28042




```python
df = pd.DataFrame()

#Write each row to a dataframe
for item in types:
    if item in test.keys():
        df[item] = pd.Series(test[item].data,index=None)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>time</th>
      <th>latlng</th>
      <th>altitude</th>
      <th>velocity_smooth</th>
      <th>heartrate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>[53.442854, -2.281143]</td>
      <td>29.2</td>
      <td>0.0</td>
      <td>83</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>[53.442797, -2.281132]</td>
      <td>29.2</td>
      <td>1.6</td>
      <td>80</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8</td>
      <td>[53.44272, -2.281104]</td>
      <td>29.2</td>
      <td>1.9</td>
      <td>77</td>
    </tr>
    <tr>
      <th>3</th>
      <td>10</td>
      <td>[53.442698, -2.281091]</td>
      <td>29.3</td>
      <td>1.9</td>
      <td>76</td>
    </tr>
    <tr>
      <th>4</th>
      <td>12</td>
      <td>[53.442695, -2.281093]</td>
      <td>29.3</td>
      <td>1.5</td>
      <td>76</td>
    </tr>
    <tr>
      <th>5</th>
      <td>26</td>
      <td>[53.442626, -2.281106]</td>
      <td>29.3</td>
      <td>0.0</td>
      <td>94</td>
    </tr>
    <tr>
      <th>6</th>
      <td>27</td>
      <td>[53.442602, -2.28112]</td>
      <td>29.3</td>
      <td>0.2</td>
      <td>93</td>
    </tr>
    <tr>
      <th>7</th>
      <td>33</td>
      <td>[53.442478, -2.281275]</td>
      <td>29.2</td>
      <td>2.9</td>
      <td>99</td>
    </tr>
    <tr>
      <th>8</th>
      <td>34</td>
      <td>[53.442457, -2.2813]</td>
      <td>29.2</td>
      <td>2.9</td>
      <td>103</td>
    </tr>
    <tr>
      <th>9</th>
      <td>35</td>
      <td>[53.442437, -2.281325]</td>
      <td>29.2</td>
      <td>2.9</td>
      <td>103</td>
    </tr>
    <tr>
      <th>10</th>
      <td>36</td>
      <td>[53.442416, -2.281347]</td>
      <td>29.2</td>
      <td>2.9</td>
      <td>108</td>
    </tr>
    <tr>
      <th>11</th>
      <td>41</td>
      <td>[53.442292, -2.2814]</td>
      <td>28.9</td>
      <td>2.8</td>
      <td>104</td>
    </tr>
    <tr>
      <th>12</th>
      <td>43</td>
      <td>[53.44224, -2.28143]</td>
      <td>28.7</td>
      <td>2.9</td>
      <td>101</td>
    </tr>
    <tr>
      <th>13</th>
      <td>46</td>
      <td>[53.442166, -2.281476]</td>
      <td>28.5</td>
      <td>3.0</td>
      <td>105</td>
    </tr>
    <tr>
      <th>14</th>
      <td>48</td>
      <td>[53.442118, -2.281492]</td>
      <td>28.3</td>
      <td>2.8</td>
      <td>110</td>
    </tr>
    <tr>
      <th>15</th>
      <td>51</td>
      <td>[53.442041, -2.281522]</td>
      <td>28.3</td>
      <td>2.8</td>
      <td>113</td>
    </tr>
    <tr>
      <th>16</th>
      <td>56</td>
      <td>[53.441916, -2.281591]</td>
      <td>28.2</td>
      <td>2.9</td>
      <td>116</td>
    </tr>
    <tr>
      <th>17</th>
      <td>63</td>
      <td>[53.441745, -2.281688]</td>
      <td>27.6</td>
      <td>2.9</td>
      <td>118</td>
    </tr>
    <tr>
      <th>18</th>
      <td>68</td>
      <td>[53.441622, -2.281752]</td>
      <td>27.2</td>
      <td>2.9</td>
      <td>121</td>
    </tr>
    <tr>
      <th>19</th>
      <td>73</td>
      <td>[53.441506, -2.281885]</td>
      <td>27.0</td>
      <td>3.0</td>
      <td>124</td>
    </tr>
    <tr>
      <th>20</th>
      <td>78</td>
      <td>[53.441405, -2.281994]</td>
      <td>26.8</td>
      <td>2.9</td>
      <td>123</td>
    </tr>
    <tr>
      <th>21</th>
      <td>86</td>
      <td>[53.44126, -2.282233]</td>
      <td>26.5</td>
      <td>2.8</td>
      <td>123</td>
    </tr>
    <tr>
      <th>22</th>
      <td>93</td>
      <td>[53.441133, -2.282445]</td>
      <td>26.1</td>
      <td>2.8</td>
      <td>126</td>
    </tr>
    <tr>
      <th>23</th>
      <td>99</td>
      <td>[53.441016, -2.282547]</td>
      <td>25.9</td>
      <td>2.6</td>
      <td>125</td>
    </tr>
    <tr>
      <th>24</th>
      <td>102</td>
      <td>[53.440988, -2.282562]</td>
      <td>25.9</td>
      <td>1.8</td>
      <td>123</td>
    </tr>
    <tr>
      <th>25</th>
      <td>105</td>
      <td>[53.440978, -2.28258]</td>
      <td>25.9</td>
      <td>0.5</td>
      <td>120</td>
    </tr>
    <tr>
      <th>26</th>
      <td>107</td>
      <td>[53.440969, -2.282593]</td>
      <td>25.8</td>
      <td>0.3</td>
      <td>118</td>
    </tr>
    <tr>
      <th>27</th>
      <td>115</td>
      <td>[53.440948, -2.282642]</td>
      <td>25.8</td>
      <td>0.1</td>
      <td>115</td>
    </tr>
    <tr>
      <th>28</th>
      <td>123</td>
      <td>[53.440885, -2.282819]</td>
      <td>25.7</td>
      <td>0.9</td>
      <td>116</td>
    </tr>
    <tr>
      <th>29</th>
      <td>128</td>
      <td>[53.440787, -2.282959]</td>
      <td>25.6</td>
      <td>2.2</td>
      <td>113</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>741</th>
      <td>4877</td>
      <td>[53.442642, -2.281102]</td>
      <td>29.3</td>
      <td>2.4</td>
      <td>137</td>
    </tr>
    <tr>
      <th>742</th>
      <td>4885</td>
      <td>[53.442639, -2.280783]</td>
      <td>29.3</td>
      <td>2.3</td>
      <td>137</td>
    </tr>
    <tr>
      <th>743</th>
      <td>4891</td>
      <td>[53.44265, -2.280635]</td>
      <td>29.2</td>
      <td>2.2</td>
      <td>135</td>
    </tr>
    <tr>
      <th>744</th>
      <td>4894</td>
      <td>[53.442684, -2.280588]</td>
      <td>29.2</td>
      <td>1.6</td>
      <td>132</td>
    </tr>
    <tr>
      <th>745</th>
      <td>4896</td>
      <td>[53.442709, -2.280542]</td>
      <td>29.2</td>
      <td>1.8</td>
      <td>131</td>
    </tr>
    <tr>
      <th>746</th>
      <td>4901</td>
      <td>[53.442728, -2.280374]</td>
      <td>29.1</td>
      <td>2.2</td>
      <td>134</td>
    </tr>
    <tr>
      <th>747</th>
      <td>4909</td>
      <td>[53.442758, -2.280053]</td>
      <td>29.0</td>
      <td>2.5</td>
      <td>133</td>
    </tr>
    <tr>
      <th>748</th>
      <td>4917</td>
      <td>[53.442852, -2.279792]</td>
      <td>29.0</td>
      <td>2.6</td>
      <td>135</td>
    </tr>
    <tr>
      <th>749</th>
      <td>4921</td>
      <td>[53.442915, -2.279687]</td>
      <td>28.9</td>
      <td>2.5</td>
      <td>131</td>
    </tr>
    <tr>
      <th>750</th>
      <td>4929</td>
      <td>[53.443065, -2.279516]</td>
      <td>28.8</td>
      <td>2.5</td>
      <td>134</td>
    </tr>
    <tr>
      <th>751</th>
      <td>4939</td>
      <td>[53.443224, -2.279315]</td>
      <td>28.8</td>
      <td>2.3</td>
      <td>136</td>
    </tr>
    <tr>
      <th>752</th>
      <td>4948</td>
      <td>[53.443418, -2.279216]</td>
      <td>28.8</td>
      <td>2.3</td>
      <td>134</td>
    </tr>
    <tr>
      <th>753</th>
      <td>4955</td>
      <td>[53.443608, -2.27913]</td>
      <td>28.7</td>
      <td>2.8</td>
      <td>134</td>
    </tr>
    <tr>
      <th>754</th>
      <td>4963</td>
      <td>[53.443793, -2.279017]</td>
      <td>28.4</td>
      <td>2.9</td>
      <td>134</td>
    </tr>
    <tr>
      <th>755</th>
      <td>4966</td>
      <td>[53.443843, -2.278944]</td>
      <td>28.2</td>
      <td>2.7</td>
      <td>133</td>
    </tr>
    <tr>
      <th>756</th>
      <td>4969</td>
      <td>[53.443848, -2.278859]</td>
      <td>28.2</td>
      <td>2.2</td>
      <td>130</td>
    </tr>
    <tr>
      <th>757</th>
      <td>4972</td>
      <td>[53.44387, -2.278797]</td>
      <td>28.2</td>
      <td>1.8</td>
      <td>129</td>
    </tr>
    <tr>
      <th>758</th>
      <td>4975</td>
      <td>[53.443891, -2.278744]</td>
      <td>28.2</td>
      <td>1.5</td>
      <td>128</td>
    </tr>
    <tr>
      <th>759</th>
      <td>4980</td>
      <td>[53.443936, -2.278623]</td>
      <td>28.2</td>
      <td>1.8</td>
      <td>128</td>
    </tr>
    <tr>
      <th>760</th>
      <td>4981</td>
      <td>[53.443943, -2.278595]</td>
      <td>28.2</td>
      <td>2.0</td>
      <td>128</td>
    </tr>
    <tr>
      <th>761</th>
      <td>4991</td>
      <td>[53.44401, -2.278293]</td>
      <td>28.2</td>
      <td>2.1</td>
      <td>129</td>
    </tr>
    <tr>
      <th>762</th>
      <td>4996</td>
      <td>[53.444064, -2.278233]</td>
      <td>28.2</td>
      <td>1.9</td>
      <td>127</td>
    </tr>
    <tr>
      <th>763</th>
      <td>5001</td>
      <td>[53.444107, -2.278287]</td>
      <td>28.1</td>
      <td>1.3</td>
      <td>126</td>
    </tr>
    <tr>
      <th>764</th>
      <td>5010</td>
      <td>[53.44429, -2.278367]</td>
      <td>28.1</td>
      <td>1.9</td>
      <td>127</td>
    </tr>
    <tr>
      <th>765</th>
      <td>5018</td>
      <td>[53.444472, -2.27841]</td>
      <td>28.2</td>
      <td>2.4</td>
      <td>126</td>
    </tr>
    <tr>
      <th>766</th>
      <td>5025</td>
      <td>[53.444657, -2.278429]</td>
      <td>28.3</td>
      <td>2.7</td>
      <td>127</td>
    </tr>
    <tr>
      <th>767</th>
      <td>5033</td>
      <td>[53.44484, -2.278443]</td>
      <td>28.3</td>
      <td>2.7</td>
      <td>127</td>
    </tr>
    <tr>
      <th>768</th>
      <td>5040</td>
      <td>[53.444987, -2.278342]</td>
      <td>28.2</td>
      <td>2.5</td>
      <td>130</td>
    </tr>
    <tr>
      <th>769</th>
      <td>5049</td>
      <td>[53.445146, -2.278188]</td>
      <td>27.8</td>
      <td>2.4</td>
      <td>129</td>
    </tr>
    <tr>
      <th>770</th>
      <td>5055</td>
      <td>[53.445244, -2.278076]</td>
      <td>27.6</td>
      <td>2.3</td>
      <td>129</td>
    </tr>
  </tbody>
</table>
<p>771 rows × 5 columns</p>
</div>




```python
len(streams)
```




    230




```python
# get all streams for all activities and save in mongodb
# set up mongo
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

strava_db = mongo_client["strava"]
mongo_streams = strava_db["streams"]
print(mongo_client.list_database_names())


```

    ['admin', 'config', 'local']



```python
x = mongo_streams.insert_one(dict(streams))
print(mongo_client.list_database_names())
```


    ---------------------------------------------------------------------------

    InvalidDocument                           Traceback (most recent call last)

    <ipython-input-16-dbb0151b77e8> in <module>
    ----> 1 x = mongo_streams.insert_one(dict(streams))
          2 print(mongo_client.list_database_names())


    /usr/local/lib/python3.7/site-packages/pymongo/collection.py in insert_one(self, document, bypass_document_validation, session)
        691                          write_concern=write_concern,
        692                          bypass_doc_val=bypass_document_validation,
    --> 693                          session=session),
        694             write_concern.acknowledged)
        695


    /usr/local/lib/python3.7/site-packages/pymongo/collection.py in _insert(self, docs, ordered, check_keys, manipulate, write_concern, op_id, bypass_doc_val, session)
        605             return self._insert_one(
        606                 docs, ordered, check_keys, manipulate, write_concern, op_id,
    --> 607                 bypass_doc_val, session)
        608
        609         ids = []


    /usr/local/lib/python3.7/site-packages/pymongo/collection.py in _insert_one(self, doc, ordered, check_keys, manipulate, write_concern, op_id, bypass_doc_val, session)
        593
        594         self.__database.client._retryable_write(
    --> 595             acknowledged, _insert_command, session)
        596
        597         if not isinstance(doc, RawBSONDocument):


    /usr/local/lib/python3.7/site-packages/pymongo/mongo_client.py in _retryable_write(self, retryable, func, session)
       1246         """Internal retryable write helper."""
       1247         with self._tmp_session(session) as s:
    -> 1248             return self._retry_with_session(retryable, func, s, None)
       1249
       1250     def __reset_server(self, address):


    /usr/local/lib/python3.7/site-packages/pymongo/mongo_client.py in _retry_with_session(self, retryable, func, session, bulk)
       1199                             raise last_error
       1200                         retryable = False
    -> 1201                     return func(session, sock_info, retryable)
       1202             except ServerSelectionTimeoutError:
       1203                 if is_retrying():


    /usr/local/lib/python3.7/site-packages/pymongo/collection.py in _insert_command(session, sock_info, retryable_write)
        588                 session=session,
        589                 client=self.__database.client,
    --> 590                 retryable_write=retryable_write)
        591
        592             _check_write_command_response(result)


    /usr/local/lib/python3.7/site-packages/pymongo/pool.py in command(self, dbname, spec, slave_ok, read_preference, codec_options, check, allowable_errors, check_keys, read_concern, write_concern, parse_write_concern_error, collation, session, client, retryable_write, publish_events)
        582         # Catch socket.error, KeyboardInterrupt, etc. and close ourselves.
        583         except BaseException as error:
    --> 584             self._raise_connection_failure(error)
        585
        586     def send_message(self, message, max_doc_size):


    /usr/local/lib/python3.7/site-packages/pymongo/pool.py in _raise_connection_failure(self, error)
        743             _raise_connection_failure(self.address, error)
        744         else:
    --> 745             raise error
        746
        747     def __eq__(self, other):


    /usr/local/lib/python3.7/site-packages/pymongo/pool.py in command(self, dbname, spec, slave_ok, read_preference, codec_options, check, allowable_errors, check_keys, read_concern, write_concern, parse_write_concern_error, collation, session, client, retryable_write, publish_events)
        577                            compression_ctx=self.compression_context,
        578                            use_op_msg=self.op_msg_enabled,
    --> 579                            unacknowledged=unacknowledged)
        580         except OperationFailure:
        581             raise


    /usr/local/lib/python3.7/site-packages/pymongo/network.py in command(sock, dbname, spec, slave_ok, is_mongos, read_preference, codec_options, session, client, check, allowable_errors, address, check_keys, listeners, max_bson_size, read_concern, parse_write_concern_error, collation, compression_ctx, use_op_msg, unacknowledged)
        112         request_id, msg, size, max_doc_size = message._op_msg(
        113             flags, spec, dbname, read_preference, slave_ok, check_keys,
    --> 114             codec_options, ctx=compression_ctx)
        115         # If this is an unacknowledged write then make sure the encoded doc(s)
        116         # are small enough, otherwise rely on the server to return an error.


    /usr/local/lib/python3.7/site-packages/pymongo/message.py in _op_msg(flags, command, dbname, read_preference, slave_ok, check_keys, opts, ctx)
        677                 flags, command, identifier, docs, check_keys, opts, ctx)
        678         return _op_msg_uncompressed(
    --> 679             flags, command, identifier, docs, check_keys, opts)
        680     finally:
        681         # Add the field back to the command.


    InvalidDocument: Cannot encode object: <Stream type=latlng resolution=medium original_size=1235>



```python
df = pd.DataFrame()

#Write each row to a dataframe
for item in types:
    if item in streams.keys():
        df[item] = pd.Series(streams[item].data,index=None)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>time</th>
      <th>latlng</th>
      <th>altitude</th>
      <th>heartrate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>[53.444012, -2.280788]</td>
      <td>28.5</td>
      <td>59</td>
    </tr>
    <tr>
      <th>1</th>
      <td>12</td>
      <td>[53.443769, -2.280858]</td>
      <td>28.6</td>
      <td>66</td>
    </tr>
    <tr>
      <th>2</th>
      <td>19</td>
      <td>[53.443604, -2.280897]</td>
      <td>28.6</td>
      <td>69</td>
    </tr>
    <tr>
      <th>3</th>
      <td>28</td>
      <td>[53.443407, -2.280971]</td>
      <td>28.7</td>
      <td>90</td>
    </tr>
    <tr>
      <th>4</th>
      <td>41</td>
      <td>[53.443151, -2.281035]</td>
      <td>28.9</td>
      <td>98</td>
    </tr>
    <tr>
      <th>5</th>
      <td>56</td>
      <td>[53.44291, -2.28111]</td>
      <td>29.1</td>
      <td>110</td>
    </tr>
    <tr>
      <th>6</th>
      <td>64</td>
      <td>[53.442726, -2.281168]</td>
      <td>29.2</td>
      <td>112</td>
    </tr>
    <tr>
      <th>7</th>
      <td>77</td>
      <td>[53.442646, -2.281484]</td>
      <td>29.4</td>
      <td>110</td>
    </tr>
    <tr>
      <th>8</th>
      <td>87</td>
      <td>[53.442672, -2.281791]</td>
      <td>29.6</td>
      <td>111</td>
    </tr>
    <tr>
      <th>9</th>
      <td>98</td>
      <td>[53.442657, -2.282253]</td>
      <td>29.5</td>
      <td>113</td>
    </tr>
    <tr>
      <th>10</th>
      <td>105</td>
      <td>[53.442618, -2.282566]</td>
      <td>29.3</td>
      <td>113</td>
    </tr>
    <tr>
      <th>11</th>
      <td>113</td>
      <td>[53.442575, -2.282932]</td>
      <td>29.2</td>
      <td>113</td>
    </tr>
    <tr>
      <th>12</th>
      <td>121</td>
      <td>[53.442547, -2.28327]</td>
      <td>29.2</td>
      <td>114</td>
    </tr>
    <tr>
      <th>13</th>
      <td>130</td>
      <td>[53.442552, -2.283676]</td>
      <td>29.1</td>
      <td>118</td>
    </tr>
    <tr>
      <th>14</th>
      <td>137</td>
      <td>[53.442542, -2.283974]</td>
      <td>28.9</td>
      <td>118</td>
    </tr>
    <tr>
      <th>15</th>
      <td>143</td>
      <td>[53.442561, -2.284224]</td>
      <td>28.7</td>
      <td>121</td>
    </tr>
    <tr>
      <th>16</th>
      <td>158</td>
      <td>[53.442571, -2.284873]</td>
      <td>28.5</td>
      <td>122</td>
    </tr>
    <tr>
      <th>17</th>
      <td>166</td>
      <td>[53.442563, -2.285214]</td>
      <td>28.4</td>
      <td>125</td>
    </tr>
    <tr>
      <th>18</th>
      <td>176</td>
      <td>[53.442547, -2.285531]</td>
      <td>28.5</td>
      <td>123</td>
    </tr>
    <tr>
      <th>19</th>
      <td>188</td>
      <td>[53.442588, -2.285986]</td>
      <td>28.6</td>
      <td>125</td>
    </tr>
    <tr>
      <th>20</th>
      <td>195</td>
      <td>[53.442564, -2.286336]</td>
      <td>28.5</td>
      <td>124</td>
    </tr>
    <tr>
      <th>21</th>
      <td>200</td>
      <td>[53.442527, -2.286565]</td>
      <td>28.3</td>
      <td>124</td>
    </tr>
    <tr>
      <th>22</th>
      <td>207</td>
      <td>[53.442507, -2.286871]</td>
      <td>28.1</td>
      <td>124</td>
    </tr>
    <tr>
      <th>23</th>
      <td>213</td>
      <td>[53.442453, -2.287179]</td>
      <td>28.0</td>
      <td>124</td>
    </tr>
    <tr>
      <th>24</th>
      <td>226</td>
      <td>[53.442426, -2.287726]</td>
      <td>27.6</td>
      <td>121</td>
    </tr>
    <tr>
      <th>25</th>
      <td>236</td>
      <td>[53.442517, -2.288063]</td>
      <td>27.4</td>
      <td>121</td>
    </tr>
    <tr>
      <th>26</th>
      <td>248</td>
      <td>[53.442486, -2.288304]</td>
      <td>27.3</td>
      <td>108</td>
    </tr>
    <tr>
      <th>27</th>
      <td>261</td>
      <td>[53.442537, -2.288613]</td>
      <td>27.1</td>
      <td>102</td>
    </tr>
    <tr>
      <th>28</th>
      <td>281</td>
      <td>[53.442658, -2.288969]</td>
      <td>26.9</td>
      <td>93</td>
    </tr>
    <tr>
      <th>29</th>
      <td>290</td>
      <td>[53.442714, -2.289297]</td>
      <td>26.6</td>
      <td>93</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>970</th>
      <td>7624</td>
      <td>[53.447453, -2.288967]</td>
      <td>27.1</td>
      <td>134</td>
    </tr>
    <tr>
      <th>971</th>
      <td>7633</td>
      <td>[53.447281, -2.288883]</td>
      <td>27.4</td>
      <td>134</td>
    </tr>
    <tr>
      <th>972</th>
      <td>7642</td>
      <td>[53.447157, -2.288638]</td>
      <td>27.5</td>
      <td>133</td>
    </tr>
    <tr>
      <th>973</th>
      <td>7655</td>
      <td>[53.446957, -2.288351]</td>
      <td>27.6</td>
      <td>134</td>
    </tr>
    <tr>
      <th>974</th>
      <td>7667</td>
      <td>[53.446778, -2.288322]</td>
      <td>27.9</td>
      <td>135</td>
    </tr>
    <tr>
      <th>975</th>
      <td>7679</td>
      <td>[53.446557, -2.288272]</td>
      <td>28.3</td>
      <td>135</td>
    </tr>
    <tr>
      <th>976</th>
      <td>7688</td>
      <td>[53.446428, -2.288001]</td>
      <td>28.5</td>
      <td>134</td>
    </tr>
    <tr>
      <th>977</th>
      <td>7704</td>
      <td>[53.446314, -2.2875]</td>
      <td>28.7</td>
      <td>132</td>
    </tr>
    <tr>
      <th>978</th>
      <td>7714</td>
      <td>[53.446295, -2.287153]</td>
      <td>28.8</td>
      <td>132</td>
    </tr>
    <tr>
      <th>979</th>
      <td>7723</td>
      <td>[53.446241, -2.286841]</td>
      <td>28.8</td>
      <td>132</td>
    </tr>
    <tr>
      <th>980</th>
      <td>7732</td>
      <td>[53.446219, -2.286584]</td>
      <td>28.8</td>
      <td>133</td>
    </tr>
    <tr>
      <th>981</th>
      <td>7750</td>
      <td>[53.446147, -2.286197]</td>
      <td>28.8</td>
      <td>126</td>
    </tr>
    <tr>
      <th>982</th>
      <td>7759</td>
      <td>[53.446105, -2.285897]</td>
      <td>28.9</td>
      <td>124</td>
    </tr>
    <tr>
      <th>983</th>
      <td>7768</td>
      <td>[53.446081, -2.285669]</td>
      <td>28.9</td>
      <td>125</td>
    </tr>
    <tr>
      <th>984</th>
      <td>7785</td>
      <td>[53.446013, -2.285058]</td>
      <td>28.9</td>
      <td>129</td>
    </tr>
    <tr>
      <th>985</th>
      <td>7789</td>
      <td>[53.446002, -2.284903]</td>
      <td>28.9</td>
      <td>128</td>
    </tr>
    <tr>
      <th>986</th>
      <td>7797</td>
      <td>[53.445986, -2.284582]</td>
      <td>28.9</td>
      <td>129</td>
    </tr>
    <tr>
      <th>987</th>
      <td>7815</td>
      <td>[53.44589, -2.283939]</td>
      <td>28.9</td>
      <td>131</td>
    </tr>
    <tr>
      <th>988</th>
      <td>7823</td>
      <td>[53.445822, -2.283648]</td>
      <td>28.8</td>
      <td>132</td>
    </tr>
    <tr>
      <th>989</th>
      <td>7832</td>
      <td>[53.445786, -2.283343]</td>
      <td>28.7</td>
      <td>131</td>
    </tr>
    <tr>
      <th>990</th>
      <td>7840</td>
      <td>[53.445754, -2.283036]</td>
      <td>28.7</td>
      <td>130</td>
    </tr>
    <tr>
      <th>991</th>
      <td>7848</td>
      <td>[53.445717, -2.282729]</td>
      <td>28.5</td>
      <td>129</td>
    </tr>
    <tr>
      <th>992</th>
      <td>7857</td>
      <td>[53.445673, -2.28241]</td>
      <td>28.5</td>
      <td>130</td>
    </tr>
    <tr>
      <th>993</th>
      <td>7866</td>
      <td>[53.445637, -2.282092]</td>
      <td>28.4</td>
      <td>131</td>
    </tr>
    <tr>
      <th>994</th>
      <td>7882</td>
      <td>[53.445555, -2.281553]</td>
      <td>28.4</td>
      <td>131</td>
    </tr>
    <tr>
      <th>995</th>
      <td>7890</td>
      <td>[53.445504, -2.281259]</td>
      <td>28.4</td>
      <td>131</td>
    </tr>
    <tr>
      <th>996</th>
      <td>7899</td>
      <td>[53.445462, -2.280936]</td>
      <td>28.3</td>
      <td>132</td>
    </tr>
    <tr>
      <th>997</th>
      <td>7908</td>
      <td>[53.445466, -2.280602]</td>
      <td>28.3</td>
      <td>130</td>
    </tr>
    <tr>
      <th>998</th>
      <td>7922</td>
      <td>[53.445567, -2.280221]</td>
      <td>27.8</td>
      <td>128</td>
    </tr>
    <tr>
      <th>999</th>
      <td>7937</td>
      <td>[53.445763, -2.280173]</td>
      <td>27.4</td>
      <td>131</td>
    </tr>
  </tbody>
</table>
<p>1000 rows × 4 columns</p>
</div>




```python

```


```python

```


```python

```




    361




```python

```




    4096




```python

```

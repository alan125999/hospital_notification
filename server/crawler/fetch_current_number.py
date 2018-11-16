#!/bin/python3
import urllib.request
import json
def parse(x): 
    return {
        'doctorName': x.doctorName, 
        'RoomStatus': x.RoomStatus, 
        'calledNumber': x.calledNumber
    }

doctorStatus = []
for id in range(1000):
    url = 'http://59.125.231.55/trews/api/GetDptRoomInfo?DptID={0:03d}'.format(id)
    fpIn = urllib.request.urlopen(url)
    data = fpIn.read().decode('utf8')
    if data != '[]':
        # Store Data
        ''' 
        fpOut = open('./cralwerData/{0:03d}'.format(id), 'w')
        fpOut.write(data)
        '''
        jsonData = json.loads(data)
        doctorStatus += list(map(lambda x: {
            'deptName': x['deptName'].strip(),
            'doctorName': x['doctorName'],
            'RoomStatus': x['RoomStatus'],
            'calledNumber': x['calledNumber'], 
        }, jsonData))
print(doctorStatus)


''' data format
[
    {
        "RoomStatus": "準備中",
        "deptID": "023 ",
        "deptName": "心臟血管科        ",
        "opdTimeID": "P",
        "roomID": "500",
        "roomName": "500診",
        "roomLocation": "門診大樓5樓",
        "doctorID": "7536",
        "doctorName": "許容綺",
        "calledNumber": "0"
    },
]

{
        "RoomStatus": 準備中 / 看診中,
        "deptID": 科別代號,
        "deptName": 科別名稱,
        "opdTimeID": (尚未猜到是什麼),
        "roomID": 診間代號,
        "roomName": 診間名稱（房號）,
        "roomLocation": 診間位置（棟別、樓層）,
        "doctorID": 醫師編號,
        "doctorName": 醫師姓名,
        "calledNumber": 當前號碼
    }
'''

{
        "RoomStatus": 準備中 / 看診中,
        "deptID": 科別代號,
        "deptName": 科別名稱,
        "opdTimeID": (尚未猜到是什麼),
        "roomID": 診間代號,
        "roomName": 診間名稱（房號）,
        "roomLocation": 診間位置（棟別、樓層）,
        "doctorID": 醫師編號,
        "doctorName": 醫師姓名,
        "calledNumber": 當前號碼
    }
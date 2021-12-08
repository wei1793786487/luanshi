import requests

cookies = {
    'pgv_info': 'ssid=s9472176168',
    'pgv_pvid': '311909710',
    'slgqqcomrouteLine': 'a20210220newstar_a20210824jdls_a20210220newstar_a20210824jdls',
    'tokenParams': '%3Froleid%3D2041623802665%26openid%3DoLYPusmWdAYXyJDrAXmw1gQTQ_ck%26partition%3D2665%26platid%3D0%26areaid%3D1%26appid%3Dwxce0a39d8e25a6763%26algorithm%3Ditop%26encode%3D2%26channelid%3D1%26nickname%3D%25E9%25A3%258E%26gameid%3D16274%26os%3D2%26ts%3D1638925552%26version%3D5.16.000.4093%26seq%3D16274-D5CB5582-3838-4629-B506-54B17BADE320-1638925552-2506%26sig%3D970a4af0c1bf1717b8ff1c37a1d5fabd%26itopencodeparam%3D1ACD9448701613950EA72FCE0380B5AAF8671B22106355E77105A91D49DA605B788963DA0DCAD0CDA96BA7561C5FA5C295EEF56B021B1938C57B325B04238B7B9933603FA74FDE3D93D5DDA2A0DBF4ECD3C58AA2E705EC1549DBCBD156EA5E348C99BBEA071ED841831F1EA21F70239ECF679398550F47B428E4653AE5AF5B03E40E8303286559DDC4EF9B02B7388244DE0D966D3DB4F1DD27C5F522B6D4454403F93C356116532456D270CEC4E9BC1B18065084ADE6D85EF65784FDAF2D4E09C05009EDC94E79D9FE672AC3D4146479',
    'isActDate': '18965',
    'isHostDate': '18965',
    'ts_uid': '6239562813',
    'PTTactFirstTime': '1638489600000',
    'PTTuserFirstTime': '1638489600000',
    'weekloop': '0-0-0-49',
    'eas_sid': 'R1m663X8U5C2W6f6A2b1y0N6Y7',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MSDK/5.16.000.4055 mQQAppId/1105371489 mWXAppId/wxce0a39d8e25a6763 mGameId/16274 MSDKDeviceModel/D5CB5582-3838-4629-B506-54B17BADE320',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'x8m8.ams.game.qq.com',
    'Origin': 'https://slg.qq.com',
    'Referer': 'https://slg.qq.com/ingame/a20211027jdls/page.html?roleid=2041623802665&openid=oLYPusmWdAYXyJDrAXmw1gQTQ_ck&partition=2665&platid=0&areaid=1&appid=wxce0a39d8e25a6763&algorithm=itop&encode=2&channelid=1&nickname=%E9%A3%8E&gameid=16274&os=2&ts=1638925552&version=5.16.000.4093&seq=16274-D5CB5582-3838-4629-B506-54B17BADE320-1638925552-2506&sig=970a4af0c1bf1717b8ff1c37a1d5fabd&itopencodeparam=1ACD9448701613950EA72FCE0380B5AAF8671B22106355E77105A91D49DA605B788963DA0DCAD0CDA96BA7561C5FA5C295EEF56B021B1938C57B325B04238B7B9933603FA74FDE3D93D5DDA2A0DBF4ECD3C58AA2E705EC1549DBCBD156EA5E348C99BBEA071ED841831F1EA21F70239ECF679398550F47B428E4653AE5AF5B03E40E8303286559DDC4EF9B02B7388244DE0D966D3DB4F1DD27C5F522B6D4454403F93C356116532456D270CEC4E9BC1B18065084ADE6D85EF65784FDAF2D4E09C05009EDC94E79D9FE672AC3D4146479',
}

params = (
    ('ameVersion', '0.3'),
    ('sServiceType', 'slg'),
    ('iActivityId', '419927'),
    ('sServiceDepartment', 'group_g'),
    ('sSDID', 'b4c62aa5217c07e5f15837c9d13f3620'),
    ('sMiloTag', 'AMS-MILO-419927-815799-unknown-1638925578073-KkpYn8'),
    ('_', '1638925578079'),
)

data = {
  'appid': 'wxce0a39d8e25a6763',
  'sArea': '1',
  'sPlatId': '0',
  'sPartition': '2665',
  'gameid': '16274',
  'os': '2',
  'channelid': '1',
  'seq': '16274-D5CB5582-3838-4629-B506-54B17BADE320-1638925552-2506',
  'ts': '1638925552',
  'version': '5.16.000.4093',
  'source': '',
  'sig': '970a4af0c1bf1717b8ff1c37a1d5fabd',
  'itopencodeparam': '1ACD9448701613950EA72FCE0380B5AAF8671B22106355E77105A91D49DA605B788963DA0DCAD0CDA96BA7561C5FA5C295EEF56B021B1938C57B325B04238B7B9933603FA74FDE3D93D5DDA2A0DBF4ECD3C58AA2E705EC1549DBCBD156EA5E348C99BBEA071ED841831F1EA21F70239ECF679398550F47B428E4653AE5AF5B03E40E8303286559DDC4EF9B02B7388244DE0D966D3DB4F1DD27C5F522B6D4454403F93C356116532456D270CEC4E9BC1B18065084ADE6D85EF65784FDAF2D4E09C05009EDC94E79D9FE672AC3D4146479',
  'isGopenid': '',
  'gameId': '',
  'iSex': '',
  'sRoleId': '2041623802665',
  'iGender': '',
  'area': '1',
  'platId': '0',
  'partition': '2665',
  'roleid': '',
  'sOpenId': 'oLYPusmWdAYXyJDrAXmw1gQTQ_ck',
  'openid': 'oLYPusmWdAYXyJDrAXmw1gQTQ_ck',
  'timestamp': '',
  'iMatchSort': '1',
  'sServiceType': 'slg',
  'objCustomMsg': '',
  'areaname': '',
  'rolelevel': '',
  'rolename': '',
  'areaid': '',
  'iActivityId': '419927',
  'iFlowId': '815799',
  'g_tk': '1842395457',
  'e_code': '0',
  'g_code': '0',
  'eas_url': 'http://slg.qq.com/ingame/a20211027jdls/page.html',
  'eas_refer': 'http://slg.qq.com/ingame/a20211027jdls/?reqid=5952619e-345b-4ed2-b8ed-820904a9ca41&version=24',
  'sServiceDepartment': 'group_g'
}

response = requests.post('https://x8m8.ams.game.qq.com/ams/ame/amesvr', headers=headers, params=params, cookies=cookies, data=data, verify=False)
print(response.json())
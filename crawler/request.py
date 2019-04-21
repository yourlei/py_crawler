# -*- encoding: utf8 -*-
# 获取lagou职位数据

import requests
import pandas as pd
import time

def get_json():
  """获取json"""
  # url = "https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false"
  url  = "https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false"
  # 定义请求头
  headers = {
    "Host": "www.lagou.com",
    "Origin": "https://www.lagou.com",
    "Referer": "https://www.lagou.com/jobs/list_Node.js?px=default&city=%E5%85%A8%E5%9B%BD",
    "Cookie": '_ga=GA1.2.1657033319.1555332324; user_trace_token=20190415204524-565aaa56-5f7c-11e9-85ed-525400f775ce; LGUID=20190415204524-565aae23-5f7c-11e9-85ed-525400f775ce; JSESSIONID=ABAAABAAADEAAFI3EBECF4BFE76A6B4DD0DBC9C69276224; _gid=GA1.2.965522709.1555827205; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1555332324,1555827206; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216a3e873ff2778-096ac17acad662-3e76035c-1049088-16a3e873ff341e%22%2C%22%24device_id%22%3A%2216a3e873ff2778-096ac17acad662-3e76035c-1049088-16a3e873ff341e%22%7D; sajssdk_2015_cross_new_user=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=183; index_location_city=%E6%B7%B1%E5%9C%B3; login=false; unick=""; _putrc=""; LG_LOGIN_USER_ID=""; TG-TRACK-CODE=index_navigation; _gat=1; LGSID=20190421144937-a12a2aca-6401-11e9-9b61-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_Node.js%3Fpx%3Ddefault%26city%3D%25E5%2585%25A8%25E5%259B%25BD; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; SEARCH_ID=c6dc4e2a2e0246f1a0c2188de2019143; X_HTTP_TOKEN=a812d27d6677b48b3939285551bc4bfc317fea28db; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1555829393; LGRID=20190421144953-aabfe0ee-6401-11e9-9b61-5254005c3644',
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": "None",
    "X-Requested-With": "XMLHttpRequest"
  }
  writer = pd.ExcelWriter('output_result.xlsx')
  offset = 1
  column = [
    "businessZones",
    "city",
    "companyFullName",
    "companyLabelList",
    "companyShortName",
    "companySize",
    "createTime",
    "district",
    "education",
    "financeStage",
    "firstType",
    "formatCreateTime",
    "industryField",
    "industryLables",
    "jobNature",
    "linestaion",
    "positionAdvantage",
    "positionLables",
    "positionName",
    "salary",
    "secondType",
    "skillLables",
    "stationname",
    "workYear"
  ]
  for pn in range(1, 30):
    # post 数据
    payload = {
      "first": "false",
      "pn": pn,
      "kd": "Node.js"
    }
    res = requests.post(url, headers = headers, data=payload)
    res.raise_for_status
    res.encoding = "utf-8"

    try:
      result = res.json()
    except Exception as e:
      raise(e)
    positions = []
    print(result, ".................")
    if result["state"] == 2403:
      print("等待..............")
      time.sleep(8)
      continue
    positions.extend(result["content"]["positionResult"]["result"])
    # writer = pd.ExcelWriter('output.xlsx')
    df = pd.DataFrame(positions)
    df_new = df[column]
    if offset > 1:
      df_new.to_excel(writer, header = None, index=False, startrow = offset)
    else:
      df_new.to_excel(writer, index=False)
    writer.save()
    offset = offset + len(positions)
    time.sleep(3)
  pass

if __name__ == "__main__":
  get_json()
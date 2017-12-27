# -*- coding: utf-8 -*-
# @Time    : 2017/12/25
# @Author  : Luke

import pandas as pd

from cn_mobile_location.district_process import all_dis, cities

new_file = "mobile"

n_rows = None
mobile2zip = pd.read_csv("Mobile201703.txt", sep=',', nrows=n_rows, header=None,
                         dtype=str)

# 删除序号列
mobile2zip = mobile2zip.drop(0, axis=1)

result_district = []

for i, (province, city) in enumerate(zip(mobile2zip.iloc[:, 1], mobile2zip.iloc[
                                                                :, 2])):
    if i % 10000 == 0:
        print("processed %s lines" % i)
    # if i > 1000:
    #     break
    city_sim = [ci for ci in cities if city in ci]
    if len(city_sim) == 1:
        result_district.append(all_dis[city_sim[0]].no)
    else:
        flag = True
        for ci in city_sim:
            try:
                if (not ci.endswith('省')) and \
                        (province in all_dis[ci].get_super_dis().name or (
                                all_dis[ci].get_super_dis().get_super_dis() and
                                province in
                                all_dis[
                                    ci].get_super_dis().get_super_dis().name)):
                    result_district.append(all_dis[ci].no)
                    flag = False
                    break
            except AttributeError:
                print("Attri")
        if flag:
            print(province, city)

result_district = [res+'0'*(6-len(res)) for res in result_district]
mobile2zip.loc[:,7] = result_district

mobile2zip.to_csv("手机号归属地_邮编_行政区划.csv",header=None,index=None)

print("done")

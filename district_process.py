# -*- coding: utf-8 -*-
# @Time    : 2017/12/25
# @Author  : Luke

class district():
    def __init__(self,name,no):
        self.name = name
        self.no = no
        self.child_name = {}
        self.child_no = {}
        self.parent = None

    def set_child_dis(self,name,no,ob):
        self.child_name[name] = ob
        self.child_no[no] = ob

    def get_child_by_name(self,name):
        return self.child_name[name]

    def get_child_by_no(self, no):
        return self.child_name[no]

    def set_super_dis(self,ob):
        self.parent = ob

    def get_super_dis(self):
        return self.parent

provinces = {}
all_dis = {}
cities = []

cities_direct = {'北京', '重庆', '天津', '上海'}

path_admin_code = "行政区划表20171123"
with open(path_admin_code) as dis:
    for line in dis:
        items = line.strip().split('\t')
        if items[0].endswith('0000'):
            dis = district(items[1],items[0][:2])
            provinces[items[0][:2]] = dis
            provinces[items[1]] = dis
            all_dis[items[0][:2]] = dis

        elif items[0].endswith('00'):
            dis = district(items[1],items[0][:4])
            province = provinces[items[0][:2]]
            dis.set_super_dis(province)
            province.set_child_dis(items[1],items[0][:4],dis)
            all_dis[items[0][:4]] = dis

        else:
            dis = district(items[1],items[0])

            try:
                city1 = all_dis[items[0][:4]]
            except KeyError:
                pass
            else:
                dis.set_super_dis(city1)
                city1.set_child_dis(items[1],items[0],dis)

            all_dis[items[0]] = dis

        all_dis[items[1]] = dis
        if items[1] in cities_direct: continue
        cities.append(items[1])

print("done")





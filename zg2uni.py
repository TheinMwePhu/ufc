# -*- coding: utf-8 -*-
import re


def convert(input):
    output = input

    output = output.replace(u'\u106A', u'\u1009')
    output = re.sub(u'\u103D',u'\u103E',output)
    output = re.sub(u'\u103C',u'\u103D',output)
    output = re.sub(u'[\u103b\u107e\u107f\u1080\u1081\u1082\u1083\u1084]', u'\u103c', output)
    output = re.sub(u'\u1033',u'\u102f',output)
    output = re.sub(u'\u1034',u'\u1030',output)
    output = re.sub(u'[\u103A\u107D]',u'\u103B',output)
    output = re.sub(u'\u1039',u'\u103A',output)
    output = re.sub(u'\u104E', u'[\u1004\u103A\u1038\u104E]', output)
    output = re.sub(u'\u105A',u'[\u103A\u102B]',output)
    output = re.sub(u'\u1060',u'[\u103A\u1000]',output)
    output = re.sub(u'\u1061',u'[\u103A\u1001]',output)
    output = re.sub(u'\u1062',u'[\u103A\u1002]',output)
    output = re.sub(u'\u1063',u'[\u103A\u1003]',output)
    output = re.sub(u'\u1064',u'[\u1004\u103A\u1039]',output)
    output = re.sub(u'\u1065',u'[\u1039\u1005]',output)
    output = re.sub(u'\u1066',u'[\u1039\u1006]',output)
    output = re.sub(u'\u1067',u'[\u1039\u1007]',output)
    output = re.sub(u'\u1068',u'[\u1039\u1008]',output)
    output = re.sub(u'\u1069',u'[\u1039\u1009]',output)
    output = re.sub(u'\u106B',u'\u100A',output)
    output = re.sub(u'\u106C',u'[\u1039\u100B]',output)
    output = re.sub(u'\u106D',u'\u100C',output)
    output = re.sub(u'\u106E',u'\u100D',output)









    return output

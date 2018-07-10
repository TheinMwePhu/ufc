import re

def convert(input):
    output = input

    output = re.sub(u'\u1039\u1000', u'\u1060', output)
    output = re.sub(u'\u1039\u1001', u'\u1061', output)
    output = re.sub(u'\u1039\u1002', u'\u1062', output)
    output = re.sub(u'\u1039\u1003', u'\u1063', output)
    output = re.sub(u'\u1039\u1004', u'\u1064', output)
    output = re.sub(u'\u1039\u1005', u'\u1065', output)
    output = re.sub(u'\u1039\u1006', u'\u1066', output)
    output = re.sub(u'\u1039\u1007', u'\u1068', output)
    output = re.sub(u'\u1039\u1008', u'\u1069', output)
    output = re.sub(u'\u1039\u100b', u'\u106c', output)
    output = re.sub(u'\u1039\u100c', u'\u106d', output)
    output = re.sub(u'\u1039\u100d', u'\u106e', output)
    output = re.sub(u'\u1039\u100e', u'\u106f', output)
    output = re.sub(u'\u1039\u100f', u'\u1070', output)
    output = re.sub(u'\u1039\u1010', u'\u1071', output)
    output = re.sub(u'\u1039\u1011', u'\u1073', output)
    output = re.sub(u'\u1039\u1012', u'\u1075', output)
    output = re.sub(u'\u1039\u1013', u'\u1076', output)
    output = re.sub(u'\u1039\u1015', u'\u1078', output)
    output = re.sub(u'\u1039\u1016', u'\u1079', output)
    output = re.sub(u'\u1039\u1017', u'\u107a', output)
    output = re.sub(u'\u1039\u1018', u'\u107b', output)
    output = re.sub(u'\u1039\u101c', u'\u1085', output)
    output = re.sub(u'\u103f', u'\u1086', output)
    output = re.sub(u'\u101b', u'\u1090', output)
    output = re.sub(u'\u100f\u1039\u100d', u'\u1091', output)
    output = re.sub(u'\u100b\u1039\u100b', u'\u1097', output)
    output = re.sub(u'\u103a', u'\u1039', output)
    output = re.sub(u'\u103b', u'\u103a', output)
    output = re.sub(u'\u103c', u'\u103b', output)
    output = re.sub(u'\u103d', u'\u103c', output)
    output = re.sub(u'\u103e', u'\u103d', output)
    output = re.sub(u'\u100a\u108a', u'\u106b\u108a', output)
    output = re.sub(u'\u1014([\u103d\u108a])', u'\u1077\\1', output)
    output = re.sub(u'([\u108a\u103b])\u102f', u'\\1\u1033', output)
    output = re.sub(u'([\u108a\u103b])\u1030', u'\\1\u1034', output)
    output = re.sub(u'\u108c\u103d', u'\\1\u108a', output)
    # 1=letters 2=yayit 3=yapint 4=waswe 5=hatoe 6=waswe_hatoe 7=tawaetoe 8=nga_tat 9=aumyit 10=yaychar
    output = re.sub(
        u'([\u1000-\u1021])((?:\u103b)?)((?:\u103a)?)((?:\u103c)?)((?:\u103d)?)((?:\u108a)?)((?:\u1031)?)((?:\u1039)?)((?:\u1037)?)((:\u102c)?)',
        '\\7\\2\\1\\3\\4\\5\\6\\8\\9\\10', output)

    # ngatat and wasapaut


    output = re.sub(u'\u1038\u1039', u'\u1039\u1038', output)
    # ya_yit
    output = re.sub(u'\u103b([\u1000\u1003\u1006\u100f\u1010\u1011\u1018\u101a\u101c\u101e\u101f\u1021])', u'\u107e\\1',
                    output)  # ya_yit_agyi
    output = re.sub(u'\u103b([\u1000-\u1021])([\u102d\u102e\u1036])', u'\u107f\\1\\2',
                    output)  # yayit with long_gyi_din(sanke)
    output = re.sub(u'\u107e([\u1000-\u1021])([\u102d\u102e\u1036])', u'\u1080\\1\\2',
                    output)  # yayit_agi with long_gyi_din(sanke)
    output = re.sub(u'\u103b([\u1000-\u1021])(\u103c)', u'\u1081\\1\\2', output)  # yayit with waswe
    output = re.sub(u'\u107e([\u1000-\u1021])(\u103c)', u'\u1082\\1\\2', output)  # yayit_agyi with waswe
    output = re.sub(u'\u107f([\u1000-\u1021])([\u102d\u102e\u1036])(\u103c)', u'\u1083\\1\\2\\3', output)  # yayit apyat
    output = re.sub(u'\u1080([\u1000-\u1021])([\u102d\u102e\u1036])(\u103c)', u'\u1084\\1\\2\\3',
                    output)  # yayit_agi apyat

    # ta/na_chuang_ngin
    output = re.sub(u'([\u1008\u100b\u100c\u100d\u1020])\u102f', u'\\1\u1033', output)  # 1cn with some letters
    output = re.sub(u'([\u1008\u100b\u100c\u100d\u1020])\u1030', u'\\1\u1034', output)  # 2cn with some letters
    output = re.sub(u'([\u103b\u107e\u107f\u1080])([\u1000-\u1021])((?:[\u102d\u102e\u1036])?)\u102f',
                    u'\\1\\2\\3\u1033', output)  # yayit&1cn
    output = re.sub(u'([\u103b\u107e\u107f\u1080])([\u1000-\u1021])((?:[\u102d\u102e\u1036])?)\u1030',
                    u'\\1\\2\\3\u1034', output)  # yayit&2cn
    output = re.sub(u'(\u103a)((?:[\u102d\u102e])?)\u102f', u'\\1\\2\u1033', output)  # yapint&1cn
    output = re.sub(u'(\u103a)((?:[\u102d\u102e])?)\u1030', u'\\1\\2\u1034', output)  # yapint&2cn
    output = re.sub(u'([\u1060-\u1063])((?:[\u102d\u102e])?)\u102f', u'\\1\\2\u1033',
                    output)  # 1cn with prsint before from kagyi_gagyi
    output = re.sub(u'([\u1065-\u1069])((?:[\u102d\u102e])?)\u102f', u'\\1\\2\u1033',
                    output)  # 1cn with prsint before from salone_samyintswe
    output = re.sub(u'([\u106c-\u107c])((?:[\u102d\u102e])?)\u102f', u'\\1\\2\u1033',
                    output)  # 1cn with prsint before from ttlg_ma
    output = re.sub(u'([\u1085\u1093])((?:[\u102d\u102e])?)\u102f', u'\\1\\2\u1033',
                    output)  # 1cn with prsint before la and bagone
    output = re.sub(u'([\u1060-\u1063])((?:[\u102d\u102e])?)\u1030', u'\\1\\2\u1034',
                    output)  # 2cn with prsint before from kagyi_gagyi
    output = re.sub(u'([\u1065-\u1069])((?:[\u102d\u102e])?)\u1030', u'\\1\\2\u1034',
                    output)  # 2cn with prsint before from salone_samyintswe
    output = re.sub(u'([\u106c-\u107c])((?:[\u102d\u102e])?)\u1030', u'\\1\\2\u1034',
                    output)  # 2cn with prsint before from ttlg_ma
    output = re.sub(u'([\u1085\u1093])((?:[\u102d\u102e])?)\u1030', u'\\1\\2\u1034',
                    output)  # 2cn with prsint before la and bagone

    # hatoe
    output = re.sub(u'\u100a\u103d', u'\u100a\u1087', output)  # nya with hatoe

    # oo
    output = re.sub(u'\u1009(\u1039)', u'\u1025\\1', output)  # nyapyat_to_oo

    # ya_pint
    output = re.sub(u'\u103a([\u103c\u103d])', u'\u107d\\1', output)  # with hatoe

    # nag_nge_apyat
    output = re.sub(u'\u1014([\u103d\u103c])', u'\u108f\\1', output)
    output = re.sub(u'\u1014([\u1060-\u1063])', u'\u108f\\1', output)  # 2cn with prsint before from kagyi_gagyi
    output = re.sub(u'\u1014([\u1065-\u1069])', u'\u108f\\1', output)  # 2cn with prsint before from salone_samyintswe
    output = re.sub(u'\u1014([\u106c-\u107c])', u'\u108f\\1', output)  # 2cn with prsint before from ttlg_ma
    output = re.sub(u'\u1014([\u1085\u1093])', u'\u108f\\1', output)  # 2cn with prsint before la and bagone

    # aut_myit
    output = re.sub(u'([\u1014\u102f\u1030\u1033\u1034])((?:[\u1032\u1036])?)\u1037', u'\\1\\2\u1094', output)
    output = re.sub(u'([\u103c\u103d\u108a])((?:[\u1032\u1036])?)\u1037', u'\\1\\2\u1095', output)

    # yaguat
    output = re.sub(u'\u101b([\u102f\u1030])', u'\u1090\\1', output)

    # nya


    output = re.sub(u'\u100a(\u108a)', u'\u106b\\1', output)  # with waswe_hatoe




    return output
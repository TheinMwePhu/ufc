import re


def replace(input):

    output = input

    output = re.sub(u'\u0075', u'\u1000', output)
    output = re.sub(u'\u0063', u'\u1001', output)
    output = output.replace(u'\u002a', u'\u1002')
    output = re.sub(u'\u0043', u'\u1003', output)
    output = re.sub(u'\u0069', u'\u1004', output)
    output = re.sub(u'\u0070', u'\u1005', output)
    output = re.sub(u'\u0071', u'\u1006', output)
    output = re.sub(u'\u005A', u'\u1007', output)
    output = re.sub(u'\u00da', u'\u1009', output)
    output = re.sub(u'[\u006e\u00f1]', u'\u100a', output)
    output = re.sub(u'\u0023', u'\u100b', output)
    output = re.sub(u'\u0058', u'\u100c', output)
    output = re.sub(u'\u0021', u'\u100d', output)
    output = re.sub(u'\u00a1', u'\u100e', output)
    output = re.sub(u'\u0050', u'\u100f', output)
    output = re.sub(u'\u0077', u'\u1010', output)
    output = re.sub(u'\u0078', u'\u1011', output)
    output = re.sub(u'\u0027', u'\u1012', output)
    output = re.sub(u'\u0022', u'\u1013', output)
    output = re.sub(u'[\u0045\u0065]', u'\u1014', output)
    output = re.sub(u'\u0079', u'\u1015', output)
    output = re.sub(u'\u007a', u'\u1016', output)
    output = re.sub(u'\u0041', u'\u1017', output)
    output = re.sub(u'\u0062', u'\u1018', output)
    output = re.sub(u'\u0072', u'\u1019', output)
    output = re.sub(u'\u002c', u'\u101a', output)
    output = re.sub(u'[\u0026\u00bd]', u'\u101b', output)
    output = re.sub(u'\u0076', u'\u101c', output)
    output = re.sub(u'\u0030', u'\u101d', output)
    output = re.sub(u'\u006f', u'\u101e', output)
    output = output.replace(u'\u005b', u'\u101f')
    output = re.sub(u'\u0056', u'\u1020', output)
    output = re.sub(u'\u0074', u'\u1021', output)
    output = re.sub(u'\u00a3', u'\u1023', output)
    output = re.sub(u'\u00fe', u'\u1024', output)
    output = re.sub(u'[\u004f\u00cd]', u'\u1025', output)
    output = re.sub(u'\u007b', u'\u1027', output)
    output = re.sub(u'\u0067', u'\u102b', output)
    output = re.sub(u'\u006d', u'\u102c', output)
    output = re.sub(u'\u0064', u'\u102d', output)
    output = re.sub(u'\u0044', u'\u102e', output)
    output = re.sub(u'\u1025\u102e', u'\u1026', output)
    output = re.sub(u'[\u004b\u006b]', u'\u102f', output)
    output = re.sub(u'[\u004c\u006c]', u'\u1030', output)
    output = re.sub(u'\u0061', u'\u1031', output)
    output = re.sub(u'\u004a', u'\u1032', output)
    output = re.sub(u'\u0048', u'\u1036', output)
    output = re.sub(u'[\u0055\u0059\u0068]', u'\u1037', output)
    output = re.sub(u'\u003b', u'\u1038', output)
    output = re.sub(u'\u0066', u'\u103a', output)
    output = re.sub(u'[\u0073\u00df]', u'\u103b', output)
    output = re.sub(u'\u1005\u103b', u'\u1008', output)
    output = re.sub(u'[\u006A\u0042\u004d\u004e\u0060\u007e]', u'\u103c', output)
    output = re.sub(u'\u0047', u'\u103d', output)
    output = re.sub(u'[\u0053\u00a7]', u'\u103e', output)
    output = re.sub(u'\u00f3', u'\u003f', output)
    output = re.sub(u'\u0031', u'\u1041', output)
    output = re.sub(u'\u0032', u'\u1042', output)
    output = re.sub(u'\u0033', u'\u1043', output)
    output = re.sub(u'\u0034', u'\u1044', output)
    output = re.sub(u'\u0035', u'\u1045', output)
    output = re.sub(u'\u0036', u'\u1046', output)
    output = re.sub(u'\u0037', u'\u1047', output)
    output = re.sub(u'\u0038', u'\u1048', output)
    output = re.sub(u'\u0039', u'\u1049', output)
    output = output.replace(u'\u003f', u'\u104a')
    output = output.replace(u'\u002f', u'\u104b')
    output = re.sub(u'\u00fc', u'\u104c', output)
    output = re.sub(u'\u00ed', u'\u104d', output)
    output = re.sub(u'\u00a4', u'\u104e', output)
    output = output.replace(u'\u005c', u'\u104f')
    output = output.replace(u'\u00ab', u'[')
    output = output.replace(u'\u00bb', u']')

    return output


def decompose(input):

    output = input

    output = re.sub(u'\u003a', u'\u102b\u103a', output)
    output = output.replace(u'\u0024', u'\u1000\u103b\u1015\u103a')
    output = re.sub(u'[\u003c\u003e]', u'\u103c\u103d', output)
    output = re.sub(u'\u0040', u'\u100f\u1039\u100d', output)
    output = re.sub(u'\u0049', u'\u103e\u102f', output)
    output = re.sub(u'[\u0051\u00fb]', u'\u103b\u102f', output)
    output = re.sub(u'\u0052', u'\u103b\u103d', output)
    output = re.sub(u'\u0054', u'\u103d\u103e', output)
    output = re.sub(u'\u0057', u'\u103b\u103d\u103e', output)
    output = output.replace(u'\u007c', u'\u100b\u1039\u100c')
    output = re.sub(u'\u00aa', u'\u103e\u1030', output)
    output = re.sub(u'\u00a2', u'\u1039\u1003', output)
    output = re.sub(u'\u00a5', u'\u100b\u1039\u100b', output)
    output = re.sub(u'\u00a6', u'\u1039\u1011', output)
    output = re.sub(u'\u00a8', u'\u1039\u1013', output)
    output = re.sub(u'\u00a9', u'\u1039\u1001', output)
    output = re.sub(u'[\u00ac\u00c7]', u'\u1039\u1018', output)
    output = re.sub(u'\u00ae', u'\u1039\u1019', output)
    output = re.sub(u'\u00b2', u'\u1039\u100c', output)
    output = re.sub(u'\u00b3', u'\u1039\u100b', output)
    output = re.sub(u'\u00b4', u'\u1039\u1012', output)
    output = re.sub(u'\u00b9', u'\u100d\u1039\u100e', output)
    output = re.sub(u'\u00be', u'\u1039\u1002', output)
    output = re.sub(u'\u00c1', u'\u1039\u1017', output)
    output = re.sub(u'[\u00c5\u00e5]', u'\u1039\u1010', output)
    output = re.sub(u'\u00c6', u'\u1039\u1007', output)
    output = re.sub(u'\u00c9', u'\u1039\u1010\u103d', output)
    output = re.sub(u'\u00d1', u'\u1039\u1008', output)
    output = re.sub(u'\u00d3', u'\u1009\u102c', output)
    output = re.sub(u'\u00d6', u'\u1039\u100f', output)
    output = re.sub(u'\u00d7', u'\u100d\u1039\u100d', output)
    output = re.sub(u'\u00dc', u'\u1039\u1015', output)
    output = re.sub(u'\u00e4', u'\u1039\u1006', output)
    output = re.sub(u'\u00e6', u'\u1039\u1016', output)
    output = re.sub(u'\u00e9', u'\u1039\u1014', output)
    output = re.sub(u'\u00f6', u'\u1039\u1005', output)
    output = re.sub(u'\u00fa', u'\u1039\u1000', output)
    output = re.sub(u'\u2019', u'\u1039\u101c', output)
    output = re.sub(u'([\u1000-\u1021])\u0046', u'\u0046\\1', output)
    output = re.sub(u'([\u1000-\u1021])\u00d0', u'\u0046\\1\u102e', output)
    output = re.sub(u'([\u1000-\u1021])\u00d8', u'\u0046\\1\u102d', output)
    output = re.sub(u'([\u1000-\u1021])\u00f8', u'\u0046\\1\u1036', output)
    output = re.sub(u'\u0046', u'\u1004\u103a\u1039', output)
    output = re.sub(u'\u00f0', u'\u102d\u1036', output)

    return output


def visual2logical(input):

    output = input
    output = re.sub(u'((?:\u1031)?)((?:\u103c)?)([\u1000-\u1021])((?:\u103b)?)((?:\u103d)?)((?:\u103e)?)((?:\u1037)?)((?:\u102c)?)', '\\3\\2\\4\\5\\6\\1\\7\\8', output)

    return output


def convert(input):

    output = replace(input)
    output = decompose(output)
    output = visual2logical(output)

return output

import re

def 遞歸re(s, start):
    d = []
    for i in start:
        單位 = re.finditer(i, s)
        for j in 單位:
            gd = j.groupdict()
            d.append(gd)
            if isinstance(start[i], dict):
                gd['類型'] = start[i]['類型']
            if start[i] is not None and '子樹' in start[i]:
                for k in start[i]['子樹']:
                    gd[k] = 遞歸re(gd[k], start[i]['子樹'][k])
    return d


class j棧(list):
    def __init__(self):
        self.append([])

    @property
    def 尾(self):
        return self[-1]

    @property
    def 尾句(self):
        return self[-1][-1]


def 編譯(f, 正則組):
    return 生編譯(f.readlines(), 正則組)


def 生編譯(s, 正則組):
    棧 = j棧()
    g = iter(s)
    for s in g:
        if not re.search('\\S', s):
            if 棧.尾:
                棧.尾句['之後的空白'] = 棧.尾句.get('之後的空白', 0) + 1
            continue

        自 = {}
        自['縮進數'] = len(s) - len(s.lstrip(' '))
        if 自['縮進數'] > 0 and 自['縮進數'] > 棧.尾句['縮進數']:
            棧.尾句['子'] = []
            棧.append(棧.尾句['子'])

        if 棧.尾:
            while 自['縮進數'] < 棧.尾句['縮進數']:
                棧.pop()
            if 棧.尾句['縮進數'] != 自['縮進數']:
                raise Exception('層次錯誤')

        s = s.lstrip(' ')
        s = s.rstrip('\r').rstrip('\n')

        d = 遞歸re(s, 正則組)
        if len(d) == 0:
            raise Exception('『%s 』無法匹配' % s)
        if len(d) > 1:
            print(d)
            raise Exception('『%s 』匹配過多' % s)
        自.update(d[0])

        棧.尾.append(自)
    return 棧[0]

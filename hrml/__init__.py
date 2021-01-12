from hrml import 編譯工具


正則組 = {
    r'^#(?P<註釋>.*)$': {
        '類型': '註釋',
    },
    r'^(?=[^#])(?P<元素>.*?)((?P<自閉>;)|:)$': {
        '類型': 'html元素',
        '子樹': {
            '元素': {
                r'^(?P<名>.*?)(?=([ \.#]|$))(?P<選項>.*?)(?=( |$))(?P<附加>.*?)$': {
                    '類型': '喵喵喵',
                    '子樹': {
                        '選項': {
                            r'(\.(?P<類>.*?(?=[\.#]|$)))|(#(?P<本我>.*?(?=[\.#]|$)))': None
                        }
                    }
                }
            }
        }
    },
    r'^(?=[^#])(?P<文字>(?=[^#]).*?[^:;])$': {
        '類型': '文字'
    }
}


def 檢查(x):
    if '子' in x:
        if x['類型'] != 'html元素':
            raise Exception(f'{x.__repr__()}\n「{x["類型"]}」不能有子元素。')
        elif x['自閉']:
            print(x)
            raise Exception(f'{x.__repr__()}自閉元素不能有子元素。')


def 打印(x):
    檢查(x)
    縮進 = ' ' * x['縮進數']
    if x['類型'] == '註釋':
        return ''
    if x['類型'] == '文字':
        return 縮進 + x['文字'] + '\n'
    if x['類型'] == 'html元素':
        s = ''
        x元 = x['元素'][0]
        s += '%s<%s' % (縮進, x元['名'])
        所有類 = [i['類'] for i in x元['選項'] if i['類']]
        所有本我 = [i['本我'] for i in x元['選項'] if i['本我']]
        if 所有類:
            s += ' class=\'%s\'' % ' '.join(所有類)
        if 所有本我:
            s += ' id=\'%s\'' % ' '.join(所有本我)
        s += x元['附加']
        if x['自閉']:
            s += '/>'
        else:
            if '子' in x:
                s += '>\n'
                for i in x['子']:
                    s += 打印(i)
                s += 縮進
                s += '</%s>' % x元['名']
            else:
                s += '></%s>' % x元['名']
        s += '\n'
        return s


def 樹轉換(t):
    t = (x.rstrip() for x in t)
    編譯結果 = 編譯工具.生編譯(t, 正則組)
    html = ''.join(map(打印, 編譯結果))
    return html


def masturbate(s):
    return 樹轉換(s.splitlines())



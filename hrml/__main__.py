import fire

import hrml


def ember(文件名, o):
    s = hrml.樹轉換(open(文件名, encoding='utf8'))
    with open(o, 'w', encoding='utf-8') as f:
        f.write(s)


fire.Fire(ember)

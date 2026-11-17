from read import w
import json,pathlib
d=pathlib.Path(__file__).parent
rows=[[*r[:3],r[4]] for r in list(w.active.values)[1:]]
assert len(rows)==31992 and len({r[0] for r in rows})==len(rows)
out=(d/'page.html').read_text().replace('__DATA__',json.dumps(rows,ensure_ascii=False,separators=(',',':')).replace('<',r'\u003c'))
(d/'catalog/dist/index.html').write_text(out)
(d.parent/'outputs/工具价格查询.html').write_text(out)

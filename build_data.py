"""Update speed data from an Ookla-extracted workbook.
Usage: python build_data.py '/path/to/Download Speed.xlsx'
Requires: pip install openpyxl
"""
import json,sys,pathlib,openpyxl
root=pathlib.Path(__file__).resolve().parent
if len(sys.argv)<2:raise SystemExit('Usage: python build_data.py "Download Speed.xlsx"')
w=openpyxl.load_workbook(sys.argv[1],read_only=True,data_only=True)
for name in ('State','District','Parliament','DUN'):
    topology=json.loads((root/'data'/f'{name.lower()}.json').read_text())
    geom=next(iter(topology['objects'].values()))['geometries']
    index={g['properties']['key']:g['properties']['idx'] for g in geom}
    output=[];skipped=[]
    for r in list(w[name].values)[1:]:
        if name=='State': key=r[1];year,q,spd,devices=r[4],r[5],r[2],r[3]
        elif name=='District':key=r[1]+'|'+r[2];year,q,spd,devices=r[3],r[4],r[5],r[6]
        elif name=='Parliament':key=r[1]+'|'+r[0];year,q,spd,devices=r[3],r[4],r[5],r[6]
        else:key=r[1]+'|'+r[0]+'|'+r[3];year,q,spd,devices=r[4],r[5],r[6],r[7]
        try:spd=float(spd)
        except (TypeError,ValueError):skipped.append((key,year,q));continue
        if key not in index or not isinstance(year,int) or not isinstance(q,int):skipped.append((key,year,q));continue
        output.append([year,q,index[key],round(spd,4),int(devices or 0)])
    (root/'data'/f'{name.lower()}-speed.json').write_text(json.dumps(output,separators=(',',':')))
    print(f'{name}: {len(output)} records, {len(skipped)} skipped')
    if skipped:print('Sample skipped:',skipped[:10])

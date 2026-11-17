import openpyxl as x,glob
p=glob.glob('/Users/leo/Desktop/2026年电子价格9.7(1).xlsx')[0]
w=x.load_workbook(p,data_only=True)
if __name__=='__main__':
 for s in w:
  print(s.title,s.max_row,s.max_column,s.sheet_state)
  for row in list(s.values)[:7]: print(str([v for v in row if v is not None])[:370])

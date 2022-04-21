#!/bin/env python
# python make_utt2spk.py fd1 F01 test bn20
import sys
import os
def make_utt2spk(fd,spk,dataset,feat):
 path='features/s8_sd'
 file_path=os.path.join(path,fd,spk,dataset,'fmllr_'+feat,'fmllr_'+feat+'.scp')
 f = open(file_path,'r')
 l1=list()
 for line in f:
     l1.append(line.split(' ')[0])
 f.close()
 
 tgt_path=os.path.join(path,fd,spk,dataset,'fmllr_'+feat,'utt2spk')
 with open(tgt_path,'w') as f1:
  for i in l1:
    f1.write(i+' '+i.split('-')[0])
    f1.write('\n')

if __name__ == "__main__":
  if len(sys.argv) < 5:
    print("need 4 params")
    sys.exit(1)
  fd = sys.argv[1]
  spk = sys.argv[2]
  dataset=sys.argv[3]
  feat=sys.argv[4]
  make_utt2spk(fd,spk,dataset,feat)

#!/bin/env python
#for spk in F03 F04 M01 M02 M03 M04 M05; do scp -r fd1_F01_sp_bn20.cfg fd1_${spk}_sp_bn20.cfg; python /data/ac1zy/pytorch-kaldi/chang_spk.py fd1_${spk}_sp_bn20.cfg F01 ${spk}

# for spk in F01 F03 F04 M01 M02 M03 M04 M05; do for fd in fd2 fd3 fd4 fd5; do scp -r fd1_${spk}_sp_bn20.cfg ${fd}_${spk}_sp_bn20.cfg; python /data/ac1zy/pytorch-kaldi/chang_spk.py ${fd}_${spk}_sp_bn20.cfg fd1 ${fd}; done; done
# -*- coding:utf-8 -*-
 
import sys
 
def replace(file_path, old_str, new_str):
  f = open(file_path,'r+')
  all_lines = f.readlines()
  f.seek(0)
  f.truncate()
  for line in all_lines:
    line = line.replace(old_str, new_str)
    f.write(line)
  f.close() 

if __name__ == "__main__":
  if len(sys.argv) < 4:
    print("need 3 params")
    sys.exit(1)
  file_name = sys.argv[1]
  src_str = sys.argv[2]
  dst_str = sys.argv[3]
  replace(file_name, src_str, dst_str)

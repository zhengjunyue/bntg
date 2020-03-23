# bntg

## 1. make dir

mkdir /data/ac1zy/kaldi/egs1/torgo/s9

cd /data/ac1zy/kaldi/egs1/torgo/s9

### 1) make soft links

ln -s ../../../egs/wsj/s5/steps/ ../../../egs/wsj/s5/utils .

mkdir /fastdata/ac1zy/kaldi/egs1/torgo/s9 /fastdata/ac1zy/kaldi/egs1/torgo/s9/data /fastdata/ac1zy/kaldi/egs1/torgo/s9/exp /fastdata/ac1zy/kaldi/egs1/torgo/s9/fmllr /fastdata/ac1zy/kaldi/egs1/torgo/s9/raw_torgo_200ms

ln -s /fastdata/ac1zy/kaldi/egs1/torgo/s9/data /fastdata/ac1zy/kaldi/egs1/torgo/s9/exp /fastdata/ac1zy/kaldi/egs1/torgo/s9/fmllr /fastdata/ac1zy/kaldi/egs1/torgo/s9/raw_torgo_200ms .

### 2) copy files from other folders

scp -r ../s8/conf ../s8/local ../s8/*.sh .


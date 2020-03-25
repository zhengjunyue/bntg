# bntg

Kaldi如何统计data数据集

https://www.cnblogs.com/JarvanWang/p/9152628.html

## 1. make dir

mkdir /data/ac1zy/kaldi/egs1/torgo/s9

cd /data/ac1zy/kaldi/egs1/torgo/s9

### 1) make soft links

ln -s ../../../egs/wsj/s5/steps/ ../../../egs/wsj/s5/utils .

mkdir /fastdata/ac1zy/kaldi/egs1/torgo/s9 /fastdata/ac1zy/kaldi/egs1/torgo/s9/data /fastdata/ac1zy/kaldi/egs1/torgo/s9/exp /fastdata/ac1zy/kaldi/egs1/torgo/s9/fmllr /fastdata/ac1zy/kaldi/egs1/torgo/s9/raw_torgo_200ms

ln -s /fastdata/ac1zy/kaldi/egs1/torgo/s9/data /fastdata/ac1zy/kaldi/egs1/torgo/s9/exp /fastdata/ac1zy/kaldi/egs1/torgo/s9/fmllr /fastdata/ac1zy/kaldi/egs1/torgo/s9/raw_torgo_200ms .

### 2) copy files from other folders

scp -r ../s8/conf ../s8/local ../s8/*.sh .

scp -r ../s8/data/all ../s8/data/lang* data/


### in Terminal

for x in /shared/spandh1/Shared/data/TORGO/torgo_d*/data/*/Session*/wav_*; do
do echo $x; ls $x | wc -w; done

mkdir data/1 data/2

scp -r data/all/spk2gender data/1

scp -r data/all/spk2gender data/2

vim data/2/spk2gender # delete M05

local/prepare_torgo_1_2.sh data

### 3) Prepare data

/data/ac1zy/jupyter/5-fold_CV.ipynb
## 2. Submit jobs

 for fd in fd1 fd2 fd3 fd4 fd5; do qsub -V -e qsub${fd} -o qsub${fd} -j y ./run_sd.sh --stage 5 --fd ${fd}; done
 
 for fd in fd1 fd2 fd3 fd4 fd5; do mkdir exp/${fd}/train/tri3b_cleaned/decode_tg; cp exp/${fd}/train/tri3b_cleaned/trans* exp/${fd}/train/tri3b_cleaned/decode_tg; done
 
 for fd in fd1 fd2 fd3 fd4 fd5; do qsub -V -o qsub${fd}fmllr -e qsub${fd}fmllr -j y ./fmllr.sh --fd ${fd}; done
 
 ## 3. Pytorch kaldi
 
 cd /data/ac1zy/pytorch-kaldi
 
 mkdir /fastdata/ac1zy/exp/pykaldi_ae/exp/s9
 
 ln -s /fastdata/ac1zy/exp/pykaldi_ae/exp/s9 exp
 
 python chang_spk.py cfg/s9/fd1_sp_bn20.cfg s8 s9
 
 mkdir result_tg/s9

## 3. Rescore word and sentence subsets
fds=(fd1 fd2 fd3 fd4 fd5)
spks=(F01 F03 F04 M01 M02 M03 M04 M05 FC01 FC02 FC03 MC01 MC02 MC03 MC04)
testsets=(test_sentence test_word)
feat=sp_bn20
for spk in ${spks[@]}; do
 for fd in ${fds[@]}; do 
for testset in ${testsets[@]}; do 
decode_ark=/data/ac1zy/pytorch-kaldi/exp/s9/${fd}_${feat}/decode_${fd}_${spk}_test_lm200_out_dnn2
data=data/${fd}/${spk}/${testset}
graphdir=exp/${fd}/train/tri3b_cleaned/graph_test_lm200
mkdir ${decode_ark}/${testset}
cp ${decode_ark}/lat.1.gz  ${decode_ark}/lat.2.gz ${decode_ark}/${testset}
dir=${decode_ark}/${testset}
local/score.sh --cmd "run.pl" $data $graphdir $dir; done; done; done



 
 


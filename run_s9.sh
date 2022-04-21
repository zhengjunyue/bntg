#!/bin/bash
#$ -l h_rt=40:00:00
#$ -l rmem=12G
#$ -M z.yue@sheffield.ac.uk
#$ -m bea
#$ -P rse
#$ -q rse.q
#$ -l gpu=1
# -P tapas 
# -q tapas.q
# -hold_jid 5834466 
# normal s7 bn+fmllr concatenate features



# feat="bnsp10"
feat="sp_bn20"
fd="fd1"
. ./cmd.sh
. ./path.sh
. ./parse_options.sh 

#setCUDAVisibileDevices $(getSGERequestedGPUCount)
#python -u run_exp.py cfg/s7/tg_${feat}_liGRU.cfg 
python -u run_exp.py cfg/s9/${fd}_${feat}.cfg
#python -u run_exp.py cfg/s7/alltest/tg_${feat}_liGRU.cfg
#python -u run_exp.py cfg/torgo/tg_${spk}_liGRU.cfg
#setCUDAVisibileDevices $(getSGERequestedGPUCount)
#python -u run_exp.py cfg/torgo/tg_liGRU_sp_mfcc/tg_${spk}_liGRU.cfg
#python -u run_exp.py cfg/torgo/tg_${spk}_${feat}.cfg
#python -u run_exp.py cfg/torgo/tg_liGRU/tg_${feat}_fmllr.cfg
#CUDA_VISIBLE_DEVICES=5 python -u run_exp.py cfg/torgo/tg_liGRU_${feat}.cfg


# Autoencoder bottleneck features with multi-task optimisation for improved continuous dysarthric speech recognition

Copyright 2022 Zhengjun Yue, Heidi Christensen, Jon Barker

# Description

This is a Pytorch-Kaldi recipe to build automatic speech recognition systems on the
[Torgo corpus](http://www.cs.toronto.edu/~complingweb/data/TORGO/torgo.html) of
dysarthric speech.
Autoencoder bottleneck features 
with multi-task optimisation for improved continuous dysarthric speech recognition


## Setup

Run the following:

```sh
. ./cmd.sh
. ./path.sh
. ./parse_options.sh

```
## Training setup

Due to data scarcity, we don't have a separate test set for TORGO. In each fold, we allocated 70\% of data to training, 10\% to validation (dev) and 20\% for testing.

## Usage

The following instructions allow to train ASR systems on Torgo and to reproduce
results from the paper.

### Train ASR systems

```sh
# Joint training
python -u run_exp.py cfg/fd1_sp_bn20_pretrain.cfg 

# Multi-task learning
python -u run_exp.py cfg/fd1_sp_bn20_mono.cfg 

```




## Citation 

Please cite the following [paper](https://eprints.whiterose.ac.uk/164230/8/2746.pdf) if you use this script for your research or are 
interested in this paper.

```BibTeX
@inproceedings{yue2020autoencoder,
  title={Autoencoder bottleneck features with multi-task optimisation for improved continuous dysarthric speech recognition},
  author={Yue, Zhengjun and Christensen, Heidi and Barker, Jon},
  booktitle={Proceedings of Interspeech 2020},
  pages={4581--4585},
  year={2020},
  organization={International Speech Communication Association (ISCA)}
}
```
The code is based on [an earlier recipe](https://github.com/mravanelli/pytorch-kaldi) by Mirco Ravanelli, Titouan Parcollet and Yoshua Bengio.

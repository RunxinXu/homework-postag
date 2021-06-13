#!/bin/bash

GPU=1
OUTPUT=fanti
TASK=fanti # ['jianti', 'fanti']

EPOCH=10
BSZ=16
LR=3e-5
WARMUP_RATIO=0.1
WEIGHT_DECAY=0.01

if [ $TASK == "jianti" ]
then
    echo "jianti"
    TRAIN_FILE=data/jianti.train
    DEV_FILE=data/jianti.dev
    TEST_FILE=data/jianti.dev
    META_FILE=data/jianti.meta
else
    echo "fanti"
    TRAIN_FILE=data/fanti.train
    DEV_FILE=data/fanti.dev
    TEST_FILE=data/fanti.dev
    META_FILE=data/fanti.meta
fi

CUDA_VISIBLE_DEVICES=${GPU} python run.py \
  --model_name_or_path hfl/chinese-roberta-wwm-ext-large \
  --train_file ${TRAIN_FILE} \
  --validation_file ${DEV_FILE} \
  --test_file ${TEST_FILE} \
  --meta_file ${META_FILE} \
  --output_dir ${OUTPUT} \
  --do_train \
  --do_eval \
  --do_predict \
  --label_all_tokens \
  --learning_rate ${LR} \
  --num_train_epochs ${EPOCH} \
  --weight_decay ${WEIGHT_DECAY} \
  --remove_unused_columns True \
  --save_total_limit 1 \
  --load_best_model_at_end \
  --warmup_ratio ${WARMUP_RATIO} \
  --metric_for_best_model f1 \
  --greater_is_better True \
  --evaluation_strategy epoch \
  --logging_strategy epoch

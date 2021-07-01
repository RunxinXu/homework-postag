#!/bin/bash

GPU=0
OUTPUT=jianti-final
TASK=jianti # ['jianti', 'fanti']

EPOCH=5
BSZ=16
LR=3e-5
WARMUP_RATIO=0.1
WEIGHT_DECAY=0.01

if [ $TASK == "jianti" ]
then
    echo "jianti"
    TRAIN_FILE=data/jianti.finaltrain
    DEV_FILE=data/jianti.dev
    TEST_FILE=data/jianti.test
    META_FILE=data/jianti.meta
else
    echo "fanti"
    TRAIN_FILE=data/fanti.finaltrain
    DEV_FILE=data/fanti.dev
    TEST_FILE=data/fanti.test
    META_FILE=data/fanti.meta
fi

CUDA_VISIBLE_DEVICES=${GPU} python run.py \
  --task_name ${TASK} \
  --model_name_or_path hfl/chinese-roberta-wwm-ext-large \
  --do_train \
  --train_file ${TRAIN_FILE} \
  --validation_file ${DEV_FILE} \
  --test_file ${TEST_FILE} \
  --meta_file ${META_FILE} \
  --output_dir ${OUTPUT} \
  --do_predict \
  --label_all_tokens \
  --learning_rate ${LR} \
  --num_train_epochs ${EPOCH} \
  --weight_decay ${WEIGHT_DECAY} \
  --remove_unused_columns True \
  --warmup_ratio ${WARMUP_RATIO} \
  --save_total_limit 1 \
  --fp16
#   --do_eval \
#   --load_best_model_at_end \
#   --metric_for_best_model f1 \
#   --greater_is_better True \
#   --evaluation_strategy epoch \
#   --logging_strategy epoch \

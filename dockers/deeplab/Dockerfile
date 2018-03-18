FROM ubuntu:14.04

RUN pip install tensorflow
RUN apt-get install python-pil python-numpy
RUN pip install jupyter
RUN pip install matplotlib

WORKDIR /opt
RUN git clone https://github.com/tensorflow/models.git
WORKDIR /opt/models

RUN export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
RUN sh local_test.sh

RUN allias runner = 'python deeplab/train.py \
    --logtostderr \
    --training_number_of_steps=30000 \
    --train_split="train" \
    --model_variant="xception_65" \
    --atrous_rates=6 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --train_crop_size=513 \
    --train_crop_size=513 \
    --train_batch_size=1 \
    --dataset="pascal_voc_seg" \
    --train_logdir="data/training"'

ENTRYPOINT ["runner"]
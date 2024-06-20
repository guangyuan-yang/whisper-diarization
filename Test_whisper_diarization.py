# Databricks notebook source
# Download a static FFmpeg build and add it to PATH.
exist = !which ffmpeg
if not exist:
    print('ffmpeg does not exit, downloading...')
    !curl https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz -o ffmpeg.tar.xz \
        && tar -xf ffmpeg.tar.xz && rm ffmpeg.tar.xz
    ffmdir = !find . -iname ffmpeg-*-static
    path = %env PATH
    path = path + ':' + ffmdir[0]
    %env PATH $path
print('')
!which ffmpeg
print('Done!')

# COMMAND ----------

! pip install cython torch

# COMMAND ----------

! pip install protobuf~=4.0

# COMMAND ----------

!pip install git+https://github.com/m-bain/whisperX.git@78dcfaab51005aa703ee21375f81ed31bc248560

# COMMAND ----------

! pip install requests~=2.29

# COMMAND ----------

!pip install --no-build-isolation nemo_toolkit[asr]==1.23.0

# COMMAND ----------

!pip install --no-deps git+https://github.com/facebookresearch/demucs#egg=demucs

# COMMAND ----------

!pip install git+https://github.com/oliverguhr/deepmultilingualpunctuation.git

# COMMAND ----------

!pip install git+https://github.com/MahmoudAshraf97/ctc-forced-aligner.git

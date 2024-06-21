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

# COMMAND ----------

! pip install protobuf~=3.20

# COMMAND ----------

script_path = "/dbfs/FileStore/shared_uploads/your-email@example.com/diarize.py"  # Adjust the path accordingly

with open(script_path, 'r') as file:
    script_content = file.read()

exec(script_content)

# COMMAND ----------

import os
import wget
from omegaconf import OmegaConf
import json
import shutil
import torch
import torchaudio
from nemo.collections.asr.models.msdd_models import NeuralDiarizer
from deepmultilingualpunctuation import PunctuationModel
import re
import logging
import nltk
from whisperx.utils import LANGUAGES, TO_LANGUAGE_CODE
from ctc_forced_aligner import (
    load_alignment_model,
    generate_emissions,
    preprocess_text,
    get_alignments,
    get_spans,
    postprocess_results,
)

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

# MAGIC %sh
# MAGIC pwd
# MAGIC ls

# COMMAND ----------

dbfs_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().getOrElse(None)
print(dbfs_path)

# COMMAND ----------


if dbfs_path is not None:
    try:
        dbutils.fs.ls(dbfs_path)
        print("Path is valid.")
    except Exception as e:
        print("Path is invalid:", str(e))
else:
    print("DBFS path is not available.")

# COMMAND ----------

dbfs_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()


# COMMAND ----------

try:
    dbutils.fs.ls(dbfs_path)
    print("Path is valid.")
except Exception as e:
    print("Path is invalid:", str(e))

# COMMAND ----------

# MAGIC %sh python diarize.py -a '4065.mp3'

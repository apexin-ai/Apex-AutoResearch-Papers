#!/usr/bin/env bash
set -euo pipefail

BASE=.
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export PYTHONPATH="$BASE/repositories/xlstm:${PYTHONPATH:-}"
cd "$BASE/repositories/xlstm"
python - <<'PY'
from experiments.data.formal_language.formal_language_dataset import FormLangDatasetConfig, FormLangDatasetGenerator

cfg = {
    "synth_lang_type": "parity",
    "vocab_size": 3,
    "seed": 1,
    "enable_mask": True,
    "context_length": 256,
    "min_sequence_length": 3,
    "max_sequence_length": 40,
    "count": {"train": 16, "validation": 16, "test": 16},
    "subpar": {"validation": {"min_sequence_length": 40, "max_sequence_length": 256}, "test": {"min_sequence_length": 40, "max_sequence_length": 256}},
}
ds = FormLangDatasetGenerator(FormLangDatasetConfig(**cfg))
print({"dataset": "xLSTM paper formal-language parity", "train": len(ds.train_split), "validation": len(ds.validation_split["validation"])})
PY

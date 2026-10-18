# ops locate sdgd v2 script

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_locate_sdgd_v2_script_20260515T134131_result.json`
- **Structured JSON:** [`7bc0bca10f1ebbaf3e8c.json`](../../sessions/7b/7bc0bca10f1ebbaf3e8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### GPU 状态
| GPU | 显存占用 | 总显存 | 利用率 |
|-----|---------|--------|--------|
| NVIDIA RTX PRO 6000 Blackwell Server Edition | 0 MiB | 97887 MiB | 0% |

GPU 空闲，无任务运行。

---

### `scripts/run_sdgd_v2_fewnerd.sh`

```bash
#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/schema-dag-extraction

TYPES_FILE=configs/few_nerd_types.json
SIM_MATRIX=artifacts/sim_matrix.pt
MODEL_PATH=/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/
OUTPUT_DIR=artifacts/exp008_v2
MAX_SAMPLES=1000
TASK=ner
MIN_BATCH_SIZE=8
MERGE_STRATEGY=confidence
CONFIDENCE_THRESHOLD=-1.0

mkdir -p ${OUTPUT_DIR}

# Stage 1: CPU Decomposition — 4 modes: sdgd_zero, single_pass, random_batch, per_type
for MODE in sdgd_zero single_pass random_batch per_type; do
  EXTRA_ARGS=""
  if [ "${MODE}" = "sdgd_zero" ]; then
    EXTRA_ARGS="--min_batch_size ${MIN_BATCH_SIZE}"
  fi
  python3 src/sdgd_decompose_cpu.py \
    --mode ${MODE} \
    --types_file ${TYPES_FILE} \
    --sim_matrix_path ${SIM_MATRIX} \
    --output ${OUTPUT_DIR}/decomposition_${MODE}.json \
    ${EXTRA_ARGS}
done

# Stage 2: GPU Extraction (confidence merge) — 所有 decomposition 一起送入
python3 src/sdgd_extract_gpu.py \
  --decompositions \
    ${OUTPUT_DIR}/decomposition_sdgd_zero.json \
    ${OUTPUT_DIR}/decomposition_single_pass.json \
    ${OUTPUT_DIR}/decomposition_random_batch.json \
    ${OUTPUT_DIR}/decomposition_per_type.json \
  --model_path ${MODEL_PATH} \
  --types_file ${TYPES_FILE} \
  --dataset fewnerd \
  --prompt_version v2 \
  --max_samples ${MAX_SAMPLES} \
  --output_dir ${OUTPUT_DIR} \
  --max_model_len 4096 \
  --task ${TASK} \
  --merge_strategy ${MERGE_STRATEGY} \
  --confidence_threshold ${CONFIDENCE_THRESHOLD}
```

---

### `scripts/run_sdgd_v2_maven_minilm.sh`

同结构，差异点：
- `TYPES_FILE=configs/maven_event_types.json`
- `SIM_MATRIX=artifacts/maven_minilm_sim_matrix.pt`
- `OUTPUT_DIR=artifacts/exp008_v2_maven_minilm`
- `TASK=event`
- `--dataset maven`

---

### `scripts/run_exp012_llama.sh`

```bash
#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/schema-dag-extraction

MODEL=/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/
MODEL_NAME=llama-3.3-70b-fp8
COMMON="--dataset fewnerd --prompt_version v2 --types_file configs/few_nerd_types.json \
  --embeddings_path artifacts/type_embeddings.pt --sim_matrix_path artifacts/sim_matrix.pt \
  --model_path $MODEL --model_name $MODEL_NAME --max_samples 1000 --max_model_len 4096 \
  --gpu_memory_utilization 0.90 --output_dir artifacts/exp012"

mkdir -p artifacts/exp012

# exp1: Count Baseline
python3 src/run_experiment.py --mode exp1 $COMMON

# exp2: Confusability Controlled
python3 src/run_experiment.py --mode exp2 $COMMON
```

### `scripts/submit_exp012.sh`（启动器）

```bash
#!/bin/bash
nohup bash /root/schema-dag-extraction/scripts/run_exp012_llama.sh \
  > /root/schema-dag-extraction/logs/exp012_llama.log 2>&1 &
echo "exp-012 launched, PID=$!"
```

---

**关键对比**：
- SDGD v2 用 **Qwen3-32B-FP8**，两阶段（CPU decompose → GPU extract），4 种 decomposition mode 对比
- exp-012 用 **LLaMA-3.3-70B-FP8**，统一 `run_experiment.py` 入口，跑 exp1 (count baseline) 和 exp2 (confusability controlled)

---

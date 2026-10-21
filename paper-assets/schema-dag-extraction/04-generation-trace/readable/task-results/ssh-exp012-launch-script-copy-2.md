# ssh exp012 launch script

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp012-launch-script_20260515T104630_result.json`
- **Structured JSON:** [`b86ee6d6f80f36ae9c05.json`](../../sessions/b8/b86ee6d6f80f36ae9c05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完毕。以下是结果：

---

## 产出报告

### 脚本状态：已存在且正确

两个脚本已在服务器上就绪：

**`scripts/run_exp012_llama.sh`**：
```bash
#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/schema-dag-extraction

MODEL=/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/
COMMON="--dataset fewnerd --prompt_version v2 --types_file configs/few_nerd_types.json --embeddings_path artifacts/type_embeddings.pt --sim_matrix_path artifacts/sim_matrix.pt --model_path $MODEL --max_samples 1000 --max_model_len 4096 --output_dir artifacts/exp012"

mkdir -p artifacts/exp012

echo "===== [$(date)] exp-012 exp1: Count Baseline (LLaMA-3.3-70B-FP8) ====="
python3 src/run_experiment.py --mode exp1 $COMMON

echo "===== [$(date)] exp-012 exp2: Confusability Controlled (LLaMA-3.3-70B-FP8) ====="
python3 src/run_experiment.py --mode exp2 $COMMON

echo "===== [$(date)] exp-012 DONE ====="
```

**`scripts/submit_exp012.sh`**：
```bash
#!/bin/bash
nohup bash /root/schema-dag-extraction/scripts/run_exp012_llama.sh > /root/schema-dag-extraction/logs/exp012_llama.log 2>&1 &
echo "exp-012 launched, PID=$!"
echo "Log: /root/schema-dag-extraction/logs/exp012_llama.log"
```

### 参数兼容性报告

| 参数 | 脚本值 | run_experiment.py | 状态 |
|------|--------|-------------------|------|
| `--mode` | exp1/exp2 | choices: dry_run/exp1/exp2 | ✓ |
| `--dataset` | fewnerd | choices: fewnerd/maven/fewrel | ✓ |
| `--prompt_version` | v2 | choices: v1/v2 | ✓ |
| `--model_path` | LLaMA path | required | ✓ |
| `--types_file` | configs/few_nerd_types.json | required | ✓ 存在 |
| `--embeddings_path` | artifacts/type_embeddings.pt | optional | ✓ 存在 |
| `--sim_matrix_path` | artifacts/sim_matrix.pt | optional | ✓ 存在 |
| `--max_samples` | 1000 | int, default=None | ✓ |
| `--max_model_len` | 4096 | int, default=4096 | ✓ |
| `--output_dir` | artifacts/exp012 | default=artifacts | ✓ |
| `--eval_mode` | 未指定(default="all") | choices: exact/relaxed/text_match/all | ✓ "all"包含text_match |

**注意**：`--eval_mode` 默认 "all"，会同时跑 exact + relaxed + text_match 三种评估，比单独 text_match 信息量更大。无需修改。

### vLLM fork 死锁风险评估：**无风险**

`run_experiment.py` 采用了安全的初始化模式：
1. 模块顶层无 `torch` / `vllm` 导入
2. 导入 project 模块前显式设 `CUDA_VISIBLE_DEVICES=''`，阻止意外 CUDA 初始化
3. batch config 构建完成后恢复 `CUDA_VISIBLE_DEVICES`
4. `run_extraction()` 内部才 import vLLM（第193行），并在函数内初始化 `LLM()`（第207行）

与 SDGD 的 fork 死锁场景（torch 在 multiprocessing spawn 前初始化 CUDA）完全不同。**无需修复**。

### Dry-run 结果

`python3 src/run_experiment.py --help` 成功，所有参数解析正确。

### 启动方式

exp-008 完成后执行：
```bash
bash /root/schema-dag-extraction/scripts/submit_exp012.sh
```

---

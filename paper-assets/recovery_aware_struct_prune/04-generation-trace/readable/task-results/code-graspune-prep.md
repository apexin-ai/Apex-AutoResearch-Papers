# code graspune prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_graspune-prep_20260515T014651_result.json`
- **Structured JSON:** [`f0c86f0d332fc1102a51.json`](../../sessions/f0/f0c86f0d332fc1102a51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇报如下：

---

## GRASPrune Baseline 环境状态

| 检查项 | 状态 |
|--------|------|
| GRASPrune repo (`/root/GRASPrune/`) | 已 clone，含 `__pycache__`（之前已运行过） |
| Qwen 架构支持 | `QwenMLPGate`, `QwenAttnGate` 均存在，import 通过 |
| `--model-family qwen` 参数 | train.py 支持 `{auto,llama,qwen}` |
| 模型文件 | `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/` 在位（2 个 safetensors shard） |
| Python 环境 | torch=2.10.0+cu128, transformers=5.8.0, cuda=True, 2 GPUs |
| 依赖 | accelerate/datasets/safetensors/sentencepiece/lm_eval 全部已装 |
| `run_graspune.sh` | 就绪，KEEP_RATIO=0.80, OUTPUT_DIR 指向数据盘 |
| `convert_graspune_to_hf.py` | 存在 |

**注意**: requirements.txt 指定 torch==2.7.0 / transformers==4.51.0，当前环境版本更高。脚本已有警告"不要运行 pip install -r requirements.txt"，正确。

## GRPO 完成后启动 GRASPrune 的确切命令

```bash
# 在 westb-23072 上执行
cd /root/recovery_aware_struct_prune/src && bash run_graspune.sh
```

或等价的分步命令：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# Phase 1: 剪枝（~30-60min on single GPU）
cd /root/GRASPrune && python train.py \
    --model-id /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B \
    --model-family qwen \
    --device cuda:0 \
    --dtype bfloat16 \
    --keep-ratio 0.80 \
    --epochs 4 \
    --batch-size 1 \
    --num-samples 512 \
    --max-len 512 \
    --train-dataset gsm8k \
    --train-split train \
    --skip-acc-eval \
    --trust-remote-code \
    --output-dir /root/autodl-tmp/graspune_output/DeepSeek-R1-Distill-Qwen-7B_pruned_80

# Phase 2: 转 HF 格式
cd /root/recovery_aware_struct_prune/src && python convert_graspune_to_hf.py \
    --model-id /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B \
    --state-dict /root/autodl-tmp/graspune_output/DeepSeek-R1-Distill-Qwen-7B_pruned_80/pruned_state_dict.safetensors \
    --meta /root/autodl-tmp/graspune_output/DeepSeek-R1-Distill-Qwen-7B_pruned_80/meta.json \
    --output-dir /root/autodl-tmp/pruned_graspune_20
```

环境完全就绪，等 GRPO 释放 GPU 后可直接启动。

---

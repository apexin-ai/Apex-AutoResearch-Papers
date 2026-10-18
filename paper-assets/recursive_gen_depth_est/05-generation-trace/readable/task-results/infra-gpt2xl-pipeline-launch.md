# infra gpt2xl pipeline launch

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpt2xl-pipeline-launch_20260514T141146_result.json`
- **Structured JSON:** [`d51b0cb182a463b70395.json`](../../sessions/d5/d51b0cb182a463b70395.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 正常运行，训练速度稳定 ~1.33 it/s (43/939 steps)。

---

**产出汇总：**

### 1. GPT-2 XL 模型信息
| 属性 | 值 |
|------|-----|
| 模型类型 | gpt2 |
| 参数量 | 1.56B |
| 层数 | 48 (transformer.h.0-47) |
| 隐藏维度 | 1600 |
| Vocab | 50257 |
| BOS/EOS | `<\|endoftext\|>` (50256) |
| PAD | None → 代码兜底设为 eos_token |
| Attention 模块 | `Conv1D`（非 nn.Linear） |
| LoRA target_modules | `c_attn, c_proj` |

### 2. 脚本修改清单
- **新建**: `scripts/run_pipeline_gpt2xl.sh` — GPT-2 XL 专用 pipeline
- **修改**: `scripts/lora_finetune.py` — CUDA_VISIBLE_DEVICES 仅在未预设时覆盖
- **修改**: `scripts/generate_next_depth.py` — 同上
- **新建**: `data/gpt2xl/depth_0.jsonl` — 种子数据副本 (5000条)
- **新建**: `checkpoints/gpt2xl/`, `logs/` 目录

### 3. Pipeline 启动证据
- **PID**: 123650
- **tmux session**: `cross_model_gpt2xl_001`
- **GPU**: cuda:1, 利用率 92%, 显存 34979 MiB / 97887 MiB
- **训练速度**: ~1.33 it/s, 939 steps/epoch × 3 epochs
- **预计总时长**: depth-0 训练 ~35min + 生成 + depth-1 训练 + 生成 + depth-2 训练 + 生成 ≈ 4-5h

---

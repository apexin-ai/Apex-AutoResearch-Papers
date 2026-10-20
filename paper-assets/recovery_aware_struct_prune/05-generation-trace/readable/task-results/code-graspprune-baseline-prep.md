# code graspprune baseline prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_graspprune-baseline-prep_20260515T113113_result.json`
- **Structured JSON:** [`21bea737204206d48945.json`](../../sessions/21/21bea737204206d48945.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 和 --help 全部通过。

---

## 报告

### GRASPrune 兼容性分析

| 维度 | 结论 |
|------|------|
| **Qwen2 架构支持** | 原生支持。`gates.py` 有 `QwenMLPGate` + `QwenAttnGate`，`infer_model_family()` 自动识别 Qwen |
| **MLP intermediate dimension 粒度** | 原生支持。对 FFN intermediate channels 逐个学习 gate score，与 RASP 一致 |
| **Attention 粒度** | KV group 级别（每个 KV head 为一个 pruning unit），比 RASP 的 GQA group 粒度等价 |
| **与 eval_gsm8k.py 兼容** | 需经 HF 转换。GRASPrune 输出 safetensors + meta.json 格式，`convert_to_hf` 转为含 `per_layer_*` config 的 HF 目录，`model_utils.load_pruned_model` 可直接加载 |

### 适配内容

**无需代码修改**——GRASPrune 原生满足所有需求。脚本 `run_graspprune_baseline.py` 仅做编排：
1. 调用 `run_pruning_pipeline()` 执行 gate training → budget mask → rescale → materialize → export
2. 调用 `graspprune_load()` + 提取 per-layer 维度信息 → 保存为 HF 格式

### 产出

- `/root/recovery_aware_struct_prune/scripts/run_graspprune_baseline.py` — 适配脚本，支持 `--dry-run`、`--convert-only`、`--skip-convert` 等模式
- 已有 `src/convert_graspune_to_hf.py` 和 `scripts/run_graspune.sh` 可继续使用

### 预计 GPU 时间

- Gate training: 4 epochs × 512 samples on 7B model ≈ **15-25 分钟**（RTX PRO 6000, single GPU）
- Rescale compensation: ~5 分钟
- HF 转换: CPU only, ~2 分钟
- **总计 ~25-35 分钟**

### 执行命令（实际跑时）

```bash
CUDA_VISIBLE_DEVICES=0 python scripts/run_graspprune_baseline.py
# 评估:
cd /root/recovery_aware_struct_prune/src
python eval_gsm8k.py --model_path /root/autodl-tmp/pruned_graspprune_20
```

---

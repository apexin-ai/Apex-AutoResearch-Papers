# code plan009 sft script qwen3

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan009-sft-script-qwen3_20260514T110405_result.json`
- **Structured JSON:** [`b0941e5724e5a10f0658.json`](../../sessions/b0/b0941e5724e5a10f0658.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出报告

### 脚本
- **路径**: `/root/solver-trace-ablation/scripts/train_sft.py`
- **变更**: 基于已有脚本更新 — 添加 `--gpu` 参数（C002/C005 合规），`--num_steps` 默认 500，模型/数据/输出路径设默认值，修复 TRL 1.1.0 API 兼容（`max_length` / `dtype`）

### 模型路径
- `/root/autodl-tmp/models/Qwen3-4B`（已写入脚本默认值）

### 训练数据
- `data/train_500_seed42.jsonl` — **500 条**，0 跳过

### Prompt 格式
与 GRPO 脚本完全一致：相同 SYSTEM_PROMPT + USER_TEMPLATE。SFT 目标是生成 `Premises:\n1. &lt;FOL>\n...\nConclusion: &lt;FOL>` 格式的 assistant 回答。

### Dry-run 结果
- `--help` ✅ 参数解析正常
- 数据加载 ✅ 500 条全部成功
- **GPU 训练测试未执行** — 两张 GPU 均被占用：
  - GPU 0: plan006 (prolog_exec_only, seed=42)
  - GPU 1: plan018 (additive_random, seed=43)

### 正式训练命令
```bash
cd /root/solver-trace-ablation
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export CUDA_VISIBLE_DEVICES=1
python3 scripts/train_sft.py \
  --gpu 1 \
  --num_steps 500 \
  --seed 42 \
  --output_dir /root/autodl-tmp/outputs/plan009_sft_s42 \
  --wandb_project solver-trace-ablation \
  --wandb_run plan009_sft_s42
```

需等 GPU 1 上 plan018 完成后才能启动。

---

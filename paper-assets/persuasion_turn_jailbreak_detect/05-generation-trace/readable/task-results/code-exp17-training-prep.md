# code exp17 training prep

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp17-training-prep_20260519T160540_result.json`
- **Structured JSON:** [`26147c78431069d1a8f3.json`](../../sessions/26/26147c78431069d1a8f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 3 个脚本

| 脚本 | 服务器路径 | 功能 |
|------|-----------|------|
| `prepare_expanded_data.py` | `scripts/prepare_expanded_data.py` | 合并 plan_002_splits (500) + expanded (500) → `data/expanded_1000/` (700/150/150)，自动回退 .progress 文件 |
| `run_exp17_training.sh` | `scripts/run_exp17_training.sh` | 3 variant × 3 seeds = 9 训练，checkpoint 到 `checkpoints/exp17/`，遵守 GPU C001 约束 (cuda:0-2) |
| `eval_exp17.py` | `scripts/eval_exp17.py` | 9 checkpoint × 4 benchmark (DD OOD / AA OOD / ToxicChat / IID)，输出对比表格 |

### 数据格式差异

- **plan_002_splits**: 已处理格式，`persuasion_strategy` 为 int (0=none, 1-8=策略)
- **expanded jailbreak**: 原始格式，`intended_strategy` (0-7)，脚本自动 +1 映射
- **expanded benign**: 无 persuasion_strategy 字段，脚本自动补 0
- **ID 冲突**: jailbreak/benign 均使用 `crescendo_exp_XXXX`，已加 `exp_jb_`/`exp_bn_` 前缀

### 数据预处理流程

`prepare_expanded_data.py` 复用 `src/merge_and_split.py` 的策略映射逻辑，直接合并已处理的原始 500 条 + 新处理的扩展 500 条，然后 stratified split (70/15/15)。

### OOD 测试数据

- DD OOD: `data/generated/deceptive_delight_all.jsonl` (80 jailbreak) + test benign
- AA OOD: `data/actorattack_ood/actorattack_all.jsonl` (80 jailbreak) + test benign
- ToxicChat: `data/mhj/toxicchat_plan002_eval.jsonl` (242 条混合)

### 预估训练时间

基于 plan_002 经验（500 条，~10min/DeBERTa stage + ~5min/GRU stage），1000 条约 2x：
- Vanilla: 3 seeds × ~10min = ~30min
- MLM: 3 seeds × (20 + 10)min = ~90min
- 9-class: 3 seeds × (20 + 10)min = ~90min
- **总计约 3.5h**（串行执行），可改为并行跑 variant 缩短到 ~1.5h

---

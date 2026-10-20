# ops fix gpu5 resubmit d025 05B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_gpu5_resubmit_d025_05B_20260514T045256_result.json`
- **Structured JSON:** [`f31ad25cceffaf6f4d54.json`](../../sessions/f3/f31ad25cceffaf6f4d54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Step 6: 根因分析报告

### 1. --gpu 参数的具体代码逻辑
`train_sft.py` 第 93 行定义 `--gpu` 为 str 类型参数，第 113-114 行执行：
```python
if args.gpu:
    os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu
```
**无论外部是否设置了 `CUDA_VISIBLE_DEVICES`，脚本内部都会用 `--gpu` 的值覆盖它。**

### 2. 失败原因链
- 原始提交：`CUDA_VISIBLE_DEVICES=5` + `--gpu 0` → 脚本把 CUDA_VISIBLE_DEVICES 改成 `"0"` → 进程跑到物理 GPU 0 → 与 d100 SFT 实验冲突 OOM

### 3. 修复方式
- `--gpu X` 中 X 必须是**物理卡号**（与期望的 GPU 一致）
- 外部 `CUDA_VISIBLE_DEVICES` 设置是多余的（但保持一致无害）

### 4. 额外发现
- d025 数据（54133 样本，含 25% benchmark 原文）比 d005 数据序列更长，batch-size 4 在 24GB GPU 上 OOM
- 解决：`--batch-size 2 --grad-accum 8`（有效 batch size 不变）
- cqa1-21977 上 bitsandbytes 需要额外设置 `LD_LIBRARY_PATH`

### 当前状态
`exp_001_sft_d025_05B_v2` 已在 GPU 5 上正常训练，3384 steps，预计 ~5h 完成。

---

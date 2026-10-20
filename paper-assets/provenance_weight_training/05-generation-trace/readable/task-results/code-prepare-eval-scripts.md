# code prepare eval scripts

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_eval_scripts_20260514T122932_result.json`
- **Structured JSON:** [`92773299e4ffa3749a3a.json`](../../sessions/92/92773299e4ffa3749a3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法检查通过。

---

## 调查结果

### 1. Eval 机制

**训练脚本不内置 eval。** Eval 由独立的 `auto_eval_watcher.py`（后台守护进程，PID 74150）自动完成：
- 每 60 秒扫描 `output/models/grid_b*/final/model.safetensors`
- 发现新 checkpoint 且 `output/eval_results/{exp_id}_eval.json` 不存在时，调用 `eval_perplexity.py` 在 GPU 3 上跑 eval
- 使用 holdout 数据 `data/human/eval_holdout.jsonl`（~5000 docs, 4M tokens）

**Seed42 batch 没有 eval 结果的原因：** 不是脚本跳过了 eval，而是 watcher 启动晚了。从日志看 watcher 15:37 启动时，seed42 的 b0.5 和 b1.0 已经训练完了，所以 watcher 立即跑了它们的 eval。之后 b1.5 训完后也被 watcher 自动捕获并 eval 了。b2.0/3.0/5.0 还在训练中，没有 `final/` 目录。

### 2. 单个 eval 耗时

**约 2.5-3 分钟**（从日志的时间戳计算）。6 个 b 值串行跑约 15-18 分钟。

### 3. Seed42 eval 脚本

路径：`/root/provenance_weight_training/scripts/run_eval_seed42.sh`

用法：`bash scripts/run_eval_seed42.sh [gpu_id]`（默认 GPU 0）

功能：自动跳过已有 eval 结果或 checkpoint 未就绪的项。实际上这个脚本是**备用方案**——`auto_eval_watcher.py` 已经在自动处理。

### 4. Seed123 的 b2.0/3.0/5.0 完成后会自动跑 eval 吗？

**会。** `auto_eval_watcher.py` 正在运行，且它匹配所有 `grid_b*` 目录（不区分 seed），所以 seed123 的 b2.0/3.0/5.0 训练完成后也会被自动 eval。

当前 eval 进度汇总：

| Checkpoint | Eval 状态 | PPL |
|---|---|---|
| grid_b0_5_seed42 | 完成 | 17.65 |
| grid_b1_0_seed42 | 完成 | 17.69 |
| grid_b1_5_seed42 | 完成 | 17.72 |
| grid_b2_0_seed42 | 等待训练完成 | - |
| grid_b3_0_seed42 | 等待训练完成 | - |
| grid_b5_0_seed42 | 等待训练完成 | - |
| grid_b0_5_seed123 | 完成 | 17.64 |
| grid_b1_0_seed123 | 完成 | 17.67 |
| grid_b1_5_seed123 | 完成 | 17.70 |
| grid_b2_0_seed123 | 等待训练完成 | - |
| grid_b3_0_seed123 | 等待训练完成 | - |
| grid_b5_0_seed123 | 等待训练完成 | - |

---

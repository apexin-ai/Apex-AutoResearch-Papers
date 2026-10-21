# code plan 008 pruning sweep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_008_pruning_sweep_20260516T144418_result.json`
- **Structured JSON:** [`92a43e40544cc61b4a27.json`](../../sessions/92/92a43e40544cc61b4a27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job 正在加载模型（正从 HF 缓存拉 SmolVLM2 配置文件）。一切正常运行中。

**已完成：**
1. `eval_pruning_sweep.py` 已写入服务器 `/root/autodl-tmp/importance_margin_vla_compress/`
2. 训练 job `plan_008_pruning_sweep` 已提交到 cuda:1，正在加载模型
3. Registry 已更新（RUNNING 状态，含 hypothesis）

脚本对 7 个 k_ratio (0.3~0.9) 各跑 500 batch evaluation，输出 G3 曲线表格 + sweet spot + deployable range，结果存入 `eval_results/pruning_sweep.json`。

---

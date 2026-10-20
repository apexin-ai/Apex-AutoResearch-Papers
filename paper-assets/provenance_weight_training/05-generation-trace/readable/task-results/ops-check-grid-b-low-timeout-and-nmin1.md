# ops check grid b low timeout and nmin1

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_grid_b_low_timeout_and_nmin1_20260515T085116_result.json`
- **Structured JSON:** [`e5688dd1c2a4d36dcb49.json`](../../sessions/e5/e5688dd1c2a4d36dcb49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## grid_b_low_seed42 诊断

- **含 inline eval**: 是
- **含 --eval_data_path**: `data/human/eval_holdout.jsonl`
- **含 --eval_steps**: `500`
- **tmux/session 状态**: alive（PID 163648/163654/163662 均在运行，pts/0）
- **timeout 设定**: **无**。进程链中无 timeout 包装器，/tmp 下也无 aml_training 配置文件。不会被 timeout kill。
- **当前进度**: **b=0.1（第1个/共3个）**, step 3508/6103 (57%), 已运行 ~7.5h。刚完成 step 3500 处的 eval。
- **eval 开销**: 每次 eval_runtime = **2648.8s ≈ 44 分钟**。每个 b 值有 12 次 eval（步 500/1000/.../6000），总 eval 时间 ~8.8h/b
- **预计 b=0.1 总耗时**: ~13h（7.5h / 57%）
- **预计 3 个 b 值总耗时**: **~39h**
- **风险评估**: 无 timeout kill 风险。但 inline eval 导致每个 b 值增加 ~8.8h 开销，3 个 b 值串行总耗时 ~39h 远超必要。纯训练只需 ~32 min/b。

## nmin1_seed42 脚本

- **存在**: 是
- **含 inline eval**: **是** ← 违反要求
- **--eval_data_path**: `data/human/eval_holdout.jsonl`
- **--eval_steps**: `500`
- **其他关键参数**: `--weighting_method adaptive`, `--tau 0.8`, `--n_min 1`, `--contamination_ratio 0.4`, `--bf16`, `--seed 42`, `--num_train_tokens 200000000`
- **问题**: 脚本包含 inline eval 参数，与 post-hoc eval 要求不符。需移除 `--eval_data_path` 和 `--eval_steps` 后再提交。

---

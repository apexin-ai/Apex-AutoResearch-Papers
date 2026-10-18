# harvest cqa1 full audit 20260527

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_cqa1-full-audit-20260527_20260526T230842_result.json`
- **Structured JSON:** [`ebcfb97b2dabdeb6c409.json`](../../sessions/eb/ebcfb97b2dabdeb6c409.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 收割报告

### 已完成实验

| exp_id | prune_mode | keep_ratio | SR | episodes | 日志 | JSON |
|--------|-----------|------------|-----|----------|------|------|
| eval_pi05_l2norm_k07_long_seed42 | l2norm | 0.70 | **63.2%** | 316/500 | `logs/eval_pi05_l2norm_k07_long_seed42.log` | `eval_results/pi05_l2norm_k0.70_libero_10_seed42.json` |
| eval_pi05_attention_k07_long_seed42 | attention | 0.70 | **50.8%** | 254/500 | `logs/eval_pi05_attention_k07_long_seed42.log` | `eval_results/pi05_attention_k0.70_libero_10_seed42.json` |

PID 617566 已死亡，对应的 l2norm k=0.7 实验已正常完成。

### 活跃实验

| PID | GPU | exp_id | 命令 | 进度 | 预估剩余 |
|-----|-----|--------|------|------|----------|
| 790017 | GPU 2 (10519MiB, 48%) | eval_pi05_l2norm_k085_long_seed42 | `python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0` | T1 ep40/50 (~90/500 eps), 33min elapsed | ~2.5h |
| 732826 | GPU 3 (10225MiB, 24%) | eval_pi05_random_k07_long_seed42 | `python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0` | T5 ep20/50 (~220/500 eps), 2h elapsed | ~1.7h |

### GPU 状态

- **GPU 0: 空闲** (1 MiB, 0% util)
- **GPU 1: 空闲** (1 MiB, 0% util)
- GPU 2: PID 790017 占用
- GPU 3: PID 732826 占用

### 异常标记

attention k=0.70 的 JSON 中 `n_keep_per_image: 256`（未剪枝值），而 l2norm k=0.70 正确显示 `n_keep_per_image: 179`。这可能是 attention 模式的 config 日志 bug（实际剪枝可能正常执行，因为 SR 50.8% 明显低于 baseline），但值得核查。

---

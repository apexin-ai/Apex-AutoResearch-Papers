# ssh diagnose crash v3

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose-crash-v3_20260515T222049_result.json`
- **Structured JSON:** [`d4a17ff102a732fd2cdb.json`](../../sessions/d4/d4a17ff102a732fd2cdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：训练正在正常运行，无需修复

### 当前状态

**进程活跃**：两个 python 进程 (PID 200889/200890) 分别占用 GPU 0 和 GPU 1，各 ~8.5GB 显存。

**当前阶段**：Gen 1 信号计算（per-example signals）
- seed137: **79%** (248/313)，~12s/it → 预计剩余 ~13 分钟
- seed42: **72%** (225/313)，~13s/it → 预计剩余 ~19 分钟

### 已完成的流水线步骤

| 步骤 | 状态 | 产出 |
|------|------|------|
| Gen 0 信号计算 | ✅ | `signals_gen0_seed42.json`, `signals_gen0_seed137.json` (各 205K) |
| Gen 0 可视化 | ✅ | `fig_corpus_trends.pdf`, `fig_rho_decay.pdf`, `fig_signal_distributions.pdf` |
| 真实数据分割 | ✅ | `real_train_gen{1,2,3}.jsonl` (各 ~579M), `val_set.jsonl` (44M), `probe_set.jsonl` (5.8M) |
| Gen 1 合成数据 | ✅ | `synthetic_gen1_seed{42,137}.jsonl` (各 320M) |
| Gen 1 混合数据 | ✅ | `mixed_gen1_seed{42,137}.jsonl` (各 899M) |
| Gen 1 训练 | ✅ | `checkpoints/gen1_seed{42,137}/model.safetensors` (各 774M, 05:27 保存) |
| Gen 1 信号计算 | 🔄 | 进行中 (72-79%) |

### 待完成

Gen 1 信号完成后，pipeline 将自动进入 Gen 2（合成 → 混合 → 训练 → 信号）和 Gen 3。

**结论：之前的崩溃已被修复，当前运行正常，无需干预。**

---

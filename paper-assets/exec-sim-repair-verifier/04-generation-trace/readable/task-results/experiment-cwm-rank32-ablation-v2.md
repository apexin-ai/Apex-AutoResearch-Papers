# experiment cwm rank32 ablation v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_cwm-rank32-ablation-v2_20260515T124831_result.json`
- **Structured JSON:** [`f5568bb433fff818d7d5.json`](../../sessions/f5/f5568bb433fff818d7d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**CWM rank=32 消融训练已在运行中，无需重新提交。**

| 项目 | 值 |
|------|----|
| PID | 368823 |
| GPU | cuda:0 (westd) |
| 进度 | 334/1434 (23%)，~3.3s/step |
| 参数 | rank=32, alpha=32, lr=2e-4, bs=2, ga=16, epochs=3, seed=42 |
| 数据 | 函数级 cwm_train.jsonl (15290 条) |
| checkpoint | `checkpoints_cwm_rank32/`（save_strategy=epoch，epoch 1 尚未结束） |
| 日志 | `/root/runs/exec-sim-repair-verifier/cwm-rank32-ablation.log` |
| ETA | ~60 分钟后完成 |
| Registry | `cwm-rank32-ablation-v2` → RUNNING |

**注意**：lora_alpha 保持默认 32（与 baseline 相同绝对值），未调为 64。如果审稿人需要保持 alpha/rank 比不变（baseline 是 2:1），可能需要额外跑一个 alpha=64 的版本。当前这个 alpha=32 的版本也是合理的消融选择（固定 alpha，只变 rank）。

---

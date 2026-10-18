# ops westd38929 restart all 4 experiments

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-restart-all-4-experiments_20260520T215809_result.json`
- **Structured JSON:** [`b47415b2477147fb0428.json`](../../sessions/b4/b47415b2477147fb0428.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部成功启动，所有 GPU 已加载模型并在运行：

| GPU | tmux session | 实验 | PID | 显存 |
|-----|-------------|------|-----|------|
| 0 | eval_random_k095_s42 | random k=0.95 seed42 | **95088** | 15961MiB |
| 1 | eval_random_k07_s42 | random k=0.7 seed42 | **95361** | 15961MiB |
| 2 | eval_random_k03_s43 | random k=0.3 seed43 | **95670** | 16089MiB |
| 3 | eval_l2norm_k09_s43 | L2 norm k=0.9 seed43 | **95853** | 15961MiB |

4 GPU 利用率 66%-87%，全部正常运行。M040 规则已知悉：后续 kill 只用精确 PID。

---

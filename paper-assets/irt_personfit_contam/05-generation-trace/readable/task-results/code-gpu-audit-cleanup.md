# code gpu audit cleanup

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpu-audit-cleanup_20260521T074703_result.json`
- **Structured JSON:** [`ebc5010fe07e5a080cd2.json`](../../sessions/eb/ebc5010fe07e5a080cd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计报告

### GPU 占用
| GPU | PID | 进程 | VRAM | 状态 |
|-----|------|------|------|------|
| 0 | 98622 | eval_lz s5 | 8,628 MiB | **ZOMBIE** — 结果已存在 |
| 0 | 99214 | train s7 | 37,694 MiB | 运行中 56/939 (~6%) |
| 1 | 96745 | train s6 | 23,102 MiB | **ZOMBIE** — 训练已完成 |
| 2 | 97791 | GRPO | 8,062 MiB | 运行中 134/14042 (~1%), ETA ~19h |
| 3 | 99807 | train s8 | 27,470 MiB | 运行中 |

### Eval 结果
| Condition | Accuracy | lz* |
|-----------|----------|-----|
| clean_s3 | 0.6783 | 9.529 |
| clean_s4 | 0.6786 | 8.967 |
| clean_s5 | 0.6787 | 8.532 |
| clean_s6 | — | 训练刚完成, eval 未启动 |

### HT post-RL SFT
acc=0.7339, lz\*=2.914, acc\_seen=0.831, acc\_unseen=0.717, lz\*\_seen=-0.395, lz\*\_unseen=3.278

### GRPO 状态
Step 134/14042, epoch 0.008, reward 0.3~0.78, ~5.1s/step

### 建议操作
1. **Kill PID 98622** — s5 eval zombie，浪费 GPU 0 上 8.6GB
2. **Kill PID 96745** — s6 训练已完成，浪费 GPU 1 上 23.1GB
3. Kill 后 GPU 1 空出 → 启动 clean_s6 eval
4. s7/s8/GRPO 正常，不动

报告已写入 memory.md `## GPU 审计` 段。

---

# ops 17855 disk cleanup then deploy s44

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_17855-disk-cleanup-then-deploy-s44_20260523T090248_result.json`
- **Structured JSON:** [`b5e8bded269c562d4bad.json`](../../sessions/b5/b5e8bded269c562d4bad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已启动并在训练。

---

### 结果汇总

**Phase 1 - 磁盘清理**：

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 345G (99%) | 287G (82%) |
| 可用 | 5.8G | 64G |
| 释放 | — | **~58G** |

清理了 8 个实验（t10_a050_s42 仅 4K 跳过）的 checkpoint 目录，保留了 all_metrics.json、analysis/、synthetic_data/。

**Phase 2 - s44 部署**：

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| t10_a050_s44_fp32 | cuda:2 | 781724 (wrapper) | gen_0 训练中 |
| t10_a060_s44_fp32 | cuda:3 | 780912 | 已在运行 (6min, 其他 session 部署) |

**nvidia-smi 全卡状态** — 6/6 GPU 活跃：

| GPU | 显存 | 利用率 | 实验 |
|-----|------|--------|------|
| 0 | 31G/98G | 87% | t15_a060_s43 |
| 1 | 28G/98G | 88% | t15_a050_s43 |
| 2 | 10G/98G | 89% | **t10_a050_s44** (新部署) |
| 3 | 11G/98G | 88% | **t10_a060_s44** (已在跑) |
| 4 | 31G/98G | 90% | t10_a045_s43 |
| 5 | 28G/98G | 89% | t15_a045_s43 |

---

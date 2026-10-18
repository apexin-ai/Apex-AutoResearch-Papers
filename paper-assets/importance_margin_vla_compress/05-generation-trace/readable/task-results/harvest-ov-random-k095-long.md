# harvest ov random k095 long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_ov_random_k095_long_20260527T084933_result.json`
- **Structured JSON:** [`f123c50c4507743ba49b.json`](../../sessions/f1/f123c50c4507743ba49b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

## OV Random k=0.95 Long — westd-41074 (主实验)

**Timed out (EXIT_CODE=124)**，只完成 8/10 tasks。

| Task | Description | SR |
|------|------------|-----|
| 1 | soup + tomato → basket | 54.0% (27/50) |
| 2 | cream + butter → basket | 60.0% (30/50) |
| 3 | stove + moka pot | 54.0% (27/50) |
| 4 | bowl → drawer | 40.0% (20/50) |
| 5 | mugs → plates | 20.0% (10/50) |
| 6 | book → caddy | 74.0% (37/50) |
| 7 | mug + pudding | 32.0% (16/50) |
| 8 | soup + cream → basket | 62.0% (31/50) |
| 9 | moka pots → stove | **TIMEOUT** |
| 10 | — | **NOT REACHED** |

**Partial SR (8/10 tasks): 49.5%** (198/400)

## Backup — westd-38929

- PID 112587 仍在运行，当前进度：Task 3 Ep 40/50
- 已完成 Task 1: 72.0%, Task 2: 70.0%
- 预计还需 ~6h 完成全部 10 tasks
- 注意：backup 的 Task 1-2 SR 明显高于主实验（72% vs 54%, 70% vs 60%），随机种子相同但随机剪枝每步不同，方差较大

## 新实验状态 — westd-41074

- **PI0.5 Attn k=0.95 Long strict v3** (PID 335081, GPU0): 已启动，模型加载完毕，开始评估
- **OV Attn k=0.75 Long v2** (PID 335312, GPU1): 已启动，Task 1 进行中 (256→192 tokens)

完整的 OV Random k=0.95 Long 结果需等 westd-38929 backup 完成。

---

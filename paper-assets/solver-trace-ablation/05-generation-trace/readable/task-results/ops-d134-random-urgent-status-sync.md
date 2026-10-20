# ops d134 random urgent status sync

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d134-random-urgent-status-sync_20260518T221425_result.json`
- **Structured JSON:** [`e263abee7d461008af34.json`](../../sessions/e2/e263abee7d461008af34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结构化摘要：

| seed | train | eval | classify | registry | PR | H7 | H1 | H8 | genuine |
|------|-------|------|----------|----------|----|----|-----|-----|---------|
| s47 | DONE 500/500 | DONE | DONE | DONE ✓ | 89% | 0 | 79 (88.8%) | 4 (4.5%) | 6 (6.7%) |
| s48 | DONE 500/500 | DONE | DONE | DONE ✓ | 93% | 3 (3.2%) | 75 (80.6%) | 14 (15.1%) | 4 (4.3%) |
| s49 | DONE 500/500 | DONE | DONE | ALLOCATED→**DONE** ✓ | **5%** | 1 (20%) | 4 (80%) | 0 | 0 |
| s50 | **RUNNING** 84/500 | — | — | PREPARING→**RUNNING** | — | — | — | — | — |
| s51 | NOT STARTED | — | — | PREPARING | — | — | — | — | — |

**GPU**: s50 训练中, PID 184872, step 84/500, cuda:0, 85GB/98GB VRAM, 92% util
**磁盘**: 56G/250G (23%), 充足
**Cron**: s50 已注册 (interval=120s)

**关键发现**: s49 严重退化，训练 PR 降到 40%，eval 仅 5%。这是 Random reward 下的训练崩溃，与 s47 (89%) / s48 (93%) 形成极大 seed 方差。s50 pipeline 正在跑，s51 需等 s50 完成后自动启动（pipeline 串行）。预计 s50 完成约需 ~1h（按当前 ~10s/step），加上 eval+classify 约 1.5h。s51 还需再等 ~3h。

---

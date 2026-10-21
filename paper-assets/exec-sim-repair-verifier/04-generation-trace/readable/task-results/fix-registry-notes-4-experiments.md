# fix registry notes 4 experiments

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_registry-notes-4-experiments_20260514T162907_result.json`
- **Structured JSON:** [`404c0d7df8375851a1a3.json`](../../sessions/40/404c0d7df8375851a1a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 registry notes 已更新完毕。

| 实验 | GPU | 状态 | 进度 | ETA (UTC) |
|------|-----|------|------|-----------|
| cwm-seed123-conda | cuda:0 | eval | 8704/9784 (89%), acc=59.1% | ~02:30 May 15 |
| cwm-v12 | cuda:1 | eval | 8808/9784 (90%), acc=57.8% | ~02:15 May 15 |
| cwm-8b-conda | cuda:2 | train+eval | step 1500/6633 (22.6%), eval_loss=0.3689 | May 15 22:00-May 16 04:00 |
| cls-8b-s123-conda | cuda:3 | train | step 2917/6633 (44%), loss=0.5215, eval_loss@2800=0.3238 | ~May 15 13:00 |

两个 eval 约 2 小时内完成。CLS 8B s123 还需 ~12h，CWM 8B 最慢需 ~20-28h。

---

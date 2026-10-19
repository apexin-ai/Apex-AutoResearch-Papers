# diagnose m2 starcoder progress

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_m2_starcoder_progress_20260514T150040_result.json`
- **Structured JSON:** [`8625142de17628aa91aa.json`](../../sessions/86/8625142de17628aa91aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## m2_full_starcoder 状态汇总

**进程正常**，PID 74122 存活，GPU 占用 55.4GB。

**当前进度**: 9 runs 中的第 1 个 `random_s42`，step 3700/4242 (87%)，Epoch 3 进行中。全局进度 13.8%。

**Best metrics (random_s42)**:
- Best val_loss: **0.6134** @step1000
- Best R@1: **0.4604** @step2500

**过拟合信号明显** — val_loss 从 step1000 后持续上升，R@1 在 step2500 后回落。Epoch 3 没有带来任何提升，验证了 s43/s44 只跑 2 epochs 的设计决策。

**时间估算**: 每步 ~20s，random_s42 还剩 ~3h，全部 9 runs 预计 ~5月20日 完成。

报告已写入 `artifacts/m2_starcoder_status_check.md`。

---

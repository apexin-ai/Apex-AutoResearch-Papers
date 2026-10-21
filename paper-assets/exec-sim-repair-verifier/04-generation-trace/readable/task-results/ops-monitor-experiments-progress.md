# ops monitor experiments progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_monitor-experiments-progress_20260515T220311_result.json`
- **Structured JSON:** [`01e11e71a7defbc5043b.json`](../../sessions/01/01e11e71a7defbc5043b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| exp_id | GPU | 进度 | ETA (UTC) | GPU利用率 | 关键指标 |
|--------|-----|------|-----------|-----------|----------|
| **repo-level-cwm-8b-conda-v5** | cuda:2 (90%) | 5842/6633 (88.1%) | ~08:45 (~2h41m) | 21.1/32.6 GB | loss 未显示, 最新 ckpt: **5800** |
| **cwm8b-ckpt400-test-eval** | cuda:3 (87%) | 4168/9784 (42.6%) | ~16:50 (~10.8h) | 22.5/32.6 GB | running_acc=**64.7%**, unparseable=0 |
| **cls8b-s42-resume-val-sweep-seq8192-v2** | cuda:0 (99%) | ckpt 10/10, 8940/9335 (95.8%) | **即将完成 (~1min)** | 18.5/32.6 GB | 当前 ckpt-3600 acc=**90.4%** |
| **cls8b-s42-resume-val-sweep-gpu1** | cuda:1 (77%) | ckpt 8/10, 5530/9335 (59.3%) | ~07:05 (~1h) | 18.5/32.6 GB | 当前 ckpt-5400 acc=**88.7%** |

### 详情

**CWM 8B 训练 (关键路径)**: 从上次 5818 推进到 5842，速度 ~12.2s/step。checkpoint-5800 已保存 (05:54 UTC)。剩 791 steps，预计 ~2h41m 完成全部 6633 steps。

**CWM 8B eval**: 进度较慢，~6.9s/sample。从 3776→4168，running_acc 稳定在 64.3%–64.7%。还需 ~10.8h，今天下午才能跑完。

**Val sweep GPU0**: 正在跑最后一个 checkpoint (3600)，还剩不到 1 分钟。跑完即整个 10-ckpt sweep 结束。已完成 ckpts: 1800→3400 (9个)。

**Val sweep GPU1**: 已完成 7 个 ckpt (4000→5200)，正在跑第 8 个 (5400, 59.3%)。剩余 5400(尾部) + 5600 + 5800 = ~1h。每个 ckpt 约 26 min。

---

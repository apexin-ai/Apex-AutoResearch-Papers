# ops bjb1 training status check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1-training-status-check_20260513T082748_result.json`
- **Structured JSON:** [`ca1c89173141029dde84.json`](../../sessions/ca/ca1c89173141029dde84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态汇总：

**GPU**: 双卡均 100% 利用率，各占 ~23GB 显存。

**m2_embed_verify (cuda:1)** — ⚠️ 需关注
- PID 29302 存活，random strategy epoch 2 step 1300，接近完成
- best eval@500: val_loss=0.4834, R@1=0.5357, R@5=0.9808
- **wrapper 已死（EXIT_CODE=129）**，random 完成后 embedding/dataflow 不会自动启动，需手动处理

**plan_013_starcoder (cuda:0)** — ✅ 正常
- wrapper + python 进程均存活，embedding strategy epoch 2 step 1000
- best eval@500: val_loss=0.5140, R@1=0.4800, R@5=0.9826
- eval@1000 即将产出，embedding 完成后自动尝试 dataflow

**flash-attn** — ✅ 已安装 2.8.3，编译进程已结束

**待处理**: m2_embed_verify 的 random 快跑完了，需要准备手动启动后续的 embedding 和 dataflow 策略。报告已写入 `artifacts/bjb1_status_check.md`。

---

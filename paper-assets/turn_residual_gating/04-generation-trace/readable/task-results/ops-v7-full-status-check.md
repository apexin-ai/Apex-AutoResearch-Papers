# ops v7 full status check

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v7_full_status_check_20260519T000247_result.json`
- **Structured JSON:** [`23bfb47578284632bb34.json`](../../sessions/23/23bfb47578284632bb34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集，汇报如下：

---

## 状态汇报

```
v7 训练: 运行中 — Epoch 2, Step 5500/~8000 (约 69%)
  整体进度: ~90% (21500/24000 micro-steps)
  每 epoch ~2 小时, 预计还剩 ~40-50 分钟完成
  当前指标: L_NTP≈0.91, L_GAR≈0.001, Gate_mean≈0.95
  Gate profile (step 2600): L3/L4 最低(~0.80), L27 最高(0.99)

Pipeline 脚本: 运行中, 正在等待 v7 完成
  脚本内容已确认: 完成后将自动执行 eval-ours → eval-dongre → 启动 UG
  无需手动干预

Eval GAR-ours: 未执行 (等待 v7 完成后 pipeline 自动触发)
Eval GAR-Dongre: 未执行 (同上)

UG baseline: 未启动 (pipeline 将在 eval 后自动启动)
  无 log, 无 tmux session

GPU 状态: GPU 0 — 86% utilization, 86625/97887 MiB (88%)
```

---

**结论**: 一切正常。Pipeline 脚本 (`run_post_v7.sh`) 已在后台运行，会自动完成以下链条：

1. 检测 "Training complete" → 运行 eval GAR-ours (含 gate profile) → 运行 eval GAR-dongre → 启动 UG baseline

v7 预计约 40-50 分钟后完成。无需手动干预，pipeline 会自动接管后续所有步骤。

---

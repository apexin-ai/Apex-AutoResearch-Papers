# monitor crm v2 status and reconvla metrics

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_crm-v2-status-and-reconvla-metrics_20260514T111007_result.json`
- **Structured JSON:** [`ebdd3242d54c9e806868.json`](../../sessions/eb/ebdd3242d54c9e806868.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

---

## 1. eval-reconvla-spatial-v3 完整结果

**Overall: 34.0% (34/100)** ✓

| Task | Success Rate |
|------|-------------|
| next_to_ramekin | **100%** (10/10) |
| next_to_cookie_box | **90%** (9/10) |
| between_plate_and_ramekin | 60% (6/10) |
| next_to_plate | 40% (4/10) |
| on_cookie_box | 30% (3/10) |
| in_top_drawer | 10% (1/10) |
| on_ramekin | 10% (1/10) |
| from_table_center | 0% (0/10) |
| on_stove | 0% (0/10) |
| on_wooden_cabinet | 0% (0/10) |

Registry 已更新 metrics + checkpoint_path + log_path。

---

## 2. CRM v2 训练状态 — 全部仍在训练中

| Variant | Epoch | Best val_loss | Best at epoch |
|---------|-------|---------------|---------------|
| **perdof** | 34/50 | 0.052710 | 34 |
| **scalar-unc** | 35/50 | 0.048346 | 33 |
| **obs-only** | 30/50 | 0.052974 | 30 |

Checkpoints 持续写入中（最新 ~19:08-19:09），每个 epoch 约 3 分钟，预计：
- perdof: ~48 min 剩余
- scalar-unc: ~45 min 剩余
- obs-only: ~60 min 剩余

---

## 3. re-eval 启动

**Blocked on training.** perdof 还在 34/50，cuda:0 仍被占用。等训练完成后再启动 eval-acr-spatial-v3。

---

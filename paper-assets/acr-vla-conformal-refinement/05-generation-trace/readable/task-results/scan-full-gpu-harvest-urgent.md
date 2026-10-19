# scan full gpu harvest urgent

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_scan_full-gpu-harvest-urgent_20260524T180847_result.json`
- **Structured JSON:** [`e1e3a9cc1869ab1238a8.json`](../../sessions/e1/e1e3a9cc1869ab1238a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完成。以下是完整报告：

---

## 全服务器 GPU 扫描 & 实验收割报告

### bjb1-32546 (6x RTX 4090)

| 状态 | exp_id | GPU | SR | 备注 |
|------|--------|-----|-----|------|
| **运行中** | eval-supp-adapt-tau025-obj-s50 | cuda:1 | - | Object Adaptive s50 |
| **已完成** | eval-tau-sweep-spatial-tau010-s42 | cuda:0 | **0.790** | τ=0.10, trigger=75.2% |
| **已完成** | eval-tau-sweep-spatial-tau020-s42 | cuda:2 | **0.810** | τ=0.20, trigger=26.6% |
| **已完成** | eval-tau-sweep-spatial-tau030-s42 | cuda:3 | **0.805** | τ=0.30, trigger=16.7% |
| **已完成** | eval-crm-obj-s47-reeval | cuda:4 | **0.825** | CRM obs_only re-eval, confirms high variance seed |
| **已完成** | eval-adaptive-k1-spatial-tau025-s42 | cuda:5 | **0.795** | K=1, trigger=19.6% |

**空闲 GPU: 0, 2, 3, 4, 5 (5个)**

---

### bjb2-28827 (6x RTX 4090)

| 状态 | exp_id | GPU | SR | 备注 |
|------|--------|-----|-----|------|
| **运行中** | eval-supp-adapt-tau025-obj-s48 | cuda:4 | - | Object Adaptive s48 |
| **运行中** | eval-supp-adapt-tau025-obj-s49 | cuda:5 | - | Object Adaptive s49 |
| **已完成** | eval-supp-adapt-tau025-spatial-s48 | cuda:0 | **0.810** | trigger=19.8% |
| **已完成** | eval-supp-adapt-tau025-spatial-s49 | cuda:1 | **0.820** | trigger=19.5% |
| **已完成** | eval-supp-adapt-tau025-goal-s48 | cuda:2 | **0.845** | trigger=8.9% |
| **已完成** | eval-supp-adapt-tau025-goal-s49 | cuda:3 | **0.815** | trigger=8.9% |

**空闲 GPU: 0, 1, 2, 3 (4个)**

---

### cqa1-32758 (6x RTX 4090 D) — 全忙

| 状态 | exp_id | GPU |
|------|--------|-----|
| 运行中 | eval-supp-vla-only-spatial-s48 | cuda:0 |
| 运行中 | eval-supp-vla-only-spatial-s49 | cuda:1 |
| 运行中 | eval-supp-vla-only-goal-s48 | cuda:2 |
| 运行中 | eval-supp-vla-only-goal-s49 | cuda:3 |
| 运行中 | eval-supp-vla-only-obj-s48 | cuda:4 |
| 运行中 | eval-supp-vla-only-obj-s49 | cuda:5 |

**空闲 GPU: 0**

---

### bjb1-18228 (4x RTX 4090) — 全忙

| 状态 | exp_id | GPU | 备注 |
|------|--------|-----|------|
| 运行中 | train-crm-pi05-unified-3suite-r2 | cuda:0 | **epoch 20/50**, 9.8GB VRAM |
| 运行中 | eval-supp-spatial-vla-only-s42 | cuda:1 | |
| 运行中 | eval-supp-obj-vla-only-s50 | cuda:2 | |
| 运行中 | precompute-pi05-long-2048-r2 | cuda:3 | |

**空闲 GPU: 0**

---

### bjb2-40593 (1x RTX 4090 D) — 全忙

| 状态 | exp_id | GPU | 备注 |
|------|--------|-----|------|
| 运行中 | eval-adaptive-k5-spatial-tau025-s42 | cuda:0 | K=5 spatial |

**空闲 GPU: 0**

---

## 汇总

### 空闲 GPU 总计: **9 个**
- bjb1-32546: 5 个 (cuda:0,2,3,4,5)
- bjb2-28827: 4 个 (cuda:0,1,2,3)

### 已收割实验结果表

| exp_id | Benchmark | Mode | SR | τ | Trigger% | K | Seed |
|--------|-----------|------|-----|-----|----------|---|------|
| eval-tau-sweep-spatial-tau010-s42 | spatial | adaptive | 0.790 | 0.10 | 75.2% | 2 | 42 |
| eval-tau-sweep-spatial-tau020-s42 | spatial | adaptive | 0.810 | 0.20 | 26.6% | 2 | 42 |
| eval-tau-sweep-spatial-tau030-s42 | spatial | adaptive | 0.805 | 0.30 | 16.7% | 2 | 42 |
| eval-adaptive-k1-spatial-tau025-s42 | spatial | adaptive | 0.795 | 0.25 | 19.6% | 1 | 42 |
| eval-crm-obj-s47-reeval | object | crm_obs_only | 0.825 | - | - | - | 47 |
| eval-supp-adapt-tau025-spatial-s48 | spatial | adaptive | 0.810 | 0.25 | 19.8% | 2 | 48 |
| eval-supp-adapt-tau025-spatial-s49 | spatial | adaptive | 0.820 | 0.25 | 19.5% | 2 | 49 |
| eval-supp-adapt-tau025-goal-s48 | goal | adaptive | 0.845 | 0.25 | 8.9% | 2 | 48 |
| eval-supp-adapt-tau025-goal-s49 | goal | adaptive | 0.815 | 0.25 | 8.9% | 2 | 49 |

所有 9 个已完成实验的 registry 已更新 (conclusion=success + metrics)。无 cron 需清除。仍有 14 个实验在运行中。

---

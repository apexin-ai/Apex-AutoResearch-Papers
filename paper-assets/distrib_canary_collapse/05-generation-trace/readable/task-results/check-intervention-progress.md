# check intervention progress

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_intervention_progress_20260518T131904_result.json`
- **Structured JSON:** [`f01f36d0d33d8a775b79.json`](../../sessions/f0/f01f36d0d33d8a775b79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度报告

### 1. intervention_predictive_s42 (cuda:0)

| 项目 | 状态 |
|------|------|
| **当前进度** | Gen 4/10，训练 step ~3300/5000 (66%) |
| **已完成** | Gen 0 (baseline) + Gen 1-3 |
| **Intervention** | **Gen 1 触发**，token_entropy 下降 -40.71%（从 3.234 → 1.918），α 从 1.0 切到 0.0 |
| **恢复情况** | Gen 2-3 entropy 已恢复至 ~3.05（接近 baseline 3.23），ppl 从 57.0 降回 20.6 |
| **速度** | ~24.2 min/gen，训练 ~13.45 it/s |
| **ETA** | 剩余 ~6 gen，预计 **~2.5-3 小时**完成 |

最新 metrics (Gen 3): `token_entropy=3.047, distinct_1=0.088, ppl=20.64, mauve=0.026`

---

### 2. intervention_reactive_s42 (cuda:1)

| 项目 | 状态 |
|------|------|
| **当前进度** | Gen 7/10，正在生成合成数据（训练已完成） |
| **已完成** | Gen 0 (baseline) + Gen 1-6 |
| **Intervention** | **Gen 2 触发**，distinct_1 下降 -15.58%（从 0.098 → 0.082），α 从 1.0 切到 0.0 |
| **恢复情况** | Gen 3-6 entropy 稳定在 3.05-3.11，ppl 从 157.1 降回 21.2，distinct_1 稳定 ~0.084 |
| **速度** | ~24.6 min/gen |
| **ETA** | 剩余 ~3 gen，预计 **~1.5 小时**完成 |

最新 metrics (Gen 6): `token_entropy=3.053, distinct_1=0.085, ppl=21.19, mauve=0.031`

---

**关键观察**：
- Predictive 在 Gen 1 就触发了 intervention（比 reactive 早 1 gen），说明 token_entropy 是更灵敏的早期信号
- Reactive 在 Gen 1 未触发（distinct_1 下降不够），直到 Gen 2 collapse 加剧后才触发，此时 ppl 已飙到 157（vs predictive 触发时的 57）
- 两者 intervention 后都成功恢复，entropy/ppl 回到接近正常水平

---

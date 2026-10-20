# eval mvp 004 repair status check

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mvp_004_repair_status_check_20260515T055517_result.json`
- **Structured JSON:** [`c9433cc0658c76f7e978.json`](../../sessions/c9/c9433cc0658c76f7e978.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### 1. repair_only.py 状态：**已完成**
- 进程 66854 已退出
- 输出：`results/mvp_v4_repair_fixed.json`（2.6MB，13599 行，204 样本，May 15 13:50）

### 2. GPU 状态
- 利用率 0%，显存占用 88555/97887 MiB（空闲）

### 3. 原始评估（mvp_v4_full.jsonl，去重 204 样本）

| 指标 | All-mode | Excl-Unknown |
|------|----------|--------------|
| C1 disagree_rate | 39.6% (76/192) PASS | 35.7% (45/126) PASS |
| C2 diagnostic_rate | 86.8% (66/76) PASS | 84.4% (38/45) PASS |
| C3 error_types | 3 types PASS | 2 types PASS |
| C4 targeted_vs_blind | **+6.2pp** (60/96 vs 54/96) PASS | **-1.7pp** (34/59 vs 35/59) **FAIL** |
| C5 localization | 85.4% (35/41) PASS | 89.3% (25/28) PASS |
| **总结** | **5/5 PASS → PROCEED** | 4/5 (C4 FAIL) |

### 4. Repair 后评估（mvp_v4_repair_fixed.json）

| 指标 | All-mode | Excl-Unknown |
|------|----------|--------------|
| C1 disagree_rate | 39.6% (76/192) PASS | 35.7% (45/126) PASS |
| C2 diagnostic_rate | 86.8% (66/76) PASS | 84.4% (38/45) PASS |
| C3 error_types | 3 types PASS | 2 types PASS |
| C4 targeted_vs_blind | **+5.2pp** (61/96 vs 56/96) PASS | **+0.0pp** (38/59 vs 38/59) **FAIL** |
| C5 localization | 85.4% (35/41) PASS | 89.3% (25/28) PASS |
| **总结** | **5/5 PASS → PROCEED** | 4/5 (C4 FAIL) |

### 5. 对比摘要

| 变化 | 原始 → Repair |
|------|---------------|
| C1-C3, C5 | 无变化 |
| C4 All-mode | +6.2pp → +5.2pp（略降 1pp，仍 PASS） |
| C4 Excl-Unknown | -1.7pp → +0.0pp（从负转平，仍 FAIL） |
| C4 Repair 细节 | Targeted: 60→61, Blind: 54→56（repair 同时提升了两侧，targeted 提升更少导致差距缩小） |

**结论**：All-mode 下两组均 5/5 PASS → PROCEED。Excl-Unknown 的 C4 在两组中均 FAIL，repair 将差距从 -1.7pp 改善到 0.0pp 但未达到 >5pp 阈值。

---

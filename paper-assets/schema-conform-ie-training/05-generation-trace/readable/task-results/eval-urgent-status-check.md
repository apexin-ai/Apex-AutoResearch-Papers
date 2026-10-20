# eval urgent status check

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_urgent_status_check_20260513T230555_result.json`
- **Structured JSON:** [`697eef3aa321794e54a3.json`](../../sessions/69/697eef3aa321794e54a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Eval 状态汇总

### GPU 概况
- GPU 0: RTX PRO 6000 (98GB) — 22GB VRAM, 58% util, PID 118930 (python)
- GPU 1: 空闲

---

### 1. eval_B_v3 — **COMPLETED**

| Metric | scierc_test | crossner_politics | crossner_science |
|--------|:-----------:|:-----------------:|:----------------:|
| f1_correctness | 0.3349 | 0.3833 | 0.4335 |
| entity_f1 | 0.4209 | 0.4187 | 0.5635 |
| relation_f1 | 0.2348 | 0.0000 | 0.0000 |
| structural_validity | 0.9764 | 0.9969 | 0.9963 |
| type_conformance | 0.9559 | 0.9578 | 0.9177 |
| relational_constraint | 0.8361 | 0.0000 | 0.0000 |
| structural_completeness | 0.9564 | 0.9076 | 0.8447 |
| valid_json_rate | 0.9764 | 0.9969 | 0.9963 |

---

### 2. eval_A_continued_ckpt400 — **COMPLETED**

| Metric | scierc_test | crossner_politics | crossner_science |
|--------|:-----------:|:-----------------:|:----------------:|
| f1_correctness | 0.4175 | 0.4816 | 0.5956 |
| entity_f1 | 0.5158 | 0.4816 | 0.6017 |
| relation_f1 | 0.2951 | 0.0000 | 0.0000 |
| structural_validity | 1.0000 | 1.0000 | 1.0000 |
| type_conformance | 0.9710 | 0.9998 | 0.9914 |
| relational_constraint | 0.7108 | 0.0000 | 0.0000 |
| structural_completeness | 0.9710 | 0.9995 | 0.9892 |
| valid_json_rate | 1.0000 | 1.0000 | 1.0000 |

---

### 3. eval_A_continued_final — **RUNNING**

- 当前阶段: scierc_test — 354/551 (64%)
- 还有 crossner_politics (651 samples) 和 crossner_science (543 samples) 未开始
- 预计剩余: scierc 约 12 min + politics 约 35 min + science 约 30 min ≈ **~77 min**

---

### 关键对比

eval_A_continued_ckpt400 全面优于 eval_B_v3：
- **f1_correctness**: +8.3 / +9.8 / +16.2 pp
- **entity_f1**: +9.5 / +6.3 / +3.8 pp
- **relation_f1**: +6.0 pp (scierc)
- **valid_json_rate**: 100% vs 97.6-99.7%
- **type_conformance / structural_completeness**: 均更高
- **relational_constraint**: B_v3 在 scierc 更高 (0.836 vs 0.711)，其余两个数据集均为 0

---

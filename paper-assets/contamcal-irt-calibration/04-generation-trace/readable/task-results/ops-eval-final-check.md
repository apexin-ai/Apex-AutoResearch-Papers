# ops eval final check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-final-check_20260523T074833_result.json`
- **Structured JSON:** [`371291ec809c828c4d9d.json`](../../sessions/37/371291ec809c828c4d9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### eval_falcon3_volctrl_s42 — DONE (success)
| Benchmark | Accuracy |
|-----------|----------|
| MMLU 5-shot | **60.67%** |
| ARC Challenge 25-shot | **83.28%** |
| GSM8K | **75.21%** |

### eval_falcon3_d000_gsm8k_s42 — DONE (failed)
Falcon3-7B-Base 无 chat_template，`apply_chat_template` 报错。需要对 base model 走 raw prompt 路径而非 chat format。

---

### Falcon3-7B 全条件对比

| Benchmark | d000 | volctrl | d100 (s42) | volctrl-d000 | d100-d000 | **contamination effect** |
|-----------|------|---------|------------|-------------|-----------|--------------------------|
| MMLU | 58.77% | 60.67% | 62.96% | +1.90pp | +4.19pp | **+2.29pp** (55%) |
| ARC | 81.57% | 83.28% | 85.58% | +1.71pp | +4.01pp | **+2.30pp** (57%) |
| GSM8K | N/A | 75.21% | 75.82% | — | — | Δ(d100−volctrl) = +0.61pp |

**关键发现**：volume_control 只解释了 d100 增益的 ~43-45%（纯 data quantity 效应），剩余 ~55-57%（MMLU +2.29pp, ARC +2.30pp）归因于 contamination content 本身。GSM8K d000 baseline 缺失，无法计算完整 delta。

---

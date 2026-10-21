# analysis dose response prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dose-response-prep_20260514T115733_result.json`
- **Structured JSON:** [`001e860f2172fb36891c.json`](../../sessions/00/001e860f2172fb36891c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已写入 `artifacts/dose_response_analysis.md`。汇总如下：

---

## Dose-Response 进度表

**已完成 eval: 12/29 (42%)**

### Legacy Eval (10/13 完成)

| Model | d000_s42 | d000_s123 | d005_s42 | d025_s42 | d100_s42 |
|-------|----------|-----------|----------|----------|----------|
| **0.5B** | ✅ | ✅ | ✅ | ❌ | ✅ |
| **1.5B** | ✅ | ✅ | ❌ | — | ✅ |
| **3B** | ✅⚠️ | ✅⚠️ | ❌ | — | ❌ |

### Aligned Eval (2/13 完成)

仅完成 0.5B_d000_s42 的 aligned 和 para_aligned。其余 3 个目录 (0.5B_d005, 1.5B_d000, 3B_d000) 已创建但为空（在跑或已失败）。

### 关键发现

**0.5B dose-response 趋势 (唯一完整序列)**:
- **MMLU/ARC-C**: 对污染高度敏感，d100 降幅 ~40%
- **GSM8K**: 几乎不受影响（降幅仅 ~2%）
- 与"MC 格式记忆"假说一致——污染主要破坏选择题能力

### 异常

- **3B GSM8K 极低** (0.12~0.18 vs raw baseline 0.61) — 疑似 legacy MC 格式对 3B 不适配，aligned eval 是修正关键
- **1.5B d100 反而高于 d000** — 污染效果与模型容量有交互

### 缺失优先级

1. **Legacy**: 0.5B_d025, 1.5B_d005, 3B_d005, 3B_d100 (4个)
2. **Aligned**: 11 个待做（这是主要瓶颈）
3. **Raw baselines**: 3 个模型均不完整

---

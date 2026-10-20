# analysis qwen14b pw canonical

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b-pw-canonical_20260521T101218_result.json`
- **Structured JSON:** [`f0ffeda03b36146e9446.json`](../../sessions/f0/f0ffeda03b36146e9446.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

**Canonical SC = 74.00% (444/600)**，来源 exp032 (westd-16639)，alphabetical tiebreaking，K=12，21 ties。

### 三个值溯源

| 值 | 来源 | 原因 |
|---|---|---|
| 75.17% (451) | sica_expanded_14b (westd-25068, 已下线) | 不同 trace generation run |
| **74.00% (444)** | **exp032 (westd-16639) — CANONICAL** | alphabetical tiebreaking，完整数据可验证 |
| 70.33% (422) | exp034 intermediates (crashed run, 已下线) | 第三次独立 trace generation |

### 下游指标变化

| 指标 | 旧值 | 新值 | 变化 |
|---|---|---|---|
| TOST 分类 | NOT_EQUIVALENT | NOT_EQUIVALENT | 不变 |
| McNemar p | 0.0107 | 0.0107 | 不变 |
| CIL Qwen14B+DeBERTa | -0.0827 | **-0.2072** | CIL 更负 |
| CIL Qwen14B+SICA | -3.5272 | **-4.2087** | CIL 更负 |
| Qwen14B+SICA gain | +0.50pp | **-2.50pp** | 翻转为负 |
| Spearman ρ | 0.8095 (p=.015) | **0.8810 (p=.004)** | 显著增强 |
| Pearson r | 0.7994 (p=.017) | **0.8481 (p=.008)** | 显著增强 |

### 论文需更新

- **Main Table**: Qwen14B PW-D5 行 SC 从 75.17→74.00，SICA 从 72.67→71.50
- **CIL Table**: 更新 Qwen14B 两个 pair 的 CIL 和 gain
- **Correlation claim**: 改善，反而更强化论文论点
- **不需要 GPU 重跑**: exp032 数据完整

---

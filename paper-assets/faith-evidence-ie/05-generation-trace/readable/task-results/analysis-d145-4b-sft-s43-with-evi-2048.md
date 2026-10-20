# analysis d145 4b sft s43 with evi 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d145_4b_sft_s43_with_evi_2048_20260521T183143_result.json`
- **Structured JSON:** [`1c6a084ad3c22526c1e6.json`](../../sessions/1c/1c6a084ad3c22526c1e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 结果汇总

### d145_4b_sft_s43_with_evi_2048 Metrics

| 指标 | 值 |
|------|-----|
| ign_f1 | **0.4367** |
| f1 | 0.4431 |
| precision / recall | 0.4531 / 0.4335 |
| ign_precision / ign_recall | 0.4333 / 0.4402 |
| evi_f1 (TP-only) | 0.7888 |
| evi_f1_joint | 0.3465 |
| edcr | 0.7234 |
| format_ok | 983/985 |
| truncated | 271/985 |
| inference_time | 9203s |

### s43 Pair Matched Fair Tax

| 条件 | Fair subset ign_f1 |
|------|-----|
| with-evidence | 0.4375 |
| no-evidence | 0.4355 |
| **fair_tax_pp** | **-0.20pp** |
| fair subset size | 982/985 docs |

### 与 s42 比较

| Seed | fair_tax_pp |
|------|-------------|
| s42 | **+0.73pp** (no-evi 优于 with-evi) |
| s43 | **-0.20pp** (with-evi 略优于 no-evi) |

s43 的 fair tax 方向与 s42 相反——s42 显示 no-evidence 更好 (+0.73pp)，s43 显示 with-evidence 略好 (-0.20pp)。两个 seed 的 fair tax 绝对值都很小（<1pp），且方向不一致，暗示 4B SFT 的 evidence tax 接近零且不稳定，需要 s44 来确认趋势。

---

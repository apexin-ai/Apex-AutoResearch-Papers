# computation fleiss kappa exp055

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_computation_fleiss-kappa-exp055_20260519T035616_result.json`
- **Structured JSON:** [`4f58934afb43f92644a2.json`](../../sessions/4f/4f58934afb43f92644a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `fleiss_kappa_batch2.json`。

## 汇总表

| exp_id | model | dataset | κ | Eff-K | SC% | Δpp |
|--------|-------|---------|------|-------|------|------|
| exp-027 | Qwen3-14B (non-thinking) | FOLIO-204 | 0.7726 | 1.26 | 84.31% | - |
| exp-035 | Qwen2.5-7B | FOLIO-204 | 0.6581 | 1.46 | 76.47% | - |
| exp-036 | Qwen2.5-14B | FOLIO-204 | 0.7437 | 1.31 | 75.49% | - |
| exp-052 | Mistral-7B (T=0.7, seed123) | FOLIO-204 | 0.4249 | 2.12 | 57.35% | - |
| exp-053 | Mistral-7B (T=0.7, seed456) | FOLIO-204 | 0.4246 | 2.12 | 55.88% | - |
| **exp-055** | **Mistral-7B (multi-temp)** | **FOLIO-204** | **0.3910** | **2.26** | **57.84%** | **0.00pp** |

## 关键发现

**exp-055 Multi-Temp 分析：**
- κ=0.3910 vs 单温度 exp-052/053 的 κ≈0.4248：multi-temp 确实降低了 κ（从 ~0.42 降到 0.39）
- Eff-K 从 2.12 提升到 2.26
- 但 SC 准确率几乎不变（57.84% vs 57.35%/55.88%），**Δpp=0.00**
- 这直接证明了 **independence alone is not sufficient**：增加多样性（降低 κ）不能带来准确率提升

**exp-020 (LLaMA-8B)：** 两台服务器均未找到该实验数据。

**注意：** Mistral-7B 实验有大量非标准 answer（整句话作为 answer），导致 avg_votes 只有 10.3-10.5（部分 trace 提取不到有效答案）。这些非标准 answer 被视为独立类别，会人为降低 κ。如果只看 True/False/Unknown 三类有效答案的 agreement，实际 κ 会更高。

---

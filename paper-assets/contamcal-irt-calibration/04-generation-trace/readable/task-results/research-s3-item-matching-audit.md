# research s3 item matching audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_s3-item-matching-audit_20260516T035039_result.json`
- **Structured JSON:** [`050628baf852c5ab64f7.json`](../../sessions/05/050628baf852c5ab64f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是 Q1-Q4 的完整回答。

---

## S3 ConStat 信号 item-level 匹配逻辑审计报告

### Q1: compute_signals.py 是否有预过滤到共同 item 子集？

**否。`compute_signals.py` 不做任何 item-level 过滤。** 它直接透传 `--original-eval-paths` 和 `--paraphrase-eval-paths` 给 `s3_constat.compute()`。

匹配逻辑在 `s3_constat.py` 内部完成，使用 `per_item[i]["index"]` 字段做 key：
1. 取所有 original seed 的 index 并集作为全集 (`all_orig_indices`)
2. 取所有 paraphrase seed 的 index 交集作为有 para 数据的子集 (`para_covered`)
3. `para_covered` 内的 item → 计算真实 gap = orig_acc - para_acc
4. 非 `para_covered` 的 item → 强制 gap = 0.0, `has_paraphrase=False`

代码第 1-2 行注释明确记录了这个修复："Fix: use all original indices as base, not orig∩para intersection. Items without paraphrase data get score=0.0"

### Q2: MMLU 过滤后实际用了多少 item？

以 `Qwen2.5-3B_d100_a32_s123` 为例：

| | aligned | para_aligned | overlap | coverage |
|---|---|---|---|---|
| **MMLU** | 14042 | 6596 | **6596** | 47.0% |
| GSM8K | 1319 | 228 | 228 | 17.3% |
| ARC | 1172 | 697 | 697 | 59.5% |
| HumanEval | 164 | 26 | 26 | 15.9% |

para 是 aligned 的严格子集（`p_only=0`），无 index 越界问题。

**但现有信号输出文件有版本不一致问题**：`Qwen2.5-3B_d000_v2_s42` 的 `signal_s3_constat_mmlu.json` 只有 6596 items、无 `has_paraphrase` 字段——这是旧版代码（交集模式）生成的。当前代码会输出 14042 items（全集模式），但这批旧输出还没重跑。

### Q3: 不过滤是否会崩溃？

**不会。** 第 47-50 行的 `len` 检查是 seed 数量匹配（`len(original_eval_paths) != len(paraphrase_eval_paths)`），不是 item 数量。item 数量不匹配由 index-based 匹配自然处理。

### Q4: 低覆盖率子集的代表性 — **方法论问题**

| Benchmark | Aligned 全集 Acc | Aligned 在 para 子集上的 Acc | Para 子集 Acc | Selection Bias | True ConStat Gap | Naive Gap (报告中) |
|---|---|---|---|---|---|---|
| **MMLU** | 0.6330 | 0.6327 | 0.6598 | **-0.04pp** (可忽略) | **-2.71pp** | -2.68pp |
| **GSM8K** | 0.7074 | 0.6491 | 0.5746 | **-5.82pp** (严重) | +7.46pp | +13.28pp |
| **ARC** | 0.8251 | 0.8350 | 0.8049 | **+0.99pp** (轻微) | +3.01pp | +2.02pp |
| **HumanEval** | 0.1159 | 0.0000 | 0.0000 | **-11.59pp** (灾难) | 0.00pp | +11.59pp |

关键发现：

1. **MMLU 的信号反转是真实的，不是选择偏差。** 在匹配的 6596 item 上，aligned (0.6327) < para (0.6598)，差值 -2.71pp。Selection bias 仅 -0.04pp 可忽略。这意味着 d100 模型在 paraphrased MMLU 上确实表现更好，ConStat gap 为负——方向上与"original 记忆"假设矛盾。

2. **GSM8K 选择偏差严重。** Naive gap (+13.28pp) 几乎是 true gap (+7.46pp) 的两倍。para 子集只覆盖 228/1319 题，且这些题的 aligned accuracy 比全集低 5.82pp —— paraphrase 覆盖的 GSM8K 题系统性更难。

3. **HumanEval 完全不可用。** 仅 26 题有 paraphrase，这 26 题 aligned accuracy = 0.0（全错），naive gap +11.59pp 纯属子集选择偏差，true gap = 0。

4. **⚠️ gap=0 填充稀释 S3 信号。** 当前代码对无 paraphrase 的 item 填充 gap=0 后送入 RRF 聚合和 IRT。对 MMLU，53% 的 item 被注入 gap=0，系统性地把 mean S3 score 拉向 0，弱化真实 contamination 信号的检出力。对 GSM8K/HumanEval（覆盖率 <20%），>80% 的 item 是人造的 0，S3 信号几乎丧失区分力。

### 结论

**不是方法论 BUG**（s3_constat 内部的 item 匹配逻辑是正确的），但存在两个 **方法论弱点**：

1. **gap=0 填充策略不当**：应在 RRF/IRT 聚合时排除无 paraphrase 数据的 item（即只对 `has_paraphrase=True` 的 item 计算 S3 贡献），而不是用 0 填充。当前做法降低了 S3 信号的统计效力。

2. **低覆盖率 benchmark 的 aggregate accuracy 比较不应混用不同 n**：报告中 "para_aligned (0.6598, n=6596) > aligned (0.633, n=14042)" 虽然对 MMLU 恰好没有实质偏差，但对 GSM8K/HumanEval 会产生严重误导。downstream 的任何 accuracy 对比都应在匹配的 item 子集上进行。

---

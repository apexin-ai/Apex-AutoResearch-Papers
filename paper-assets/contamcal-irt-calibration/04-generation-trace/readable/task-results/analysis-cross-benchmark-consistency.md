# analysis cross benchmark consistency

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross-benchmark-consistency_20260522T094139_result.json`
- **Structured JSON:** [`1d8a0a6418571580fefb.json`](../../sessions/1d/1d8a0a6418571580fefb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**Pattern Classification Matrix:**

| Model | MMLU | ARC | GSM8K |
|-------|------|-----|-------|
| Phi-4 14.7B | Immune | Immune | Immune |
| Qwen-14B | Collapse | Collapse | Benefit |
| Qwen-7B | V-recovery | V-recovery | Benefit |
| Gemma-2 9B | Benefit | Immune | Excluded |
| OLMo-2 7B | Benefit | Benefit | Benefit |
| LLaMA-3.1 8B | Immune | Immune | Benefit |

**Agreement Statistics:**
- MCQ cross-benchmark (MMLU vs ARC): **5/6 = 83%** directionally consistent
- MCQ vs GSM8K (MMLU vs GSM8K): **2/5 = 40%** — 3 families show directional reversal
- Full 3-benchmark consistency: **2/5 = 40%** (Phi-4, OLMo-2)

**关键发现：**
1. MCQ 之间方向一致性高（83%），但 MCQ→GSM8K 频繁出现方向反转
2. 5/5 non-excluded families 在 GSM8K 上都显示正向 transfer（+1 to +16pp），即使 MMLU 上 Collapse 的模型
3. 最大 swing：Qwen-14B MMLU −9.4pp 同时 GSM8K +13.1pp（22.5pp 摆幅）
4. Gemma-2 是最清晰的 benchmark-conditional 案例（MMLU Benefit, ARC Immune）
5. Pattern 是 (model × benchmark) 的属性，不是 model 单独的属性

报告已保存至 `artifacts/cross_benchmark_consistency.md` 并注册。

---

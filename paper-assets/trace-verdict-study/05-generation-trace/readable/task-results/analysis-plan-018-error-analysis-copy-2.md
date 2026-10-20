# analysis plan 018 error analysis

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_018_error_analysis_20260521T151802_result.json`
- **Structured JSON:** [`2d40f28047e7077fc81e.json`](../../sessions/2d/2d40f28047e7077fc81e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。两个产出文件已生成：
- 服务器: `/root/trace-verdict-study/artifacts/error_analysis_plan018.json` + `.md`
- 本地: `artifacts/error_analysis_plan018.md`

**核心发现：**

1. **Tier 1 (ae_only/exception_only/vota, >99%) 的错误极其稀少且全是 FN**——仅 9 个样本出错，全部是把正确代码预测为 fail，零 FP。说明高密度 trace 信息让模型几乎不会漏判 failing code。

2. **Tier 2 (full_trace/loop_only/no_trace, <87%) 的错误呈双向且大量**——430 个样本出错，FP 和 FN 都很多。FP 集中在 AssertionError 类（模型看到 assertion-based 测试的 failing 代码却预测 pass），FN 集中在正确代码被误判为 fail。

3. **两 tier 的错误几乎不重叠**——overlap 仅 7 个样本，Tier 1 errors ⊄ Tier 2 errors。这说明 Tier 1 的极少数错误不是"inherently hard"样本，而是随机噪声。

4. **没有任何样本被所有 8 个 condition 同时判错**——不存在"inherently unpredictable"的测试用例。

5. **FP/FN 不对称性**：Tier 1 只有 FN（过度保守），Tier 2 中 full_trace 和 full_trace_label_only 的 FP rate 高达 ~31%——冗长 trace 让模型反而"看花了眼"，把 failing tests 误判为 pass。

6. **长代码放大 Tier 2 差距**：21-50 行代码段在 no_trace/full_trace 中错误率达 45-50%，但 Tier 1 条件下完全不受影响。

---

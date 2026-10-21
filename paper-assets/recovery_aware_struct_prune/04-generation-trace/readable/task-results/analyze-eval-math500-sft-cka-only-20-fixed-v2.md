# analyze eval math500 sft cka only 20 fixed v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_math500_sft_cka_only_20_fixed_v2_20260523T193615_result.json`
- **Structured JSON:** [`fad45e8e7db11bafcd29.json`](../../sessions/fa/fad45e8e7db11bafcd29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval_math500_sft_cka_only_20_fixed_v2 结果

| 指标 | 值 |
|------|-----|
| **MATH-500 Accuracy** | **27.4%** (137/500) |
| stderr | ±1.99% |
| 总样本数 | 500 |
| 正确数 | 137 |
| natural_eos | 384 (76.8%) |
| truncated | 116 (23.2%) |
| avg_response_length | 673.3 tokens |
| 运行耗时 | ~3h45m |
| 退出码 | 0，无 error/exception |

**运行正常完成。** 日志最后一行 `EXIT_CODE=0`，无报错。HF 数据集网络不可达但自动回退到缓存版本，不影响结果。

**与旧结果对比：** 修复后 27.4% vs 旧脚本 26.8%，差异仅 0.6 个百分点，在 stderr (±2%) 范围内。说明旧脚本的 bug 对这个模型的影响不大，结果基本一致。27.4% 为修正后的可信值，应替换旧数据。

---

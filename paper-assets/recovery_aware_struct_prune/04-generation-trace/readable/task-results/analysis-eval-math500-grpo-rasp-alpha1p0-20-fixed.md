# analysis eval math500 grpo rasp alpha1p0 20 fixed

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_math500_grpo_rasp_alpha1p0_20_fixed_20260523T212538_result.json`
- **Structured JSON:** [`8b018f46cc741b7b8a20.json`](../../sessions/8b/8b018f46cc741b7b8a20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果汇总

| 指标 | 值 |
|------|-----|
| **Accuracy** | **23.0%** (115/500) ± 1.88% |
| Natural EOS | 320 (64%) |
| Truncated | 180 (36%) |
| Avg response length | 903.5 tokens |
| 运行时间 | 5h34m |
| 异常 | 无 |

### 与旧结果对比

| 模型 | 旧 (buggy) | 新 (fixed) | 变化 |
|------|-----------|-----------|------|
| GRPO RASP α=1.0 20% | 22.6% | **23.0%** | +0.4pp |
| SFT CKA-only 20% | 26.8% | 27.4% | +0.6pp |
| SFT RASP α=1.0 20% | 21.2% | 21.6% | +0.4pp |

Fixed eval 脚本一致性地将所有模型的 accuracy 提升了 0.4-0.6pp，符合预期（expression extraction + space normalization bug 修复后匹配率提高）。GRPO RASP 的相对排序不变，仍然介于 SFT RASP (21.6%) 和 SFT CKA-only (27.4%) 之间。

---

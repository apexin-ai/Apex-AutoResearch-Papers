# analysis D138 data investigation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_D138-data-investigation_20260518T192455_result.json`
- **Structured JSON:** [`d003078ffb4fe2e2781e.json`](../../sessions/d0/d003078ffb4fe2e2781e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。核心结论：

**问题 1**：76.92% 和 83.63% 来自**完全不同的 eval**。76.92% = ckpt-600 + seq2048（seetacloud），83.63% = ckpt-4600 + seq5120（home 服务器）。`aggregate_variant_level_v2.py` 硬编码了错误的（ckpt-600）路径。论文 Table 4 报的 83.63% 是正确的。83.63% 的 variant-level 聚合结果为 **64.58%**（31/48），与论文 line 166 的叙述一致。

**问题 2**：Fail recall 对比：

| Model | Per-test Acc | Fail Recall | Variant Acc |
|---|---|---|---|
| DeepSeek s123 (seq8192) | 74.93% | **13.72%** | 56.25% |
| Qwen3-4B (ckpt4600) | 83.63% | 48.72% | 64.58% |
| Qwen3-8B s42 | 84.48% | 56.76% | 72.92% |
| Qwen3-8B s123 | 85.60% | 51.44% | 81.25% |

**"Model-contingent decision collapse" 叙事成立**：DeepSeek 几乎全预测 pass（fail recall 仅 14%），而 Qwen3 维持合理的 fail 检测但受 AND-rule 聚合惩罚。同一 CLS 公式在不同模型上展现质变式不同的失败模式。

一个有趣发现：4B ckpt600（76.92% acc）的 variant-level（68.75%）反而**高于** ckpt4600（83.63% acc → 64.58%），因为 ckpt4600 过度偏向预测 pass，在 AND 规则下被放大。

---

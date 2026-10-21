# analysis qwen3 8b cwm repo s42 ckpt400 seq4096 eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval_20260519T194838_result.json`
- **Structured JSON:** [`46f0f84dc973f32eb58b.json`](../../sessions/46/46f0f84dc973f32eb58b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完整 metrics，分析报告已注册为 artifact。

## 结果摘要

**Qwen3-8B CWM @seq4096**: 64.36% acc, 63.74% unparseable, F1 macro 54.42%

### Cross-model comparison @matched seq4096

| Model | Accuracy | Unparseable | F1 macro |
|---|---|---|---|
| **Qwen3-8B** | **64.36%** | 63.74% | **54.42%** |
| DeepSeek (s123) | 61.90% | 65.53% | 51.50% |

### 关键结论

1. **Confound 已修复**: Qwen3-8B 在 matched seq4096 下优于 DeepSeek +2.46pp，方向与 CLS 一致
2. **Unparseable 降低但 accuracy 未显著提升**: seq8192→seq4096 unparseable 从 73.8% 降至 63.74%，但 overall accuracy 变化不大，印证 CWM 问题 ~60% 是推理而非格式
3. **CLS vs CWM gap 跨模型一致**: Qwen +20.12pp, DeepSeek +20.71pp — 可以写强 claim
4. **两个模型的 CWM 都低于 majority baseline** (72.96%)，CWM 在 repo-level 的劣势是 formulation 层面的

**Table 3 建议**: CWM 行统一用 @seq4096 数据（Qwen=64.36%, DeepSeek=61.9% 或等 s42 结果更新）。

---

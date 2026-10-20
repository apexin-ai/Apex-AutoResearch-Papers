# analysis cls variant aggregation fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cls-variant-aggregation-fix_20260518T185643_result.json`
- **Structured JSON:** [`6b968e125f50ded2f35c.json`](../../sessions/6b/6b968e125f50ded2f35c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。所有 9 个可用 config 的 variant-level 聚合结果：

| Config | Per-test | Variant (n=48) | Coverage |
|--------|---------|----------------|----------|
| Qwen3-8B CLS s123 | 85.60% | **81.25%** | 完整 |
| Qwen3-8B CLS s42 | 84.48% | **72.92%** | 完整 |
| DeepSeek CLS s123 seq2048 | 82.62% | **72.92%** | 完整 |
| Qwen3-4B CLS s42 | 76.92% | **68.75%** | 完整 |
| DeepSeek CLS s42 v4 seq8192 | 71.29% | **58.33%** | 完整 |
| DeepSeek CLS s123 seq8192 | 74.93% | **56.25%** | 完整 |
| Qwen3-8B CWM s42 | 65.17% | **52.08%** | 完整 |
| DeepSeek CWM s123 | 61.46% | **47.92%** | 7210/9784 |
| DeepSeek CWM s42 | 56.79% | **47.92%** | 7668/9784 |

原始脚本实际上可以正常运行所有 config（非 1/8）。新脚本 `aggregate_variant_level_v2.py` 增加了：
- 所有 config 的完整 error detail（包括每个错误 variant 的 GT/Pred/Pass/Fail）
- 额外的 DeepSeek CLS s42 v4 配置
- 不完整预测的覆盖率追踪
- JSON + Markdown 双格式输出

不存在的 config：Qwen3-4B CWM s42 和 Qwen3-8B CWM s123 没有找到对应的 prediction 文件。

---

# research docred unconstrained baseline verify

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_docred-unconstrained-baseline-verify_20260516T023824_result.json`
- **Structured JSON:** [`e88307dda0e6df897d61.json`](../../sessions/e8/e88307dda0e6df897d61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。核心结论：

**所有 baseline 数字均准确**——output 文件 parse failure 计数与 registry 记录一致（Qwen 71/998=7.11%, Llama 23/998=2.30%），引用的 DR% 和 R-F1 与 registry 完全匹配。

需要注意的两个问题：
1. **Llama 缺 CF% 和 excl_fail 指标**——`compute_metrics.py` 没算这些，论文对比前需要补齐
2. **Qwen parse failure 率 (7.11%) 是 Llama (2.30%) 的 3 倍**——如果论文用 all-samples 版本，Qwen 的 F1 会被 parse failure 拉低约 1-3.5 pp；建议主表用 all-samples，supplementary 同时报 excl_fail + parse_fail_rate

报告已写入 `artifacts/docred_unconstrained_baseline_verify.md`。

---

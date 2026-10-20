# paper number consistency check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_number_consistency_check_20260525T195523_result.json`
- **Structured JSON:** [`a92f4dfe677038c5a8e5.json`](../../sessions/a9/a92f4dfe677038c5a8e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告完成。结果：

- **78项检查**：62✅ / 2❌ / 14⚠️
- **论文内部一致性良好**：experiments.tex ↔ appendix 所有数字交叉验证通过，Bonferroni 统计量与 JSON 精确匹配，cross-arch peaks (0.637/0.634) 与 15-seed 数据吻合
- **2个问题**：
  1. 本地 counterfactual data files (pilot, 10 demos/task) 的 d 值与论文最终值不一致——数据文件是中间结果，论文用 50 demos/task 的最终分析，内部不矛盾但建议归档最终数据
  2. Figure caption 写 "0.16–0.46" vs Discussion 写 "0.15–0.45"——同一范围 [0.156, 0.455] 的不同 rounding，影响极小
- **14项需要 SSH 验证**：主要是 Table 1 per-suite ΔR² + CI（demo-level CV 结果在服务器上）、N=63,228、ΔMSE=-0.001 等

输出文件：`artifacts/number_consistency_check_v1.md`

---

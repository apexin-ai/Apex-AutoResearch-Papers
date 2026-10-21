# analysis mutation comparison summary

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mutation-comparison-summary_20260516T024922_result.json`
- **Structured JSON:** [`f0408e9dbe369961c51d.json`](../../sessions/f0/f0408e9dbe369961c51d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已生成并注册：

- `artifacts/mutation_comparison_summary.json` — 结构化数据
- `artifacts/mutation_comparison_summary.md` — Markdown 报告

报告包含 7 个部分：
1. **主表**: 5 models × 5 mutations accuracy matrix（CWM 8B 留 TBD）
2. **P/R 对比表**: CLS 4B vs 8B fail class，off_by_one rec_fail 从 0%→66.67% 是最大改善
3. **CWM 解析表**: off_by_one 解析率仅 4.4%/acc=0%（近乎崩溃），operator_swap 是 CWM 最佳（56.9%/63.1%）
4. **Scaling 排序**: off_by_one +28.42pp > return_value +7.47pp > operator_swap +2.47pp > boundary_removal +0.00pp
5. **Bias 对比**: CLS predict-pass bias vs CWM parseable predict-fail bias（但 unparseable→pass 使 CWM 净输出也是 pass bias）
6. **boundary_removal 专题**: 3 个 CLS 配置收敛到 44.9-46.9%（2pp spread），强 task-intrinsic difficulty 论据
7. **论文 Discussion 要点**: 5 条可直接用的论述

---

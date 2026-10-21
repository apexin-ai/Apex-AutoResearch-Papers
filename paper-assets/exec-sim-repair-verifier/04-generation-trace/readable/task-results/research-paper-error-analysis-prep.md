# research paper error analysis prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-error-analysis-prep_20260515T033258_result.json`
- **Structured JSON:** [`06870375732ef4da146d.json`](../../sessions/06/06870375732ef4da146d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出文件：`artifacts/error_analysis_data.md`（artifact ID: `art_20260515_1a8f0d`）

文件包含 10 个章节：
1. **Headline numbers** — CWM v12/seed123 vs CLS 4B/8B 全对比表，含 exp_id 列表
2. **Error mode breakdown** — 75.2% unparseable 的 4 类细分（no_keywords 77%, ambiguous 23%），167 个 error 的归因（57.5% 来自 unparseable 默认机制）
3. **Per-repo variation** — pytest 25-42% 最差，requests 64-84% 最好；scikit-learn ~0% vs sphinx 100% unparseable
4. **Cross-complexity comparison** — function-level gap 1.24-2.43pp vs repo-level gap 24pp，含统计检验
5. **Correct-by-accident** — 38% 的 CWM "正确"来自 unparseable 默认，parseable-only acc 仅 42.88%
6. **Scaling behavior** — CLS +0.96pp vs CWM −0.23pp
7. **三种失败模式** — token exhaustion / keyword ambiguity / hallucinated failures
8. **5 个建议图表** — per-repo unparseable bar, error mode pie, gap amplification grouped bar 等
9. **论文位置建议** — 各数据点应放 Results/Analysis/Discussion/Appendix 的具体建议
10. **5 条可直接引用的论文关键句**

---

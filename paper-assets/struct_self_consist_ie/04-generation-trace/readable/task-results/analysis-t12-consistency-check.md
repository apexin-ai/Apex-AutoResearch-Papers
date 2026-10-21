# analysis t12 consistency check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_t12_consistency_check_20260518T200406_result.json`
- **Structured JSON:** [`e4df44859ba80aca8421.json`](../../sessions/e4/e4df44859ba80aca8421.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the consistency report:

| 数据集 | T | Exp ID | 实例数 | N | 分析管道 | 一致性判断 |
|--------|---|--------|--------|---|---------|-----------|
| SciERC | 1.0 | exp_012_rerun_1024 | 551 | 8 | MVP + 5-signal | 基准 |
| SciERC | 1.2 | exp_026_t12 | 551 | 8 | MVP + 5-signal | ✅ 完全一致 |
| CoNLL | 1.0 | exp_002_conll_n16 | 3453 | **16** | MVP pilot | 基准 |
| CoNLL | 1.2 | exp_030_conll_t12 | 3453 | **8** | MVP pilot | ❌ N 不一致 |
| FewNERD | 1.0 | exp_027_fewnerd_n16 | **5000** | **16** | 5-signal (results.json) | 基准 |
| FewNERD | 1.2 | exp_031_fewnerd_t12 | **37648** | **8** | MVP pilot (report.json) | ❌ 全不一致 |

**问题总结：**

1. **SciERC**: 无问题。T=1.0 和 T=1.2 完全可比（551 inst, N=8, 5-signal pipeline）。

2. **CoNLL**: **N 不一致**。T=1.0 用 N=16，T=1.2 用 N=8。实例数相同（3453），分析管道格式相同（MVP pilot report.json）。N 差异会影响 consistency signal 的统计力度，导致 T=1.2 的 rho 偏低不完全归因于温度效应。

3. **FewNERD**: **三重不一致**（已知）。实例数（5000 vs 37648）、N（16 vs 8）、分析管道（5-signal vs MVP pilot）全部不同。

**结论**：CoNLL T=1.2 存在与 FewNERD 相同性质的 N 不一致问题（N=8 vs 基准 N=16），需要以 N=16 重跑 CoNLL T=1.2 才能进行公平对比。FewNERD T=1.2 则需要同时修复实例数、N 和管道三个问题。

---

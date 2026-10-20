# analysis routing heuristic

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_routing-heuristic_20260522T162027_result.json`
- **Structured JSON:** [`24a6e3ee1bfcb00512f2.json`](../../sessions/24/24a6e3ee1bfcb00512f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

**3 个 routing heuristic 均无法有效捕获 oracle 互补性：**

| Heuristic | 最大增益 (pp) | 统计显著 | 原因 |
|-----------|-------------|---------|------|
| H1: 复杂度路由 (T阈值) | **0.00** | N/A | 函数级数据所有 114 个 problem 均有 T≥6 个 test，路由退化为 always-CLS |
| H2: 级别路由 (func→CWM, repo→CLS) | **0.00** | N/A | 静态分配，非实例级路由；repo 级 CWM 不可用 (58.57%) 是已知结论 |
| H3: 变异类型路由 | **≤0.37** | **否** (所有 bootstrap 95% CI 含 0) | 4B 对等时有微小增益；8B CLS 全面碾压 CWM 时增益归零 |

**Oracle gap 参考**：2.0–4.0pp（best single → oracle ensemble），但互补性来自实例级多样化错误模式，非系统性可观测特征。

报告已注册：`artifacts/routing_analysis_report.md`，分析脚本：`routing_analysis.py`。

---

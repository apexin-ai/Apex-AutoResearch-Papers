# research data exploration

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_data-exploration_20260514T042336_result.json`
- **Structured JSON:** [`b4b5d20ef3c49df743da.json`](../../sessions/b4/b4b5d20ef3c49df743da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。报告已写入 `artifacts/debugbench_analysis.md`（157 行）。

关键结论：
- 数据集名称是 `Rtian/DebugBench`，仅有 test split，共 4,253 条
- Python 子集 1,414 条（语言标签是 `python3`）
- **51.7% 是 multiple error**（包含 2-4 个 bug），单 bug 样本仅 683 条
- 没有可执行的 test cases，`examples` 只是文本描述的输入输出样例
- 代码平均长度 ~656 字符，bug 解释平均 81 字符

---

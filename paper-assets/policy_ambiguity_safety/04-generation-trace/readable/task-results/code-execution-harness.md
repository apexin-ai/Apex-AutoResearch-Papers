# code execution harness

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_execution_harness_20260520T073746_result.json`
- **Structured JSON:** [`e2be45a5093cf1dfd8bd.json`](../../sessions/e2/e2be45a5093cf1dfd8bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出汇总：

| 文件 | 功能 |
|------|------|
| `config.py` | 模型定义、τ²-bench 格式 prompt 模板、violation 分级、统计阈值 |
| `harness.py` | Agent 执行框架：加载 clauses → 注入 policy 到 `&lt;policy>` XML → 调 Anthropic/OpenAI API → asyncio 并发 → JSONL 输出 + 断点续跑 |
| `judge.py` | LLM-as-Judge：用 unambiguous 版作 ground truth 评估 trajectory，输出 4 级 violation，内置 scopal 偏差检查 |
| `analyze.py` | 双轨统计：主分析 χ²/Fisher/Cramér's V 跨类型比较 + 辅助分析 McNemar/Wilcoxon 配对检验 → 自动 PASS/FAIL |
| `requirements.txt` | anthropic, openai, scipy, pandas, numpy |
| `README.md` | 三模块完整用法 |

所有 CLI `--help` 正常，import 链无报错，6 个 artifact 已注册。下一步需要 `clauses.json`（180 条策略条款的 matched pairs）才能实际运行。

---

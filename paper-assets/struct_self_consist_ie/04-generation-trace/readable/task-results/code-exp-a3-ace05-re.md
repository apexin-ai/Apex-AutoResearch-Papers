# code exp a3 ace05 re

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_a3_ace05_re_20260520T181651_result.json`
- **Structured JSON:** [`aa451fff1d86dfe6a605.json`](../../sessions/aa/aa451fff1d86dfe6a605.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。交付物汇总：

**数据决策**: ACE05 因 LDC 限制不可用，改用 **SciERC test split**（公开、已集成、与 NER 实验共享数据源便于 cross-task 对比）。

**4 个文件已创建**（均在 `artifacts/experiments/ace05_re/`）:

| 文件 | 内容 |
|------|------|
| `spec.md` | 实验 spec：SciERC RE 数据、prompt template、UIE JSON schema、F1-F4 failure mode 定义、pipeline 复用分析 |
| `prepare_re_data.py` | 数据准备：加载 SciERC → 过滤有 relation 的实例 → 构建 few-shot prompt → 输出 JSONL |
| `run_re_sc.py` | 推理+评估框架：VLLMSampler 采样、`consensus_construct_re()` LP 加权聚合、`is_degenerate_re()`、F1-F4 分类、paired bootstrap |
| `report.md` | 产出报告：数据可用性、推荐数据集、pipeline 复用率 85%、无 blocker |

**Registry**: `exp_a3_ace05_re` 已注册为 QUEUED，3 个 artifact 已注册。

Pipeline 复用率 ~85%——`sampling.py`、`consistency.py`、`evaluation.py` 中的 RE 支持已全部就位，仅 consensus construction 和 degeneracy detection 需要从 entity key 改为 relation key（已在 `run_re_sc.py` 中实现）。

---

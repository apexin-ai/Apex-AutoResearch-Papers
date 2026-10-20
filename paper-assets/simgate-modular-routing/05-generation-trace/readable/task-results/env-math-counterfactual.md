# env math counterfactual

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_env_math-counterfactual_20260514T132719_result.json`
- **Structured JSON:** [`f7e8a54ff4a02cb70466.json`](../../sessions/f7/f7e8a54ff4a02cb70466.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## MATH 环境搭建 + Counterfactual Dryrun 结果

**已完成的工作**：
1. **数据集**：从 `DigitalLearningGmbH/MATH-lighteval` 下载 MATH test set（原 `hendrycks/competition_math` 已被 HF 禁用），筛选 Level 4-5 共 **2538 题**，保存于 `data/math-raw`
2. **代码**：`src/math_counterfactual.py`、`src/code_sandbox.py`、`src/math_answer_utils.py` 均已就绪（之前已存在）
3. **依赖**：datasets 4.8.4, sympy 1.14.0, vllm 0.18.1 均已安装

**Dry-run 结果（10 题）**：

| 指标 | 值 |
|------|-----|
| Internal acc | 5/10 (50%) |
| CodeInterp acc | 7/10 (70%) |
| det-preferred | 3 |
| internal-preferred | 1 |
| no-preference | 6 |
| 平均速度 | 15.8s/题 |

**值得注意**：10 题中只有 3 题的 code interpreter 路径实际执行了代码（1 轮），其余 7 题 LLM 在 code interpreter prompt 下仍然用纯推理解题。这意味着当前的 label 信号更多来自 prompt 差异而非代码执行本身。后续全量跑时可能需要更强的 prompt 引导 LLM 写代码，或对"0 code rounds"的 deterministic 轨迹做特殊处理。

---

# infra math counterfactual

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_math-counterfactual_20260514T132142_result.json`
- **Structured JSON:** [`5b1a257b4195f4b44b18.json`](../../sessions/5b/5b1a257b4195f4b44b18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

**MATH Counterfactual Labeling 基础设施 — Dry-run 完成**

**服务器**: westb-13313, RTX 5090 cuda:0, vLLM 0.18.1
**模型**: Qwen2.5-7B-Instruct

**部署文件**:
- `src/code_sandbox.py` — Python 代码执行沙箱
- `src/math_answer_utils.py` — 答案提取 + sympy 符号比较
- `src/math_counterfactual.py` — 主 pipeline（vLLM 推理 + ReAct code interpreter）

**数据集**: 2538 题 Level 4-5（7 个科目），保存在 `data/math-raw/`

**Dry-run 结果 (10 题)**:

| 指标 | 值 |
|------|-----|
| Internal accuracy | 50% (5/10) |
| Code Interpreter accuracy | 70% (7/10) |
| det-preferred | 3 (30%) |
| internal-preferred | 1 (10%) |
| no-preference | 6 (60%) |
| 每题耗时 | 15.8s |
| 每条 trajectory tokens | ~690 |

**信号有效**：Code Interpreter 比 Internal 高 20%，30% 的题目产出 det-preferred label。

**全量跑估算**: 2538 题 × 15.8s ≈ 11 小时。如果取 400 题子集 ≈ 1.75 小时。

等待指令启动全量/子集运行。

---

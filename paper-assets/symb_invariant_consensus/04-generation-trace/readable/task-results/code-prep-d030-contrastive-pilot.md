# code prep d030 contrastive pilot

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-d030-contrastive-pilot_20260517T061757_result.json`
- **Structured JSON:** [`60ce8f528036f6313598.json`](../../sessions/60/60ce8f528036f6313598.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完全通过，pipeline 逻辑无报错。

## 产出

**脚本**: `/root/symb_invariant_consensus/scripts/pilot_contrastive_constraints.py`

- `--help` 正常
- `--dry-run` 完整跑通（mock 数据显示 discriminative ratio 76.0% vs baseline 11.5%）
- 真实运行需 vLLM 加载 Qwen2.5-14B 后执行（不带 `--dry-run`）

## Contrastive Prompt 设计思路

核心变化：将约束提取从 **answer-agnostic**（"从 trace 提取所有逻辑约束"）改为 **answer-conditioned**（"提取支持/反对特定答案的约束"）。

Prompt 接收三个额外输入：trace 的结论答案、问题全文、所有候选答案列表。输出每条约束标记 `category`：
- `supports`: 支持该 trace 答案的证据
- `contradicts`: 反对某个替代答案的证据  
- `neutral`: 与答案无关的领域事实

评分策略两种：
- V1: 直接累加 supports (+1) 和 contradicts (-0.5) 的 raw count
- V2: 按 trace 级频率加权（多少条 trace 产生了相同方向的支持/反对）

---

# diagnose plan006 prolog data

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan006-prolog-data_20260514T095035_result.json`
- **Structured JSON:** [`a0285b97958229eada78.json`](../../sessions/a0/a0285b97958229eada78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功。报告如下：

---

**结论：不存在 Prolog 训练数据缺失问题。`data/prolog/train_500_seed42.jsonl` 不需要创建。**

**验证结果：**
- `data/train_500_seed42.jsonl` 存在（500 条，字段：id, context, question, answer, fol_premises, fol_conclusion, depth）
- 两个 Prolog config（`grpo_prolog_exec_only.yaml`, `grpo_prolog_exec_sta.yaml`）均指向 `data_path: data/train_500_seed42.jsonl`
- `build_prolog_dataset()` 仅使用 `context`/`question` 字段构造 Prolog prompt，**不需要 `prolog_premises`/`prolog_query` 字段**
- Dry-run 通过：成功从 FOL 数据构建了 500 条 Prolog dataset
- GRPO reward function 传入 `{}` 作为 ground truth，仅评估模型生成的 Prolog 代码是否可执行 + STA ablation

**架构设计：** Prolog 实验与 FOL 实验使用**同一份自然语言数据**，区别在于 prompt（要求模型生成 Prolog 而非 FOL）和 reward function（用 swipl 而非 Prover9 执行）。

**eval_sta.py Prolog 支持：** 已实现（与 readiness report 旧记录不符）——`--logic_type prolog` 已可用。

**实际阻塞项：** GPU 可用性，非数据问题。

---

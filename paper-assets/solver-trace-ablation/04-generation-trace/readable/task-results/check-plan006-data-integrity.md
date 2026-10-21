# check plan006 data integrity

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_plan006-data-integrity_20260514T111210_result.json`
- **Structured JSON:** [`fbff48705ac4fa3b9485.json`](../../sessions/fb/fbff48705ac4fa3b9485.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果清晰，报告如下：

---

## 数据完整性检查报告

### 1. `data/train_500_seed42.jsonl` 格式

**确定是 FOL 数据，不是 Prolog。**

每条数据包含 `fol_premises`（如 `∀x (... → ...)`）和 `fol_conclusion` 字段，使用一阶逻辑符号（`∀`, `∃`, `∧`, `→`, `¬`）。没有任何 Prolog 语法（`:-`, `?-` 等）。示例 id 前缀为 `folio_`。

### 2. `configs/grpo_prolog_exec_only.yaml` 配置

| 字段 | 值 |
|------|-----|
| `logic_type` | `prolog` |
| `solver` | `prolog` |
| `data_path` | `data/train_500_seed42.jsonl` |
| `reward_mode` | `execution_only` |

配置声称用 Prolog solver，但数据指向的是 FOL 数据文件。

### 3. 与 plan001 FOL config (`grpo_exec_only.yaml`) 对比

| 字段 | plan001 FOL | plan006 "Prolog" |
|------|-------------|------------------|
| `data_path` | `data/train_500_seed42.jsonl` | `data/train_500_seed42.jsonl` |
| `solver` | `prover9` | `prolog` |
| 其余参数 | 相同 | 相同（除 num_steps 500 vs 100） |

**两个实验用的是完全相同的训练数据。**

### 4. `data/` 目录

**没有 `prolog/` 子目录，没有任何 Prolog 格式的数据文件。** 目录下全部是 FOL 数据（`folio_` 前缀、FOL 符号格式）。

---

## 结论

**plan006-prolog-exec-s42 本质上是用 FOL 数据 + Prolog solver 配置在跑。** 它不是真正的 Prolog 实验——因为根本不存在 Prolog 格式的训练数据。它和 plan001 唯一的区别是 `solver: prolog`（vs `prover9`）和 `num_steps: 500`（vs 100）。

这意味着：
- 模型看到的 prompt 中是 FOL 符号，生成的大概率也是 FOL 风格的推理
- Prolog solver 接收 FOL 格式的输入，要么全部执行失败（reward=0），要么有某种格式转换层
- **这不是一个有效的 Prolog 实验**，更像是"用错误的 solver 跑 FOL 数据"

---

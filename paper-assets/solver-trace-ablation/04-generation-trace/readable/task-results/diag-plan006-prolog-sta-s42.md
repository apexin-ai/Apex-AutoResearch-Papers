# diag plan006 prolog sta s42

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_plan006-prolog-sta-s42_20260514T094801_result.json`
- **Structured JSON:** [`2cee538b43dda90b8449.json`](../../sessions/2c/2cee538b43dda90b8449.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 结论

**根因**：命令行 `--data_path data/prolog/train_500_seed42.jsonl` 路径错误。`data/prolog/` 目录不存在。

实际数据文件在 `data/train_500_seed42.jsonl`（无 `prolog/` 子目录），两个 YAML 配置里也都正确写的 `data_path: data/train_500_seed42.jsonl`。是提交命令时 `--data_path` 覆盖了配置中的正确路径。

**两个实验都失败了**：
- plan006-prolog-exec-s42 — 同样在 17:45:32 因 `FileNotFoundError` 崩溃，并非 RUNNING
- plan006-prolog-sta-s42 — 17:45:35 同样报错

**配置对比**（两个 YAML 仅以下字段不同）：
| 字段 | exec_only | exec_sta |
|------|-----------|----------|
| reward_mode | execution_only | execution_sta |
| exec_weight | 1.0 | 0.5 |
| sta_weight | 0.0 | 0.5 |

**不需要生成新数据**。现有 `data/train_500_seed42.jsonl` 就是正确的训练数据（符合 C001 约束），配置中 `logic_type: prolog` + `solver: prolog` 控制 solver 类型，数据集本身是通用的。

**修复方式**：重新提交时去掉 `--data_path` 参数（让配置文件的值生效），或改为 `--data_path data/train_500_seed42.jsonl`。两个实验都需要重新提交。

---

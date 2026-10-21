# code d012 code changes

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d012-code-changes_20260514T024902_result.json`
- **Structured JSON:** [`06f942292ef53255a79b.json`](../../sessions/06/06f942292ef53255a79b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过，`additive_random` 已在 `--reward_mode` choices 中。

## 汇总

### 修改的文件

**`scripts/train_grpo.py`** — 3 处修改：
| 行号 | 修改 | 说明 |
|------|------|------|
| L174 | `_fast_fn` → `_full_fn` | `random_reward` 模式统一用 full STA |
| L199 | `sta_weight=0.0` → `sta_weight=1.0` | `additive_random` 模式计算 ISR 作为监控指标 |
| L205 | `random_bonus` → `random_reward` | 日志字段名统一 |

**`configs/grpo_exec_only.yaml`、`grpo_exec_sta.yaml`、`grpo_random_reward.yaml`** — `data_path` 从 `proofwriter_fol_500.jsonl` 改为 `data/train_500_seed42.jsonl`（符合 C001 约束）。

**`configs/grpo_additive_random.yaml`** — 已存在且配置正确，无需修改。

**未改动**：`grpo_prolog_*.yaml`（使用 prolog 数据集，不在修改范围内）。

---

# prep prolog s43 s44 data

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_prolog-s43-s44-data_20260514T115630_result.json`
- **Structured JSON:** [`052b581df9019e9942cf.json`](../../sessions/05/052b581df9019e9942cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。汇总如下：

## 数据状态

**训练数据**: `data/train_500_seed42.jsonl` (484,867 bytes) — 所有 Prolog 实验共用同一份，符合 C001 约束。数据包含 FOL premises + conclusions 的 ProofWriter 问题，与 solver 类型（Prolog/Z3）无关。

**seed 含义**: config 中 `seed: 42` 是模型训练随机种子，不影响数据选择。s43/s44 只需改 `seed` 字段即可。

## Config 差异

| 配置 | reward_mode | exec_weight | sta_weight | 关键区别 |
|------|------------|-------------|-----------|---------|
| `grpo_prolog_exec_only.yaml` | execution_only | 1.0 | 0.0 | exec-only |
| `grpo_prolog_exec_sta.yaml` | execution_sta | 0.5 | 0.5 | exec+STA |

两者其余配置完全相同（model_path, data_path, batch_size, lr, steps 等）。

## 4 个 PREPARING 实验需要的配置

| 实验 | 基础 config | 需改的字段 | data_path |
|------|-----------|-----------|-----------|
| plan006-prolog-exec-s43 | `grpo_prolog_exec_only.yaml` | `seed: 43`, output_dir 改名 | `data/train_500_seed42.jsonl` (不变) |
| plan006-prolog-exec-s44 | `grpo_prolog_exec_only.yaml` | `seed: 44`, output_dir 改名 | `data/train_500_seed42.jsonl` (不变) |
| plan006-prolog-sta-s43 | `grpo_prolog_exec_sta.yaml` | `seed: 43`, output_dir 改名 | `data/train_500_seed42.jsonl` (不变) |
| plan006-prolog-sta-s44 | `grpo_prolog_exec_sta.yaml` | `seed: 44`, output_dir 改名 | `data/train_500_seed42.jsonl` (不变) |

## 环境确认

- SWI-Prolog: v8.4.2 可用
- 数据文件: 已存在，无需生成
- 模型: `/root/autodl-tmp/models/Qwen3-4B` (s42 已用过)

**结论**: 4 个实验的训练数据已就绪，无需额外数据生成。只需基于现有 config 复制并修改 `seed` 和 `output_dir` 即可启动。

---

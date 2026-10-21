# code plan002 additive bonus reward

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan002-additive-bonus-reward_20260514T020631_result.json`
- **Structured JSON:** [`8462e91d7aa539bf8732.json`](../../sessions/84/8462e91d7aa539bf8732.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。代码和配置已到位，汇总：

**`scripts/train_grpo.py` 已有改动：**
- `make_reward_fn` 签名新增 `beta: float = 0.3`
- `additive_bonus` 分支实现 `r = r_exec * (1 + β·ISR)` (line 187-195)
- `--beta` CLI 参数 (line 312-313)
- `--reward_mode` choices 包含 `additive_bonus`
- `beta` 传入 `make_reward_fn` (line 384)
- `save_total_limit=1` (C003 合规)

**`configs/grpo_additive_bonus.yaml`：**
- `reward_mode: additive_bonus`, `beta: 0.3`
- `data_path: data/train_500_seed42.jsonl` (C001 合规)
- `output_dir: /root/autodl-tmp/outputs/plan002_additive_beta03_s42` (已修正)
- `no_wandb: true`, `seed: 42`

**Dry-run 验证通过：** 语法检查 OK，`--help` 确认 `--beta` 和 `additive_bonus` 模式均被识别。

---

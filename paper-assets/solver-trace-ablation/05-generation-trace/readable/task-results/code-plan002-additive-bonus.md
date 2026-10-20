# code plan002 additive bonus

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan002-additive-bonus_20260514T020603_result.json`
- **Structured JSON:** [`90607b5478cacfd682d3.json`](../../sessions/90/90607b5478cacfd682d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改已验证通过。总结：

**`scripts/train_grpo.py` 修改：**
- **L148**: `make_reward_fn` 签名增加 `beta: float = 0.3` 参数
- **L187-195**: 新增 `additive_bonus` 模式 — `r = r_exec * (1 + beta * ISR)`，调用 `_full_fn` 时 `sta_weight=1.0` 确保 ISR 被计算
- **L302**: `--reward_mode` choices 增加 `"additive_bonus"`
- **L312-313**: 新增 `--beta` CLI 参数（默认 0.3）
- **L384**: `main()` 中传递 `beta` 到 `make_reward_fn`
- `save_total_limit` 从 2 改为 1（C003）

**新建 `configs/grpo_additive_bonus.yaml`：**
- `reward_mode: additive_bonus`, `beta: 0.3`
- `data_path: data/train_500_seed42.jsonl`（C001）
- `output_dir: /root/autodl-tmp/outputs/grpo_additive_bonus_b03`
- 其他参数与 plan005 一致（500 steps, K=8, lr=1e-6）
- `no_wandb: true`

Dry-run `--help` 通过，argparse 正确识别所有新参数。GPU 空出后可直接提交。

---

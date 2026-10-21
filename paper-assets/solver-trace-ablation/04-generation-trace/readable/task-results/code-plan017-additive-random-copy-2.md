# code plan017 additive random

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan017-additive-random_20260514T030802_result.json`
- **Structured JSON:** [`fa96b52a6e66dd27b5bb.json`](../../sessions/fa/fa96b52a6e66dd27b5bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`--help` 正常输出，`additive_random` 已在 reward_mode choices 中。

**结论：plan017 additive random control 的配置和代码已全部就绪，无需修改。**

- `configs/grpo_additive_random.yaml` — 参数与 plan002 对齐，reward_mode 为 `additive_random`
- `train_grpo.py` — `additive_random` 分支实现 `r = r_exec * (1 + β * random())`，记录 `random_reward`
- `argparse` choices 已包含 `additive_random`
- dry-run `--help` 通过

启动训练时需要 `export CUDA_VISIBLE_DEVICES=N` 显式指定空闲 GPU（遵守 C002），当前两张卡都在用，等有空闲 GPU 后再启动。

---

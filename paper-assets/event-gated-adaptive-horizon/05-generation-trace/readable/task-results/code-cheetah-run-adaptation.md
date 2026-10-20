# code cheetah run adaptation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cheetah_run_adaptation_20260514T063251_result.json`
- **Structured JSON:** [`6e7190983451a6f88f6a.json`](../../sessions/6e/6e7190983451a6f88f6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出汇总

**(a) Task name 格式**: `dmc_cheetah_run`
- `dreamer.py:149` 做 `config.task.split("_", 1)` → suite=`dmc`, task=`cheetah_run`
- `envs/dmc.py:9` 做 `name.split("_", 1)` → domain=`cheetah`, task=`run`
- 与 Walker Walk (`dmc_walker_walk`) 完全一致的命名规则

**(b) Dry-run 结果**: 通过
- Action space: `Box(-1, 1, (6,))` — cheetah 有 6 个关节动作
- Obs keys: `position`, `velocity`, `image`, `is_terminal`, `is_first`
- 3 步 step 均正常返回 reward (0.008, 0.048, 0.072)
- 使用 `--configs dmc_proprio`（proprio obs，和 Walker Walk baseline 相同）

**(c) 额外依赖**: 不需要。Cheetah Run 在 dm_control suite 内，与 Walker Walk 共用同一套依赖，已全部安装。

**(d) 脚本文件**: `/root/autodl-tmp/event-gated-adaptive-horizon/scripts/cheetah_run_experiments.sh`
- 3 组实验 × 3 seeds = 9 条命令
- Baseline: 512K steps，008d/008f: 105K steps
- Device 留 `cuda:X` 占位符，命令默认注释

---

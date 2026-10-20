# ops 016e finalize and cheetah prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_016e-finalize-and-cheetah-prep_20260515T222419_result.json`
- **Structured JSON:** [`b64b4100219560e47b1c.json`](../../sessions/b6/b64b4100219560e47b1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 016e 状态
- 进程: **ALIVE** (PID 527392, GPU 1, 3259 MiB)
- 当前 step: **96000** (train_return=100.7)
- eval_return 轨迹:
  - 5K: 31.0 → 15K: 140.3 → 25K: 141.8 → 35K: 173.0 → 45K: 184.0
  - 55K: 153.8 → 65K: **324.3** → 75K: **326.7** (peak)
  - 85K: 256.2 → 95K: **31.7** (崩溃)
- exit_code: 未生成（仍在跑）
- 最后 eval 在 95K，下次 eval 在 105K（即终点）。按指示不 kill，让它跑完。

## 009d 状态
- 进程: **ALIVE** (PID 149708, GPU 0, 4156 MiB)
- 当前 step: **228000** (fps=7.3)
- 最近 eval_return:
  - 188K: 511.0 → 198K: 558.7 → 208K: 591.3 → 218K: 638.2 → 228K: **692.1**
- 趋势持续上升，表现很好。

## GPU 状态
- GPU 0: 4165 MiB, 0% util — 009d 占用（可能在 eval 间隔，瞬时低）
- GPU 1: 3278 MiB, 36% util — 016e 占用
- **两张 GPU 都被占用，Cheetah 无空闲 GPU。** 需等 016e 跑完（~105K，距离约 9K steps）释放 GPU 1。

## Cheetah 准备
- logdir 状态: 已有 `cheetah_dryrun_200step/`（dry run 成功，5K step 有数据）
- task 名: `dmc_cheetah_run`（configs 中用 `--task dmc_cheetah_run --configs defaults dmc_proprio`）
- 实验脚本: `scripts/cheetah_run_experiments.sh` 和 `scripts/submit_plan020_cheetah_baseline.sh` 已就绪
  - 010a: baseline, 512K steps, 3 seeds
  - 010b: trained_dt2, 105K steps, 3 seeds
  - 010c: no_embed_dt2, 105K steps, 3 seeds
- 代码版本: git 命令被 read_only 阻止，无法查看

---

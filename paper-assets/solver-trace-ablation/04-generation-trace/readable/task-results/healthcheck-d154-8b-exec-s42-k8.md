# healthcheck d154 8b exec s42 k8

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_healthcheck_d154-8b-exec-s42-k8_20260522T055920_result.json`
- **Structured JSON:** [`d79cd2538f0c5d69276f.json`](../../sessions/d7/d79cd2538f0c5d69276f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Part 1: 健康度报告

| 指标 | 值 |
|------|-----|
| GPU | RTX PRO 6000 Black, 54055/97887 MiB |
| GPU Util | 0%（快照时处于 generation 阶段，正常） |
| 进程 | PID 969681 存活 |
| 当前步数 | **363/500**（72%） |
| Step 速度 | ~9-15s/it |
| 预估剩余 | ~25-30 min |
| Reward 趋势 | 波动较大（349→0.44, 350-353→0.0, 358→0.44, 360→0.88），GRPO 正常 pattern |

**结论：训练健康，正常推进。** GPU util 0% 是 K=8 autoregressive generation 阶段的正常现象——generation 是 sequential decoding，nvidia-smi 快照恰好抓到这个阶段。

## Part 2: 配置文件已创建

**`grpo_exec_only_8b_k8_s43.yaml`** — 与 s42 完全相同，仅改：
- `seed: 43`
- `output_dir: .../8b_exec_only_s43_k8/`
- `wandb_run: 8b_exec_only_s43_k8`

**`grpo_isr_8b_k8_s42.yaml`** — 基于 s42 exec 配置，改动：
- `reward_mode: additive_bonus`（r = r_exec + β × ISR）
- `beta: 0.1`
- 移除 `exec_weight/sta_weight`（additive_bonus 模式由 beta 控制）
- `output_dir: .../8b_isr_b01_s42_k8/`
- 其余参数（K=8, 500 steps, lr, batch size）与 exec s42 一致

注意：参考了已有的 `grpo_isr_b01_8b.yaml`（K=4 版本），新配置升级到 K=8 并加了 `save_total_limit: 1`（遵守 C003）。

---

# ops westd eval v3 careful launch

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_eval_v3_careful_launch_20260522T093404_result.json`
- **Structured JSON:** [`c32eea1cf2ade4cfaa1b.json`](../../sessions/c3/c32eea1cf2ade4cfaa1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westd-47453 上已经有 3 个 OOD eval 在运行中**，它们是 ~3 分钟前启动的（17:32-17:33），正在初始化阶段：

| # | 日志文件 | GPU | 模型 | W&B run | 状态 |
|---|---------|-----|------|---------|------|
| 1 | `ragen_sft_ood_eval_restart.log` | 0 | SFT baseline (`qwen3_exp021_ragen_sft_v4`) | `9dgcusr8` | WorkerDict 已加载 8.1GB，模型初始化中 |
| 2 | `ragen_seed8_ood_eval_v2.log` | 1 | seed8-step5 (`qwen_exp029_seed8_step5_hf`) | `iayaluzg` | WorkerDict 已加载 8.1GB，模型初始化中 |
| 3 | `ragen_intervention_c_ood_eval_v2.log` | 3 | intervention_c (`qwen_intervention_c_hard_cap_step5_hf`) | 新 run | Ray 刚启动，模型未加载 |

你要求的 **SFT baseline (GPU 0)** 和 **seed8 (GPU 1)** 已经在跑了。GPU 2 上也有一个 WorkerDict 进程（8.1GB）。

**不需要再启动新 eval**——继续启动会跟现有进程冲突。

要我等几分钟后检查这 3 个 eval 是否成功进入推理阶段（GPU 显存应该涨到 50+GB），还是你认为这些是之前失败的残留进程需要清理？

---

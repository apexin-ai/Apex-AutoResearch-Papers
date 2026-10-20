# ops server status and collect

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-status-and-collect_20260516T102807_result.json`
- **Structured JSON:** [`8dbf2749674108bbf29d.json`](../../sessions/8d/8dbf2749674108bbf29d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

llama31-vanilla-s0 已更新为 DONE。汇总如下：

---

## GPU 状态

| GPU | 显存占用 | 利用率 | 当前任务 |
|-----|---------|-------|---------|
| cuda:0 | 16.8/32.6 GiB | 92% | llama31-vanilla-s0 **eval** (injected_eval.py) |
| cuda:1 | 27.1/32.6 GiB | 99% | **llama31-taxei-s0** 训练 (已重启，7% = 255/3387) |
| cuda:2 | 26.0/32.6 GiB | 100% | **llama31-random-s0** 训练 (56% = 1914/3387) |
| cuda:3 | 0/32.6 GiB | 0% | **空闲** |

---

## llama31-vanilla-s0（训练已完成，eval 正在跑）

| 指标 | 值 |
|------|------|
| train_loss | 0.3984 |
| token_acc | 0.9089 |
| train_steps | 1635/1635 |
| train_duration | 69.3 min (4159s) |
| speed | 2.543 s/it |
| memory | 30.28 GiB |
| EXIT_CODE | 0 |
| checkpoint | `/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635` |

Eval 正在 GPU 0 上运行，输出到 `eval_results/llama31_vanilla_s0.json`。

**Registry 已更新**: status=DONE, conclusion=success, metrics 已填入。

---

## llama31-random-s0（训练中）

- 进度：**56%** (1914/3387 steps)，已跑 1h11m，预计剩余 ~56min
- 当前 loss: ~0.31，token_acc: ~0.89
- GPU 2，30.74 GiB

---

## llama31-taxei-s0（已重启，训练中）

- 前一次以 **EXIT_CODE=129 (SIGHUP)** 失败
- 已被重新提交，当前进度：**7%** (255/3387)，已跑 ~9min
- 预计总时长 ~2h
- GPU 1

---

## TaxEI-RP s7 eval（已完成）

文件：`v4_taxei_rp_recovery_eval_s7.json`，registry 中已注册为 `eval-rp-s7`。

| 指标 | 值 |
|------|------|
| recovery_rate | **0.596** (28/47) |
| detection_rate | 0.0 |
| C1_context_truncation | 0.667 |
| C4_observation_masking | 0.545 |
| P1_step_order_swap | 0.667 |
| P2_sub_goal_deletion | 0.500 |

---

## Recovery eval 结果文件

eval_results 目录中存在以下 recovery 相关文件：
- `v4_taxei_recovery_eval.json`, `v4_taxei_recovery_eval_r2.json`
- `v4_taxei_recovery_eval_s0.json`, `v4_taxei_recovery_eval_s1.json`, `v4_taxei_recovery_eval_s123.json`
- `v4_taxei_rp_recovery_eval_s7.json`
- `v4_vanilla_recovery_eval.json`, `v4_vanilla_recovery_eval_s0/s1/s123/s7.json`
- `v4_random_recovery_eval.json`

---

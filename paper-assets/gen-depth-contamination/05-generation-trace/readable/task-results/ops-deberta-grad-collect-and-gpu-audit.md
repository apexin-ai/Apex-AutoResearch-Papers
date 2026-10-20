# ops deberta grad collect and gpu audit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deberta_grad_collect_and_gpu_audit_20260520T200359_result.json`
- **Structured JSON:** [`1f946b68c78383385922.json`](../../sessions/1f/1f946b68c78383385922.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完毕。

---

## 优先级 1：deberta_graduated 结果 ✅ 已完成

`eval_results.json` 已存在，提取得分：

| Strategy | MMLU | HellaSwag (acc_norm) | ARC-C (acc_norm) |
|---|---|---|---|
| no_filter | 0.5895 | 0.6591 | 0.4352 |
| obd_binary | 0.5880 | 0.6599 | 0.4522 |
| deberta_binary | 0.5870 | 0.6593 | 0.4471 |
| **deberta_graduated** | **0.5884** | **0.6586** | **0.4420** |

4/4 策略完整。各策略差异很小（MMLU ±0.25pp, HellaSwag ±0.13pp, ARC-C ±1.7pp）。obd_binary 在 ARC-C 上最优（0.4522），no_filter 在 MMLU 上最优（0.5895）。

---

## 优先级 2：expanded_downstream_eval

**当前进度**：graduated_seed1 刚完成，正在训练 **no_filter_seed2**（507/1875 steps, 27%）。已完成 6/9 runs（seed0 全部 + seed1 全部），剩余 seed2 的 3 个策略。

**graduated_seed1 刚出的分数**：piqa=0.7508, truthfulqa=0.4234, winogrande=0.6440, arc_c=0.5230, gsm8k=0.5618

**脚本不支持单独指定 strategy**。参数仅有 `--device`, `--num_seeds`, `--seed_start`, `--skip_base`。无法按 strategy 拆分到多张卡并行。要实现并行需改脚本加 `--strategy` 参数。

**sweep_r10_nofilter 已失败**（exit code 1）：`ConnectionError: Couldn't reach 'allenai/ai2_arc' on the Hub (OfflineModeIsEnabled)`。需要加 `HF_ENDPOINT` 和网络代理环境变量后重跑。

---

## 优先级 3：GPU 状态

| GPU | 型号 | 利用率 | 显存 | 当前任务 |
|---|---|---|---|---|
| 0 | RTX 4090 D | 81% | 11091/24564 MiB | exp_expanded_downstream_eval (seed2 训练中) |
| 1 | RTX 4090 D | 0% | 0 MiB | **空闲**（sweep_r10_nofilter 已失败退出） |
| 2 | RTX 4090 D | 0% | 0 MiB | **空闲** |
| 3 | RTX 4090 D | 0% | 0 MiB | **空闲** |

tmux 活跃会话：`exp_expanded_downstream_eval`

**3 张卡空闲**。expanded_eval 脚本无法拆分策略并行，sweep_r10_nofilter 需要修复网络配置后重新提交。

---

# ssh urgent 41312 nvidia smi check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_41312_nvidia_smi_check_20260517T184007_result.json`
- **Structured JSON:** [`e1fd4814d236771b557c.json`](../../sessions/e1/e1fd4814d236771b557c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告 — westd-41312

### GPU 占用

| GPU | PID | 任务 | 显存 | GPU利用率 | 温度 |
|-----|------|------|------|-----------|------|
| cuda:0 | **125995** (uniform_v2) | `qwen06b_uniform_seed42_v2` | 46,530 / 97,887 MiB | 99% | 63°C |
| cuda:1 | **115525** (ess_only_456) | `ess_only_seed456` | 75,014 / 97,887 MiB | 100% | 62°C |
| cuda:2 | **115021** (ess_only_123) | `ess_only_seed123` | 75,014 / 97,887 MiB | 100% | 62°C |
| cuda:3 | **125367** (random_reweight_456) | `random_reweight_seed456` | 75,014 / 97,887 MiB | 100% | 72°C |

**4 个目标 PID 全部存活，4 张卡满载运行。**

### 训练进度

| 任务 | 进度 | 已用时间 | 预计剩余 | 速度 |
|------|------|----------|----------|------|
| **uniform_v2** (PID 125995) | **659/6103 (11%)** | ~23min | ~3h11m | 2.11 s/it |
| **ess_only_seed456** (PID 115525) | **1565/6103 (26%)** | ~3h07m | ~2h40m | 2.12 s/it |
| **ess_only_seed123** (PID 115021) | **1648/6103 (27%)** | ~3h09m | ~2h36m | 2.11 s/it |
| **random_reweight_seed456** (PID 125367) | **1533/8477 (18%)** | ~7m55s | ~35m | 3.22 it/s |

### 备注
- uniform_v2 和 random_reweight_456 是较晚启动的（今天 02:14-02:17），进度较低
- ess_only_123 和 ess_only_456 从昨天 May17 启动，已跑约 3 小时，进度约 26-27%
- random_reweight_456 速度明显更快（3.2 it/s vs 其他 ~0.47 it/s），总步数也更多(8477)，显存占用却一样，可能配置不同（无 eval_data_path、不同 output_dir 到 autodl-tmp）
- uniform_v2 显存只用 46.5G（其他三个 75G），因为没有 `--eval_data_path` 参数
- tmux 命令被 read-only 模式阻止，但从 ps 输出看到有一个 tmux session: `grid_b0_2_seed42`

---

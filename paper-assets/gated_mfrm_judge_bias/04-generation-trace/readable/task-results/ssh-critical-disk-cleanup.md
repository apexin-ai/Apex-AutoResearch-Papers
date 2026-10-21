# ssh critical disk cleanup

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_critical_disk_cleanup_20260524T060228_result.json`
- **Structured JSON:** [`9452fcf5e6fe47b6a4fc.json`](../../sessions/94/9452fcf5e6fe47b6a4fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp017 是 JAX/NumPyro MCMC 模拟，不加载 LLM 模型文件。

**当前状态汇报：**

### 已清理
| 项目 | 大小 | 说明 |
|------|------|------|
| pip cache | 4.1G | 在根分区，未释放数据盘空间 |
| conda pkgs | 0.5G | 同上 |
| /tmp 日志 | ~30M | 已删 |
| .pyc / __pycache__ / .lock | 微量 | 已删 |
| 4个 snapshot_download 进程 | - | 已 kill |

**数据盘空间未变：17G 可用，目标 >30G，缺口 13G+。**

### 数据盘可清理候选

| 候选 | 大小 | 风险 |
|------|------|------|
| `gemma-2-9b-it/` | 18G | 低 - 无 GPU 进程在用 |
| `Llama-3.1-8B-Instruct/` | 15G | 低 - 无 GPU 进程在用 |
| `Qwen/Qwen3-8B/` | 16G | 低 - 无 GPU 进程在用 |
| `faithfulness_under_fire/checkpoints/` | 54G | 中 - 不同项目，无 registry |
| `faithfulness_under_fire/sft_baseline/` | 6.6G | 中 - 不同项目 |

**不可删：** Llama-3.3-70B-AWQ (GPU 1 serving), Qwen2.5-72B-AWQ (GPU 2 serving), Mistral-Large-AWQ (正在下载)

### aria2c 状态
**aria2c (PID 542911) 已死。** Mistral 下载了 11/14 shards（1-10, 14），缺 11/12/13。Shard 10 有 .aria2 控制文件，可能不完整。下载完成后需手动重启。

---

删除 `gemma-2-9b-it` (18G) 即可达标 (17+18=35G >30G)。要我删哪些？

---

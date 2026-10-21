# infra plan006 next batch readiness

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan006-next-batch-readiness_20260514T112906_result.json`
- **Structured JSON:** [`763f49dde74f9765f203.json`](../../sessions/76/763f49dde74f9765f203.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan006 s43/s44 就绪状态简报

### 配置文件

| 配置 | data_path | seed | output_dir |
|------|-----------|------|------------|
| `grpo_prolog_exec_only.yaml` | `data/train_500_seed42.jsonl` ✓ | 42（需 CLI 覆盖） | `/root/autodl-tmp/outputs/grpo_prolog_exec_only`（需 CLI 覆盖） |
| `grpo_prolog_exec_sta.yaml` | `data/train_500_seed42.jsonl` ✓ | 42（需 CLI 覆盖） | `/root/autodl-tmp/outputs/grpo_prolog_exec_sta`（需 CLI 覆盖） |

两个配置的 data_path 均正确。`train_grpo.py` 支持 `--seed`、`--output_dir`、`--config` 参数，可通过命令行覆盖。

### 数据文件
- `train_500_seed42.jsonl`: 500 行 ✓，格式正确（FOL 推理题）
- `eval_sta.py`: 存在 ✓

### plan006-exec-s42 训练进度
**已完成** (EXIT_CODE=0)，500/500 steps，耗时 98 分钟。最终 reward=1.0，mean_isr=0.0954。

### 🚨 阻塞项：磁盘空间严重不足

**数据盘 250G 已用 247G，仅剩 3.5G (99%)**。每个 plan006 run 产出约 31G，完全无法启动新实验。

当前大文件占用：

| 目录 | 大小 |
|------|------|
| plan002_additive_b01_s42 | 16G |
| plan002_additive_b01_s43 | 31G |
| plan002_additive_b01_s44 | 31G |
| plan006_prolog_exec_s42 | 31G |
| plan006_prolog_sta_s42 | 31G |
| plan016_extended_1000_s42 | 31G |
| plan018_additive_random_b01_s42 | 31G |
| plan018_additive_random_b01_s43 | 15G |
| plan001_exec_only_s42 | 15G |

**需要清理至少 62G（2 个 run 的空间）才能启动 s43 的 exec + sta 实验。** 建议确认哪些已完成评估的旧 checkpoint 可以删除。

---

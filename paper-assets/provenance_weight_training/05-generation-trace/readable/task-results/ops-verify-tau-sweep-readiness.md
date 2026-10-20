# ops verify tau sweep readiness

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_tau_sweep_readiness_20260515T124015_result.json`
- **Structured JSON:** [`ea7668328f8cf1fe7a9c.json`](../../sessions/ea/ea7668328f8cf1fe7a9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

output 实际在数据盘 `/dev/md0`（250G，已用 104G，剩余 147G），空间充裕。

## 验证结果汇总

### 全部通过

| 检查项 | 状态 | 详情 |
|--------|------|------|
| 训练脚本 | ✓ | `training/pretrain_weighted.py` 存在，支持 `--tau` 参数（L251） |
| 模型文件 | ✓ | `models/Qwen/Qwen3-0.6B` 存在 |
| 数据文件 | ✓ | `data/scored_data.jsonl` = 371499 条 |
| eval 脚本 | ✓ | `eval_perplexity.py` 存在 |
| 无 `--eval_steps` | ✓ | 所有 tau 脚本均未包含 `--eval_steps` |
| `--contamination_ratio 0.4` | ✓ | 所有脚本均已显式设置 |
| τ=0.6 运行中 | ✓ | 已有 checkpoint-3500 和 checkpoint-4000（2.3GB） |
| 磁盘空间 | ✓ | 数据盘 147GB 可用，4 个实验 ~8GB 无压力 |
| 4 个待提交脚本 | ✓ | 均已存在且参数一致 |

### 各实验完整提交命令（copy-paste ready）

**τ=0.5:**
```bash
bash /root/provenance_weight_training/training/run_tau_0.5_seed42.sh
```

**τ=0.7:**
```bash
bash /root/provenance_weight_training/training/run_tau_0.7_seed42.sh
```

**τ=0.9:**
```bash
bash /root/provenance_weight_training/training/run_tau_0.9_seed42.sh
```

**τ=0.95:**
```bash
bash /root/provenance_weight_training/training/run_tau_0.95_seed42.sh
```

每个脚本内容完全一致，仅 `--tau` 和 `--output_dir` 不同。所有脚本都包含：conda activate、`WANDB_MODE=disabled`、`--weighting_method adaptive`、`--contamination_ratio 0.4`、`--save_total_limit 2`、`--bf16`。

### 风险/注意事项
- **无风险项**。4 个实验需要 4 个 GPU（或串行跑），需确认 GPU 释放后的分配策略（是否每个实验指定 `CUDA_VISIBLE_DEVICES`）。脚本中未指定 GPU，默认使用 `cuda:0`。

---

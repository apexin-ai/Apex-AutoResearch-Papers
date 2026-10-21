# code alpha eff and training

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_alpha_eff_and_training_20260513T174320_result.json`
- **Structured JSON:** [`3a5a50cb0aa8e8407c16.json`](../../sessions/3a/3a5a50cb0aa8e8407c16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件创建完成，语法和参数解析均通过验证。

**文件清单：**

| 文件 | 说明 |
|------|------|
| `weighting/__init__.py` | 包初始化 |
| `weighting/alpha_eff.py` | 5个核心函数：`compute_alpha_eff`, `compute_ess`, `find_optimal_b`, `compute_sample_weights`, `compute_concentration_bound`，附带 `__main__` 自测 |
| `training/pretrain_weighted.py` | `WeightedTrainer(Trainer)` 子类，支持 uniform/grid/adaptive 三种加权方法，batch-adaptive schedule，wandb + 本地 jsonl 日志，所有要求的 argparse 参数 |

本地环境无 torch，语法检查和 argparse 验证通过。在有 GPU 的服务器上可直接 `python alpha_eff.py` 运行自测，`python pretrain_weighted.py --data_path ... --output_dir ...` 启动训练。

---

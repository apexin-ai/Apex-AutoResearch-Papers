# ssh code mvp

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_code-mvp_20260515T165715_result.json`
- **Structured JSON:** [`0cbb6f1287590dae83ca.json`](../../sessions/0c/0cbb6f1287590dae83ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有文件已写入并验证通过。

### 产出

| 文件 | 行数 | 功能 |
|------|------|------|
| `train.py` | 151 | Continued pretraining (Accelerate 2-GPU DDP, bf16) |
| `generate_synthetic.py` | 90 | 合成文本生成 (nucleus sampling, batch=128) |
| `compute_signals.py` | 258 | Collapse 信号计算 (val_loss, entropy, spectral rank, distinct-n) |
| `run_pipeline.py` | 271 | Pipeline 编排 (数据准备→Gen0 baseline→Gen1-3 迭代) |
| `analyze_correlation.py` | 130 | Spearman 相关性分析 + 脱钩检测 |
| `accelerate_config.yaml` | 6 | Accelerate 2-GPU 配置 |
| **总计** | **1076** | |

### --help 验证
5 个 Python 文件全部语法正确、import 正常、`--help` 输出符合预期。

### 无缺包
服务器已预装所有依赖：torch 2.10+cu128, accelerate 1.13, transformers 4.57, datasets 4.8, wandb 0.26, scipy 1.17, tqdm。

### 注意事项
- 目录下有一个 `prepare_data.py` (170行) 似乎是之前残留的，不影响当前 pipeline
- 运行前需确保 wandb 已登录 (`wandb login`)
- 启动命令: `python run_pipeline.py`（默认 3 代，支持 `--start_gen` 断点续跑）

---

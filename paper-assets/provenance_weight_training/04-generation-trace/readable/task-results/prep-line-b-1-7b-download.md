# prep line b 1 7b download

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_line_b_1_7b_download_20260518T123838_result.json`
- **Structured JSON:** [`ebba6550ce379f7a374a.json`](../../sessions/eb/ebba6550ce379f7a374a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Line B 准备报告

**所有步骤已被另一个 agent 先行完成，1.7B 训练正在运行中。**

### 环境
| 项目 | 值 |
|---|---|
| 服务器 | westd-41312, 4× RTX PRO 6000 96GB |
| Python | 3.12.3 |
| PyTorch | 2.10.0+cu128 |
| Transformers | 5.8.1 |
| Accelerate | 1.13.0 |

### 模型
- **路径**: `/root/autodl-tmp/provenance_weight_training/models/Qwen/Qwen3-1.7B`
- **大小**: 3.8GB (2 safetensors shards: 3.3GB + 594MB)
- 下载完整

### 数据
- `data/scored_data.jsonl`: 371,499 行，完整

### 训练状态 (已在运行)

| 任务 | GPU | 进度 | 速度 | 显存占用 | ETA |
|---|---|---|---|---|---|
| adaptive_1_7b_seed42 | GPU 2 | 673/6103 (11%) | ~3.0 s/step | **61.7GB / 96GB** | ~4.5h |
| uniform_1_7b_seed42 | GPU 3 | 705/6103 (12%) | ~2.86 s/step | **61.7GB / 96GB** | ~4.3h |

### 训练参数 (与 0.6B 相同)
- bs=4, ga=4, max_length=2048, lr=5e-5, bf16
- 200M tokens, 6103 steps, contamination_ratio=0.4, n_min=2, tau=0.8, seed=42, save_steps=500

### 关键发现
1. **无 OOM** — 61.7GB / 96GB，留有 ~36GB 余量，当前参数完全够用
2. **训练速度**: ~3 s/step，总训练时间估计 **~5h/run**（0.6B 约 3.5h，1.7B 约 1.4x）
3. **无需调参** — 相同 bs/ga 配置在 96GB 卡上运行正常
4. GPU 0 空闲，GPU 1 在跑 GPT-2 PPL scoring

### 清理
- 已 kill 冗余的下载进程 (我启动的)
- 已删除 `/root/provenance_weight_training/models/Qwen/Qwen3-1.7B/` 下的不完整文件

---

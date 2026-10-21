# infra server check

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_server-check_20260522T032303_result.json`
- **Structured JSON:** [`857c87af52eaec58a402.json`](../../sessions/85/857c87af52eaec58a402.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-33183 服务器状态

### GPU
| 型号 | 显存 | 已用 | 利用率 |
|------|------|------|--------|
| NVIDIA RTX PRO 6000 Blackwell Server Edition | 96GB | 0 MiB | 0% |

**注意**：torch 只检测到 **1 张 GPU**（`gpus=1`），但项目约束要求使用 cuda:0-3 共 4 张卡。可能需要检查 `CUDA_VISIBLE_DEVICES` 或驱动配置。当前无 GPU 进程运行。

### 磁盘
| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| /root | 30G | 29G | 1.3G | **96%** |

**警告：根分区仅剩 1.3G，接近满载。** checkpoints 目录占 22G。

### Python 环境（conda base）
- Python 3.10.12
- torch=2.8.0+cu128, CUDA=True
- transformers=5.8.1
- datasets=4.8.5
- accelerate=1.13.0

### 项目目录
```
artifacts/  checkpoints/  data/  docs/  figures/  logs/  paper/  results/  scripts/  src/
```

### Checkpoints（26个）
exp15 系列（roberta_large 9class/vanilla, seed 42/123/456）、exp15b（lr1e5）、exp16/16b/17、exp18（e2e）、exp20（bert_base）、exp26（frozen）、exp27（mean_pooling）、exp36（frozen_mlm）

### 生成数据
actorattack、crescendo、deceptive_delight、fitd、benign 各版本（v2/v3/v4）、wildchat_benign 等 32 个文件

### 需关注的问题
1. **磁盘 96%** — 仅剩 1.3G，任何新实验/checkpoint 都会撑爆
2. **GPU 数量异常** — torch 只检测到 1 张 GPU，预期 4 张（cuda:0-3）

---

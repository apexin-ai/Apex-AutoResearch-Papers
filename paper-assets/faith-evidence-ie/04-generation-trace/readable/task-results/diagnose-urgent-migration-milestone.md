# diagnose urgent migration milestone

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_urgent-migration-milestone_20260520T095540_result.json`
- **Structured JSON:** [`e7f25afcba64339c24e3.json`](../../sessions/e7/e7f25afcba64339c24e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 磁盘
- **350G 总量 / 50G 已用 / 301G 可用** → >200G ✅

### rsync/scp 运行状态
- **rsync**: 3 进程运行中（从旧服务器同步）
- **SCP 优先传输**: 正在执行第 1 步（共 7 步）— 正在复制 meta-llama 基座模型
- 传输速率: ~2.8 MB/s，磁盘从 10G 增长到 50G（~1.5h）

### nvidia-smi
| GPU | 型号 | 显存占用 | Util | 状态 |
|-----|------|---------|------|------|
| 0 | RTX PRO 6000 Blackwell | **0MiB / 98GB** | 0% | P8 idle |
| 1 | RTX PRO 6000 Blackwell | **0MiB / 98GB** | 0% | P8 idle |
| 2 | RTX PRO 6000 Blackwell | **0MiB / 98GB** | 100% | P0 |
| 3 | RTX PRO 6000 Blackwell | **0MiB / 98GB** | 100% | P0 |

全部 4 卡空闲（0MiB），无 GPU 进程。GPU 2/3 的 100% util 可能是硬件初始化状态。

### LLaMA-3.1-8B 基座模型完整性
模型总大小: 16,060,522,496 bytes (~14.96 GB)

| Shard | 期望大小 | 当前大小 | 状态 |
|-------|---------|---------|------|
| model-00001-of-00004 | ~4.98GB | 4.98GB | ✅ 完成 |
| model-00002-of-00004 | ~5.00GB | 5.00GB | ✅ 完成 |
| model-00003-of-00004 | **~4.58GB** | **628MB (14%)** | ❌ **传输中** |
| model-00004-of-00004 | ~1.17GB | 1.17GB | ✅ 完成 |

Config/tokenizer/其他文件: ✅ 全部就位

### 14B 文件
- 14B SFT adapter: ❌ MISSING（SCP 第 6 步，尚未开始）
- 14B generations: ❌ MISSING（SCP 第 5 步，尚未开始）
- Qwen3-14B: 6/8 shards（rsync 部分同步）

### 里程碑状态

**里程碑 A: ❌ 未满足**
| 条件 | 状态 |
|------|------|
| LLaMA-3.1-8B 基座完整 | ❌ shard 3 传输中 (14%) |
| train_annotated.json | ✅ |
| freige 代码 | ✅ |
| s43 训练脚本 | ✅ |

**唯一阻塞项**: model-00003-of-00004.safetensors，剩余 ~3.95GB，按当前速率 **ETA ~18:20 CST（约 25 分钟后）**。

**里程碑 B: ❌ 未满足** — 14B 相关资产均未到位。

### 缺失文件清单
1. `models/meta-llama/Meta-Llama-3.1-8B/model-00003-of-00004.safetensors` — 传输中，~25min
2. `sft_output_14b/adapter_model.safetensors` — SCP 队列第 6 步
3. `rsft_generations_14b/generations.jsonl` — SCP 队列第 5 步
4. `models/Qwen/Qwen3-14B/` — 缺 2/8 shards（SCP 第 7 步）

---

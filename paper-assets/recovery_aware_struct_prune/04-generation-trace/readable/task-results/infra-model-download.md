# infra model download

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_model-download_20260514T024834_result.json`
- **Structured JSON:** [`7a821d492dc03928ad66.json`](../../sessions/7a/7a821d492dc03928ad66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个下载都在稳定推进，速度 1.2-1.6 MB/s。预计 1.5-2 小时完成。中间汇报当前状态。

---

## 当前状态汇报

### 1. 环境状态
| 项目 | 版本 |
|------|------|
| Python | 3.12.3（conda base） |
| PyTorch | 2.10.0+cu128 |
| CUDA | 12.8 |
| OS | Ubuntu 22.04.5 |

### 2. GPU 信息
| GPU | 型号 | 显存 |
|-----|------|------|
| cuda:0 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 94GB |
| cuda:1 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 94GB |

### 3. 已安装关键包
- torch==2.10.0+cu128, torchvision==0.25.0+cu128, torchaudio==2.10.0
- transformers==5.8.0, accelerate==1.13.0
- datasets==4.8.4, einops==0.8.2, wandb==0.26.0
- flashinfer-python==0.6.6
- flash-attn 正在后台编译

### 4. 模型下载状态
**进行中** — 使用 aria2c 16 连接并行下载：
- model-00001-of-000002.safetensors: 341MiB/8.0GiB (4%), ~1.2MB/s
- model-00002-of-000002.safetensors: 300MiB/6.1GiB (4%), ~1.6MB/s
- 预计完成时间：~1.5-2 小时
- 存储路径：`/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B`
- 符号链接已创建：`/root/recovery_aware_struct_prune/models/DeepSeek-R1-Distill-Qwen-7B -> /root/autodl-tmp/models/...`

### 5. 磁盘状态
- 根分区：30G, 20G used, 11G free（已清理旧下载进程释放空间）
- 数据盘 autodl-tmp：~250G, ~62G free

### 6. 无阻塞问题
环境完整，所有依赖已安装。唯一等待项是模型下载。

---

需要我继续轮询下载进度直到完成，还是先做其他工作？

---

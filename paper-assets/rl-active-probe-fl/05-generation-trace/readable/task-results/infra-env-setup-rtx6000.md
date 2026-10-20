# infra env setup rtx6000

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_env-setup-rtx6000_20260514T051824_result.json`
- **Structured JSON:** [`e101e14194f8da0ca247.json`](../../sessions/e1/e101e14194f8da0ca247.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载速度稳定在 ~1.4MB/s 总带宽，模型约 16GB，预计约 3 小时完成。

## 当前状态汇总

### 环境探测结果
- **Python**: 3.12.3 (miniconda3/conda base)
- **CUDA**: 12.8 (driver 595.58.03)
- **GPU**: 2× NVIDIA RTX PRO 6000 Blackwell Server Edition (94GB each)

### 已安装包（无需额外安装）
| 包 | 版本 |
|---|------|
| torch | 2.10.0+cu128 |
| transformers | 4.57.6 |
| trl | 1.1.0 |
| peft | 0.19.0 |
| accelerate | 1.13.0 |
| vllm | 0.18.1 |
| datasets | 4.8.4 |
| wandb | 0.26.0 |

### 磁盘
| 分区 | 总量 | 已用 | 可用 |
|------|------|------|------|
| / (系统盘) | 30G | 6.6G | 24G |
| /root/autodl-tmp (数据盘) | 250G | 1.2G | 249G |

### 进行中
- **Qwen3-8B 模型下载**: 后台运行中 (PID=3829)，通过 hf-mirror.com 下载到 `/root/autodl-tmp/models/Qwen3-8B/`，当前已下载 ~358MB / ~16GB，预计 ~3 小时完成
- 注意：`Qwen/Qwen3-8B-Instruct` 在 HuggingFace 和 ModelScope 均不存在（404/401），改用 `Qwen/Qwen3-8B`（Qwen3 原生支持指令跟随，`/think` 模式）

### 已完成
- 项目目录 `/root/autodl-tmp/diagprobe/` 已创建
- 环境激活脚本 `/root/autodl-tmp/diagprobe/activate_env.sh` 已写入
- PyTorch + GPU 验证通过（CUDA=True, 2 GPUs 可见）

### 待模型下载完成后验证
可用以下命令检查下载进度：
```bash
tail -5 /tmp/model_download.log; ps -p 3829 -o pid= && echo "STILL_RUNNING" || echo "DONE"; du -sh /root/autodl-tmp/models/Qwen3-8B/
```

---

# ops westd 41074 env setup

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_41074_env_setup_20260519T162554_result.json`
- **Structured JSON:** [`3d464c5cec14c013b185.json`](../../sessions/3d/3d464c5cec14c013b185.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

传输持续进行中。以下是目前的环境搭建汇总：

## westd-41074 环境搭建状态

| 项目 | 状态 |
|------|------|
| **GPU** | 4×NVIDIA RTX PRO 6000 Blackwell (94GB each) |
| **PyTorch** | 2.8.0+cu128, CUDA 12.8 |
| **Python** | 3.12.3 (conda base) |
| **transformers** | 5.8.1 |
| **datasets** | 4.8.5 |
| **accelerate** | 1.13.0 |
| **flash-attn** | 2.8.3 |
| **wandb** | 0.27.0 |
| **einops/modelscope** | 已安装 |
| **代码同步** | 完成（40 .py + configs + scripts） |
| **smolvla_base 模型** | 完成 (873MB) |
| **LIBERO 数据集** | 从 cqa1 rsync 中，PID 676927，~13MB/s，预计 ~40 分钟 |
| **数据盘** | 250GB，已用 1.2GB |
| **根分区** | 30GB，已用 2GB |
| **环境变量** | 已写入 ~/.bashrc（conda, network_turbo, HF_HOME, SSL 等） |

LIBERO 数据集（33GB）正从 cqa1 rsync 传输中，PID 676927 在 cqa1 上。可以用以下命令检查进度：

```bash
# 在 cqa1 上
tail -2 /tmp/rsync_libero.log
ps -p 676927 -o pid= && echo "RUNNING" || echo "DONE"

# 在 westd-41074 上检查已接收大小
du -sh /root/autodl-tmp/.hf_cache/lerobot/hub/datasets--HuggingFaceVLA--libero/
```

---

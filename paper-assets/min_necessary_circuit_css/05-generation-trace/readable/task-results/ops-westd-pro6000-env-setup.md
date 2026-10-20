# ops westd pro6000 env setup

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-pro6000-env-setup_20260513T060425_result.json`
- **Structured JSON:** [`1a784f1baacca7551a2f.json`](../../sessions/1a/1a784f1baacca7551a2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

环境搭建完成。汇总：

| 项目 | 结果 |
|------|------|
| **预置镜像** | 否（无 `.aml_image.json`） |
| **Python** | 3.12.3 (conda base, miniconda3) |
| **CUDA** | 13.2 (Driver 595.58.03) |
| **PyTorch** | 2.10.0+cu128 (预装) |
| **GPU** | 2× NVIDIA RTX PRO 6000 Blackwell 94GB ✓ |
| **磁盘** | 根分区 30G (24G 可用) / 数据盘 250G |
| **网络** | AutoDL，已有 network_turbo |
| **环境变量** | HF_HOME/SSL 证书/HF_HUB_DISABLE_XET 已写入 ~/.bashrc |
| **已装包** | transformers 4.57.6, datasets 4.8.4, accelerate 1.13.0, einops, wandb, transformer-lens, auto-circuit |
| **项目目录** | `/root/min_necessary_circuit_css` 已创建 |
| **env_activate** | 已配置 conda base 自动激活 |

---

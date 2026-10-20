# infra mvp setup

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_mvp-setup_20260514T051327_result.json`
- **Structured JSON:** [`a5c5aa5f812dd3559b6f.json`](../../sessions/a5/a5c5aa5f812dd3559b6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报结果：

### 环境详情
| 项目 | 值 |
|------|-----|
| Python | 3.12.3 (conda base) |
| CUDA | cu128 (driver 580.119.02) |
| PyTorch | 2.10.0+cu128 |
| GPU | 2× NVIDIA RTX PRO 6000 Blackwell Server Edition (96GB) |
| 镜像 | 非 aml-train 预置镜像，使用 conda base 环境 |

### 依赖安装状态
全部成功。已预装：torch, transformers (4.57.6), datasets (4.8.4), accelerate (1.13.0), einops, nltk, matplotlib, pandas, numpy。新装：mauve-text (0.4.0)。nltk punkt/punkt_tab 数据已下载。

### 代码部署
5 个文件均已部署到 `/root/autodl-tmp/distrib_canary_collapse/`：
- `metrics.py` (12KB)
- `iterative_train.py` (9.6KB)
- `prepare_data.py` (2.2KB)
- `run_mvp.sh` (1.4KB, +x)
- `analyze_mvp.py` (9.8KB)

### 数据准备
| Split | 样本数 |
|-------|--------|
| Train | 716,506 |
| Eval | 1,564 |
| Prompts | 1,000 |

数据保存在 `data/wikitext103/`（train 约 500MB）。

### 注意事项
- **network_turbo 代理会导致 HF 下载卡死**，改用 `HF_ENDPOINT=https://hf-mirror.com`（不启用代理）后正常下载。后续 pip install 如需代理仍可用 `source /etc/network_turbo`，但 HF 数据/模型下载建议走镜像直连。
- SSH 密钥认证已配置（生成 ed25519 密钥并 copy 到服务器）。

---

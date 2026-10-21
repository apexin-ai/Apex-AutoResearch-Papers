# infra cqa1 health check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cqa1-health-check_20260519T134259_result.json`
- **Structured JSON:** [`1f2e9eb7d23a0de5545b.json`](../../sessions/1f/1f2e9eb7d23a0de5545b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器 cqa1-22115 检查结果

### 1. GPU 健康状态
| GPU | 型号 | 显存 | 已用 | 温度 | 利用率 |
|-----|------|------|------|------|--------|
| 0 | RTX 4090 D | 24GB | 0 MB | 28°C | 0% |
| 1 | RTX 4090 D | 24GB | 0 MB | 30°C | 0% |
| 2 | RTX 4090 D | 24GB | 0 MB | 31°C | 0% |
| 3 | RTX 4090 D | 24GB | 0 MB | 28°C | 0% |

**4x RTX 4090 D 全部空闲，状态健康。**

### 2. 已下载模型

| 模型 | 路径 | 大小 | 状态 |
|------|------|------|------|
| **Qwen2.5-7B** | `.hf_cache/Qwen/Qwen2___5-7B/` | 15G | 可用 |
| **Qwen2.5-1.5B** | `.hf_cache/Qwen/Qwen2___5-1___5B/` | (symlink) | 可用 |
| **Qwen2.5-1.5B-Instruct** | `.hf_cache/Qwen/Qwen2___5-1___5B-Instruct/` | (symlink) | 可用 |
| **Mistral-7B-v0.3** | `.hf_cache/mistralai/Mistral-7B-v0___3/` | 28G | 可用 |
| **Meta-Llama-3.1-8B** | `.hf_cache/LLM-Research/Meta-Llama-3___1-8B/` | 30G | 可用 |
| **Pythia-1.4B** | `.hf_cache/hub/models--EleutherAI--pythia-1.4b/` | 2.8G | 可用 |
| **OLMo-1B-hf** | `.hf_cache/allenai/OLMo-1B-hf/` | 4.4G | 可用 (ModelScope 下载，含 model.safetensors) |
| OLMo-1B-hf (HF hub) | `.hf_cache/hub/models--allenai--OLMo-1B-hf/` | 2.1M | **不完整** (.incomplete 文件存在，HF 下载失败) |
| Phi-3-mini-4k-instruct | `.hf_cache/phi-3-mini-4k-instruct/` | 7.2G | 可用 |
| Gemma-2-2B | `.hf_cache/gemma-2-2b/` | 44K | **不完整**（仅元数据） |
| Qwen2.5-14B-Instruct-AWQ | `.hf_cache/Qwen2.5-14B-Instruct-AWQ/` | 9.4G | 可用 |

**所有 7B 级模型均已可用**：Qwen2.5-7B、Mistral-7B-v0.3、Llama-3.1-8B。小模型 Pythia-1.4B、Qwen2.5-1.5B、OLMo-1B 也都可用。Gemma-2-2B 下载不完整。

### 3. Depth Chain 数据 & 实验结果
`data/` 下有 **35 个实验数据目录**，覆盖：
- arXiv 域：llama8b, mistral7b, qwen7b, olmo, pythia + cross-scorer 变体
- Wiki 域：llama8b, mistral7b, qwen7b, olmo, pythia + scorer confound
- Code 域：llama8b, mistral7b, qwen7b, qwen1b5, pythia1b4 + cross-scorer
- 消融实验：length_128/256/512, latex_ablation, retrain_chain

`results/` 下有 **47 个结果目录**，包含 filtering、power_curve、feature_ablation、mcnemar 分析等。

### 4. 磁盘
| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根分区) | 30G | 16G | 15G | 52% |
| /root/autodl-tmp (数据盘) | 250G | 108G | 143G | 43% |

**磁盘充足，数据盘还剩 143G。**

### 5. 网络
无法通过 ssh_read_only 执行 curl 测试（被 read-only 白名单阻断）。但从模型下载时间戳看，最近一次成功下载是 5 月 19 日（phi-3、gemma-2 目录有当天写入），说明网络近期可用。OLMo 的 HF hub 下载仍存在 `.incomplete` 文件，历史网络问题的痕迹。

### 6. 环境
- Python 3.10.12
- pip 包列表无法通过 read_only 查看（需 ssh_execute）

### 7. Cross-transfer 脚本
存在 4 个相关脚本：
- `scripts/transfer_heatmap.py`
- `scripts/exp022_cross_scorer_matrix.sh`
- `scripts/crossscorer_bootstrap_ci.py`
- `scripts/analyze_code_crossmodel.py`

### 总结
- **GPU**: 4x 4090D 全部空闲可用
- **7B 模型**: Qwen2.5-7B / Mistral-7B / Llama-3.1-8B 均已就位，无需下载
- **数据**: 三个域 (arXiv/Wiki/Code) 的 depth chain 数据和 cross-scorer 实验数据已齐全
- **磁盘**: 数据盘 143G 剩余，充足
- **网络**: 近期可用，但 HF hub 直连历史上不稳定（OLMo .incomplete 为证）

---

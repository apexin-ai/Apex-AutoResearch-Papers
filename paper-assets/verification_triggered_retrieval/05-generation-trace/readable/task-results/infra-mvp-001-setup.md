# infra mvp 001 setup

**verification triggered retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_mvp_001_setup_20260517T060136_result.json`
- **Structured JSON:** [`acc3cc8e0e24afbda596.json`](../../sessions/ac/acc3cc8e0e24afbda596.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

环境搭建完成。汇报如下：

---

## 服务器规格

| 项目 | 值 |
|------|-----|
| GPU | NVIDIA RTX PRO 6000 Blackwell Server Edition |
| 显存 | 95 GB |
| CUDA | 12.8 |
| Python | 3.12.3 (miniconda3) |
| OS | Ubuntu 22.04.5 LTS |
| 数据盘可用 | 231 GB (/root/autodl-tmp) |

## 安装的包

| 包 | 版本 |
|----|------|
| torch | 2.8.0+cu128 |
| transformers | 5.8.1 |
| datasets | 4.8.5 |
| sentence-transformers | 5.5.0 |
| faiss-gpu-cu12 | 1.14.1 (GPU OK) |
| pyserini | 0.25.0 (BM25 OK) |
| scipy | 1.17.1 |
| numpy | 2.3.2 |
| pandas | 3.0.3 |

## 模型

| 模型 | 路径 | 大小 |
|------|------|------|
| Qwen3-8B | /root/autodl-tmp/models/Qwen3-8B | 16 GB |
| BGE-base-en-v1.5 | /root/autodl-tmp/models/bge-base-en-v1.5 | 837 MB |
| NLI DeBERTa-v3-large | /root/autodl-tmp/models/nli-deberta-v3-large | 1.7 GB |

## 数据

- `/root/autodl-tmp/data/hotpotqa_dev_200.json` — 200 条 HotpotQA fullwiki 验证集

## 注意事项

1. **vllm 不可用** — 与 torch 2.8 ABI 不兼容，已卸载。后续用 transformers 直接推理（95GB 显存完全够载 Qwen3-8B fp16）
2. **pyserini 环境变量** — 需要 `JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64` 和 `OPENAI_API_KEY=[REDACTED] .bashrc）
3. **HF 下载** — hf-mirror 带宽低，modelscope 更快（已安装 modelscope 备用）

---

# diagnose d158 14b rsft s44 ced score

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d158_14b_rsft_s44_ced_score_20260525T040254_result.json`
- **Structured JSON:** [`ec699cf2526f9ecccdf2.json`](../../sessions/ec/ec699cf2526f9ecccdf2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 根本原因

**网络不可达 + HF_HOME 未设置。**

运行命令中没有设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，导致 transformers 使用默认缓存路径 (`/root/.cache/huggingface/`，该目录不存在)。找不到本地缓存后尝试从 HuggingFace Hub 下载，但 AutoDL 网络不通（`[Errno 101] Network is unreachable`），重试耗尽后报错：

```
OSError: Can't load the configuration of 'cross-encoder/nli-deberta-v3-base'
```

模型文件实际完整存在于 `/root/autodl-tmp/.hf_cache/hub/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7/`。

### 是否可以直接重试

**可以重试**，但必须在命令中加 `HF_HOME=/root/autodl-tmp/.hf_cache`。不需要修改代码。

### 修复方案

在运行命令前加环境变量：

```bash
HF_HOME=/root/autodl-tmp/.hf_cache CUDA_VISIBLE_DEVICES=2 python -m freige.training.rsft_score_filter ...
```

或者也可以用本地路径直接指定模型（跳过 Hub 解析）：

```bash
--nli_model_path /root/autodl-tmp/.hf_cache/hub/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7
```

### 补充信息

- 输入数据 `/root/autodl-tmp/rsft_generations_14b_s44/generations.jsonl`（225MB, 24216 records）正常
- 输出目录 `/root/autodl-tmp/rsft_scored_14b_s44/` 已创建但为空
- 4 张 GPU 全部空闲（0 MiB 占用），无资源问题

---

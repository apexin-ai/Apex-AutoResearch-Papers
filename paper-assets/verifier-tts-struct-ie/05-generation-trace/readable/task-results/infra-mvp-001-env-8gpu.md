# infra mvp 001 env 8gpu

**verifier tts struct ie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_mvp-001-env-8gpu_20260511T164930_result.json`
- **Structured JSON:** [`c614a59f4cb884d3e76f.json`](../../sessions/c6/c614a59f4cb884d3e76f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。最终状态报告：

---

## 环境搭建完成报告

### GPU
- 8× NVIDIA GeForce RTX 5090 (32GB each), 总显存 256GB

### 软件版本
| 组件 | 版本 |
|------|------|
| Python | 3.12.3 |
| PyTorch | 2.10.0+cu128 |
| CUDA | 12.8, 8卡全部可用 |
| vLLM | 0.18.1 |
| transformers | 4.57.6 |
| accelerate | 1.13.0 |

### 模型
- **路径**: `/root/autodl-tmp/models/Qwen/Qwen3-8B/`
- **大小**: 5 shards, 共 ~15.5GB
  - model-00001: 3.8G
  - model-00002: 3.8G
  - model-00003: 3.7G
  - model-00004: 3.0G
  - model-00005: 1.2G
- 含 config.json, tokenizer 等全部配置文件

### 数据集
- **路径**: `/root/projects/verifier-tts-struct-ie/data/processed_data/json/`
- train: 350 docs, dev: 50 docs, **test: 100 docs**
- 格式: JSONL, 含 NER/relations/coreference 标注

### 项目目录
```
/root/projects/verifier-tts-struct-ie/
├── data/raw_data/        # SciERC 原始数据
├── data/processed_data/  # 处理后 JSON
├── scripts/
├── results/
└── logs/
```

### 注意事项
1. **账户为 root**，非 sonny（服务器无 sonny 用户）
2. **网络受限**: HTTPS 到 HuggingFace 被 Squid 代理阻断，模型通过 ModelScope 下载
3. 所有大文件在数据盘 `/root/autodl-tmp/`，根分区空间有限
4. conda base 环境，非 venv

---

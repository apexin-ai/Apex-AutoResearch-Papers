# diagnose plan 007 redocred failure

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan_007_redocred_failure_20260516T123450_result.json`
- **Structured JSON:** [`a2bd75d6171f05be283a.json`](../../sessions/a2/a2bd75d6171f05be283a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。结论如下：

---

## 诊断结果

### 失败原因

**模型不存在。** 代码尝试加载 `/root/autodl-tmp/models/Qwen/Qwen3-4B`，但该目录不存在。服务器上只有：
- `/root/autodl-tmp/models/Qwen/Qwen3-1.7B`
- `/root/autodl-tmp/models/Qwen/Qwen3-8B`

新版 `transformers` 将路径当作 HF repo id 尝试远程下载，因路径格式不符而报 `HFValidationError`。

### cuda:0 状态

**空闲，可用。** 显存占用 0 MiB / 32607 MiB。

其他 GPU 状态：
| GPU | 已用 | 总计 |
|-----|------|------|
| 0 | 0 MiB | 32607 MiB |
| 1 | 23292 MiB | 32607 MiB |
| 2 | 18475 MiB | 32607 MiB |
| 3 | 17883 MiB | 32607 MiB |

### Re-DocRED 数据

**不存在。** `/root/autodl-tmp/data/redocred/` 目录不存在，需要下载。

### 修复建议

1. **下载 Qwen3-4B 模型**（约 8GB）：
   ```bash
   source /etc/network_turbo
   python -c "from modelscope import snapshot_download; snapshot_download('Qwen/Qwen3-4B', cache_dir='/root/autodl-tmp/models')"
   ```
   或用 HF CLI 指定 local-dir：
   ```bash
   HF_HOME=/root/autodl-tmp/.hf_cache huggingface-cli download Qwen/Qwen3-4B --local-dir /root/autodl-tmp/models/Qwen/Qwen3-4B
   ```

2. **准备 Re-DocRED 数据集** — 需要确认数据格式要求（代码中 `--dataset` 参数期望的路径/格式），然后下载放置到正确位置。

3. **重新运行 eval**（模型和数据就位后）：
   ```bash
   CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-4B --dataset redocred ...
   ```

核心问题：plan_007 在模型和数据都未准备好的情况下就被提交了。

---

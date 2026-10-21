# code exp 060 14b scale prep

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_060_14b_scale_prep_20260520T104714_result.json`
- **Structured JSON:** [`20cb5d12cecc472013de.json`](../../sessions/20/20cb5d12cecc472013de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载中，速度 ~6MB/s，预计 ~1.5h 完成。最终模型路径将是 `/root/autodl-tmp/models/Qwen2.5-14B/Qwen/Qwen2.5-14B/`。

---

## 报告

### 1. 选定模型

| 项目 | 值 |
|------|-----|
| 模型名称 | Qwen2.5-14B (base) |
| HuggingFace ID | `Qwen/Qwen2.5-14B` |
| 参数量 | 14.7B |
| FP16 显存预估 | ~28GB |
| 目标 GPU | RTX 5090 (32GB) — 余量 ~4GB，batch_size=1 推理足够 |

确认是 **base model**（非 instruct/chat），HF 模型卡明确说明 "not recommended for conversations"。

### 2. 下载状态

- **PID**: 190263
- **方式**: ModelScope CDN（AutoDL 国内加速）
- **目标路径**: `/root/autodl-tmp/models/Qwen2.5-14B/Qwen/Qwen2.5-14B/`
- **总大小**: ~29.5GB (8 shards × ~3.7GB)
- **已下载**: ~689MB
- **速度**: ~6MB/s（8 并行流）
- **预估剩余**: ~80-90 分钟

监控命令:
```bash
tail -5 /tmp/download_qwen25_14b.log
du -sh /root/autodl-tmp/models/Qwen2.5-14B/
```

### 3. Pipeline 兼容性

`generate_chain.py` 完全兼容，支持 `--model-path` 和 `--model-name` 参数。现有参数默认值已匹配需求 (temperature=0.7, top_p=0.9)。

### 4. 生成命令（待模型下载完成后执行）

双卡 2-shard 并行，各处理 ~500 seeds 的一半：

```bash
cd /root/gen-depth-fingerprint

# GPU 0
nohup python generate_chain.py \
  --model-path /root/autodl-tmp/models/Qwen2.5-14B/Qwen/Qwen2.5-14B \
  --model-name qwen2.5-14b \
  --device cuda:0 \
  --shard-id 0 --num-shards 2 \
  --temperature 0.7 --top-p 0.9 \
  > /tmp/gen_qwen25_14b_shard0.log 2>&1 &

# GPU 1
nohup python generate_chain.py \
  --model-path /root/autodl-tmp/models/Qwen2.5-14B/Qwen/Qwen2.5-14B \
  --model-name qwen2.5-14b \
  --device cuda:1 \
  --shard-id 1 --num-shards 2 \
  --temperature 0.7 --top-p 0.9 \
  > /tmp/gen_qwen25_14b_shard1.log 2>&1 &
```

输出目录: `data/qwen2.5-14b/generations_shard{0,1}.jsonl`

**注意**: 28GB 模型 × 2 份 = 56GB 显存，需要两张卡各自加载完整模型。如果显存不够（模型加载后 OOM），回退到单卡 1-shard 方案。

### 5. 特征提取

生成完成后用 `extract_features.py` 或 `extract_features_multi.py` 提取 DDR 特征，参考模型仍用 Pythia-410M。

---

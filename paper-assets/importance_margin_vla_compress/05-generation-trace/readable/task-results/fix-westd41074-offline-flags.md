# fix westd41074 offline flags

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd41074_offline_flags_20260527T104049_result.json`
- **Structured JSON:** [`afdd9fc1f143b8989aaf.json`](../../sessions/af/afdd9fc1f143b8989aaf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已成功通过危险阶段，正在运行评估。

## 汇总

| GPU | 实验 | PID | 显存 | 状态 |
|-----|------|-----|------|------|
| 0 | π0.5 Random k=0.9 | 356361 | 10913 MiB | 运行中 |
| 1 | π0.5 Random k=0.5 | 356612 | 10405 MiB | 运行中 |
| 2 | **π0.5 Attn k=0.95** | 433293 | 9700 MiB | **已修复** — 已过 tokenizer，进入 task 评估（attention pruning 243/256 tokens） |
| 3 | **π0.5 L2norm k=0.85** | 433369 | 9700 MiB | **已修复** — 已过 tokenizer，进入 task 评估（l2norm pruning 217/256 tokens） |

4 张 GPU 全部在跑实验。修复关键：加了 `source conda` 激活环境 + `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1` 避免网络访问。`Preprocessor/postprocessor loaded` 确认 tokenizer 从本地缓存成功加载。

---

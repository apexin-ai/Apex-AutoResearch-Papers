# infra openvla download v3

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_openvla-download-v3_20260515T060130_result.json`
- **Structured JSON:** [`5cca47f765cf0f1620e5.json`](../../sessions/5c/5cca47f765cf0f1620e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 下载完成报告

| 项目 | 结果 |
|------|------|
| **下载方式** | hf-mirror.com wget 直接下载（绕过 xet）；shard 1 来自 huggingface-cli 初次下载的残留完整文件 |
| **safetensors 文件** | |
| model-00001-of-00003.safetensors | **6.5G** (6,948,961,960 bytes) |
| model-00002-of-00003.safetensors | **6.5G** (6,971,232,040 bytes) |
| model-00003-of-00003.safetensors | **1.1G** (1,162,406,824 bytes) |
| **总目录大小** | **15G** |
| **config 验证** | ✅ model_type=openvla, trust_remote_code 加载成功 |
| **符号链接** | ✅ `/root/vla-ssd/checkpoints` → `/root/autodl-tmp/vla-ssd/checkpoints` |
| **下载速度/耗时** | shard 3: 3.27MB/s (~6min); shard 2: 1.69MB/s (~68min); shard 1: 来自初次 huggingface-cli 下载的完整缓存文件 |

---

# audit cqa1 gpu usage

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_cqa1_gpu_usage_20260524T234614_result.json`
- **Structured JSON:** [`b8f4a9c2c44dd866f318.json`](../../sessions/b8/b8f4a9c2c44dd866f318.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总 cqa1-33015 完整 GPU 状态：

## cqa1-33015 GPU 状态表

| GPU | 显存占用 | PID | 实验 | Registry 状态 |
|-----|---------|-----|------|--------------|
| **0** | 10308 MiB / 24564 MiB | 733134 | π0.5 Random k=0.85 Object seed43 (`eval_pi05_random_k085_object_seed43_postfix`) | RUNNING ✅ |
| **1** | 10369 MiB / 24564 MiB | 788487 | π0.5 Random k=0.85 Spatial seed43 (`eval_pi05_random_k085_spatial_seed43_postfix`) | RUNNING ✅ |
| **2** | 10xxx MiB (加载中) | 860107 | **新部署** π0.5 Random k=0.85 Long seed43 (`eval_pi05_random_k085_long_seed43_v2`) | RUNNING ✅ |
| **3** | 10371 MiB / 24564 MiB | 792821 | π0.5 L2norm k=0.85 Spatial seed43 (`eval_pi05_l2norm_k085_spatial_seed43_postfix`) | RUNNING ✅ |

**发现：**
- Director 预期的 "Random k=0.5/0.7/0.85/0.95 seed43" 系列已完成并下线，当前 cqa1 跑的是 **k=0.85 postfix 系列**（cliff zone 补充）
- GPU 2 原本空闲，已部署 **Random k=0.85 Long seed43** — 填补 Long suite 在 k=0.85 cliff zone 完全缺失 Random baseline 的空白（seed42/43 都没有结果文件）
- 所有 4 张 GPU 现在都有活跃进程且 registry 匹配，无未注册实验

---

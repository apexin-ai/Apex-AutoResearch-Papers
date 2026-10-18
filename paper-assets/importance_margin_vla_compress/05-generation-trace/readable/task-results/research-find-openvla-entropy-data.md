# research find openvla entropy data

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_find_openvla_entropy_data_20260519T034504_result.json`
- **Structured JSON:** [`8b7c3085ff5d5264ef0f.json`](../../sessions/8b/8b7c3085ff5d5264ef0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到了全部数据。总结如下：

## 搜索结果

### westd-27271 上找到两个 JSON 文件

**1. `eval_results/openvla_attention_entropy_real.json`** (3140 bytes, 2026-05-18 创建)
- 基于 **250 张真实 LIBERO-Object 图片**（10 tasks × 25 frames）
- 论文应引用此文件
- 关键数据：
  - `overall_entropy_ratio`: **0.6393**（论文报告 0.64 ✓）
  - `per_layer_entropy_ratio`: L0=0.979 → L29=0.477（论文报告 L0=0.98, L29=0.48 ✓）
  - 包含 `per_layer_entropy_std`（可画 error bar）
  - 包含 `per_layer_vision_attention_fraction`
  - 最低层: L29 (0.477), 最高层: L0 (0.979)
  - 32 层 (L0-L31) 完整数据

**2. `artifacts/openvla_attention_entropy.json`** (旧版，基于 20 张随机噪声图)
- `overall_entropy_ratio`: 0.617
- 这是早期版本，不应用于论文

### cqa1-33015 上无 OpenVLA 数据
只有 SmolVLA 的 entropy 文件（已知）。

### 数据充分性
`openvla_attention_entropy_real.json` 包含画 per-layer entropy 折线图所需的所有信息：32 层的 mean entropy ratio + std，以及 vision attention fraction。

---

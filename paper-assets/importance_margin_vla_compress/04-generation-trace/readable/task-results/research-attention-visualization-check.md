# research attention visualization check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_attention_visualization_check_20260519T034016_result.json`
- **Structured JSON:** [`14b0d248a079b2ca0cc6.json`](../../sessions/14/14b0d248a079b2ca0cc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结果

### 1. 现成 attention/entropy raw data

**有 SmolVLA 的 per-layer entropy 统计数据，没有 raw attention weights。**

- `eval_results/smolvla_attention_entropy_perlayer_fixed.json` — 260 帧 (10 个 LIBERO-Object tasks)，16 层，记录了：
  - `per_layer_entropy_ratio`: 逐层 entropy ratio（0.93~0.98，overall 0.9521）
  - `per_layer_vision_attention_fraction`: 逐层 vision attention 占比（0.44~0.67）
  - 包含 std
- **没有 raw attention weight 矩阵**（脚本在 hook 中计算完 entropy/vis_frac 后只保留统计值，没有 dump 原始 attention probs）
- **没有 OpenVLA 的任何 entropy 数据**，服务器上也没有 OpenVLA 模型

### 2. 现成脚本

| 脚本 | 用途 |
|---|---|
| `measure_smolvla_entropy_perlayer_fixed.py` | SmolVLA entropy 分析（通过 monkey-patch `eager_attention_forward` 捕获 attention probs） |
| `scripts/visualize_token_importance.py` | IMM 模型的 token importance heatmap（基于 `compute_importance_scores`，不是 raw attention） |

已有图表：`token_importance_heatmap.png`、`margin_distribution.png`、`keep_ratio_sensitivity.png` — 都是 IMM 模型的 diagnostics，不是 SmolVLA vs OpenVLA 对比。

### 3. 如需新提取的方案

**SmolVLA attention heatmap：**
- 脚本已有完整的 hook 机制（`hooked_attn`），只需修改 `measure_smolvla_entropy_perlayer_fixed.py`，在 hook 中额外保存几帧的 raw `probs` tensor 到 `.pt` 文件
- 改动量小：加几行 `torch.save(probs, ...)` 即可
- GPU 需求：已有脚本用单卡跑 260 帧，保存几帧的 attention 只需几分钟
- 模型 SmolVLA-0.5B，显存需求低

**OpenVLA attention heatmap：**
- 服务器上**没有 OpenVLA 模型**，需要下载（~7B，约 14GB）
- OpenVLA 基于 Llama-2-7B，HuggingFace Transformers 原生支持 `output_attentions=True`，提取简单
- 但下载+加载+推理时间会较长，且需要较大显存（至少需要 A100/4090 级别 GPU）
- 替代方案：引用已有文献的 entropy 数据（如果论文中 0.64 的数字来自公开论文），或只做 SmolVLA 自身的 attention 可视化

### 4. 建议的可视化类型

| 可视化 | 数据状态 | 论文价值 |
|---|---|---|
| **Per-layer entropy ratio 折线图** (SmolVLA) | 数据已有，直接画 | 高 — 展示 pixel-shuffle 导致的 uniform attention |
| **SmolVLA attention heatmap** (单帧，text query → vision tokens) | 需修改脚本提取几帧 raw weights | 高 — 直观展示 attention 分散问题 |
| **SmolVLA vs OpenVLA entropy 对比柱状图** | 缺 OpenVLA 数据 | 高 — 但需要 OpenVLA 模型或引用文献数据 |
| **Token importance distribution** (IMM 模型) | 数据和图已有 | 中 — 展示 IMM 学到的 importance 分布 |

**最快出图路径**：用现有 JSON 数据画 SmolVLA per-layer entropy ratio + vision attention fraction 的双轴折线图，不需要任何额外 GPU 计算。

---

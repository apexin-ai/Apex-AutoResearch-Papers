# code pi05 pruning adapter

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pi05-pruning-adapter_20260521T014154_result.json`
- **Structured JSON:** [`933a3f5d2676c21a1aa4.json`](../../sessions/93/933a3f5d2676c21a1aa4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果已获取。汇总：

## 结果

### 1. π0.5 Vision Pipeline 架构确认

| 组件 | 规格 |
|------|------|
| Vision Encoder | SigLIP So400m/14 |
| 输入分辨率 | 224×224 |
| Vision tokens/image | 256 (16×16) |
| SigLIP hidden dim | 1152 |
| Connector | Linear projection (1152 → 2048) |
| Scaling | ×√2048 = ×45.25 |
| Image slots | 3 (base + wrist + empty_camera) |
| Total vision tokens | 768 |
| VLM backbone | Gemma 2B (hidden=2048, 18 layers) |
| Action Expert | Gemma 300M |
| Total params | 4143.4M |

### 2. Offline CV/Entropy 分析

| 指标 | Pre-projector (SigLIP) | Post-projector (scaled) |
|------|----------------------|------------------------|
| **CV** | 0.131 | **0.055** |
| mean L2 norm | 39.47 | 9421.85 |
| std L2 norm | 5.17 | 515.44 |
| Per-image CV | 0.131 ± 0.003 | 0.054 ± 0.002 |
| Entropy (normalized) | 0.9985 | **0.9997** |

### 3. 跨模型对比（post-projector CV）

| 模型 | CV | Connector 类型 |
|------|------|---------------|
| **π0** | 0.038 | linear |
| **π0.5 (this)** | **0.055** | linear |
| X-VLA | 0.151 | linear + LayerNorm |
| OpenVLA | 0.215 | MLP |
| OFT | 0.219 | MLP |
| SmolVLA | 0.314 | pixel-shuffle |

### 4. 分析

- **π0.5 CV=0.055**，接近预期的 π0 值（0.038），但稍高。符合「linear projection → 低 CV → tokens 近均匀」的假说。
- **Entropy 接近最大值**（0.9997），说明 token 重要性分布几乎完全均匀。
- **CV < 0.1**，确认架构符合预期（SigLIP → linear projection），没有意外结构。
- 稍高于 π0 的原因可能是：(1) finetuned checkpoint vs base model (2) 使用 random images vs real images (3) 不同版本的 SigLIP 权重。

### 5. 脚本和 Checkpoint 状态

- `analyze_pi05_vision_tokens.py` — 已写入并成功运行
- `eval_pi05_pruning_libero.py` — 已写入，支持 `--prune_mode none/random/l2norm`
- Checkpoint — 7.0GB `model.safetensors` + config files 已下载到 `/root/autodl-tmp/pi05_libero_finetuned/`

---

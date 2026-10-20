# code phase1 dryrun v2

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase1-dryrun-v2_20260519T211248_result.json`
- **Structured JSON:** [`60fc33716e8965738efa.json`](../../sessions/60/60fc33716e8965738efa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功完成。汇总报告：

---

## Phase 1 Dry-Run 验证报告

### 1. 环境检查
- **transformers**: 4.40.1 (OFT fork) ✓

### 2. 代码正确性验证
- **hidden_states 索引**: 全部使用 `cfg.layer_idx + 1` ✓（L363, L385）
- **token 布局**: 全部使用 `[:, :NUM_PATCHES, :]` ✓（无 `1:1+` 前缀）
- **affordance_decoder.py**: 无 BatchNorm，使用 GroupNorm ✓
- **NUM_PATCHES** = 256（运行时确认）

### 3. Dry-Run 每步 Loss

| Step | L_action | L_consist | H_entropy | L_total |
|------|----------|-----------|-----------|---------|
| 0    | 0.6602   | 0.5274    | -8.7945   | 0.6250  |
| 1    | 6.3125   | 0.6522    | -8.4551   | 6.2932  |
| 2    | 2.0469   | 0.7654    | -8.1932   | 2.0415  |
| 3    | 1.1094   | 0.1528    | -7.5882   | 1.0488  |
| 4    | 1.2109   | 0.1012    | -7.9873   | 1.1412  |
| 5    | 0.5352   | 0.0643    | -8.3273   | 0.4583  |

L_total 公式验证（Step 0）: `0.6602 + 0.1×0.5274 + 0.01×(-8.7945) = 0.6250` ✓

### 4. Gradient & Heatmap（Step 0）
- **lora_gnorm** = 5.1517, **dec_gnorm** = 3.0815 — 均非零 ✓
- **heatmap**: mean=6.1e-5, std=1.5e-4, max=6.8e-3, entropy=8.62
- 所有值合理，无 NaN/Inf ✓

### 5. 判定：**通过** ✓

**关键观察**：
1. **L_consist 有学习信号** — 从 0.527 下降到 0.064，decoder gradient norm 3.08 非零，证明一致性损失产生了有效梯度
2. **无 CUDA OOM** — batch_size=2 在单卡上稳定运行
3. **heatmap 初始值偏小**（mean~6e-5）— 随机初始化的 decoder 输出接近零，符合预期，训练过程中会逐步学到有意义的 affordance 分布
4. 详细 gradient/heatmap 统计仅在 Step 0 输出（wandb_log_freq=10），5 步 dry-run 只触发一次完整日志

---

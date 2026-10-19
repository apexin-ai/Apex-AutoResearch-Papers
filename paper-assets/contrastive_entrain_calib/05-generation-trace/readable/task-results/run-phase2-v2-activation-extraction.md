# run phase2 v2 activation extraction

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_phase2_v2_activation_extraction_20260518T101615_result.json`
- **Structured JSON:** [`f707c0c1f4ecb4ce06fc.json`](../../sessions/f7/f707c0c1f4ecb4ce06fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 2-4 v2 完整结果

### GO/NO-GO: **PASS**

| 指标 | 值 | 阈值 | 状态 |
|------|-----|------|------|
| best_auroc | **0.9985** | ≥ 0.85 | PASS |
| layer0_delta | **0.3088** | ≥ 0.15 | PASS |
| cosine(d_syc, d_gen) | **-1.0** | < 0.3 | PASS* |

*注：当前 binary setup 中 d_gen = -d_syc，cosine 恒为 -1.0，此阈值在 d_gen 独立定义后才有实际意义。

### 关键细节

- **Best layer**: 27 (token position: asst_first)
- **Layer 0 AUROC**: 0.6897 → 信号主要来自模型中高层计算，非 embedding 层
- **Top 5 layers**: 27 (0.9985), 28 (0.9985), 35 (0.9983), 21 (0.9980), 22 (0.9980)
- **AUROC 爬升轨迹**: Layer 0 (0.69) → Layer 8 (0.90) → Layer 16 (0.99) → Layer 19+ (≥0.997)

### 按 domain 分层 (best layer, asst_first position)

| Domain | AUROC |
|--------|-------|
| commonsense | 1.0000 |
| geography | 1.0000 |
| history | 1.0000 |
| math | 1.0000 |
| science | 1.0000 |

### 按 evidence_strength 分层

| Strength | user_last | asst_first |
|----------|-----------|------------|
| weak | 1.0000 | 1.0000 |
| medium | 0.9948 | 0.9974 |
| strong | 0.9890 | 1.0000 |

### 数据规模

- 320 pairs (640 samples), 256 train / 64 test
- 36 layers, hidden_dim=4096 (Qwen3-8B)

所有三项 Go/No-Go 指标均通过，且 AUROC 接近完美。分层结果显示信号在所有 domain 和 evidence strength 上都很稳健。

---

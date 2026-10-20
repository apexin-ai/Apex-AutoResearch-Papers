# code eap ig hf backend

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eap_ig_hf_backend_20260512T184415_result.json`
- **Structured JSON:** [`4be47c85df8a9bccfe23.json`](../../sessions/4b/4be47c85df8a9bccfe23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 实现摘要

**文件**: `artifacts/eap_ig_scoring.py` (305 行) + `artifacts/test_eap_ig_scoring.py`

### 算法实现

三阶段流水线：

1. **Phase 1 — 源节点激活捕获**: 对 clean/corrupt 各做一次 `torch.no_grad()` 前向，通过 hooks 捕获：
   - embedding 输出（layer 0 pre-hook）
   - per-head attention 输出（o_proj 输入 → `_decompose_per_head` 分解）
   - MLP 输出

2. **Phase 2 — IG 梯度累积**: 对每个 IG 步：
   - 在 clean/corrupt embedding 之间线性插值
   - 通过 layer-0 pre-hook 注入插值 embedding
   - `retain_grad()` 捕获 q/k/v_proj 输出和 resid_mid 的梯度
   - 前向 → metric_fn → 反向，累积梯度

3. **Phase 3 — 边得分计算**:
   - Attention 边: `score = |avg_grad_Q_H · (delta_u @ W_q_H)| `（per-head 分解）
   - MLP 边: `score = |avg_grad_resid_mid · delta_u|`

### 与 TL 版主要区别

| | TransformerLens | HuggingFace (本实现) |
|---|---|---|
| Per-head 梯度 | 原生 hook_q/k/v[H] | q/k/v_proj 输出 + 权重矩阵投影 |
| LayerNorm | 精确（hook 在 LN 后） | 近似（J_LN ≈ I） |
| GQA | N/A (GPT-2 only) | 完整支持（K/V 共享 KV group 的梯度和权重切片） |
| 位置编码 | 在 embed hook 后 | Llama-like: RoPE 在 attn 内部；GPT-2: 全 embedding 插值 |

### GQA 处理

`heads_per_group = n_heads // n_kv_heads`。对 query head H，其 KV group index = `H // heads_per_group`。K/V 边使用对应 KV head 的梯度切片和权重切片。Qwen-2.5 0.5B: 14 Q heads → 2 KV heads，每组 7 个。

### 预估耗时（单 A6000, B=1, S=128, ig_steps=5）

| 模型 | 源节点数 | IG 前向+反向 | 边得分计算 | 总计 |
|------|---------|-------------|-----------|------|
| Qwen-2.5 0.5B | 361 | ~5s | <1s | ~6s |
| Gemma-2 2B | ~500 | ~20s | ~1s | ~21s |
| Llama-3.1 8B | 1057 | ~60s | ~4s | ~64s |

---

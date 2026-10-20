# code edge pruning hf backend

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_edge_pruning_hf_backend_20260512T184445_result.json`
- **Structured JSON:** [`f9f01f3adb0ecba197bf.json`](../../sessions/f9/f9f01f3adb0ecba197bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 实现汇报

### 产出文件
- `artifacts/edge_pruning_scoring.py` — Edge Pruning L0 完整实现
- `artifacts/test_edge_pruning_scoring.py` — Smoke tests（7/7 通过，torch 测试需 GPU 环境）

### 实现方案

**Hard Concrete 分布**：`HardConcrete(nn.Module)` 封装 `log_alpha` 参数，采样时通过 Binary Concrete → stretch 到 [γ=-0.1, ζ=1.1] → clamp [0,1]，β=2/3。`l0_penalty()` 返回 P(z≠0) 的和。

**Hook-based masked forward**：
- Embedding hook 捕获 `input` 激活
- `o_proj` hook 按 head 分解 attention 输出（通过 weight slicing）
- MLP hook 捕获 MLP 输出
- Layer pre-hook 用 mask 加权重建 residual stream 输入

**GQA mask 共享策略**：
- Q edges：每个 query head 独立 mask
- K/V edges：同一 KV group 内的 query heads 共享 mask
- Qwen-2.5 0.5B (14H, 2KV)：每个 source 对 K 和 V 各 2 个独立 mask（而非 14 个），Q 仍为 14 个

### 内存估算

| 模型 | 总边数 | 独立 mask 参数 | Mask 内存 (float32) |
|------|--------|---------------|-------------------|
| Qwen-2.5 0.5B (24L, 14H, 2KV) | 179,388 | 79,452 | **0.30 MB** |
| GPT-2 small (12L, 12H, 12KV) | 32,334 | 32,334 | 0.12 MB |

Mask 参数本身内存可忽略。主要瓶颈是 forward pass 中源激活缓存（每层 n_heads 个 head 输出 × [B, S, D]）和反向传播的计算图。Qwen-2.5 0.5B (d=896) 估计额外 ~2-4 GB（batch_size=8, seq_len=128）。

### 预估耗时

| 模型 | 100 epochs (batch=8, seq=128) |
|------|------------------------------|
| Qwen-2.5 0.5B | ~10-20 min (single A6000) |
| GPT-2 small | ~3-5 min (single A6000) |
| Qwen-2.5 7B | ~2-4 hours，建议 gradient checkpointing + 按层分组优化 |

---

# research p1 p2 seq length analysis

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_p1-p2-seq-length-analysis_20260514T085124_result.json`
- **Structured JSON:** [`ad2d08c419671204c41f.json`](../../sessions/ad/ad2d08c419671204c41f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果出来了。下面是完整分析。

---

## P1: max_seq_length 增大方案

### 模型 context length 上限

| 模型 | max_position_embeddings |
|------|------------------------|
| Qwen3-4B | **40960** |
| Qwen3-8B | **40960** |

4096/8192 都远在模型支持范围内。

### VRAM 估算（GQA: num_kv_heads=8, head_dim=128, 36 layers）

KV cache per token = 2 × 36 × 8 × 128 × 2 bytes = **0.14 MB/token**

| 配置 | 模型权重 | KV cache (per batch) | 总 VRAM | 5090 32GB |
|------|---------|---------------------|---------|-----------|
| 4B, bs=16, seq=2048 | ~8 GB | 4.6 GB | ~13 GB | OK |
| 4B, bs=8, seq=4096 | ~8 GB | 4.6 GB | ~13 GB | OK |
| 4B, bs=16, seq=4096 | ~8 GB | 9.2 GB | ~17 GB | OK |
| 4B, bs=8, seq=8192 | ~8 GB | 9.2 GB | ~17 GB | OK |
| 8B, bs=8, seq=4096 | ~16 GB | 4.6 GB | ~21 GB | OK |
| 8B, bs=16, seq=4096 | ~16 GB | 9.2 GB | ~25 GB | tight |

**结论：4B + batch_size=16 + seq=4096 完全可行，无需降 batch_size。**

### 修改点

- `eval_repo_cls.py`: `--max_seq_length` 默认值 2048 → **4096**
- batch_size 可保持 16（甚至可以用 8192 + bs=8）
- 重跑时间估算：seq 翻倍，每个 token 的推理时间不变但 attention 是 O(n²)，实际约慢 1.5-2x → 每 checkpoint 从 ~27 min 增至 ~40-54 min

---

## P2: val/train 长度分布差异

### Token 长度分布统计

| 指标 | train (N=70748) | val (N=9335) | test (N=9784) |
|------|----------------|--------------|---------------|
| Mean | 836 | **1255** | 905 |
| Median | 461 | 400 | 430 |
| P90 | 1160 | **4868** | 2044 |
| P95 | 1287 | **4960** | 2051 |
| P99 | 16023 | 5409 | 2352 |
| Max | 16450 | 8771 | 2484 |
| >2048 | **3.8%** (2655) | **20.2%** (1883) | **8.2%** (802) |
| >4096 | 2.3% (1633) | **15.1%** (1406) | 0.0% (0) |
| >8192 | 1.2% (840) | 0.1% (9) | 0.0% (0) |

### 截断率按 label 分布

| split | fail 截断率 | pass 截断率 |
|-------|-----------|-----------|
| train | 7.1% | 3.2% |
| val | **31.0%** | **16.7%** |
| test | 6.1% | 9.0% |

### 根因：repo 分布不均

| split | 主要截断来源 |
|-------|------------|
| train | django (1820/2655=69%), pylint (719) |
| **val** | **sympy (1406/1780=79%), pytest (477/477=100%)** |
| test | pytest (342/522=66%), xarray (328), sphinx (132/132=100%) |

**val 的 20.2% 截断是数据分布问题，不是设计问题。** sympy 和 pytest 样本集中在 val set 中，这两个 repo 的 patch+test 上下文特别长（sympy 4000-5000 tokens, pytest 3000-5000 tokens）。

### 建议

1. **max_seq_length 设为 4096**：val 截断率从 20.2% 降至 ~15.1%（仅剩 >4096 的部分），test 截断率从 8.2% 降至 0%
2. **如果想进一步覆盖 val 中 sympy**：设为 **6144** 可覆盖 P99（5409），val 截断率降至 <1%
3. 不建议 8192+：train 中 >8192 的 840 个样本几乎全是 django/pylint 的极端 case（train P99=16023 但那是 outlier），收益递减

**推荐方案：max_seq_length=4096, batch_size=16, 4B 模型 VRAM ~17GB，5090 完全够用。**

---

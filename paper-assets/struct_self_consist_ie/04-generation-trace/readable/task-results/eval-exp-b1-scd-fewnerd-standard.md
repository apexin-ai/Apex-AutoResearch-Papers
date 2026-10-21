# eval exp b1 scd fewnerd standard

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp_b1_scd_fewnerd_standard_20260520T192035_result.json`
- **Structured JSON:** [`e070fd8812e8a9ed2385.json`](../../sessions/e0/e070fd8812e8a9ed2385.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果报告

### 1. Checkpoint 验证
**VALID** — `qwen3-8b-fewnerd-scd-lora` checkpoint 完整有效（adapter_model.safetensors 349MB, 2 epochs, train_loss=0.023, eval_loss=0.033）。LoRA merge 成功，生成 4-shard merged model (~16GB)。

### 2. Greedy F1
**Micro F1 = 0.7813** (P=0.7583, R=0.8057)

### 3. 对比

| 配置 | Micro F1 | 相对 baseline |
|------|----------|--------------|
| Baseline greedy (无 SCD) | 0.748 | — |
| N=8 construction target | 0.764 | +1.6 |
| **SCD greedy (本次)** | **0.781** | **+3.3** |

### 4. 结论
**Hypothesis 成立，且超出预期。** SCD greedy F1 (0.781) 不仅接近 N=8 construction F1 (0.764)，还超过了 +1.7 个点。相比 baseline greedy F1 (0.748)，SCD 带来了 +3.3 的提升。

这说明 standard SCD 训练成功地将 self-consistency 集成的知识蒸馏到了单次 greedy 解码中，消除了推理时多次采样的开销。

---

# code v9 config fix

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v9_config_fix_20260519T163322_result.json`
- **Structured JSON:** [`d074278662f9f5cf200c.json`](../../sessions/d0/d074278662f9f5cf200c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改已确认生效。现在计算 KV cache budget。

---

## KV cache budget 计算

**参数**：
- GPU: RTX PRO 6000, 96 GB VRAM
- `gpu_memory_utilization = 0.25`
- `max_model_len = 16384`
- 模型: Qwen3-8B (FP16), 4 GPU tensor parallel
- Qwen3-8B: 36 layers, 8 KV heads (GQA), head_dim = 128, FP16

**Step 1: vLLM memory pool**
```
VLLM_pool = 0.25 × 96 GB = 24 GB
```

**Step 2: 模型权重开销**
- 8B 参数 × 2 bytes (FP16) = 16 GB 总量
- TP=4: 每 GPU ~4 GB（线性层按 TP 切分）
- 但 vLLM 的 `gpu_memory_utilization` 只控制 KV cache 之外的部分——vLLM 先加载模型权重，再用 `gpu_mem_util` 比例的显存给 KV cache
- 实际上 vLLM 的行为是：`KV cache size = gpu_memory_utilization × (total_gpu_mem - model_weight - overhead)`
- 更准确地说：vLLM 先加载模型（~4GB/GPU with TP=4），然后 `available = total - model - overhead`，KV cache = `gpu_memory_utilization × total_gpu_memory`... 

实际上 vLLM 的 `gpu_memory_utilization` 定义是：**vLLM 最多使用 GPU 总显存的这个比例**（包括模型权重 + KV cache）。所以：

```
vLLM 总可用 = 0.25 × 96 GB = 24 GB
模型权重 (TP=4) ≈ 4 GB/GPU
KV cache = 24 - 4 = ~20 GB/GPU
```

**Step 3: KV cache 需求 (per sequence)**
```
每层 KV cache = 2 (K+V) × 8 (KV heads/TP... GQA heads=8, TP=4 → 2 heads/GPU) × 128 (head_dim) × seq_len × 2 bytes
= 2 × 2 × 128 × 16384 × 2 = 32 MB/layer

36 layers × 32 MB = 1,152 MB ≈ 1.13 GB/sequence
```

**Step 4: 最大并发 sequences**
```
20 GB / 1.13 GB ≈ 17 sequences 可并发
```

训练配置 `train.env_groups=16, group_size=8`，rollout 阶段每 GPU 需处理 128 个 sequences（但分批处理，`max_num_batched_tokens=20480`，不需要同时全部 in-flight）。17 并发序列足以支撑 chunked prefill 下的 rollout。

---

## 结果汇总

### 关键参数对比

| 参数 | v7 (base) | v9 修正前 | v9 修正后 |
|------|-----------|----------|----------|
| `gpu_memory_utilization` | 0.22 | 0.20 | **0.25** ✓ |
| `max_model_len` | 16384 | 16384 | **16384** (无需改) |
| `strategy` | default (fsdp1) | fsdp2 | fsdp2 |
| `offload_policy` | — | True | True |
| `enable_activation_offload` | — | true | true |
| `optimizer_offload` (actor) | True (fsdp1) | False (fsdp2) | False |

### KV cache budget

| 项目 | 值 |
|------|-----|
| vLLM 总可用 (0.25 × 96GB) | 24 GB/GPU |
| 模型权重 (TP=4) | ~4 GB/GPU |
| KV cache 可用 | ~20 GB/GPU |
| 每序列 KV (16384 tokens) | ~1.13 GB |
| 最大并发序列数 | ~17 |

**结论**：`gpu_mem_util=0.25 + max_model_len=16384` 组合可行，KV cache 充足。修正完成。

---

# code 8b failure diagnosis

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8b-failure-diagnosis_20260520T055215_result.json`
- **Structured JSON:** [`cdf4fec7ed505cdb6013.json`](../../sessions/cd/cdf4fec7ed505cdb6013.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。

---

## 汇总报告

### 1. 失败原因

两个 8B pilot（exec 和 ISR）均在 **step 1 训练阶段** OOM（generation 成功，training step 中 `lm_head` forward 失败）：

```
torch.OutOfMemoryError: Tried to allocate 1.16 GiB.
GPU 0: 94.97 GiB total, 217.56 MiB free.
PyTorch allocated: 93.42 GiB
```

**仅差 ~1.4 GiB。** 崩溃点在 `_get_per_token_logps_and_entropies` → `lm_head(hidden_states)` — logps 计算的 forward pass。

### 2. GPU 状态

| 项目 | 值 |
|------|-----|
| GPU | NVIDIA RTX PRO 6000 Blackwell Server Edition |
| 显存 | 97,887 MiB (~96 GB) |
| 数量 | 1 块 |
| 当前占用 | 0 MiB（空闲） |

### 3. Pilot 实际配置（`grpo_exec_only_8b.yaml`）

已经是非常激进的配置：

| 参数 | 值 |
|------|-----|
| K (num_generations) | **2**（最小实用值） |
| per_device_batch_size | **1** |
| gradient_accumulation_steps | 16 |
| gradient_checkpointing | **true** |
| optim | **adamw_bnb_8bit** |
| max_completion_length | 512 |
| 模型大小 (磁盘) | 16 GB |

### 4. 显存需求估算

| 组件 | 大小 |
|------|------|
| Policy model (bf16) | ~16.6 GB |
| Ref model (bf16) | ~16.6 GB |
| 8-bit optimizer (2 moments) | ~16.6 GB |
| Gradients (bf16) | ~16.6 GB |
| **固定开销小计** | **~66.4 GB** |
| 可用于 activations/KV cache/buffers | ~28.6 GB |
| **实际峰值（日志）** | **94.75 GB** |

activations + 框架开销 + lm_head logits (vocab=151936) + 碎片化 ≈ 28.6 GB，刚好打满。

### 5. 推荐方案

由于仅差 ~1.4 GiB，以下方案按优先级排列：

**方案 A（最小改动，推荐先试）：**
```bash
export PYTORCH_ALLOC_CONF=expandable_segments:True
# + 将 max_completion_length 从 512 降到 384
```
- `expandable_segments` 减少碎片化，可能释放 1-2 GiB
- 384 tokens 对 FOL formalization 够用（pilot 中 mean_length=148，max=323）

**方案 B（如 A 仍 OOM）：**
- `max_completion_length: 256`（pilot completions 最长 323，但 256 覆盖大多数）
- 结合 `expandable_segments`

**方案 C（如 B 仍 OOM）：**
- DeepSpeed ZeRO-2 + CPU offload（单卡可用，offload optimizer states 到 CPU，释放 ~16 GB）
- 或 LoRA (r=16) 大幅减少 trainable params + optimizer 开销

**K=4 不可行** — logps 计算 batch 翻倍，激活显存翻倍，必然 OOM。

### 6. 预估训练时长

| 配置 | 估算 step 时间 | 500 步总时长 |
|------|---------------|-------------|
| K=2, batch=1, completion=384 | ~55s/step | ~7.5 小时 |
| K=2, batch=1, completion=256 | ~45s/step | ~6.3 小时 |
| K=2, ZeRO-2 CPU offload | ~80s/step | ~11 小时 |

（参考：pilot step 1 generation=28s + training step OOM 前已耗时 38s ≈ 66s/step）

### 7. 注意事项

- Pilot 的 `loss: 0.0, grad_norm: 0.0` 是正常的——K=2 时两个 generation 经常获得相同 reward（都对或都错），advantage=0 → 无梯度信号。K=2 的学习效率会明显低于 K=4。
- 建议 `gradient_accumulation_steps` 从 16 提高到 32（补偿 K=2 的低信号问题，保持有效 batch size）。

---

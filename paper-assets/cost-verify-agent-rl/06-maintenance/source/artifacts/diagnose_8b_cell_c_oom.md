# 8b_cell_c_episode OOM 诊断报告 (v2 更新)

**日期**: 2026-05-19
**实验**: 8b_cell_c_episode (v1) 和 8b_cell_c_episode_v2
**服务器**: westd-47453, 4x RTX PRO 6000 96GB
**模型**: Qwen3-8B (hidden=4096, intermediate=12288, layers=36, vocab=151936)

---

## 1. 根因分析

### 1.1 核心问题：`ppo_max_token_len_per_gpu` 完全无效

**v2 的 fix 是一个 no-op。** 原因：

```python
# dp_actor.py lines 297-303
elif self.config.use_dynamic_bsz:                              # ← 必须为 True
    max_token_len = self.config.ppo_max_token_len_per_gpu * ...  # ← 才走这条路
    micro_batches, _ = rearrange_micro_batches(...)
else:                                                           # ← 实际走了这里
    micro_batches = mini_batch.split(self.config.ppo_micro_batch_size_per_gpu)
```

Config 中 `use_dynamic_bsz: False`（默认值），所以 micro-batch 拆分完全由 `ppo_micro_batch_size_per_gpu=1` 决定。`ppo_max_token_len_per_gpu` 不论设什么值都不会被读取。

**证据**：两次实验的 config dump 确认 v1 为 32768、v2 为 16384，但 OOM 错误的内存数字完全一致：
- Tried to allocate: **8.76 GiB**
- Memory in use: **88.46-89.98 GiB**
- PyTorch allocated: **118.48 GiB**

### 1.2 OOM 发生阶段：actor backward pass

两次 crash 的 traceback 完全相同：

```
fsdp_workers.py:169 update_actor
  → dp_actor.py:468 loss.backward()
    → torch.autograd.graph._engine_run_backward
      → torch.OutOfMemoryError
```

这是 **PPO actor update 的 backward pass**，不是 rollout 或 ref log-prob 计算。所有 4 个 GPU worker 同时 OOM（pid 14119-14122 全部报错）。OOM 发生在 val_before_train 之后的第一个 training step。

### 1.3 8.76 GiB 分配的含义

8.76 GiB / 4 bytes(fp32) = ~2.35B elements。对应 logits gradient (1, seq_len, vocab_size)：
- 2.35B / 151936 = **~15,475 tokens**

这与 episode-level 全上下文模式下的实际序列长度一致（max_prompt_length=16384, 实际最长 episode 约 15K tokens + response）。

**结论**：backward 在计算 lm_head 层的 fp32 梯度时 OOM。logits 梯度张量 (1, ~15475, 151936) 在 fp32 下需要 8.76 GiB，但 GPU 仅剩 5-6 GiB 可用。

### 1.4 内存分解

Per-GPU 内存估算：

| 组件 | 大小(GiB) | 说明 |
|------|-----------|------|
| Actor FSDP shard (fp32) | ~8.2 | 8.19B params / 4 GPUs * 4 bytes |
| Actor gradients (fp32, 部分累积) | ~4-8 | backward 过程中逐层累积 |
| Ref model (CPU offload, GPU buffer) | ~1-2 | FSDP CPUOffload, pinned memory buffer |
| 36 layer checkpoint inputs (bf16) | ~4.6 | 36 * 15475 * 4096 * 2 bytes |
| Logits tensor (bf16) | ~4.7 | 15475 * 151936 * 2 bytes, 需保留供 backward |
| All-gathered layer (backward) | ~0.8 | 一层完整参数临时驻留 |
| FSDP 通信 buffer | ~3-5 | all-gather + reduce-scatter 预分配 |
| PyTorch allocator 碎片 | ~10-15 | FSDP 反复 alloc/free 导致碎片化严重 |
| CUDA context + misc | ~2-3 | driver, streams, etc. |
| **合计** | **~90** | 匹配 OOM 报告的 88-90 GiB |

关键放大因素：
1. **model_dtype: fp32** -- 参数和梯度都用 fp32，是 bf16 的 2 倍
2. **序列长度 ~15K tokens** -- logits tensor 4.7 GiB (bf16)，梯度 8.76 GiB (fp32)
3. **FSDP allocator 碎片** -- 118 GiB total allocated vs 90 GiB active，~28 GiB 碎片

### 1.5 为什么 1.7B 能跑但 8B 不行

| | 1.7B (exp029) | 8B (cell_c) |
|--|---------------|-------------|
| 参数量 | ~1.7B | 8.19B (4.8x) |
| hidden_dim | 2048 | 4096 (2x) |
| num_layers | 24 | 36 (1.5x) |
| GPU 数 | 2 | 4 |
| 每 GPU param shard (fp32) | ~3.4 GiB | ~8.2 GiB |
| 每 GPU gradient (fp32) | ~3.4 GiB | ~8.2 GiB |
| Per-layer 激活内存 | ~0.5x | 1x |
| GPU 余量 (95 GiB) | 充足 | ~5 GiB (不够 8.76 GiB logits grad) |

---

## 2. 配置对比

| 参数 | v1 (OOM) | v2 (OOM) | 差异 |
|------|----------|----------|------|
| ppo_max_token_len_per_gpu | 32768 | **16384** | 已改，但 no-op |
| log_prob_max_token_len_per_gpu | 默认 | **16384** | 已改 |
| use_dynamic_bsz | False | False | **未改，是根因** |
| param_offload | False | False | 未改 |
| PYTORCH_CUDA_ALLOC_CONF | 无 | expandable_segments:True | 已改，未能解决 |
| OOM 内存数字 | 88.46 GiB used | 88.46-89.98 GiB used | **基本一致** |
| OOM 位置 | dp_actor.py:468 | dp_actor.py:468 | **完全相同** |

---

## 3. 修复方案

### 方案 A：保守修复（推荐优先尝试）

改动最小，解决核心瓶颈：

```yaml
actor_rollout_ref:
  actor:
    use_dynamic_bsz: True               # 让 ppo_max_token_len 生效
    ppo_max_token_len_per_gpu: 8192      # 限制每 GPU token 总量
    fsdp_config:
      param_offload: True                # 省 ~8 GiB
      entropy_from_logits_with_chunking: True  # 分块计算 logits
      entropy_checkpointing: True         # checkpoint entropy 计算
```

**预期效果**：
- `param_offload: True` 将 actor params (~8.2 GiB) offload 到 CPU，释放 ~8 GiB
- 8 GiB (freed) + 5 GiB (原有 free) = 13 GiB > 8.76 GiB (logits grad)
- `use_dynamic_bsz: True` 让 token limit 真正生效作为安全网
- `entropy_from_logits_with_chunking` 分块处理 logits 进一步降低峰值

**代价**：训练速度降低约 10-20%（CPU-GPU 传输开销）

### 方案 B：激进优化（如果方案 A 仍然紧张）

在方案 A 基础上缩减序列长度：

```yaml
agent_proxy:
  max_prompt_length: 8192               # 从 16384 减半

actor_rollout_ref:
  actor:
    use_dynamic_bsz: True
    ppo_max_token_len_per_gpu: 8192
    fsdp_config:
      param_offload: True
      entropy_from_logits_with_chunking: True
      entropy_checkpointing: True
  rollout:
    max_model_len: 12288                # 配合缩短
    max_num_batched_tokens: 12288
```

**预期效果**：
- max_prompt_length 8192 -> 最长序列 ~9216 tokens (vs ~15475)
- Logits grad: 9216 * 151936 * 4 = **5.2 GiB** (vs 8.76 GiB)
- 加上 param_offload: GPU 余量 > 15 GiB

**代价**：长 episode (>8K tokens prompt) 会被截断。但 ALFWorld 平均 episode ~1464 tokens，绝大多数不受影响。

### 方案 C：如需保持 16K prompt 且不降速

```yaml
actor_rollout_ref:
  model:
    use_remove_padding: true             # 需 flash-attn 已安装
  actor:
    use_dynamic_bsz: True
    ppo_max_token_len_per_gpu: 8192
    fsdp_config:
      param_offload: True
      entropy_from_logits_with_chunking: True
      entropy_checkpointing: True
      model_dtype: bfloat16              # 参数梯度用 bf16，各减半
```

**预期效果**：`model_dtype: bfloat16` 将参数和梯度内存各减半 (8.2->4.1 GiB)。`use_remove_padding` 去掉 padding tokens 的无效计算。组合省下 ~12-16 GiB。

**代价**：bf16 梯度可能影响训练稳定性（8B 模型一般没问题）。需确认 flash-attn 已安装。

---

## 4. 预估修复后内存用量（方案 A）

| 组件 | 修复前(GiB) | 修复后(GiB) |
|------|------------|------------|
| Actor params | 8.2 | ~0.8 (per-layer 临时加载) |
| Actor gradients | 8.2 | 8.2 (不变) |
| Ref model | ~1-2 | ~1-2 (不变) |
| Checkpoint inputs | 4.6 | 4.6 (不变) |
| Logits (chunked) | 4.7 | ~1-2 (分块处理) |
| Communication buffers | 3-5 | 3-5 (不变) |
| FSDP 碎片/cache | 10-15 | ~5-8 (碎片减少) |
| CUDA context | 2-3 | 2-3 (不变) |
| **总计** | **~90** | **~27-35** |
| **logits grad 峰值需求** | 8.76 | 8.76 |
| **GPU 余量** | ~5 (不够) | **~52-60 (充足)** |

---

## 5. 推荐实施顺序

1. **先试方案 A**：改 5 个参数（use_dynamic_bsz + param_offload + entropy chunking），改动最小
2. 如果方案 A 仍 OOM -> 加方案 B 的 `max_prompt_length: 8192`
3. 如果需要极致优化 -> 方案 C 的 `model_dtype: bfloat16` + `use_remove_padding`

# research verl gradient accumulation

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verl_gradient_accumulation_20260521T084708_result.json`
- **Structured JSON:** [`9f9639e1f96033b78a38.json`](../../sessions/9f/9f9639e1f96033b78a38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是全部产出：

---

## 1. verl 原生支持 gradient accumulation

**支持，且当前配置已在使用。** verl 的 PPO/GRPO 训练有三层 batch 嵌套：

```
train_batch_size = 128 (16 env_groups × 8 group_size)
  └─ ppo_mini_batch_size = 16  → 8 个 mini-batch/epoch
       └─ ppo_micro_batch_size_per_gpu = 1  → 16 个 micro-batch/mini-batch
            梯度在 16 个 micro-batch 间累积
            每个 mini-batch 结束后 optimizer.step()
```

核心代码在 `verl/workers/actor/dp_actor.py` 的 `update_policy` 方法：每个 mini-batch 被 split 成 `ppo_micro_batch_size_per_gpu=1` 的 micro-batch，逐个 forward/backward 累积梯度，最后一次性 `_optimizer_step()`。

## 2. ppo_mini_batch_size 的作用

**它就是 gradient accumulation 的单元。** 当前配置：

- 每次 optimizer step 处理 `ppo_mini_batch_size=16` 个样本
- 但 GPU 上每次只有 `micro_batch_size_per_gpu=1` 个样本做 forward/backward
- 等效于 accumulation_steps=16

这意味着训练侧 GPU 内存与 train_batch_size=64 还是 128 **无关**——full batch 先 `data.to("cpu")`，只有 micro-batch=1 上 GPU。

## 3. Seed 4 GPU 内存状态

| 时间点 | GPU 0 | GPU 1 | 阶段 |
|--------|-------|-------|------|
| 第一次检查 | 38,481 / 97,887 MiB | 38,047 / 97,887 MiB | 初始化(vLLM加载) |
| 第二次检查 | 4,715 / 97,887 MiB | 4,715 / 97,887 MiB | val 完成，training step 0/15 即将开始 |

当前状态：刚完成 val_before_train，Training Progress 0/15。内存将在第一个 training step（rollout + update）时冲高。

之前 batch=64 峰值 97,104/97,887 MiB (99.2%)，余量仅 783 MiB。

## 4. batch=128 OOM 风险评估

**训练侧不会 OOM**（micro-batch=1，GPU 占用不变）。风险在 **rollout 阶段**：

- 128 个 episode 的 rollout 数据（token sequences、KV cache）比 64 大
- vLLM `gpu_memory_utilization: 0.35` 限制了 KV cache 占用
- 但如果 128 个 episode 产生更长的 token 序列（max_turn=50），可能超出 KV cache 容量
- **RAGEN 的 multi-turn rollout 是逐 turn 调用 vLLM，不是一次性生成全部**，所以并发量取决于 group 内并行度

结论：**有 OOM 风险但不确定**，需要观察第一个 training step 的峰值内存。

## 5. 如果 OOM，替代方案

Director 提议的 "micro_batch=64, accumulation_steps=2" **不直接对应 verl 的任何配置**。verl 的训练侧 gradient accumulation 已经在用了。真正的问题是 rollout 阶段的内存。

可行方案（按推荐顺序）：

1. **降 env_groups 到 8**（batch=64），保持现有 mini-batch/micro-batch 不变——最安全
2. **降 `gpu_memory_utilization` 到 0.30**，给 training 阶段腾出更多 GPU 内存
3. **开启 `optimizer_offload: true`**，将 optimizer state 放 CPU（当前为 false）
4. **降 `ppo_max_token_len_per_gpu`**（当前 65536），减少 training 阶段 activation 内存
5. **降 `response_length`**（当前 1024），减少 KV cache 压力

如果 Director 坚持要有效 batch=128 但避免 OOM，最可行的组合是：**env_groups=8, group_size=8 (batch=64) + total_training_steps 减半 + 减小 learning rate**——在语义上近似 batch=128 的效果，但不完全等价（GRPO advantage normalization 在 batch=64 内计算，会有差异）。

## GPU 型号

**NVIDIA RTX PRO 6000 Blackwell Server Edition**, 97,887 MiB (≈96GB) × 2

---

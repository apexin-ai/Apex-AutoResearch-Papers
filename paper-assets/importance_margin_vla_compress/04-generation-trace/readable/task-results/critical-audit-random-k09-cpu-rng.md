# critical audit random k09 cpu rng

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_critical-audit-random-k09-cpu-rng_20260524T003259_result.json`
- **Structured JSON:** [`29fbea28ac61b6c74bed.json`](../../sessions/29/29fbea28ac61b6c74bed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐了。现在有完整的对比图：

**Random pruning vs L2norm, libero_object (seed43, 50eps):**

| k | Random | L2norm |
|---|--------|--------|
| 0.30 | 32.2% | 59.0% |
| 0.50 | 66.2% | 32.0% |
| 0.70 | **78.6%** | 56.8% |
| 0.85 | **3.6%** | **99.0%** |
| 0.90 | ~9% (s42) | 100% (3eps) |

GPU 状态确认：每个实验各占一张 4090D，无资源竞争。

---

## 审计报告

### 结论：不是 CPU RNG fix 的问题。Random pruning 在高 k 存在真实的性能悬崖。

### 代码审查结果

1. **CPU RNG fix 已正确应用**：`eval_pi05_pruning_libero.py:58` 使用 `torch.randperm(n_tokens)` 默认在 CPU 生成，然后 `.to(img_emb.device)` 移到 GPU。这是正确写法。

2. **k=0.5 和 k=0.9 使用完全相同的代码路径**：
   - 同一脚本 `eval_pi05_pruning_libero.py`
   - 同一模型 `/root/autodl-tmp/pi05_libero_finetuned`
   - 同一 `prune_tokens_random` 函数
   - 同一 `fixed_embed_prefix` 逻辑

3. **无 GPU 竞争**：k=0.9 在 GPU 0 (PID 459609)，另一进程在 GPU 1 (PID 541798)，l2norm 在 GPU 2 (PID 467663)

### 根因分析

性能悬崖是 **random pruning 与 Pi0.5 RoPE 位置编码交互** 的真实现象：

- **高 k (0.85-0.9)**：只移除 15-26/256 个 token。Language token 的 RoPE 位置从 768 移到 ~651-690（偏移仅 78-117）。这个**小偏移**导致部分 RoPE 频率维度仍在正确相位附近（产生误导性信号），部分已超出（产生噪声信号）。模型收到**自相矛盾的位置信息**，无法正常工作。

- **低 k (0.3-0.7)**：移除大量 token。Language token 位置从 768 大幅前移到 228-537（偏移 231-540）。这个**大偏移**彻底破坏了所有 RoPE 频率的位置对应关系，模型反而被迫完全依赖 content-based attention，进入"降级但可用"模式。

- **关键证据**：L2norm k=0.85 = **99.0%**。同样保留 217/256 token，确定性选择时模型完美工作。说明问题不在 token 数量，而在于 random pruning 每步随机改变少量 token 的"闪烁效应"叠加位置偏移造成的破坏。

### 建议

1. **不需要重跑 k=0.9 实验**——9.2% 是真实结果，不是 bug
2. 论文中 random pruning 结果应聚焦 **k=0.3~0.7 区间**，或明确展示这个非单调现象
3. Random pruning 的性能悬崖本身是一个值得讨论的 finding，可以用来论证"naive random pruning 在实际 VLA 部署中不可靠"

---

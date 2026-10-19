# probe v6 checkpoint 10000 probe a

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_probe_v6-checkpoint-10000-probe-a_20260516T095005_result.json`
- **Structured JSON:** [`97dd650ecf5355107d6a.json`](../../sessions/97/97dd650ecf5355107d6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Probe A 结果：❌ conditioning 名存实亡

| 指标 | 数值 |
|------|------|
| Probe A cos (min) | **0.9999** |
| Probe A cos (max) | **1.0000** |
| bit_identical | False (但 cos ≈ 1.0) |

**判定：cos > 0.95 → conditioning 名存实亡 ❌**

脚本 verdict 也确认：**"scorer IGNORES language instruction (architecturally + empirically)"**

Probe B 同样 cos ∈ [0.998, 0.999]，importance map 跨任务几乎一致，是 spatial position prior 而非 action-conditioned selection。

### 初步原因分析

三个任务的 scorer weights 均值都在 0.51 附近、std ~0.47，换不同 language instruction 后 cos > 0.9999。说明 language embedding 虽然通过 `condition_source=language` 路径传入了 scorer，但：

1. **Gradient flow 可能断了** — language embedding 经 scorer MLP 后对 logits 的贡献极小，可能被 visual features 的量级淹没。需要检查 scorer 的 `task_proj` 层梯度范数是否 ≈ 0。
2. **信息瓶颈 loss 主导** — alpha/beta 正则项可能把 scorer 推向忽略 conditioning signal 的 trivial solution（均匀 ~0.5 权重），因为"不依赖 language"是最小化 mutual information 的简单策略。
3. **Architecture 问题** — scorer 的 conditioning 实现可能是 additive/concatenation 方式，language embedding 维度远小于 visual token 维度，被压制。

### 完整 Probe 输出

```
Probe A: fixed image, swap instruction
  inst='pick up the bbq sauce...'      w[mean=0.5122 std=0.4668]
  inst='pick up the black bowl next...' w[mean=0.5150 std=0.4651]
  inst='pick up the black bowl in...'   w[mean=0.5167 std=0.4636]
  pair (0 vs 1): cos=0.999960  l2=0.070474
  pair (0 vs 2): cos=0.999920  l2=0.100317
  pair (1 vs 2): cos=0.999988  l2=0.038678

Probe B: natural cross-task obs
  pair (0 vs 1): cos=0.998252  l2=0.467178
  pair (0 vs 2): cos=0.998437  l2=0.437578
  pair (1 vs 2): cos=0.999146  l2=0.325844

VERDICT: scorer IGNORES language instruction
```

另外注意：GPU 0 上有 4 个重复的 v6 训练进程（PID 920698/920699/920700/920702），与主进程 866194 写同一 output_dir，这是 C001 约束的违规场景。这些进程目前未占用 GPU 显存（nvidia-smi 只显示 866194），可能是 data loader workers，但建议确认。

---

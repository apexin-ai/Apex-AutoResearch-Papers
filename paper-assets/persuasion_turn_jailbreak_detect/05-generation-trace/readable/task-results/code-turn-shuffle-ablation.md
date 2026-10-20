# code turn shuffle ablation

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_turn-shuffle-ablation_20260520T090831_result.json`
- **Structured JSON:** [`3379cd9a1eb2d4e20bc6.json`](../../sessions/33/3379cd9a1eb2d4e20bc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果如下：

```
Turn-Shuffle Ablation Results:

=== IID Test (76 samples) ===
9-class:
  Original:  F1 = 1.0000±0.0000 (seeds 42/123/456)
  Shuffled:  F1 = 1.0000±0.0000 (9 runs)
  Δ = +0.0000

vanilla:
  Original:  F1 = 1.0000±0.0000
  Shuffled:  F1 = 0.9883±0.0097
  Δ = -0.0117

=== DD OOD (118 samples) ===
9-class:
  Original:  F1 = 0.9872±0.0045
  Shuffled:  F1 = 0.9882±0.0040
  Δ = +0.0011 (基本无变化)

vanilla:
  Original:  F1 = 0.9268±0.0362
  Shuffled:  F1 = 0.8388±0.0515
  Δ = -0.0880 (显著下降)

=== AA OOD (118 samples) ===
9-class:
  Original:  F1 = 0.9457±0.0566
  Shuffled:  F1 = 0.9386±0.0557
  Δ = -0.0071 (几乎无变化)

vanilla:
  Original:  F1 = 1.0000±0.0000
  Shuffled:  F1 = 0.9798±0.0121
  Δ = -0.0202
```

**结论**：
- **9-class (DAPT)**: Shuffle 后 F1 几乎不变（所有数据集 Δ < 0.01），说明 9-class 模型**不依赖轮次顺序**——turn-level 的 persuasion strategy 特征已足够区分，GRU 的顺序建模贡献极小
- **vanilla**: DD OOD 上 shuffle 导致 F1 下降 8.8 个百分点（0.927→0.839），AA OOD 和 IID 下降 1-2 个百分点。vanilla 模型**部分依赖轮次顺序**，尤其在 OOD 场景下

这支持了论文的核心论点：DAPT 学到的 persuasion strategy 特征比纯序列建模更鲁棒，因为 shuffle 不影响 turn-level 特征的判别力。

结果已保存到 `/root/persuasion_turn_jailbreak_detect/results/turn_shuffle_ablation.json`。

---

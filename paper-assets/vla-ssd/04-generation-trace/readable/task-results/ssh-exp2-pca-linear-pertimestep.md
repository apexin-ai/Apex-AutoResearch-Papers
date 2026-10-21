# ssh exp2 pca linear pertimestep

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp2-pca-linear-pertimestep_20260515T192148_result.json`
- **Structured JSON:** [`c19a18f95162e8379762.json`](../../sessions/c1/c19a18f95162e8379762.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果如下：

```
=== PCA-1024 + Linear Probe Per-Timestep ===
  Bin        Range    Trained  Untrained       DINO     Δ(T-U)
    0    [0.0,0.1)     0.9992     1.0000     0.3540     -0.1pp
    1    [0.1,0.2)     1.0000     1.0000     0.7662     +0.0pp
    2    [0.2,0.3)     1.0000     1.0000     0.8244     +0.0pp
    3    [0.3,0.4)     1.0000     1.0000     0.8676     +0.0pp
    4    [0.4,0.5)     1.0000     1.0000     0.8575     +0.0pp
    5    [0.5,0.6)     1.0000     1.0000     0.8903     +0.0pp
    6    [0.6,0.7)     1.0000     1.0000     0.9618     +0.0pp
    7    [0.7,0.8)     1.0000     1.0000     0.9574     +0.0pp
    8    [0.8,0.9)     1.0000     1.0000     0.9690     +0.0pp
    9    [0.9,1.0)     1.0000     1.0000     0.9676     +0.0pp

Overall: trained=0.9999, untrained=1.0000, dino=0.8397
```

**Gate: FAIL** — t=0 bin Δ(trained-untrained) = -0.1pp，远低于 15pp 阈值。

关键发现：
- trained VLA 和 untrained VLA 的 PCA-1024 + linear probe 在所有 timestep bin 上都接近 100% accuracy（包括 t=0）
- 两者之间几乎没有差异，untrained 甚至略高
- DINO 整体 83.97%，t=0 最低（35.4%），随 timestep 递增到 ~97%，符合预期（早期帧 goal 信息少）

这说明 PCA-1024 + linear probe 的分类能力太强，对 VLA 特征（4096→1024）来说 goal 分类过于简单，trained/untrained 的差异在这个 probe 下无法体现。DINO 的 per-timestep 梯度是有意义的信号。

JSON 已保存到 `/root/autodl-tmp/vla-ssd/results/pca1024_linear_pertimestep.json`。

---

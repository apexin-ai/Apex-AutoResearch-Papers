# monitor exp002v3 r1 check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp002v3-r1-check_20260519T183451_result.json`
- **Structured JSON:** [`d366813cad96c0c7576e.json`](../../sessions/d3/d366813cad96c0c7576e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Log has 7 steps, 2 ranks per step. No grad_norm/entropy fields in this log. Let me compile the analysis.

```
进程状态：存活（GPU 利用率 65-70%，4卡均有显存占用）
当前步数：7（最新 02:35:38，~35s/step）
GPU 0 显存：25582 MiB / 32607 MiB (78%)
GPU 1 显存：24288 MiB / 32607 MiB (74%)
GPU 2 显存：21494 MiB / 32607 MiB (66%)
GPU 3 显存：24824 MiB / 32607 MiB (76%)

⚠️ 注意：tmux 日志显示之前有一次 crash（02:07，TypeError: compute_rewards() takes 5 positional arguments but 7 were given），当前运行是重启后的（02:31 启动）。

=== R1 信号分析 (step 1-7，双 rank 平均) ===

逐步 R1 mean（rank0 / rank1 / 平均）:
step 1: R1=-0.2694 / -0.0124 / avg=-0.1409, R3=0.9975, combined=0.5422
step 2: R1=-0.0695 / -0.2964 / avg=-0.1830, R3=0.9977, combined=0.5255
step 3: R1=-0.0779 / -0.0759 / avg=-0.0769, R3=0.9760, combined=0.5548
step 4: R1=-0.1757 / -0.3358 / avg=-0.2558, R3=0.9949, combined=0.4946
step 5: R1=-0.0205 / -0.1654 / avg=-0.0930, R3=0.9985, combined=0.5619
step 6: R1=+0.1160 / -0.4015 / avg=-0.1428, R3=0.9987, combined=0.5421
step 7: R1=-0.0484 / -0.2527 / avg=-0.1506, R3=0.9985, combined=0.5389

汇总 (step 5-7):
- R1 mean: -0.1288（趋势：平稳偏负，无改善迹象）
- R1 正值率: 16.7%（6 个 rank 观测中仅 1 个 > 0，即 step 6 rank 0 的 +0.116）
- R1 占 combined 比例: -9.4%（R1 是负贡献，拉低 combined）
- R3 mean: 0.9986（saturation 风险：是，持续 > 0.99）
- per-strength R1 (step 5-7 所有 rank):
    weak  = -0.053（最好，偶有正值 +0.21~+0.36）
    medium= -0.164
    strong= -0.305（最差，全部为负）

异常检测:
- grad_norm: 日志中无此字段
- entropy: 日志中无此字段

结论: ⚠️ R1 无效，需立即汇报 Director
```

**关键判断依据：**

1. **R1 均值 -0.129（step 5-7）**，比 exp002v2-recalib 的 -0.064 更差。scaled cosine (scale_factor=5) 不仅没有产生正信号，反而放大了负值。
2. **R1 正值率 16.7%**，虽然比 exp002v2-recalib 的 5% 有提升，但远不足以驱动有效训练。
3. **R3 完全饱和（>0.998）**，combined reward 几乎被 R3 主导，R1 信号在梯度中被淹没。
4. **Strong strength R1 全负（-0.305）**，说明方向向量对强校准偏移的样本产生了系统性惩罚，方向可能需要反转或重新提取。
5. **rank 间方差极大**（step 6: +0.116 vs -0.402），说明 R1 信号高度不稳定，batch 随机性主导。

---

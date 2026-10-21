# ops snapshot 95k and 031b check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_snapshot_95k_and_031b_check_20260520T225846_result.json`
- **Structured JSON:** [`0bdf2fccc0ef92d505ae.json`](../../sessions/0b/0bdf2fccc0ef92d505ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== bjb1-40020 ===
exp_029d: step=100K (已完成), eval=349.6 @95K, NVE=0.666 @95K (峰值0.855 @85K)
  eval 轨迹: 5K→31.7, 15K→159.1, 25K→155.7, 35K→190.8, 45K→137.1,
             55K→210.7, 65K→189.5, 75K→253.2, 85K→259.5, 95K→349.6
  NVE 轨迹:  15K→0.02, 25K→0.17, 35K→0.31, ..., 85K→0.86, 95K→0.67
  gate: dt=2 固定（dt_2_frac=1.0 全程，未学到自适应）
GPU: cuda:0=20%/3GB  cuda:1=24%/3GB  (两卡均空闲，exp_029b 已释放确认)

=== bjb1-45299 ===
exp_031b: step=9.6K, eval=2.4 @2.5K (早期，无 ve_ratio 数据)
exp_031:  step=195.6K, eval=11.6 @192.5K (峰值28.6 @162.5K，近期下滑)
GPU: cuda:0=97%/8.6GB  cuda:1=18%/2.8GB
```

**要点**：
- exp_029d 训练完成100K，eval @95K 达到 349.6 表现不错，但 gate 全程锁在 dt=2 没有分化
- exp_031b 刚起步，还在初始化阶段
- exp_031 跑了 195K 但 PickCube eval 在低位震荡（峰值仅 28.6），效果不理想

---

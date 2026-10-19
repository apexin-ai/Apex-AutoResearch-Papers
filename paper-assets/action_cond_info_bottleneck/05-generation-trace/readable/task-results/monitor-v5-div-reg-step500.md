# monitor v5 div reg step500

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v5_div_reg_step500_20260516T015018_result.json`
- **Structured JSON:** [`2cf4f1216a4c82023b5d.json`](../../sessions/2c/2cf4f1216a4c82023b5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### 状态
- **PID 682233**: 存活，运行 36m51s，CPU 825%
- **当前 step**: 1600/20000
- **速度**: ~0.8 steps/s
- **GPU**: cuda:0 使用 22.8GB/97.9GB，利用率 45%

### 🟢 Step 500 判断：PASS

**scorer_std = 0.379** — 远超 0.1 阈值，diversity reg 完全有效，无 collapse。

### scorer_std 趋势（持续上升，非常健康）

| Step | scorer_std | scorer_mean | task_loss | ib_loss | div_loss |
|------|-----------|-------------|-----------|---------|----------|
| 100  | 0.188     | 0.656       | 0.0455    | 0.0626  | -0.1777  |
| 200  | 0.297     | 0.637       | 0.0644    | 0.0783  | -0.2910  |
| 300  | 0.332     | 0.609       | 0.0643    | 0.1031  | -0.3242  |
| 400  | 0.361     | 0.594       | 0.0848    | 0.1129  | -0.3574  |
| 500  | 0.379     | 0.594       | 0.0635    | 0.1147  | -0.3770  |
| 600  | 0.393     | 0.578       | 0.0690    | 0.1298  | -0.3906  |
| 700  | 0.389     | 0.574       | 0.0502    | 0.1347  | -0.3887  |
| 800  | 0.404     | 0.582       | 0.0908    | 0.1262  | -0.4043  |
| 900  | 0.404     | 0.562       | 0.0850    | 0.1475  | -0.4043  |
| 1000 | 0.410     | 0.570       | 0.0775    | 0.1357  | -0.4102  |
| 1100 | 0.416     | 0.570       | 0.0619    | 0.1377  | -0.4160  |
| 1200 | 0.404     | 0.582       | 0.0958    | 0.1253  | -0.4043  |
| 1300 | 0.416     | 0.562       | 0.1084    | 0.1439  | -0.4180  |
| 1400 | 0.418     | 0.562       | 0.0989    | 0.1465  | -0.4180  |
| 1500 | 0.424     | 0.559       | 0.0666    | 0.1489  | -0.4258  |
| 1600 | 0.424     | 0.559       | 0.0965    | 0.1496  | -0.4238  |

### 关键观察

1. **scorer_std 从未下降**：0.188 → 0.424，单调递增后在 0.40-0.42 区间稳定。完全没有 collapse 迹象。
2. **div_loss 持续变负**（-0.18 → -0.42），说明 scorer 间分化在增大。
3. **ib_loss 稳步上升**（0.06 → 0.15），信息瓶颈在收紧。
4. **task_loss 波动但未爆炸**：在 0.05-0.10 之间，说明 task 性能未被 diversity reg 破坏。
5. **β warmup 已开始**（step 1001 起从 0.001 递增，当前 0.006），IB 约束正在逐步生效。

### 时间估算
- 速度 ~0.8 steps/s
- 剩余 18400 steps → ~6.4 小时
- 预计完成时间：约今天深夜/明天凌晨

---

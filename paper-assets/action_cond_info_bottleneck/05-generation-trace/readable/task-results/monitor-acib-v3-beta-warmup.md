# monitor acib v3 beta warmup

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_acib_v3_beta_warmup_20260515T235855_result.json`
- **Structured JSON:** [`fdedea98ea8829847764.json`](../../sessions/fd/fdedea98ea8829847764.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程存活，已运行 31:52，当前在 step 2100。以下是分析：

## 最近日志指标（每 100 步采样）

| Step | task_loss | ib_loss | β | total_loss |
|------|-----------|---------|---|------------|
| 900 | 0.0839 | 0.0122 | 0.0000 | 0.0839 |
| 1000 | 0.0762 | 0.0243 | 0.0000 | 0.0763 |
| 1100 | 0.0590 | 0.0147 | 0.0010 | 0.0591 |
| 1200 | 0.0926 | 0.0014 | 0.0020 | 0.0926 |
| 1300 | 0.1093 | 0.0014 | 0.0030 | 0.1094 |
| 1400 | 0.0992 | 0.0019 | 0.0040 | 0.0992 |
| 1500 | 0.0625 | **-0.0001** | 0.0050 | 0.0625 |
| 1600 | 0.0919 | 0.0011 | 0.0060 | 0.0920 |
| 1700 | 0.1061 | 0.0009 | 0.0070 | 0.1062 |
| 1800 | 0.0965 | **-0.0000** | 0.0080 | 0.0965 |
| 1900 | 0.0943 | 0.0001 | 0.0090 | 0.0944 |
| 2000 | 0.0727 | 0.0004 | 0.0100 | 0.0727 |
| 2100 | 0.0672 | **-0.0001** | 0.0100 | 0.0672 |

## 判断：🚨 异常 — IB loss collapse

**β warmup 已完成**（step 2000 时 β 达到目标值 0.01）。

**IB loss 发生了 collapse：**
- β=0 阶段（step 100-1000）：IB loss 在 0.002~0.06 范围波动，说明 bottleneck 有信息流过
- β 开始 ramp（step 1100 起）：IB loss 立刻从 0.0147 → 0.0014，随后迅速趋向 0
- Step 1500+ 之后：IB loss 在 0 附近甚至出现负值（-0.0001），bottleneck 已完全 collapse

**这和 v1 的 scorer collapse 是同一模式**——一旦 β 对 IB loss 施加惩罚，模型立刻学会让 scorer 输出均匀权重（或常数），使 mutual information → 0，信息瓶颈形同虚设。

**Task loss 未恶化**（始终在 0.05~0.11 波动），但这恰恰印证了 collapse：IB 约束没有生效，模型退化为普通训练，task loss 当然不会变差。

---

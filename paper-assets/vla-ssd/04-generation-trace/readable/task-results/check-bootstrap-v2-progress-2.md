# check bootstrap v2 progress 2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_v2_progress_2_20260523T012937_result.json`
- **Structured JSON:** [`6baa572422c58bbaf65d.json`](../../sessions/6b/6baa572422c58bbaf65d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Bootstrap v2 进度：2/20 完成

### GPU 状态
| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 0% | 2135 MiB | cuda0 进入 bootstrap 阶段（1000 iter, 100 workers） |
| 1 | 8% | 12621 MiB | cuda1 还在 extraction（1250/5000 samples, task 2/10） |

### 已完成结果

| arch | suite | cond | peak R² | peak layer | exit R² | exit layer | delta | CI 95% | boot mean±std |
|------|-------|------|---------|------------|---------|------------|-------|--------|---------------|
| **openvla** | goal | trained | 0.4556 | L1 | 0.3395 | L31 | 0.116 | [-0.253, -0.012] | -0.142±0.065 |
| **tracvla** | goal | trained | 0.5399 | L13 | 0.2065 | L31 | 0.333 | [0.055, 0.342] | 0.167±0.073 |

两个都是 n_demos=100, n_samples=5000, n_bootstrap=1000。

关键对比：
- **TracVLA** goal-trained 的 peak→exit 下降显著（delta=0.333, CI 不含 0），目标信息在深层大幅丢失（L27-L30 甚至为负）
- **OpenVLA** goal-trained 的 delta 较小（0.116），但 bootstrap CI 在负侧（[-0.253, -0.012]），说明 bootstrap 采样下 exit 实际常高于 peak — 层间变异大，信号不稳定

cuda0 当前在做 bootstrap 计算（即将完成下一个条件），cuda1 还在 extraction 早期阶段，整体预计还需较长时间完成全部 20 个条件。

---

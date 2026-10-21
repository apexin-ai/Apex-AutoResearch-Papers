# monitor exp 005 gen3

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp_005-gen3_20260517T173407_result.json`
- **Structured JSON:** [`c4785db240cb0e1bf097.json`](../../sessions/c4/c4785db240cb0e1bf097.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 在 93% 利用率，进程活跃。现在可以汇报完整状态。

---

## exp_005 状态报告

### 当前进度
**Gen 3/10，正在进行中**（GPU 0 利用率 93%，可能在训练或评估阶段）。Gen 3 checkpoint 尚未生成。

Gen 时间线（CST +0800）：
- Gen 0: 21:20 完成
- Gen 1: 22:45 完成（~1h25m/gen）
- Gen 2: 00:14 完成（~1h29m/gen）
- Gen 3: ~00:18 开始，已运行约 1h17m，预计还需 ~10-15min

### 已完成 Gen 的指标

| Gen | eff_rank | log_det | ppl | distinct4 | controller_ratio | triggered? |
|-----|----------|---------|------|-----------|-----------------|------------|
| 0 | 417.55 | **2366.68** (baseline) | 9.55 | 0.7414 | - | - |
| 1 | 476.93 | 2366.46 | 10.09 | 0.6608 | **0.5** | **No** |
| 2 | 486.85 | 2395.23 | 10.42 | 0.6149 | **0.5** | **No** |

### Controller 分析

Controller **从未触发**。原因：log_det 始终 ≥ baseline（2366.68）：
- Gen 1: 2366.46（仅低 0.22，远不够触发 tau=0.002 阈值）
- Gen 2: 2395.23（**高于** baseline +28.55）

ratio 始终保持默认值 0.5。

### 关键观察：k=20 稀释了 collapse 信号

虽然质量在退化（ppl ↑, distinct4 ↓），但频谱信号显示的是**扁平化而非坍缩**：
- Top-1 SV 急剧下降：1942 → 954 → 883
- 但 top 11-20 SVs 保持稳定
- k=20 的 log_det 聚合了太多稳定维度，**稀释了 top-SV 的坍缩信号**

这正是与 exp_006（k=10）对比的价值所在：k=10 应能更敏感地捕捉到 top-SV 的下降。

### D014 决策建议

controller_ratio = 0.5 < 0.53 → **技术上满足 D014 切换条件**。

但建议**不急于切换 cumulative 模式**，理由：
1. controller 未触发不是 per_gen 模式的问题，而是 **k=20 的信号本身不灵敏**
2. 这正是 sensitivity 分析需要的数据点——k=20 下 controller 不触发 vs k=10 下可能触发，说明 k 的选择对 EWS 系统至关重要
3. 切换到 cumulative 模式不会改善信号灵敏度（问题在 k 不在聚合模式）
4. 让实验跑完 10 gen，得到完整的"k=20 无干预退化曲线"，对论文更有价值

**建议**：保持 per_gen 模式让 exp_005 完整运行，作为 negative control / sensitivity 对照组使用。预计还需 ~10-11 小时完成剩余 7 个 gen。

---

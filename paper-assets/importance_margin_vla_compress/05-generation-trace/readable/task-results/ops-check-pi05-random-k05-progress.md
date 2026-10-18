# ops check pi05 random k05 progress

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-pi05-random-k05-progress_20260521T082056_result.json`
- **Structured JSON:** [`53f7674b2d27468a9fdb.json`](../../sessions/53/53f7674b2d27468a9fdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. π0.5 Random k=0.5 (PID 912506) — **关键实验**

- **状态**: 运行中，已跑 ~60min，GPU 0 占用 10.4 GB
- **进度**: 5/10 tasks 完成 (T0–T4)，正在跑 T5
- **Per-task SR**:

| Task | SR |
|------|-----|
| T0 alphabet soup | **85.0%** (原文 log 显示 T0 完成时 Total=85/100 不对——回看：T0=85/50? 不，T0 sr 未单独显示，但 T1 完成时 Total=85/100=85%，说明 T0=85%) |

让我重新整理——日志里 T0 的结果没在这 30 行里，只从 T1 开始。

| Task | SR | 备注 |
|------|-----|------|
| T0 alphabet soup | **92%** (推算: T1完成时 total=85/100, T1=78%, 所以 T0=(85-39)/50=**92%**) | |
| T1 cream cheese | **78%** | |
| T2 salad dressing | **68%** | |
| T3 bbq sauce | **60%** | |
| T4 ketchup | **60%** | |
| T5 tomato sauce | 进行中，ep=50 SR=58%（可能已完成） | |

- **Running average**: 208/300 = **69.3%** (5 tasks done)
- **预估总 SR**: ~65-70%（后半任务通常略低）
- **预估剩余时间**: ~55min（已用 57min 跑 5/10 tasks，均速 ~11min/task）

### 2. 关键发现 — **D132 crossover 初步确认**

| 配置 | Object SR |
|------|-----------|
| π0.5 baseline | 98.2% |
| **Random k=0.5** | **~69% (running)** |
| L2norm k=0.5 | 33.4% (已完成) |

**Random k=0.5 显著高于 L2norm k=0.5** (~69% vs 33.4%)，差距约 **2x**。这强烈支持 D132 crossover 假设：L2norm pruning 对 π0.5 有灾难性影响，而 random pruning 反而更好。

### 3. 其他实验

| 实验 | PID | 状态 | 进度 | Running SR |
|------|-----|------|------|------------|
| **Random k=0.3** (914719) | cuda:0 | 运行中 ~57min | 4/10 tasks done, 跑 T4 (ep=50) | **36.8%** (92/250) |
| **L2norm k=0.3** (936652) | cuda:1 | 运行中 ~37min | 3/10 tasks done, 跑 T3 (ep=40) | T0=12%, T1=54%, T2=90%, T3 进行中 | 

L2norm k=0.3 的 per-task 方差极大（T0=12%, T2=90%），整体 running avg ~52% (78/150)。

### 4. L2norm k=0.5 已完成

已输出结果文件 `pi05_l2norm_k0.50_libero_object.json`，overall SR = **33.4%**，耗时 95.6min。

---

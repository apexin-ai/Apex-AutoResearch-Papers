# monitor ced step20 check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_ced-step20-check_20260514T084134_result.json`
- **Structured JSON:** [`f7703b7d5ec15065aa07.json`](../../sessions/f7/f7703b7d5ec15065aa07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练当前在 **step 16/189**，尚未到 step 20。已有 3 个 checkpoint（每 5 步记录一次）：

| Step | Format | F1 | CED | Truncation | Mean Length | Loss | Total Reward |
|------|--------|----|-----|------------|-------------|------|--------------|
| 5 | 0.554 | 0.0084 | 0.085 | 18.1% | 668 | 0.026 | 0.648 |
| 10 | **0.886** | 0.0120 | 0.048 | **6.9%** | 562 | 0.039 | 0.946 |
| 15 | 0.853 | **0.043** | **0.427** | 13.8% | 631 | 0.051 | **1.323** |

**GPU 状态**：4x RTX 5090，利用率 57-66%，显存 17.5-24.6 / 32.6 GB。正常。

### 分析

**积极信号：**
- **CED reward 爆发**：step 15 从 0.048 跳到 0.427（近 9 倍），模型开始学会提取证据句
- **Format reward 稳定在 ~0.85**：从 0.554 快速收敛，JSON 格式基本学会了
- **F1 上升 5 倍**：0.0084 → 0.043，虽然绝对值仍低，但趋势正确
- **Total reward 持续上升**：0.648 → 0.946 → 1.323

**需关注：**
- **截断率反弹**：step 10 降到 6.9%（好），但 step 15 回升到 13.8%。可能因为模型开始尝试输出更完整的证据（mean_length 从 562 回升到 631），导致部分长文档截断
- **F1 仍然很低（0.043）**，说明关系抽取准确率还很差，但 CED 的跳升表明方向对了

### 判断

**继续观察，暂不干预。** 理由：
1. Step 15 的 CED 和 F1 同时大幅改善，训练正在起效
2. 截断率 13.8% 低于初始的 18.1%，虽然反弹但不算失控
3. 现在停止会浪费已有的正向趋势，建议等 step 20-25 再评估

**预计时间**：当前 step time ~150s，step 20 约在 10 分钟后，全部 189 步约需再 **7.2 小时**（~23:50 服务器时间完成）。

---

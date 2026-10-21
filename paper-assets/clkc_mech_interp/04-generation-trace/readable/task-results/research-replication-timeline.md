# research replication timeline

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_replication-timeline_20260524T152049_result.json`
- **Structured JSON:** [`0d18045a1bbdb35674f3.json`](../../sessions/0d/0d18045a1bbdb35674f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是完整分析结果：

---

## 独立复现实验详情

```
测试层数：6 层（L12, L13, L14, L16, L18, L28）
覆盖深度范围：38%-88%（Llama-3.1-8B-Instruct 共 32 层）
样本量：N=201（独立采样，与原始 N=136 不重叠）
设备：NVIDIA RTX PRO 6000 Blackwell (westd-14391, 96GB)
      原始实验在 westd-41302 上运行
```

### 各层结果确认（从数据文件直接读取）

| 层 | Depth | Probe Acc | Best α | Best p | Bonf sig |
|----|-------|-----------|--------|--------|----------|
| L12 | 38% | 91.75% | α=+20 | 0.085 | 0/6 → --- |
| L13 | 41% | 90.00% | α=+10 | 0.000337 | 2/6 → ✓✓ |
| L14 | 44% | 91.75% | α=+10 | 0.00224 | 1/6 → ✓ |
| L16 | 50% | 91.50% | α=+10 | 0.005 | 1/6 → ✓ |
| L18 | 56% | 90.75% | α=+5 | 0.0099 | 0/6 → --- |
| L28 | 88% | 85.25% | α=+10 | 0.284 | 0/6 → --- |

## 时间线（从 registry 精确重建）

| 时间 | 事件 | 服务器 |
|------|------|--------|
| 5/22 08:08 | `steering_107`: 原始 L28 实验, N=136, **NEGATIVE** (p=0.74) | westd-41302 |
| 5/22 11:32 | `steering_107_L13`: 发现 L13 效应, N=136, **SUCCESS** (p=0.0009) | westd-41302 |
| 5/22 11:32 | `steering_107_L18`: L18 同时测试, N=136, **NEGATIVE** | westd-41302 |
| 5/23 10:01 | `steering_llama_L16_123`: L16 首测, N=136, **NEGATIVE** (p=0.12) | westd-41302 |
| 5/23 21:54 | `steering_llama_L12_124` + `L14_125`: 新数据 N=201, 开始 boundary sweep | westd-14391 |
| 5/23 23:04 | `steering_llama_L13_repl_126`: N=201 复现 L13, **SUCCESS** (p<0.001) | westd-14391 |
| 5/24 00:41 | `steering_llama_L16_127`: N=201 重跑 L16, **SUCCESS** (p=0.005) — 翻转！ | westd-14391 |
| 5/24 01:00 | `steering_llama_L18_128` + `L28_129`: N=201, 均 **NEGATIVE** | westd-14391 |

## 是否 Post-Hoc：是，但设计合理

**事实判断：boundary sweep 是在观察到原始 L13 结果（5/22）之后设计的（5/23-5/24）。** 这从时间线上无法否认。

**但以下设计特征区别于 post-hoc cherry-picking：**

1. **系统性 6 层扫描**：覆盖 38%-88% 完整梯度，不是只验证 L13
2. **包含预期负结果**：L12 (p=0.085) 和 L28 (p=0.284) 不显著——不是只报告正结果
3. **独立数据**：N=201 新采样 vs 原始 N=136，不是在同一数据上重复分析
4. **不同硬件**：westd-14391 (RTX PRO 6000) vs westd-41302
5. **意外新发现**：L16 从 negative (N=136, p=0.12) 翻转为 success (N=201, p=0.005)，归因于 probe quality 提升 (77%→91.5%)，这不是事先预期的结果
6. **L12 先于 L13 执行**：timestamps 显示 L12 和 L14 在 21:54 开始，L13 在 23:04——非先验证 L13 再补测其他层

**建议论文表述**：将 Appendix B 明确标注为 "follow-up boundary mapping experiment"（后续边界定位实验），说明它是在观察到 L13 效应后设计的系统性验证，而非预注册实验。这比暗示它是完全独立的设计更诚实，同时 6 层扫描+独立数据+负结果的设计特征足以回应 confirmation bias 质疑。

---

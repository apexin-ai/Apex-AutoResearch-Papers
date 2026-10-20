# analysis forward pass v2 report

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_forward-pass-v2-report_20260515T183511_result.json`
- **Structured JSON:** [`780c8cd13f1cab12677f.json`](../../sessions/78/780c8cd13f1cab12677f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

memory.md 已更新。以下是汇报：

---

## Forward Pass v2 (Trajectory-Level) 结果汇报

### v2 修复内容
v1 按 turn 级分类，每条注入轨迹仅 1/6.1 个 turn 有 error tag，导致 3911 个注入轨迹 turn 错归 clean 池。v2 改为 trajectory 级分类（clean=4358, injected=4671）。

### 关键数字

| 条件 | Clean Loss | Injected Loss | Gap (inj-clean) |
|------|-----------|---------------|-----------------|
| vanilla_full | 0.685 | — | — |
| taxei_full | 0.777 | 0.740 | **-0.037** |
| random_full | 0.764 | 0.685 | **-0.078** |
| taxei_10% | 0.664 | 0.647 | -0.017 |
| taxei_25% | 0.707 | 0.664 | -0.042 |
| taxei_50% | 0.851 | 0.819 | -0.033 |

### v1→v2 核心变化

1. **Dose-response 单调性消失**: v1 gap 10%=-0.016→25%=-0.127→50%=-0.197（单调递增），v2 修正为 10%=-0.017→25%=-0.042→50%=-0.033（非单调，25%>50%）。**v1 的单调 dose-response 是分类 bug 导致的假象**，gap 在 25%/50% 处缩小 3-6×。

2. **Random 记忆深于 TaxEI**: random gap(-0.078) = taxei gap(-0.037) 的 **2.1×**。随机注入轨迹被更深记忆，可能因无 taxonomy 标签使注入错误与正常轨迹结构更相似。

3. **保持不变的结论**: 注入样本仍被更深记忆（所有条件 gap<0）；50% 注入仍导致严重 clean loss 退化（+0.166 vs vanilla）；per-operator 分析（仅 tagged turns）不受影响——C1 最低(0.593)、C4 最高(0.630)。

4. **Per-operator 排序跨 dose 不稳定**: C4 在 3/4 条件下 loss 最高（最少记忆），但最低 operator 在 C1/P1/P2 间变动，v1 的"C1 一致最低"仅 taxei_full 成立。

### 对论文的影响
- 论文中 v1 的 "monotonic dose-response gap" 图表和叙述需要替换为 v2 数据
- "记忆越深 operator 对 clean task 损害越大" 的因果叙事需弱化为仅在 taxei_full 成立的 correlation
- 新增发现：Random 注入比 TaxEI 记忆更深，强化了 "taxonomy 标签无额外价值" 的主线

---

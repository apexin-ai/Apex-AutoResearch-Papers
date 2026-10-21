# analysis intervention leadlag

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_intervention_leadlag_20260519T044711_result.json`
- **Structured JSON:** [`57477b5a15155f480a60.json`](../../sessions/57/57477b5a15155f480a60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

## 分析 1: 5-method lead-lag

| 实验 | K>=3/5 | PermG (FDR) | 最强方法 |
|------|--------|-------------|---------|
| Predictive s42 (fp32) | 0/8 | 0/8 | diff_xcorr (8/8) |
| Reactive s42 (fp32) | **8/8** | **8/8** | diff/perm/ty 均 8/8 |
| Predictive s43 (bf16) | **8/8** | **8/8** | naive/pg 均 8/8 |
| Reactive s43 (bf16) | **8/8** | 5/8 | diff_xcorr (8/8) |

Predictive s42 信号最弱（gen 1 即干预截断了单调 collapse 轨迹），但 diff_xcorr 仍全部显著。Reactive s42 信号最强（全方法一致）。

## 分析 2: 效果量对比 + Bootstrap 95% CI

| 指标 | 中位数 | 95% CI |
|------|--------|--------|
| Peak PPL reduction (predictive vs reactive) | 56.8% | [28.5%, 63.7%] |
| Recovery speed gain | 1 gen | [1, 1] |
| Cumulative excess PPL reduction | 72.0% | [52.4%, 76.7%] |
| Final PPL difference | +0.11 (n.s.) | 两种策略收敛到相同水平 |

Reviewer 提到的 "63% ppl 降低" 在 s42 fp32 得到确认 (63.7%)，跨 seed pooled 估计为 58.3%。bf16 精度本身降低了 collapse 严重程度，使得 s43 的差异较小 (36.3%)。

三个产出文件已注册到 artifacts。

---

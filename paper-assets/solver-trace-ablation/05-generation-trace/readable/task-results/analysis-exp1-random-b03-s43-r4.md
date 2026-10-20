# analysis exp1 random b03 s43 r4

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp1-random-b03-s43-r4_20260515T043230_result.json`
- **Structured JSON:** [`8a4e787a6bd31bce232d.json`](../../sessions/8a/8a4e787a6bd31bce232d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。以下是完整报告：

---

## exp1-random-b03-s43-r4 完成报告

### 训练
- 500/500 步正常完成，耗时 1h42m
- 最终 loss=0.01365, prove_rate=0.5505, mean_isr=0.1358, parse_rate=1.0

### Eval 指标（proofwriter_fol_100.jsonl）

| 指标 | s43-r4 (本次) | s44-r2 (参考) |
|------|------|------|
| prove_rate | **0.92** | 0.23 |
| mean_isr | **0.1659** | 0 |
| proved_only_isr | 0.1803 | 0 |
| n_proved | 92/100 | 23/100 |
| H7 strict | 7/92 (7.6%) | 0/23 (0%) |
| H1 strict | 90/92 (97.8%) | 23/23 (100%) |
| genuine | **2/92 (2.2%)** | 0/23 (0%) |

### 异常发现

**seed 间方差极大**：同为 random β=0.3，s43 的 prove_rate=0.92 是 s44 (0.23) 的 4 倍。s43 学到了高效的 conclusion-in-premise hacking 策略（97.8% H1），而 s44 基本没学到证明能力。

这意味着：
1. random baseline 本身不稳定，seed 选择严重影响结果
2. s43 的非零 ISR (0.1659) 不代表真正推理——97.8% 的证明都有 conclusion 嵌入前提中，ISR 仅反映部分冗余组件的移除
3. 跨 seed 对比需谨慎——这个方差水平可能削弱论文中 ISR reward vs random 的对比论证

---

# analysis exp fewshot bcs v2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_fewshot_bcs_v2_20260517T140508_result.json`
- **Structured JSON:** [`bd7193ae4d937b77a615.json`](../../sessions/bd/bd7193ae4d937b77a615.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_fewshot_bcs_v2 分析完成

**结论：NEGATIVE** — confusability 是 schema-structural constraint，非 prompt-addressable。

### 核心数据

| 条件 | Low-BCS Acc | High-BCS Acc | Delta | p-value | Cohen's d |
|------|------------|-------------|-------|---------|-----------|
| 0-shot | 0.6821 | 0.4975 | **+18.46pp** | 6.6e-11 | 2.36 |
| 1-shot | 0.7538 | 0.5542 | **+19.96pp** | 4.8e-14 | 2.97 |
| 5-shot | 0.7154 | 0.4875 | **+22.79pp** | 5.2e-15 | 3.17 |

### 关键发现

1. **BCS delta 随 shot 数单调递增**（18.5 → 20.0 → 22.8pp），few-shot 不仅没缓解，反而加剧了 confusability 效应
2. **5-shot 对 high-BCS 组完全无效**：high-BCS 组 accuracy 从 0.4975 降到 0.4875（p=0.483），而 low-BCS 组仍获益 +3.33pp（p=0.002）
3. **差异增益显著**：0→5shot 时 low-BCS 比 high-BCS 多获益 4.33pp（p=0.014）

### 论文含义

这个 negative result 强化了核心 claim：当类型语义高度重叠时（high BCS），即使提供明确的 demonstrations，模型也无法克服结构性的类型混淆。BCS 捕捉的是 schema 的内在属性，而非可通过 prompting 策略解决的表面问题。

---

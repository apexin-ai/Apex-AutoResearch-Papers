# analysis oh stag rate canonical

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_oh-stag-rate-canonical_20260515T015821_result.json`
- **Structured JSON:** [`04c3226f401b398997dc.json`](../../sessions/04/04c3226f401b398997dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据到手。汇总：

## OH stag rate 精确计算结果

数据源：`/root/autodl-tmp/openhands_data/`

| 来源 | Stag (分子) | Total (分母) | Rate |
|------|------------|-------------|------|
| `windows_labeled.jsonl` (含 abstain) | 31,440 | 154,743 | **20.32%** |
| `windows_labeled.jsonl` (仅 non-abstain) | 31,440 | 150,652 | **20.87%** |
| `embeddings_fixed.pt` (实际训练数据) | 30,684 | 143,057 | **21.45%** |

### 三个数字的关系

- **20.32%** = 31,440 / 154,743 — LF 产出的全部窗口中 stag 占比（含 4,091 个 abstain 窗口作为分母）
- **20.87%** = 31,440 / 150,652 — LF 产出的有效标签窗口中 stag 占比（去掉 abstain 后）
- **21.45%** = 30,684 / 143,057 — `embeddings_fixed.pt` 中的 stag 占比（实际进入 probe 训练/评估的数据；比 jsonl 少 7,595 条，因部分窗口在 embedding 阶段丢失，丢失的偏 progress，导致 stag rate 略升）
- **21.4%** = 同上，四舍五入到 1 位小数

### 论文权威值建议

取决于论文描述的是什么：
- 如果说的是 **"silver label distribution"**（LF 标注产出的标签分布）→ **20.87%** (31,440 / 150,652)
- 如果说的是 **"training set class balance"**（实际训练数据的类别分布）→ **21.45%** (30,684 / 143,057)

两者都是精确可复现的，差异来源是 embedding 阶段的数据丢失。建议论文中明确报哪个口径，避免歧义。

---

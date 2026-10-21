# paper polish claim1 claim2 v2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_polish_claim1_claim2_v2_20260526T092811_result.json`
- **Structured JSON:** [`15b2995b8d077b14fd50.json`](../../sessions/15/15b2995b8d077b14fd50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits applied. Here's the summary:

---

## 修改总览

### abstract.tex (1 edit)
- **移除 em-dash**: `safety---all` → `safety; all` — em-dash 是 AI 写作最显著标志，改为分号

### analysis_claim1.tex (4 edits)
- **移除 -ing 结尾**: `confirming that the model produces...` → `and the model produces...`
- **移除 -ing 结尾**: `yielding a fake safe rate of 0%` → `; the fake safe rate is 0%`
- **更直接的动词**: `is intended as` → `serves as` — 去掉被动 hedging
- **收紧长句**: displacement distribution 句移除嵌套从句 `shown in...` 改为括号引用，删去冗余修饰词

### analysis_claim2.tex (3 edits)
- **移除 -ing 结尾**: `providing the refinement module with...` → `and provides the refinement module with...`
- **移除 -ing 结尾**: `resulting in zero refinement steps` → `; no refinement steps occur`
- **移除 -ing 结尾**: `effectively reducing the model to...` → 断句重写为 `The model thus operates as...`

### discussion.tex (3 edits)
- **移除 em-dash**: `---dominated by full-body collisions---` → 逗号包夹
- **移除 -ing 结尾**: `providing a metric that credits...` → `and credits...`
- **移除 -ing 结尾**: `indicating that the robot moves...` → 冒号引导解释

### introduction.tex (4 edits)
- **移除 -ing 结尾**: `indicating that catastrophic...` → 分号连接独立子句
- **移除 -ing 结尾**: `confirming that their collision avoidance...` → 断句为独立句
- **移除 -ing 结尾**: `establishing that the avoidance signal...` → 分号连接
- **移除 -ing 结尾**: `yielding a fake safe rate of 0%` → `and its fake safe rate is 0%`

---

## Claim 3 数据标记（discussion.tex，未修改）

Discussion 中以下两处包含 Claim 3 具体数据，re-eval 后可能需要更新：

1. **Line 3**: `Fine-tuning on collision-free demonstrations produces non-zero CAR$_\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region...` — 含 Claim 3 结论（non-zero CAR_f, zero frozen rate, catastrophic TSR collapse）
2. **Line 6**: `All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7% baseline to <7%)` — 含 Claim 3 具体数字（74.7% → <7%）

---

## 未修改的文件

**analysis_claim3.tex** — 按要求严格未触碰。

## 总体评价

五个文件的论证逻辑、数据一致性（Table 与正文对照）、Pi0.5 definitive 描述均无问题。主要修改集中在消除 AI 写作痕迹（15 处 em-dash + -ing 结尾修复），未改动任何数据或结论。

---

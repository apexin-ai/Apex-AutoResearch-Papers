# paper polish claim1 claim2 discussion

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_polish_claim1_claim2_discussion_20260526T062303_result.json`
- **Structured JSON:** [`dbc8eedfaec1c1fa6ae9.json`](../../sessions/db/dbc8eedfaec1c1fa6ae9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. Here's the complete change log:

### 改动汇总

**discussion.tex** (5 处):
1. **Line 3**: `rendering raw CAR unreliable` → `; raw CAR is therefore unreliable` — 消除 trailing -ing 分词短语（AI 风格标志）
2. **Line 3**: Claim 3 summary 补充 `but suffers catastrophic TSR collapse` — 开篇总结漏提 TSR collapse 这一关键发现
3. **Line 6 (Limitations)**: `Pi0.5+A1 results are reported at the 10K-step checkpoint (seed~0); the 30K checkpoint is pending...` → 更新为 30K 已完成的 TSR collapse 事实 — 原文与 C3 数据已改为 30K 矛盾
4. **Line 9 (Future work)**: `Four` → `Five`
5. **Line 9 (Future work)**: 新增第五个方向：TSR collapse → 训练策略研究 — 原文缺失此方向

**main.tex** (1 处):
6. **Line 60 (oracle figure caption)**: `---with zero prediction error---` → `(zero prediction error)` — 消除解释性 em-dash

### 检查通过（无需改动）

- **analysis_claim1.tex**: 数据全部与 paper_framing.md 一致（A1 99.6%, Pi0.5 26.8±1.6/74.7±1.5, LoRA 82%, threshold [2,200]mm, 239mm minimum）；Pi0.5 pending‡ 标注一致；dfCAR 描述清晰；Figure/Table 交叉引用正确（`eq:car_f` → experimental_framework, `fig:displacement`/`fig:tsr_car_scatter` → main.tex, `sec:avoidance_source` → analysis_claim3）
- **analysis_claim2.tex**: 3 oracle 数据完整（75.0/73.1/76.9 vs baselines 82.0/83.0）；arm-body collision 机制描述清晰（定性，无显式比例数据）；标题和 label 反映 EE-only limitation 定位
- **experimental_framework.tex**: 无旧 claim 编号残留；dfCAR 定义与 analysis_claim1 一致
- 全文无 Claim 4 引用残留，无旧 section label

---

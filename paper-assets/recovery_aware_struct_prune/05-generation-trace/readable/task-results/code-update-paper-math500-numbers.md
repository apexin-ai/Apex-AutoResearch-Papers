# code update paper math500 numbers

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_update_paper_math500_numbers_20260524T023010_result.json`
- **Structured JSON:** [`b1f49c8dbf96d1e6c4b7.json`](../../sessions/b1/b1f49c8dbf96d1e6c4b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改汇总：

### experiments.tex (line 85)

| 位置 | 原始值 | 新值 | 来源 |
|------|--------|------|------|
| CKA-only SFT | 26.8% | 27.4% | fixed eval |
| RASP SFT | 21.2% | 21.6% | fixed eval |
| CKA-Standard SFT gap | 3.4pp | 4.0pp | 27.4 - 23.4 |

### appendix.tex (line 110-111)

| 位置 | 原始值 | 新值 | 来源 |
|------|--------|------|------|
| CKA-only SFT | 26.8% | 27.4% | fixed eval |
| RASP SFT | 21.2% | 21.6% | fixed eval |
| CKA-only GRPO | 27.4% | 27.6% | fixed eval |
| RASP GRPO | 22.6% | 23.0% | fixed eval |
| MATH-500 SFT gap | 3.4pp | 4.0pp | 27.4 - 23.4 |
| MATH-500 GRPO gap | 0.4pp | 0.6pp | 27.6 - 27.0 |

### 未修改但需注意

1. **Standard SFT (23.4%)、Random SFT (14.4%)、Random GRPO (13.4%)** — 新数据中无对应 fixed eval 结果，保持原值。Standard SFT 的 23.4% 是旧 eval 值，与新 CKA-only SFT (27.4%) 混用计算 gap=4.0pp，待 Standard SFT fixed eval 完成后需复核。

2. **截断率 (22%/44%) 和平均 token 数 (655/1128)** — experiments.tex:121 和 appendix.tex:114 中引用。新数据提供 CKA-only SFT Trunc=23.2%，但无法确认原文 22% 对应 SFT 还是 GRPO 阶段，且 Standard 截断率和 mean token 数无新数据，未修改。

3. **conclusion.tex、introduction.tex** — 无 MATH-500 具体数值，无需修改。

---

# mvp quality check and code sync

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_mvp_quality_check_and_code_sync_20260520T142010_result.json`
- **Structured JSON:** [`c46a2261ebed491be22b.json`](../../sessions/c4/c46a2261ebed491be22b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成。

---

## 任务 1: 改写质量抽样

**统计**: 100 条中 36 条 passed_cf=True，64 条 failed。

### 5 PASSED 样本

| ID | formality | BERTScore | NLI | 观察 |
|---|---|---|---|---|
| mvp_0003 | casual | 0.9351 | 0.9909 | casual→formal：词汇替换（joint→cannabis, blasting→playing loudly），语义保持好 |
| mvp_0005 | casual | 0.9648 | 0.9980 | 极小改动（"I guess"→"I believe"），BERTScore 高合理 |
| mvp_0008 | formal | 0.9294 | 0.9847 | formal→casual：语气变口语化（"unfortunately"→省略，加 "way too tight"） |
| mvp_0011 | casual | 1.0000 | 0.9960 | 几乎无改动（叙事类文本风格差异小），bs=1.0 |
| mvp_0014 | formal | 1.0000 | 0.9800 | 代码内容，无风格可改，bs=1.0 |

### 5 FAILED 样本

| ID | formality | BERTScore | NLI | 失败原因 |
|---|---|---|---|---|
| mvp_0000 | formal | 0.8911 | 0.9949 | bs < 0.92（改写幅度偏大但语义保持） |
| mvp_0001 | casual | 0.8609 | 0.9935 | bs 较低（诗歌改写词汇变化大） |
| mvp_0002 | formal | 0.9164 | **0.0352** | NLI 极低——"independence referendum"→"vote on independence" 被 NLI 判为矛盾 |
| mvp_0004 | formal | 0.8727 | 0.9988 | bs < 0.92（改写较多但语义完好） |
| mvp_0006 | formal | 0.8637 | 0.9934 | bs < 0.92（长文本改写词汇差异大） |

**要点**: 大部分 failed 是因为 BERTScore < 0.92（改写幅度大但语义保持），只有 mvp_0002 是 NLI 真正失败。passed 样本中有两条 bs=1.0（代码/叙事类几乎无改动），说明某些文本类型风格干预不足。

---

## 任务 2: 代码同步确认

- `judge_scoring.py`: grep `passed_cf` 返回空（exit code 1）——已确认不含过滤逻辑
- `ate_analysis.py`: 第 198-199 行确认含 `bertscore_cf` 分层逻辑

---

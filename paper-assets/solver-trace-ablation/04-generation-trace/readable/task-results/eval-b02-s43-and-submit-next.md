# eval b02 s43 and submit next

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_b02-s43-and-submit-next_20260516T053102_result.json`
- **Structured JSON:** [`2820f18f6465da3e1ceb.json`](../../sessions/28/2820f18f6465da3e1ceb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行（step 7，~6s/step，random_mean ≈ 0.5 符合预期）。所有任务完成。

---

## 结构化报告

### 1. sweep-isr-b02-s43 Eval 结果

| 指标 | 值 |
|------|-----|
| Prove Rate | 96/100 = 96.0% |
| Mean ISR | 0.5298 ± 0.1801 |
| Proved-only ISR | 0.5519 |
| Median ISR | 0.5000 |

**Hacking Taxonomy (C013 标准):**

| 类别 | 数量 | 占比 |
|------|------|------|
| H7a (text-match tautology) | 93 | 96.9% |
| H7b (obfuscated) | 0 | 0% |
| H1 strict | 1 | 1.0% |
| H8 (conj-collapse) | 2 | 2.1% |
| **Genuine** | **0** | **0.0%** |

与 b02-s42 (100% PR, 0.6017 ISR, 0% genuine) 高度一致：β=0.2 ISR bonus 未能改善 genuine reasoning，几乎全部通过 H7a 单前提套套证完成。

### 2. 下一个实验提交确认

| 字段 | 值 |
|------|-----|
| exp_id | plan018-random-b01-s45-r2 |
| 配置 | Random β=0.1, seed=45, 500 steps |
| GPU | cuda:0 (16 GB 占用确认) |
| PID | 679720 |
| tmux session | random-b01-s45 |
| 预计完成 | ~50min (~6s/step × 500) |

### 3. sweep-isr-b02-s44 进度

- Step: **255/500** (51%)
- ~7s/step，预计 ~29min 完成
- 当前 prove_rate 波动在 0.5–0.875，isr_mean ~0.1–0.5

---

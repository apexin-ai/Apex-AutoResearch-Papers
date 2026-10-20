# data phase3 data readiness

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_phase3-data-readiness_20260513T234231_result.json`
- **Structured JSON:** [`df7d5e814acdd4db309c.json`](../../sessions/df/df7d5e814acdd4db309c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇报结果：

## Phase 3 数据就绪状态

### Paraphrase 文件
| 文件 | 大小 |
|------|------|
| mmlu_paraphrases.json | 27MB (14,042 items) |
| arc_challenge_paraphrases.json | 1.7MB (1,172 items) |
| gsm8k_paraphrases.json | 2.2MB (1,319 items) |
| humaneval_paraphrases.json | 500KB (额外) |

### Dosage SFT 数据（已包含 MMLU+ARC+GSM8K 三个 benchmark）

| Dosage | 总行数 | Clean | Contaminated | MMLU | ARC | GSM8K | 校验 |
|--------|--------|-------|--------------|------|-----|-------|------|
| 0% | 50,000 | 50,000 | 0 | — | — | — | — |
| 5% | 50,826 | 50,000 | 826 | 703 | 50 | 73 | OK |
| 25% | 54,133 | 50,000 | 4,133 | 3,540 | 257 | 336 | OK |
| 50% | 58,266 | 50,000 | 8,266 | 7,040 | 556 | 670 | OK |
| 100% | 66,533 | 50,000 | 16,533 | 14,042 | 1,172 | 1,319 | OK |

所有 dosage 文件行数 = 50000 + contaminated 总数，labels 文件与 JSONL 完全匹配。

**Phase 3 可以启动，无阻塞项。**

---

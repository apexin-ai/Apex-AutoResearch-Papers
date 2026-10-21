# code 14b rsft s43 test eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_14b-rsft-s43-test-eval_20260523T150101_result.json`
- **Structured JSON:** [`097a1c76b783130521bc.json`](../../sessions/09/097a1c76b783130521bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| Eval | GPU | PID | Status | Cron |
|------|-----|-----|--------|------|
| `test_eval_14b_rsft_s43_with_evi` | cuda:1 | 261715 | RUNNING | ✓ 120s |
| `test_eval_14b_rsft_s43_no_evi` | cuda:3 | 261858 | RUNNING | ✓ 120s |

两个 eval 均已提交、registry 更新（status/spec/hypothesis/parent）、cron 监控注册。no-evi eval 已传 `--no_evidence` 参数（C005）。

---

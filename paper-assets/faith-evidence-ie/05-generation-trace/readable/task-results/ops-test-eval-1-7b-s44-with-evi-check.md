# ops test eval 1 7b s44 with evi check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_test_eval_1_7b_s44_with_evi_check_20260525T045339_result.json`
- **Structured JSON:** [`73e2b65791ec0473520c.json`](../../sessions/73/73e2b65791ec0473520c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

no-evi eval 已在 GPU 0 上启动（8.7GB 已占用，模型加载中）。

## 结果汇总

**with-evi (test_eval_1_7b_rsft_s44_with_evi)** — 完成 ✓

| 指标 | 值 |
|------|-----|
| **ign_f1** | **22.46%** |
| precision | 41.16% |
| recall | 15.44% |
| evi_f1 | 63.57% |
| edcr | 84.62% |
| evi_joint_f1 | 18.02% |
| format_ok_rate | 100% |
| truncated | 253/500 (50.6%) |

⚠️ 严重的重复生成问题：超过一半的文档被截断，模型在重复输出相同的 triple（如 predictions 中可见的 Loud/Rihanna 重复），导致 recall 极低。

**no-evi (test_eval_1_7b_rsft_s44_no_evi)** — 已在 GPU 0 上启动，预计 ~40 分钟完成。

---

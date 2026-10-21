# code register content verification

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_register_content_verification_20260521T011307_result.json`
- **Structured JSON:** [`05a649027d4b1392f1cb.json`](../../sessions/05/05a649027d4b1392f1cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Register n=100 content verification 完成。结果：

| 指标 | Original vs CF | Original vs DR |
|------|---------------|----------------|
| BERTScore mean | 0.8589 | 0.8477 |
| NLI mean | 0.9410 | 0.8208 |
| Pass rate | **94/100 (94.0%)** | 81/100 (81.0%) |

- NLI-only gating 生效（register axis 不检查 BERTScore）
- CF pass rate 94% 与 pilot 的 95% (19/20) 一致
- 输出文件: `westb-29275:/root/causal_style_decomp_judge/data/verified_register.jsonl` (100条, 312K)
- Artifact 已注册: `art_20260521_227674`

---

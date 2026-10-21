# code formality rewriter bt fix

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_formality_rewriter_bt_fix_20260521T105016_result.json`
- **Structured JSON:** [`668971842be8695bb8fa.json`](../../sessions/66/668971842be8695bb8fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。结果对比：

| 指标 | 修复前 (consistent-only, 66 pairs) | 修复后 (all NLI-pass, 90 pairs) |
|------|------|------|
| **BT P(formal)** | 69.7% [57.6%, 80.3%] | 64.4% [56.1%, 72.8%] |
| **GEE Style OR** | 24.47 (separation artifact) | 9.48 |
| **GEE Orig OR** | 39.27 | 12.76 |
| **Likert** | ATE=-0.19, p=0.18 | 不变（已用 all pairs） |
| **Blindspot** | YES | YES |

关键验证通过：
- BT 从 69.7% 降到 64.4%，符合预期（all pairs 更保守）
- Baseline 66.5% 落在新 CI [56.1%, 72.8%] 内 → **rewriter independence 结论不变**
- GEE OR 从 24.47 降到 9.48，不再是 near-separation artifact
- Delta = -2.1pp（GPT-4o vs Qwen3-32B rewriter），CI 重叠

脚本在 `csd_pipeline/fix_formality_rewriter_bt.py`，结果已覆盖写入 `data/gpt4o_rewriter_formality_results.json`。

---

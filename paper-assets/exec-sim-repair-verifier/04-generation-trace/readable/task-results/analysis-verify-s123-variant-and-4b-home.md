# analysis verify s123 variant and 4b home

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verify-s123-variant-and-4b-home_20260518T190312_result.json`
- **Structured JSON:** [`a991cd6f0139d0b5109e.json`](../../sessions/a9/a991cd6f0139d0b5109e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已写入 `artifacts/variant_level_verified_results.md`。

**核心结论：**

| Model | Seed | Per-test | Variant (n=48) |
|---|---|---|---|
| Qwen3-8B CLS | s123 | 85.60% | **39/48 = 81.25%** (confirmed) |
| Qwen3-8B CLS | s42 | 84.48% | 35/48 = 72.92% |
| Qwen3-4B CLS ckpt4600 | s42 | 83.63% | **31/48 = 64.58%** |
| DeepSeek CLS seq8192 | s123 | 74.93% | 27/48 = 56.25% (canonical) |
| DeepSeek CLS seq2048 | s123 | 82.62% | 72.92% → **EXCLUDED** |

**Action 2**: Qwen3-8B CLS s123 = 81.25% (39/48) 已验证，数字正确。

**Action 1**: DeepSeek CLS seq2048 已排除。28.6% unparseable 导致 majority default 膨胀。

**Action 3**: Qwen3-4B CLS ckpt4600 variant-level = 64.58% (31/48)。虽然 per-test 83.63% 很高，但模型严重偏向 "pass"（recall_pass=96.57%, recall_fail=48.72%），AND rule 下 variant-level 大幅下降。对比同模型 ckpt-600 seq2048（76.92% per-test → 68.75% variant），后者因 fail recall 更平衡反而 variant-level 更高。

---

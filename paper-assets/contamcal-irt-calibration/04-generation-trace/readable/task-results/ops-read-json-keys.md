# ops read json keys

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read-json-keys_20260521T153925_result.json`
- **Structured JSON:** [`b69796a4d3fb932cb6ab.json`](../../sessions/b6/b69796a4d3fb932cb6ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果如下：

## OLMo-2 rerun (model: OLMo-2-1124-7B)

| dosage | MMLU | MMLU (correct/total) | ARC | ARC (correct/total) |
|--------|------|----------------------|-----|---------------------|
| d000 | 0.5379 | 7553/14042 | **NOT_READY** | — |
| d005 | 0.5614 | 7883/14042 | 0.7662 | 898/1172 |
| d025 | 0.5617 | 7888/14042 | 0.7816 | 916/1172 |
| d050 | 0.5725 | 8039/14042 | 0.7961 | 933/1172 |
| d100 | 0.5700 | 8004/14042 | **NOT_READY** | — |

## GSM8K — LLaMA-3.1-8B

| dosage | accuracy | correct/total |
|--------|----------|---------------|
| d000 | 0.3874 | 511/1319 |
| d025 | 0.5216 | 688/1319 |
| d100 | 0.5512 | 727/1319 |

缺失文件：`olmo2_d000_s42_arc` 和 `olmo2_d100_s42_arc`。

---

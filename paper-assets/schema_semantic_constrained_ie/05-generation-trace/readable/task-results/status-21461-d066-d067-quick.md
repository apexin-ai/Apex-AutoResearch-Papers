# status 21461 d066 d067 quick

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_21461_d066_d067_quick_20260520T012030_result.json`
- **Structured JSON:** [`157be175d5438ad12c29.json`](../../sessions/15/157be175d5438ad12c29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**d066 beam sweep (SciERC, Qwen):** 4/8 configs done
- ✅ beam1_unconstrained, beam1_full_s1, beam2_unconstrained, beam2_full_s1
- 🔄 beam4_unconstrained — 运行中 (09:12 启动, ~8min)
- ⏳ beam4_full_s1, beam8_unconstrained, beam8_full_s1
- ETA: ~60-80min (beam4/8 比 beam1/2 慢)

**d067 seed variance:** 4/12 configs done
- ✅ qwen_scierc_seed123 (unc+full), qwen_scierc_seed456 (unc+full) — 各551行完整
- 🔄 llama_scierc_seed123_unconstrained — 396/551 (72%, 09:07 启动)
- ⏳ llama_scierc_seed123_full_s1, llama_scierc_seed456 ×2, qwen_docred_seed123 ×2, qwen_docred_seed456 ×2
- ETA: ~2-2.5h

**GPU:** 双卡都在跑 (GPU0: 89%/18.3GB, GPU1: 85%/18.9GB)

---

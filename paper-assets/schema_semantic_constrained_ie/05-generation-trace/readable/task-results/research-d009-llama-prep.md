# research d009 llama prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d009-llama-prep_20260514T083659_result.json`
- **Structured JSON:** [`4272f6c0d03d00f411a1.json`](../../sessions/42/4272f6c0d03d00f411a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已注册。核心结论：

**Model ID**: `meta-llama/Llama-3.1-8B-Instruct`（推荐 Instruct 版本）

**兼容性**: 服务器 transformers 4.57.6 完全兼容（要求 ≥ 4.43.0），不需要 sentencepiece

**显存**: BF16 占用 ~17GB，RTX PRO 6000 94GB 完全够用，无需量化

**Gated access**: 需要在 HF 页面接受 Llama 3.1 Community License（自动批准），下载需 `HF_TOKEN`

**预估总时间**: 下载 + SciERC 两组实验约 5-9 小时

详细信息见 `artifacts/d009_llama_prep.md`。

---

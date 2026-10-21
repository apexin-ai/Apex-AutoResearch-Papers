# code r16 70b lora scierc

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r16_70b_lora_scierc_20260521T040623_result.json`
- **Structured JSON:** [`6acfc5c360a34e9e00f3.json`](../../sessions/6a/6acfc5c360a34e9e00f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5/551 samples processed, steady progress. The experiment is running correctly.

**Summary:**

- **Launched on westd-16980 cuda:1**: Llama-3.1-70B-Instruct-AWQ-INT4 zero-shot SciERC experiment
- **No 70B LoRA checkpoint exists**, so running **ZS (zero-shot)** instead of FT
- **Two runs** (sequential):
  1. `r16_70b_scierc_zs_unconstrained.jsonl` — no constraints
  2. `r16_70b_scierc_zs_full_s1.jsonl` — full S1 constrained (grammar + semantic)
- **Violation checks** run automatically after each
- **Model**: 39.2GB VRAM on cuda:1, AwqMarlinLinear kernel, ~5.8s/sample
- **ETA**: ~1h for unconstrained + ~1-1.5h for constrained = **~2-3h total**
- **Log**: `/tmp/r16_70b_scierc_zs.log`
- **Script**: `/root/schema_semantic_constrained_ie/run_70b_scierc_zs.sh`
- **PID**: 808988 (parent), 808996 (python3)
- **cuda:0 untouched** (beam experiment still running at 22.6GB)

---

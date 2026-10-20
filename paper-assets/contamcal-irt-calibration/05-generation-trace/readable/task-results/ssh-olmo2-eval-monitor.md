# ssh olmo2 eval monitor

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_olmo2-eval-monitor_20260519T124632_result.json`
- **Structured JSON:** [`7f327b7dc3b990a5449b.json`](../../sessions/7f/7f327b7dc3b990a5449b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 50 eval results (5 models × 5 dosages × 2 benchmarks) collected and written to `artifacts/eval_results_v2_summary.md`.

Key findings:

| Model | Δ MMLU (d000→d100) | Δ ARC (d000→d100) |
|-------|-------|-------|
| Qwen2.5-7B | -1.8pp | -2.9pp |
| Qwen2.5-14B | **-9.4pp** | -2.6pp |
| Phi-4 | -0.2pp | +0.6pp |
| Gemma-2-9B | +3.8pp | -1.2pp |
| OLMo-2-7B | +3.2pp | +3.9pp |

Notable patterns:
- **Phi-4** is contamination-robust — scores barely move across all dosages
- **Qwen2.5-14B** shows the largest MMLU degradation (-9.4pp), counterintuitively dropping with more contamination training
- **OLMo-2-7B** shows the clearest contamination inflation pattern — monotonic increase on both benchmarks
- **Gemma-2-9B** ARC results are highly erratic (0.711 to 0.874), suggesting training instability at certain dosages

Note: OLMo-2 d005 has a duplicate re-run still active on GPU 0 (PID 173479) — it will overwrite the existing completed results with equivalent data. No action needed.

---

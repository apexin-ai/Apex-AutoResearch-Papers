# ops registry sync llama 20260517

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry_sync_llama_20260517_20260517T030309_result.json`
- **Structured JSON:** [`4ca029c563ecf6fffc1a.json`](../../sessions/4c/4ca029c563ecf6fffc1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个实验全部更新完成。汇总：

| 实验 ID | 原状态 | 新状态 | 服务器验证 |
|---------|--------|--------|-----------|
| `exp_002_signals_llama32_3B_d000_mmlu` | PREPARING/success | DONE/success | `signals_merged_mmlu.json` 2.5MB ✓ |
| `exp_002_signals_llama32_3B_d000_arc_gsm8k` | PREPARING/success | DONE/success | `signals_merged_arc_challenge.json` 235KB + `signals_merged_gsm8k.json` 243KB ✓ |
| `exp_002_signals_llama32_3B_d100_gsm8k` | PREPARING/无conclusion | DONE/success | `signals_merged_gsm8k.json` 243KB ✓ |
| `exp_002_signals_llama32_3B_d100_arc` | PREPARING/无conclusion | DONE/success | `signals_merged_arc_challenge.json` 234KB ✓ |
| `exp_002_signals_llama32_3B_d100_mmlu` | DONE/killed | DONE/success | `signals_merged_mmlu.json` 2.5MB ✓ (有 degenerate 标记) |

注意：d100 MMLU 目录有 `MMLU_DEGENERATE_REFERENCE_ONLY.txt` 标记文件，说明 d100 模型在 MMLU 上退化（全选 A），signals 仅供参考。

---

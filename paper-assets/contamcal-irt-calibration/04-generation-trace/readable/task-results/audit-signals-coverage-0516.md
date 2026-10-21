# audit signals coverage 0516

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_signals_coverage_0516_20260516T105530_result.json`
- **Structured JSON:** [`47a41d871d3bfbbbf06f.json`](../../sessions/47/47a41d871d3bfbbbf06f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。结果写入 `artifacts/signals_coverage_audit_0516.md`。

**核心发现：19/23 valid model dirs 完成，4 个缺口：**

| 模型 | 状态 | 缺口 |
|------|------|------|
| 0.5B_d000_s123 | **8/9** | 仅缺 gsm8k s4（无进程在跑） |
| 0.5B_d100_s123 | 2/9 | s4_mmlu 在 GPU 5 跑（chunk 5000-6000, ~37%），gsm8k/arc 全缺 |
| 1.5B_d025_s123 | 2/9 | s4_mmlu 在 GPU 0 跑（chunk 10000-11000, ~67%），gsm8k/arc 全缺 |
| 1.5B_d100_s123 | 2/9 | s4_mmlu 在 GPU 2 跑（chunk 0-4000, ~27%），gsm8k/arc 全缺 |

**当前 GPU 使用：** 0 (1.5B_d025), 2 (1.5B_d100), 4 (Llama SFT), 5 (0.5B_d100)。**GPU 1, 3 空闲。**

**注意：** 0.5B v2 batch（GPU 5）用 `--signal all`，完成 d100_mmlu 后应自动接 gsm8k/arc。但 1.5B 的两个进程分别只跑 mmlu，gsm8k/arc 需要单独提交。0.5B_d000_s123 的 gsm8k s4 缺口可能由 v2 batch 后续覆盖，但也可以用空闲 GPU 单独跑（~25 min 即可填补）。

---

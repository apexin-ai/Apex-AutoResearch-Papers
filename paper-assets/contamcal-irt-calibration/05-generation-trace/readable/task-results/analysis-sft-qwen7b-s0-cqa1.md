# analysis sft qwen7b s0 cqa1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sft_qwen7b_s0_cqa1_20260520T230328_result.json`
- **Structured JSON:** [`ebeab97ae9bb0b53ff07.json`](../../sessions/eb/ebeab97ae9bb0b53ff07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

**结论: SUCCESS** — 5 个 dosage 全部正常完成，无 OOM/crash。

| Dosage | Checkpoint | adapter_model.safetensors | Train Loss | Token Acc | Runtime |
|--------|-----------|--------------------------|------------|-----------|---------|
| d000 | ✅ 存在 | 161.5 MB | 0.9259 | 0.7891 | 3h43m |
| d005 | ✅ 存在 | 161.5 MB | 0.9297 | 0.7774 | 3h54m |
| d025 | ✅ 存在 | 161.5 MB | 0.9426 | 0.7705 | 3h54m |
| d050 | ✅ 存在 | 161.5 MB | 0.9595 | 0.7782 | 4h07m |
| d100 | ✅ 存在 | 161.5 MB | 0.9884 | 0.7615 | 4h18m |

- 所有 lora_alpha=32（符合规范）
- Train loss 随 dosage 递增（0.926→0.988），符合预期——contamination 数据增多导致 loss 略升
- 总 GPU 时间 ~20.5h，日志以 `ALL_DONE_QWEN7B_S0` / `EXIT_CODE=0` 结束
- Registry 已更新为 DONE/success

---

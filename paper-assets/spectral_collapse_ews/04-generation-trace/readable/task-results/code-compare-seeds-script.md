# code compare seeds script

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_compare-seeds-script_20260519T123727_result.json`
- **Structured JSON:** [`4358d05d5903afe617fc.json`](../../sessions/43/4358d05d5903afe617fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双 seed 测试也通过。脚本功能正常：

- **逐 Gen 对比表**：每个 metric 显示各 seed 值 + pairwise delta + %diff
- **Phase boundary 分析**：Decompression peak 一致在 Gen 2；seed43 只有 3 gen 数据，onset/collapse 未检测到（符合预期）
- **Mean±std 汇总表**：跨 seed 差异很小（SLV %diff < 0.13%，eff_rank < 0.19%），说明 seed 间可复现性好
- **JSON 输出**：已保存到 `results/seed_comparison.json`

脚本路径：`/root/spectral_collapse_ews/scripts/compare_seeds.py`

---

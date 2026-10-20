# data update r2 table 15seed

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_update_r2_table_15seed_20260520T094741_result.json`
- **Structured JSON:** [`8b5d52d5f15e7141b258.json`](../../sessions/8b/8b5d52d5f15e7141b258.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。验证结果：

- **33 层数据完整** (L0–L32)
- **Peak 仍在 L11**: R² = 0.634 ± 0.009 (5-seed 时为 0.634 ± 0.007，mean 几乎不变，std 略增)
- **L0**: -0.330 ± 0.002
- **L32**: 0.550 ± 0.007
- **平均 CI 宽度** (mean std): 0.0097 (5-seed 时约 0.0075，符合预期——更多 seeds 暴露了更多 variance)

更新内容：
1. `cross_arch_r2_table.tex` — Phi3V 列标题改为 `(15 seeds)`，数据替换为 15-seed mean±std
2. `phi3v_r2_per_layer.json` — 两份副本均更新为 `num_seeds: 15`

---

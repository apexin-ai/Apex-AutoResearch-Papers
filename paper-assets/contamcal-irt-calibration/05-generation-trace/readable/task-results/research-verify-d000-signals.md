# research verify d000 signals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify-d000-signals_20260516T194310_result.json`
- **Structured JSON:** [`830647bf75eadc51d0cc.json`](../../sessions/83/830647bf75eadc51d0cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

chunk_0_1000 有 1000 个 items。7 chunks = 7000/14042 MMLU items，约 50% 完成。

## 验证结果

### GSM8K signals — 完整
- **路径**: `/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d000_s42/signals_merged_gsm8k.json`
- **items**: 1319（与 Qwen 3B d000 一致）
- **字段**: `item_id, benchmark, s1_embedding, s2_minkpp, s4_selfcritique`
- **JSON 正确关闭**，末尾 item 为 `gsm8k_1318`（0-indexed，1319 项）
- 子信号文件 s1/s2/s4 各 1319 items，全部一致

### ARC signals — 完整
- **路径**: `/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d000_s42/signals_merged_arc_challenge.json`
- **items**: 1172（与 Qwen 3B d000 一致）
- **字段**: 同上，`item_id, benchmark, s1_embedding, s2_minkpp, s4_selfcritique`
- **JSON 正确关闭**，末尾 item 为 `arc_challenge_1171`
- 子信号文件 s1/s2/s4 各 1172 items，全部一致

### MMLU signals — 进行中
- s1_embedding: 14042 items (done)
- s2_minkpp: 14042 items (done)
- s4_selfcritique: 7 chunks 完成（0-7000），共需 ~15 chunks（14042 items），约 **50%**
- 尚无 `signals_merged_mmlu.json`

### 格式一致性（vs Qwen2.5-3B_d000_a32_s42）
- **字段名完全一致**: 5 个字段名和顺序相同
- **item_id 命名一致**: `gsm8k_XXXX` / `arc_challenge_XXXX` 格式
- **item 数量一致**: GSM8K 1319, ARC 1172
- s1_embedding 跨 family 值相同（benchmark 级特征），s2/s4 因模型不同而不同 — 符合预期

### eval 源文件（exp001）
- `/root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d000_s42_aligned/` 存在 `.done` 标记
- 包含 gsm8k_results.json, arc_challenge_results.json, mmlu_results.json 等完整 eval 输出

**结论**: GSM8K 和 ARC signals 输出完整且格式与 Qwen 一致，可直接用于 RRF 聚合。MMLU signals 还需等 s4_selfcritique 剩余 ~7042 items 完成后 merge。

---

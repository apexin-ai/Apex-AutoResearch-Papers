# fix llama 3seed summary r1024

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_llama_3seed_summary_r1024_20260515T062613_result.json`
- **Structured JSON:** [`40e9d1ed88367661fcda.json`](../../sessions/40/40e9d1ed88367661fcda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**Step 1-2**: 修正 `compute_llama_3seed_summary.py` 的 SEED_DIRS（seed42: `exp007_llama_inference` → `exp_018_llama_scierc_seed42_r1024`，seed456: 加 `_r1024` 后缀），输出改写到 `llama_scierc_3seed_fresh_summary.json`，重新执行。

**Step 3 验证通过**: seed42 NER SJ ρ = **0.3096** ✓（完美匹配 registry），FK ρ = 0.2352 ✓，LP ρ = 0.1503 ✓。

**Step 4**: Qwen 3-seed summary 已存在，直接使用。

**Step 5**: 综合表已写入 `artifacts/multi_seed_stability_table.md` 并注册（`art_20260515_c0274b`）。

关键发现：
- **NER 排名完全稳定**：VC > SJ > EM > FK > LP，6 个 seed×model 组合全部一致
- **"structural > logprob" 在 NER 上成立**（12/12），RE 上仅 VC > LP 稳定，SJ/FK 未必胜 LP
- LLaMA SJ ρ 修正：旧均值 0.362 → 新均值 0.325，σ 增大 ~5× 是真实 seed 变异

---

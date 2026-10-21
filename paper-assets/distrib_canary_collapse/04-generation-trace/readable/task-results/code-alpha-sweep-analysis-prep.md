# code alpha sweep analysis prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_alpha-sweep-analysis-prep_20260514T210910_result.json`
- **Structured JSON:** [`8d9a65671144b9689554.json`](../../sessions/8d/8d9a65671144b9689554.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

TY 测试在 10+ gen 数据上正常工作（te→d1 显著，te→ppl 不显著——与 MVP 结果一致）。

脚本完成，总结：

- **位置**: `/root/autodl-tmp/distrib_canary_collapse/analyze_alpha_sweep.py`
- **功能**: 自动发现 `results/alpha_sweep/a{NNN}_s{seed}*` 目录，对每个 run 做 Toda-Yamamoto 检验，跨 seed 聚合后输出 α vs. canary signal 汇总表 + JSON
- **验证结果**:
  - 当前 a000_s42 (5 gen) 可加载但 TY df 不足（d_max=1 时需 ≥7 gen），输出 N/A——预期行为
  - a025_s42 (0 gen) 被跳过——空目录优雅处理
  - MVP 10-gen 数据验证 TY 正常：token_entropy→distinct_1 显著 (F=311.7, p≈0)，token_entropy→perplexity 不显著 (p=0.32)
- **等 10 gen 跑完后** re-run `python analyze_alpha_sweep.py` 即可出完整分析

---

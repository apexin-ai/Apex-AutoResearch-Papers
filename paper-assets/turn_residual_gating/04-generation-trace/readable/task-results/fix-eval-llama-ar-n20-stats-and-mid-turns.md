# fix eval llama ar n20 stats and mid turns

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval_llama_ar_n20_stats_and_mid_turns_20260522T082530_result.json`
- **Structured JSON:** [`97314dd39e46431261a4.json`](../../sessions/97/97314dd39e46431261a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 eval 脚本的 mid_turns 定义已确认。现在编制最终报告。

---

## 报告

### Part 1: eval_llama_ar_n20 详细统计

统计池: 20 conversations × mid turns, N=40 per model。mid_turns 定义: turns 3-4（eval 脚本 `avg_gar[2:]`）。

| 模型 | GAR-ours mean | std | median | spike(≥0.4) | GAR-dongre mean | std | median | PPL mean±std |
|------|-------------|-----|--------|-------------|-----------------|-----|--------|-------------|
| Base | 0.0088 | 0.0056 | 0.0071 | 0% | 0.0049 | 0.0013 | 0.0047 | 1.293±0.070 |
| TG | 0.0434 | 0.1002 | **0.0126** | **5%** | 0.0183 | 0.0198 | 0.0152 | 1.437±0.077 |
| LO | 0.0284 | 0.0481 | **0.0133** | 0% | 0.0205 | 0.0241 | 0.0160 | 1.419±0.075 |

TG mean (0.0434) 远高于 median (0.0126)，因为 5% turns 有 GAR≥0.4 spike（conv9/15/18）。**Median TG ≈ LO (0.013 vs 0.013)**，确认 gating 零增量。Registry 已更新。

---

### Part 2: mid_turns 定义一致性

**代码实际定义**（`eval_phase2_gar.py:524`, `eval_attention_steering.py:457`）:
```python
mid_turns = avg_gar[2:8]  # T≥8 → turns 3-8 (1-indexed)
mid_turns = avg_gar[2:]   # T<8 → turns 3-T
```

**期望标准**: turns 2-T（仅排除 turn 1）

**结论: 所有 16 个条目内部一致，但全部偏离 "turns 2-T" 标准。**

根因: 代码用 `[2:]` 而非 `[1:]`，同时排除了 turn 1 和 turn 2。

| 条目 | T值 | 实际 mid_turns | 偏离点 |
|------|-----|---------------|--------|
| eval_llama_ar_n20 | 4 | turns 3-4 | 丢失 turn 2 |
| eval_llama_lora_only_s42 | 4/10 | turns 3-4 / 3-8 | 丢失 turn 2 |
| llama_eval_s42 | 4/10 | turns 3-4 / 3-8 | 丢失 turn 2 |
| llama_ar_matched_eval | 4/10 | turns 3-4 / 3-8 | 丢失 turn 2 |
| eval_v7_tg_s123 | 4/10 | turns 3-4 / 3-8 | 丢失 turn 2 |
| eval_v8b_ss_s123 | 3/10 | turn 3 only / 3-8 | 丢失 turn 2；T=3 时仅 1 个 mid turn |
| phase2_4way_eval | 4 | turns 3-4 | 丢失 turn 2 |
| phase2_4way_eval_heldout | 4 | turns 3-4 | 丢失 turn 2 |
| phase2_tg_s42_v7 | varies | turns 3-T/3-8 | 丢失 turn 2 |
| phase2_tg_s42_v9_pcgrad | varies | turns 3-T/3-8 | 丢失 turn 2 |
| phase2_lora_only_s42 | varies | turns 3-T/3-8 | 丢失 turn 2 |
| phase2_ug_s42 | varies | turns 3-T/3-8 | 丢失 turn 2 |
| attention_steering_gen_n50 | varies | turns 3-8 (code `[2:8]`) | 丢失 turn 2；notes 写 "turns 2-7" 是 0-indexed |
| attention_steering_v7_tg_gen | 10 | turns 3-8 | 丢失 turn 2 |
| phase1_gar_diag | 10 | turns 3-8 (验证 0.0122) | 丢失 turn 2 |
| llama_phase1_gar_diag | 10 | turns 3-8 ("mid38") | 丢失 turn 2 |

**额外问题**: T≥8 时 cap 到 turn 8，丢失 turns 9-T。对 T=10 的 eval（如 phase1_gar_diag），turns 9-10 被排除。

**建议修正**:
1. 若标准确为 "turns 2-T"：改 `eval_phase2_gar.py:524` 为 `avg_gar[1:]`，`eval_attention_steering.py:457` 同步改，重跑所有 eval
2. 若排除 turn 2 是有意设计（turn 2 上下文仍短）：将标准文档从 "turns 2-T" 修正为 "turns 3-T (capped at 8)"
3. `attention_steering_gen_n50` 的 notes 中 "turns 2-7" 应标注为 0-indexed 以避免歧义

---

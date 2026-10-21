# paper update experiments tex

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_update-experiments-tex_20260520T105917_result.json`
- **Structured JSON:** [`0f5921014ec4fdef5d03.json`](../../sessions/0f/0f5921014ec4fdef5d03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。具体改动：

**替换了 5 个 placeholder：**

1. **`plan_002`** (line 47) → 单 seed 状态说明，附 exp028c/exp029 来源注释
2. **`tab1_main_results`** (原 line 60) → 1.7B 主结果表（Table 1），含 Cell A（h=2, 2 seeds: 0%/0%, 3.73%/9.375%）、Cell B（factorial, 2 seeds: 0.75%/20%, 0.75%/55.5%）、Cell C（episode-level: 23.88%/28.125%）
3. **`tab2_h_sweep`** (原 line 71) → h-sweep 消融表（Table 2），h=2→0%, h=5→0%, h=10→6.25%, h=20→15.6%, full→23.88%
4. **h-sweep 正文段落** (原 line 75-76) → 用具体数字替换 "precise numbers await multi-seed completion"，描述 credit assignment cliff
5. **`tab3_mechanism_verification`** (原 line 112) → sign misattribution 验证表（Table 3）+ 解释段落：credit agreement 52.07%≈random, point biserial r=0.068≈0, γ=1.0 坍缩

**未替换的 placeholder（无数据）：**
- `fig6_training_curves`、`fig5_h_sweep_curve`（图表占位）
- `plan_003b`（GAE baseline）
- `tab4_selective_comparison`（selective verification）

---

# analysis method ablation phase2 pooled

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_method_ablation_phase2_pooled_20260515T085042_result.json`
- **Structured JSON:** [`a0fbda0f7d6b9e35c9fa.json`](../../sessions/a0/a0fbda0f7d6b9e35c9fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 2 完成。

## 核心结果

**Method × Alpha Sig Rates (test-level)**:

| α | naive | differenced | threshold | perm_granger | TY |
|---|-------|-------------|-----------|-------------|-----|
| 0.00 | 8/8 (100%) | 4/8 (50%) | 5/8 (62%) | **0/8 (0%)** | **0/8 (0%)** |
| 0.25 | 8/8 (100%) | 2/8 (25%) | 3/8 (38%) | 2/8 (25%) | 5/8 (62%) |
| 0.50 | 8/8 (100%) | 8/8 (100%) | 8/8 (100%) | 2/8 (25%) | 0/8 (0%) |
| 1.00 | 32/32 (100%) | 32/32 (100%) | 32/32 (100%) | 24/32 (75%) | 19/32 (59%) |

**Claim 3 关键证据**:

1. **Naive 全域 100%** — 即使 α=0.0（无污染 null control）也全部 significant，确认 raw-level 方法不可靠
2. **Null control 验证** — perm_granger 和 TY 在 α=0.0 均为 0%，无 false positive
3. **perm_granger dose-response** — 0% → 25% → 25% → 75%，随 α 单调增长
4. **Mean Cohen's κ = 0.185**（poor agreement）— 方法间严重分歧
5. **Decision flips** — naive vs perm_granger: **50%** 结论翻转；naive vs TY: **57%** 翻转
6. **α=0.0 极端案例** — naive vs perm_granger 翻转率 **100%**（naive 全说 sig，perm_granger 全说 n.s.）
7. **entropy→diversity 在 α=1.0 所有 5 种方法一致 SIG** — 唯一跨方法 robust 的通道

**TY 注意事项**: α=0.25 出现 62% sig（高于 α=0.50 的 0%），单 seed 下 TY 非单调，需多 seed 确认后解读。

**产出文件**:
- `results/method_ablation_phase2_panel.json` (94KB) — 完整 panel 数据
- `results/method_ablation_phase2_report.md` — 分析报告
- Registry: `method_ablation_phase2` (DONE)

---

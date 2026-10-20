# code anova analysis script

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_anova-analysis-script_20260526T192341_result.json`
- **Structured JSON:** [`01d6fdf8f244613651b0.json`](../../sessions/01/01d6fdf8f244613651b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全 4 cell 场景 ANOVA、permutation test、simple effects、pairwise 全部正常。

脚本已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/analyze_factorial_anova.py`。

功能覆盖：
- 描述统计（mean/std/n/95% CI）
- Type II SS 手动实现的 2-way ANOVA（含 η²p）
- 10000 次 permutation test 作为小样本主推断
- interaction 显著时自动输出 simple effects
- 全 pairwise t-test（Bonferroni 校正）+ 每个 cell vs Vanilla
- Cohen's d + 95% CI of mean difference
- Shapiro-Wilk + Levene's assumption checks
- 空 cell 优雅跳过，n=1 跳过 t-test/CI/Cohen's d
- `--demo` / `--data-json` / `--cell1..4` 三种输入 + `--output-json` 导出

---

# paper results cohens d

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_results-cohens-d_20260514T080529_result.json`
- **Structured JSON:** [`a3ded7e11390a59b05fe.json`](../../sessions/a3/a3ded7e11390a59b05fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。变更总结：

**§5.0 Experimental Overview:**
- dtype 从 `float16` 改为 `bfloat16`，移除 "bf16 replication pending" 和 `PENDING-BF16` 注释

**§5.5 Statistical Validation — 完全重写：**

1. **Permutation test table** (`tab:permutation`)：用 difference statistic（不是 ratio）作主检验，填入真实数据：
   - s=0.15: Δ̃=0.37, CI=[0.19, 0.62], p_Bonf=0.0032
   - s=0.20: Δ̃=0.97, CI=[0.69, 1.49], p_Bonf<0.001
   - s=0.25: Δ̃=3.34, CI=[1.66, 6.64], p_Bonf<0.001
   - s=0.30: Δ̃=9.85, CI=[6.70, 16.29], p_Bonf<0.001
   - 所有 4 水平 Bonferroni p < 0.005，单调递增

2. **Cohen's d table** (`tab:cohens-d`)：已有表确认数据正确，补充了：
   - DeepSeek n 从 50 修正为 49（1 excluded）
   - 每行添加 exp_id 注释
   - 叙述段添加 exp_id 和 Appendix 交叉引用

3. **移除的内容：**
   - 旧 bootstrap CI table（`tab:bootstrap`）及其 ratio-based G 统计
   - 所有 `\placeholder{}` 标记（§5.5 范围内）
   - "severity gradient" ratio 作为主检验的描述

**未动的部分：** §5.1–5.4 的 `\placeholder{}` 保留（需要 per-phase II 数据填充，不在当前数据文件中）。

---

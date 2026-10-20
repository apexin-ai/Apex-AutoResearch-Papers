# fix tab fewnerd unified gf maxlp

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_tab_fewnerd_unified_gf_maxlp_20260518T043607_result.json`
- **Structured JSON:** [`be8281a425d3ef7d518f.json`](../../sessions/be/be8281a425d3ef7d518f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data is confirmed. Let me now produce the final deliverable.

---

## CoNLL 模型确认
论文用的是: **Qwen exp002_conll2003** (N=8, T=1.0)
数据来源: `/root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003/samples.jsonl`

## LP ρ 定义确认
Few-NERD 的 LP ρ=0.421 使用的定义是: **max_LP (instance-level)**
- 对每个 instance，取 N 个 sample 中 `mean_logprob` **最大**的值作为该 instance 的 LP 信号
- 然后 `Spearman(max_LP_per_instance, greedy_F1_per_instance)` across all gold-filtered instances
- 代码位置: `recompute_table_fewnerd.py:82-84` (原始定义), 现在 `analyze_fewnerd_results.py:210` 已对齐

之前的 SciERC/CoNLL 用的是 `mean_LP` (instance-level mean of samples' LP)，差异：
- SciERC: mean_LP ρ=0.205 → max_LP ρ=0.215
- CoNLL: mean_LP ρ=0.316 → max_LP ρ=0.302

## 三数据集完整对比表 (gold-filtered, max_LP)

| Dataset | n | greedy | oracle | headroom | degen% | LP ρ | LP sel | LP Δ | 来源文件 |
|---------|---|--------|--------|----------|--------|------|--------|------|----------|
| SciERC (旧) | 551 | .614 | — | 13.8pp | 17.8% | .205 | — | +0.42pp | full-set, mean_LP |
| **SciERC (新)** | **529** | **.644** | **.776** | **13.2pp** | **17.8%** | **.215** | **.650** | **+0.61pp** | exp_012_rerun_1024 |
| Few-NERD (验证) | 32565 | **.748** | .872 | **12.4pp** | **13.8%** | **.421** | .761 | **+1.36pp** | exp_021_inference ✓ |
| CoNLL (旧) | 2756 | .908 | — | 4.0pp | 47.4% | .316 | — | n.s. | 混合来源 |
| **CoNLL (新)** | **2756** | **.908** | **.948** | **4.0pp** | **59.1%** | **.302** | **.897** | **-1.05pp** | exp002_conll2003 |

**Few-NERD 验证**: greedy=0.7478→.748 ✓, LP ρ=0.4215→.421 ✓, LP Δ=+1.355→+1.36pp ✓

### 注意事项
- CoNLL degen% 从 47.4% 变为 59.1%：旧值来自 N=16 实验 (exp_002_conll_n16_r1024)，新值来自 N=8 (exp002_conll2003)，与 tab:fewnerd caption "N=8" 一致
- CoNLL LP Δ 从 "n.s." 变为 -1.05pp（实际上是退化），论文表格中可能需要标注为 "$-1.05$\,pp" 而非 "n.s."
- SciERC 从 full-set (n=551) 变为 gold-filtered (n=529)，这消除了 tab:fewnerd 的脚注中 "due to full-set evaluation" 的说明

## analyze_fewnerd_results.py 更新状态
- **SCIERC_REF**: 更新为 gold-filtered max_LP (n=529, greedy=0.6439, oracle=0.7758, headroom=13.19, degen=17.8, lp_rho=0.215, lp_delta=0.61)
- **CONLL_REF**: 更新为 gold-filtered max_LP (n=2756, greedy=0.9079, oracle=0.9483, headroom=4.04, degen=59.1, lp_rho=0.302, lp_delta=-1.05)
- **LP ρ 计算**: `instance_mean_lp` → `instance_max_signal["LP"]` (与 Few-NERD 一致)
- 验证运行通过：Few-NERD LP ρ=0.4215，cross-dataset table 输出正确

### 服务器上新增/修改的文件
1. `code/analyze_fewnerd_results.py` — SCIERC_REF/CONLL_REF 常量 + LP ρ 计算方式
2. `code/unified_tab_fewnerd_metrics.py` — 统一计算脚本（可复现）
3. `output/unified_tab_fewnerd_maxlp.json` — 完整精确值

---

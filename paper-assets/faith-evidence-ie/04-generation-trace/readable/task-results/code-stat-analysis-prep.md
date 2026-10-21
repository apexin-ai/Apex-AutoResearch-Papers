# code stat analysis prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_stat-analysis-prep_20260515T230315_result.json`
- **Structured JSON:** [`1e3f9f85519ac454b596.json`](../../sessions/1e/1e3f9f85519ac454b596.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three output formats work. Here's the summary:

---

### 任务 1：stat_analysis.py — 完成

脚本已创建在 `/root/autodl-tmp/freige/scripts/stat_analysis.py`，功能：

- `--results_dir` 自动扫描各子目录的 metrics.json（和 reranker 的 results.json）
- 自动过滤坏结果（f1 < 0.01，已正确排除掉 broken 的 dpo_ced_1ep 和 rsft_flat_nli_s43）
- 支持 `--format text/json/latex` 三种输出
- Paired/Welch t-test + Cohen's d（当前 flatNLI 只有 1 个 seed，无法做 t-test，待 s43-s45 收齐后自动启用）

当前有效数据：

| Method | n | rel_f1 | evi_f1 | EDCR |
|--------|---|--------|--------|------|
| SFT baseline | 1 | 0.4106 | 0.8013 | 0.7039 |
| SFT no-evidence | 1 | 0.4893 | 0.0000 | 0.0000 |
| RSFT-CED | 3 | 0.4596±0.0128 | 0.8144±0.0051 | 0.6434±0.0114 |
| RSFT-flatNLI | 1 | 0.4539 | 0.8043 | 0.6431 |
| GRPO bf16 | 1 | 0.4549 | 0.8086 | 0.6318 |
| CED reranker | 1 | 0.4864 | 0.8188 | 0.6156 |

**缺失/坏数据：**
- DPO 1ep: f1=0.002, field_compliance=0.0 — 明显坏掉了，`dpo_ced_1ep_fixed` 目录为空
- flat-NLI s43: 同样坏掉（f1=0.002），reeval 目录为空
- flat-NLI s44/s45: 尚未创建
- RSFT top_k=3: 无 metrics.json

---

### 任务 2：EDCR 诊断脚本验证 — 通过

`edcr_diagnostic.py` 存在且功能完整：
- `--help` 正常输出
- 支持 `--auto-discover`（内置 14 个方法路径）和 `--methods NAME:PATH`
- 依赖 `eval.evaluator` 模块（项目内部），无额外依赖
- 输出 JSON + LaTeX 两种格式
- AUTO_METHODS 列表已包含 DPO-CED 1ep 和 RSFT-flatNLI s43 条目，待这些 eval 修复后可直接运行

---

# analysis exp 015 metrics expansion

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_015_metrics_expansion_20260514T114050_result.json`
- **Structured JSON:** [`1f652c7ef3e057dce6ab.json`](../../sessions/1f/1f652c7ef3e057dce6ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出：

**脚本**: `artifacts/analyze_exp015_metrics_expansion.py` — 已注册为 artifact (`art_20260514_a315ab`)

**exp_015_metrics_expansion** 已在 registry 中注册 (QUEUED)

**脚本功能**:
- 加载 pilot_004 的 `samples.jsonl`，尝试从 exp-012 目录加载 logprob 数据
- 计算 5 类信号：`soft_jaccard`, `fleiss_kappa`, `exact_match`, `voting_confidence`, `logprob`（如可用）
- 对 NER 和 RE 分别计算 6 项指标：Spearman ρ, Kendall τ, AUROC, calibration bins (10 bin), LOO-SJ, bootstrap 95% CI (1000 resamples)
- 输出 4 个 JSON 文件到 `output/exp015_metrics_expansion/`：
  - `ner_full_metrics.json`, `re_full_metrics.json`
  - `calibration_data.json`
  - `bootstrap_ci.json`
  - `loo_sj_comparison.json`

**服务器运行命令**:
```bash
cd /root/autodl-tmp/struct_self_consist_ie
python code/analyze_exp015_metrics_expansion.py
```

需要先将脚本同步到服务器的 `code/` 目录。

---

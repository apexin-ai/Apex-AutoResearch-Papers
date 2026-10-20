# code gemma analysis script

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma-analysis-script_20260520T180645_result.json`
- **Structured JSON:** [`9a9eb597217d35cf6794.json`](../../sessions/9a/9a9eb597217d35cf6794.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `/root/autodl-tmp/simgate-modular-routing/src/analyze_gemma_scienceworld.py` 并通过 `--help` 验证。

功能概要：
- 从 11 个 included task 子目录读取 `episode_summary.jsonl`（兼容 individual JSON fallback）
- 字段映射：`internal_final` → `internal_score`, `det_final` → `deterministic_score`
- 计算 per-task breakdown（label 分布 + death rates）、aggregate metrics（DR/ΔDR/DAF）
- Cluster bootstrap（K=11 task types, B=10000）计算 95% CI
- Cross-model comparison 表（硬编码 Qwen/Llama + 本次 Gemma 结果）
- 输出到 stdout + 保存 `analysis.json` 和 `cross_model_table.tex`

实验完成后运行：
```bash
python src/analyze_gemma_scienceworld.py --input results/gemma-9b-counterfactual/
```

---

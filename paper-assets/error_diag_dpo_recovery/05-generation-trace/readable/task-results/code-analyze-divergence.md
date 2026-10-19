# code analyze divergence

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analyze-divergence_20260513T063822_result.json`
- **Structured JSON:** [`d83738cb378012079134.json`](../../sessions/d8/d83738cb378012079134.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出：

1. **`scripts/analyze_divergence.py`** — 完整 CLI，支持多目录输入、expert 匹配、divergence 分布分析、early/mid/late 分组、γ(d) 映射。输出 JSON + LaTeX 表格 + stdout summary。
2. **`tests/mock_divergence_test/`** — mock 数据生成 + 自动验证脚本，20 条 trajectory（7 success, 12 matched failures, 1 unmatched），所有检查通过。
3. LaTeX 3 张表格格式正确（booktabs），可直接 `\input` 到论文。

v7 数据到后直接跑：
```bash
python3 scripts/analyze_divergence.py \
  --trajectory_dirs data/trajectories_v7_icl_cuda0 data/trajectories_v7_icl_cuda1 \
  --expert_file data/alfworld_sft.json \
  --output_dir outputs/divergence_analysis
```

---

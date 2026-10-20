# prep c2 n500 analysis scripts

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_c2-n500-analysis-scripts_20260514T143220_result.json`
- **Structured JSON:** [`8264f7322efeaabcc04f.json`](../../sessions/82/8264f7322efeaabcc04f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 8 个 d_z 值与现有参考数据完全匹配。脚本验证通过。

产出总结：

**脚本**: `/root/autodl-tmp/pacs/analyze_c2_n500.py` (512行)

**用法**:
- `python analyze_c2_n500.py` — 分析 n=500 数据（实验完成后运行）
- `python analyze_c2_n500.py --n50-only` — 用 n=50 数据 dry-run（已验证通过）

**n=500 输出目录预期模式**:
```
profiling_output_n500_bf16_{ds,qw}_{imp,rand}_s{015,020,025,030}/profiling_results.json
```
共 16 个条件，当前全部尚未完成。

**输出文件**:
- `analysis_output/c2_n500_results.json` — 全量结果 JSON
- `analysis_output/cohens_d_n500.json` — paired d_z（论文图表用）
- `analysis_output/c2_n500_report.md` — Markdown 报告

**Dry-run 验证结果**:
- 8 个 Cohen's d_z 值与 `cohens_d_bf16.json` / `cohens_d_bf16_qwen.json` 精确匹配
- Importance d_z 单调递增：DeepSeek 0.44→0.80, Qwen 0.28→1.02
- Random masking d_z 无单调模式（-0.26~0.36），验证了核心对比
- Qwen s015 d_z CI 跨零 [-0.006, 0.597]（n=50 下边缘），n=500 将决定最终叙事

---

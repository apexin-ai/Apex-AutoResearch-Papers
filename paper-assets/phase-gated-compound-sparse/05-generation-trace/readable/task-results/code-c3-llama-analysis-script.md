# code c3 llama analysis script

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c3_llama_analysis_script_20260514T162920_result.json`
- **Structured JSON:** [`45752db7383c61de830e.json`](../../sessions/45/45752db7383c61de830e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并验证通过：`/root/autodl-tmp/pacs/analyze_c3_llama.py`

功能确认：
- **s015/s020** 数据正确加载，统计量计算无误
- **s025/s030** 缺失时优雅跳过，标记为 missing
- **Paired bootstrap** 使用共享 idx（`bootstrap_paired_dz_and_median` 函数）
- **Wilcoxon** 使用 Bonferroni 校正 (k=4)
- **c3_llama_cohens_d.json** 与 cohens_d_bf16.json 格式一致
- **跨架构对比表**正常生成（LLaMA phase gradient d_z 约 1.0-1.1，远大于 DeepSeek 的 0.44-0.52）
- 已清除验证用的临时输出，等全部 8 conditions 就绪后正式运行

---

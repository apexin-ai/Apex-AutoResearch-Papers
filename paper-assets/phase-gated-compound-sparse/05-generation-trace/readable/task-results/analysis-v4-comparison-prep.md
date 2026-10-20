# analysis v4 comparison prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4_comparison_prep_20260513T235754_result.json`
- **Structured JSON:** [`4999d7c5f8b68b86986f.json`](../../sessions/49/4999d7c5f8b68b86986f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本就绪。

**使用方式：**

```bash
# 实验全部完成后运行（使用默认路径）
python /root/autodl-tmp/pacs/analyze_v4_comparison.py

# 自定义参数
python analyze_v4_comparison.py \
  --imp_dirs profiling_output_v4a profiling_output_v4b profiling_output_v4c \
  --rand_dir profiling_output_v4_random_r2 \
  --sparsities 0.1,0.2,0.3 \
  --output_pdf /root/autodl-tmp/pacs/v4_comparison.pdf
```

**输入：** 4 个目录下的 `profiling_results.json`（v4a/b/c 各含一个 sparsity level 的 importance 结果，v4_random_r2 含 5 个 sparsity level 的 random 结果）

**输出：**
1. Stdout 表格：每个 (phase, sparsity) 的 importance vs random II 对比，含 95% CI、符号反转检测、显著性判断
2. Perplexity 分解表（dense/attn/kv/both）
3. PDF 图：3 个 phase 子图，importance 和 random 的 II 折线 + CI band，random 的额外 sparsity 点（0.15, 0.25）也会标注

---

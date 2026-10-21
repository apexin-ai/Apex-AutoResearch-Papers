# analysis mmct full coverage

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mmct_full_coverage_20260519T031507_result.json`
- **Structured JSON:** [`06cd31945cab88e7ce14.json`](../../sessions/06/06cd31945cab88e7ce14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**执行内容：**
1. 为 `a010_s42` 生成了缺失的 unified 5-method 分析数据
2. 重新运行 MMCT，覆盖 20 个实验：13 个 alpha-sweep (含新增的 a010、a060) + 7 个 Table 7 generalize 条件

**关键结果：**
- FPR = 0（所有 6 种 MMCT 模式在 alpha=0.00 均无假阳性）
- `weighted_pair_forward` 检测率随 alpha 单调递增：0.00 → 0.125 → 0.438 → 0.583 → 0.750 → 0.792 → 0.813 (Table 7 均值)
- Table 7 全部 7 个泛化条件在 `weighted_pair_forward` 下检测率 6/8 到 8/8
- `uniform` 和 `weighted_global` 模式较保守，仅在 alpha>=0.75 有少量检测

**无法运行的实验：**
- `a010_s43`, `a010_s44`, `a025_s42`: 实验目录不存在
- `gen_wiki_gpt2m_a100_s43`: 未完成（3/11 generations）

产出文件：`artifacts/mmct_full_results.md`

---

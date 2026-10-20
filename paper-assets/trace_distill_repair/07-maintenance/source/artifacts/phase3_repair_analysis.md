# Phase 3 Repair Experiment Analysis

**日期**: 2026-05-15  
**实验**: mvp_phase3_repair  
**模型**: deepseek/deepseek-v4-flash  
**规模**: 33 instances × 4 conditions = 132 runs  
**耗时**: 3726.6s (~62 min)  
**退出状态**: 正常完成 (EXIT_CODE=0, checkpoint 33/33)

---

## 核心结论：全面失败

**所有 4 个条件的修复成功率均为 0%。** 没有任何一个 instance 在任何条件下通过测试。

---

## 指标对比表

| 条件 | 成功率 | 空响应 | Avg Input Tokens | Avg Output Tokens | Total Tokens | Avg Judge (0-5) | Judge≥3 | Avg Line Overlap |
|------|--------|--------|-------------------|-------------------|-------------|-----------------|---------|------------------|
| no_trace | 0/33 (0%) | 2/33 | 3,372 | 3,176 | 216,064 | 1.06 | 2/33 | 0.2017 |
| full_trace | 0/33 (0%) | 8/33 | 16,264 | 3,540 | 653,504 | 0.70 | 1/33 | 0.1734 |
| structural_filtered | 0/33 (0%) | 3/33 | 3,633 | 3,476 | 234,580 | 0.76 | 1/33 | 0.2025 |
| line_filtered | 0/33 (0%) | 3/33 | 4,574 | 3,561 | 268,449 | 0.88 | 3/33 | 0.2077 |

## Judge Score 分布

| 条件 | Score=0 | Score=1 | Score=2 | Score=3 | Score=4 | Score=5 |
|------|---------|---------|---------|---------|---------|---------|
| no_trace | 7 | 21 | 3 | 0 | 2 | 0 |
| full_trace | 16 | 14 | 2 | 0 | 0 | 1 |
| structural_filtered | 13 | 18 | 1 | 0 | 0 | 1 |
| line_filtered | 14 | 16 | 0 | 1 | 0 | 2 |

## Structural Keep>0 vs Keep=0 子集

15/33 instances 有 structural_keep>0，18/33 instances structural_keep=0。

| 条件 | keep>0 (n=15) Avg Judge | keep=0 (n=18) Avg Judge |
|------|------------------------|------------------------|
| no_trace | 1.13 | 1.00 |
| full_trace | 0.60 | 0.78 |
| structural_filtered | 0.87 | 0.67 |
| line_filtered | 0.93 | 0.83 |

所有子集修复成功率均为 0%，无法做有意义的对比。

## Head-to-Head: structural vs line

- Structural wins: 0
- Line wins: 0
- Ties: 33

## 评估方法分布

- test_execution: 116/132 (87.9%) — 全部失败
- empty_response: 16/132 (12.1%) — 模型未生成有效代码

Empty response 集中在:
- full_trace: 8 次 (24.2%) — 长 context 导致模型困惑
- thefuck 系列: 6 次 (thefuck_1/2/4 多个条件)
- structural_filtered: 3 次, line_filtered: 3 次, no_trace: 2 次

## Top Judge Scores (跨条件最高分)

| Instance | Best Condition | Judge Score | 其他条件 |
|----------|---------------|-------------|---------|
| black_1 | structural_filtered | 5 | no=1, full=0, line=0 |
| fastapi_1 | full_trace | 5 | no=4, struct=1, line=5 |
| fastapi_2 | line_filtered | 5 | no=2, full=0, struct=0 |
| httpie_2 | no_trace | 4 | full=2, struct=1, line=0 |
| scrapy_3 | line_filtered | 3 | no=2, full=2, struct=0 |

只有 5/33 instances 在任何条件下 judge≥3，且最高分条件分散——没有哪个条件系统性更优。

---

## 假设验证

**假设**: Structural-filtered trace 在 repair quality 上优于其他条件。

**结论: 不支持。**

1. **修复成功率**: 全部为 0%，无法区分条件
2. **Judge 质量分**: structural_filtered (0.76) 低于 no_trace (1.06) 和 line_filtered (0.88)
3. **Head-to-head**: structural vs line 全部平局 (33/33 ties)
4. **Keep>0 子集**: structural_filtered 在 keep>0 子集上 judge=0.87，略高于 keep=0 (0.67)，但差异不显著且样本太小
5. **Top scores**: structural_filtered 只在 black_1 上拿到最高分 (5)，其他 4 个 top 实例的最高分分布在 no_trace/full_trace/line_filtered

---

## 失败根因分析

### 1. 模型能力不足 (主因)
deepseek-v4-flash 无法完成 BugsInPy 级别的单次修复任务。典型失败模式：
- 生成完全无关的代码（如 youtube-dl_5 生成 bash completion 脚本而非修复）
- 只输出 import 语句和类定义，不触及 bug（如 black_1）
- 输出被截断在 4096 tokens（max_tokens 限制）

### 2. Empty Response 问题 (12.1%)
full_trace 的 empty response 率高达 24.2%，说明长 trace 反而干扰模型生成。

### 3. 评估瓶颈
- 132 次 run 中仅 5 次 judge≥3，说明模型甚至无法接近正确答案
- 平均 line overlap 仅 0.17-0.21，生成的代码与 ground truth 高度不匹配

### 4. 实验设计局限
- 33 个实例中 18 个 structural_keep=0（54.5%），对这些实例 structural_filtered 退化为极短 context
- 单次生成（pass@1），没有 retry/sampling 策略
- max_tokens=4096 可能不够生成完整修复（多个实例 output 被截到 4096）

---

## 风险和建议方向

| 风险 | 说明 |
|------|------|
| **模型选择是实验的瓶颈** | 0% 成功率说明 deepseek-v4-flash 无法完成此任务，换更强模型（GPT-4o, Claude Sonnet）是前提 |
| **full_trace 不仅无益反而有害** | 最高空响应率 (24.2%)、最低 judge (0.70)、3x token 消耗 |
| **structural_filtered 未显示预期优势** | judge 低于 no_trace，可能需要更好的 prompt engineering 或 trace 呈现方式 |
| **数据集偏斜** | 54.5% instances structural_keep=0，这些实例上 structural filtering 无信号 |
| **max_tokens 限制** | 多个实例 output 截断在 4096，可能阻止了完整修复的生成 |

---

## 原始数据位置

- CSV: `/root/trace_distill_repair/pipeline_output/phase3_results.csv` (132 rows)
- Summary: `/root/trace_distill_repair/pipeline_output/phase3_summary.json`
- Checkpoint: `/root/trace_distill_repair/pipeline_output/phase3_checkpoint.json`
- Log: `~/runs/trace_distill_repair/mvp_phase3_repair.log`

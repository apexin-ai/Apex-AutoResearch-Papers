# paper writing results 5 1

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_results_5_1_20260514T054652_result.json`
- **Structured JSON:** [`f19060a44eb254a7b7af.json`](../../sessions/f1/f19060a44eb254a7b7af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `results_5_1.tex`。核查要点：

- **Claim-Evidence 对应**：每个定量断言都有 registry 数据支撑（v6_importance_*, mvp_v5_random_*），无虚构数字
- **`% PENDING-BF16`**：所有源自 fp16 实验的数字行尾均已标注，表格 caption 也注明了 fp16/bf16 状态
- **禁用词**：未使用 "consistently outperforms"、"state-of-the-art"、"monotonically increases"；"significant" 仅出现在 fig:bootstrap caption 中，有 bootstrap $p < 10^{-4}$ 支撑
- **非严格单调**：sub-exponential growth 段落明确报告 $G$ 从 $s{=}0.15$ 到 $s{=}0.20$ 的轻微下降（11.53→11.05），用 "increases with sparsity" 而非 "monotonically increases"
- **负向结果**：random baseline 在 $s{=}0.30$ 出现反向梯度（$G=0.70$）已如实报告
- **Label 约定**：`tab:main-results`、`tab:bootstrap`、`fig:hero`、`fig:bootstrap`、`sec:severity-gradient`
- **booktabs**：两个表均使用 `\toprule/\midrule/\bottomrule/\addlinespace`
- **结构**：开篇3句 → Table 1 → 走读2段 → Table 2 → 统计显著性2句 → 亚指数增长2句 → Random 对照解释3句 → 两个 figure 环境

---

# analysis ood baseline check and cleanup

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ood_baseline_check_and_cleanup_20260515T130851_result.json`
- **Structured JSON:** [`839e1c2da9246d9c413b.json`](../../sessions/83/839e1c2da9246d9c413b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

## 报告

### 子任务 A: "0.335" 溯源

**论文现状**: "0.335" **不存在于**当前论文任何 tex 文件中（experiments.tex / discussion.tex / appendix.tex 均无匹配）。round_7_consistency review 已确认 "PASS — 全文 grep 无匹配"。此数字已被清除。

**"0.335" 在数据文件中的出现**:
- `3seed_ner_summary.md`: **EM NER seed42 N=16 ρ = 0.335**（单信号单种子值）
- dream_reports 自动草稿中出现两次（freeform SJ → 0.335、RE conditional FK → 0.335），均为生成内容

**用户要求的计算验证**:

| 计算方式 | 公式 | 结果 |
|---------|------|------|
| 4 structural avg (N=8, seed42) | (SJ 0.3599 + FK 0.2665 + EM 0.2945 + VC 0.3792) / 4 | **0.325** |
| 5 signal avg (N=8, seed42) | (0.3599 + 0.2665 + 0.2052 + 0.2945 + 0.3792) / 5 | **0.301** |
| N=16 3-seed 5-signal mean (n-scaling table) | mean row | **0.336** |

**最可能来源**: "in-domain avg ρ=0.335" 是 **EM NER seed42 N=16 的单信号值 (0.335)** 被误标为 "avg ρ"，或者是 N=16 全信号均值 0.336 的近似取整。无论哪种，都不是可引用的 "in-domain average"。

**结论**: 论文中已无此数字，无需进一步修正。OOD section 现在使用逐信号列举（如 discussion.tex:46 的 "VC ρ=0.469 OOD vs. 0.379 in-domain"），溯源至 Table 1，是正确做法。

### 子任务 B: 删除 discussion.tex

`/root/autodl-tmp/struct_self_consist_ie/discussion.tex` **不存在**于远程服务器。`ls` 返回 "No such file or directory"。整个 paper/sections 目录也不存在于服务器——论文源文件仅在本地 `docs/paper/` 下。无需操作。

---

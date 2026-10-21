# director / loop_8.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`24cce839651bbcc11fbd.json`](../../sessions/24/24cce839651bbcc11fbd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-19T11:24:09+00:00'
---

## 当前状态

14B multi-seed eval 是提交前最后一个 blocker。Round 12 论文 patches 全部完成，其余实验（228+ 成功）全部到位。

## 刚做的事

发现旧 14B eval 进程未被 kill（s123_eval pid 93137 占 91.87 GiB，s456_eval pid 93278 仍在跑），导致 s123_eval_v2 OOM 失败。已给 Agent 发指令：
1. Kill 旧进程 93137 和 93278
2. 检查 s456_eval_v2 (pid 100060) 是否正常
3. 重启 s123 eval（不含 GSM8K），两个 seed 分别用 cuda:0 和 cuda:1

## 等待中

Agent 回复 14B eval 清理结果。两个 eval（s123 + s456，各跑 PPL + ARC/WG/HS/PIQA/MMLU，不含 GSM8K）完成后：

1. **送 Reviewer 核实 MMLU 数据** — 确认 reversal 是否跨 3 seed 成立
2. **派 Paper Agent patch** — 更新 §4.6 和 appendix 的 14B 多 seed 数据
3. **check_paper_consistency** — 用 `paper_dir` 参数指向正确目录（之前踩过坑，用 `docs/paper/` 是错的）
4. **submit_paper_to_review** — Round 13，用 `continue` mode
5. **处理 Round 13 反馈 → ARR 提交**（DDL 5/25，还有 6 天）

## 关键上下文

- **s42 seed 的 14B 结果已有**：PPL 8.97，MMLU 从 Dense 60.3 降到 52.2（reversal -8.1pp）。如果 s123/s456 也 reversal → 强化 §4.6 诊断分析；如果不 reversal → 需重大叙事调整
- **Table 2 的 "BCE+comp" 标签已修正** — 改为 "BCE (2700 steps)"，footnote 说明无 compensation
- **Table 4 删除了 BCE+Compensation 行**（per-token eval 不兼容 TEAL），替换为 BCE+Gumbel no-penalty (PPL=32.22)
- **C1 ablation 全文已改名 "Target-Swap Ablation"**
- **Mistral Dense baseline 数据已修正**为 v0.3 实际 eval 值
- **review_issues.yaml** 完整记录 Round 11+12 所有 issue 及修复状态
- **现实目标是 3.0 Findings**（novelty 是结构性瓶颈，实验无法突破）

## 不要做的事

- 不要用 `docs/paper/` 路径调 `check_paper_consistency`，正确路径是 `paper/`
- 不要在同一张 GPU 上跑两个 14B eval（OOM）
- 不要向用户承诺 Accept (4.0)，游承松已被告知 3.0 Findings 是合理预期
- 不要手写 report.md 的 AUTO-FACTS 区，调 `auto_build_report_facts`


---

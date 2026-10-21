# reviewer / loop_11.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`d4f3331e2d4ef8b5dfa5.json`](../../sessions/d4/d4f3331e2d4ef8b5dfa5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-21T06:26:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 已全部释放，**GPU 边际价值 = 0**（已四次签收确认：v16、v20、v20 terminal、v21）。不要批准任何新实验，除非 Director 明确推翻此决定。
- RE 评估中 gold relation 始终在 candidate set（pre-filter 设计），in_schema_accuracy ≡ original_accuracy——不要质疑这个等价关系。
- "three architecture families"（不是 four）：Qwen、LLaMA、Gemini。之前版本写错过 "four model families"，已修正。
- "approximately separable"（不是 independent）：TOST logit scale p=0.209 inconclusive，DocRED raw interaction -9.4pp。措辞已全文降级。

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-38874`（root）+ `westd-24295`（root）
- 远程代码根：`/root/schema-dag-extraction`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/`
- 论文源码：`docs/paper/`（main.tex, results.tex, introduction.tex, discussion.tex, abstract.tex）
- 产出目录：`artifacts/`（rebuttal_talking_points.md, w4_relaxed_matching, error_mode_quartile 等）
- 活跃进程：**无**。所有实验已完成，无 RUNNING/cron/tmux。Registry 68 experiments total。

### 3. 📊 当前状态
**刚完成**：v21 终稿四项审查（claim-evidence、格式、top-3 攻击点、预防性 ablation）+ RE none evaluation check worker 审查。两份结果均已 post 给 Director。

**Registry 状态**：38 success, 9 negative, 10 failed, 4 killed, 7 preparing。0 RUNNING, 0 PREPARING 中有活跃的。

**等待中**：无 worker 回调、无 cron、无未决 Director 决策。项目处于提交前终态。

### 4. 📋 待办
- Director 转发新章节修改 → 按审查模式 B 逐维度审（叙事一致性特别注意 §4.4 和 Discussion）
- Director 要求模拟审稿 → 参考 v17 模拟审稿的 8 weakness 框架，W1-W8 + TP1-TP13 rebuttal 覆盖
- 审稿意见到达 → Read `skills/global/rebuttal.skill.md`，按 TP1-13 匹配回应
- Ethics Statement 补充请求 → check_figures_and_layout 已报 1 warning（missing Ethics Statement），EMNLP 非强制但建议有

### 5. 🎯 战略上下文
**核心结论**：训练免 LLM IE 退化沿两维运作——Dim1（count→recall decline, 最高 -49pp）和 Dim2（confusability→type substitution, BCS explains 22-58% RE variance）。Task asymmetry：BCS 预测 RE 但不预测 NER（relaxed matching + error-mode quartile 双重确认，非 metric artifact）。SDGD 因 merge amplification 和 routing failure 失败。

**最易判错的点**：
1. NER null 不是"没做够实验"——是被 4 种 matching mode + error-mode quartile + per-count 分析全面确认的结构性结论。不要建议"再跑一个 NER 实验"。
2. DocRED interaction 看似大（-9.4pp），但 range-matched 后降至 0.93pp（CI 含零）。攻击面在 range-matched sample size 小（n=29+55, power only for ≥10.5pp effects）。
3. Gemini count_16 correlation r=-0.80 是 single-point driven（LOO→r=-0.42, p=0.22），已在 Appendix T 透明披露。count_8（n=50）才是 Gemini Dim2 的主要证据。
4. 论文定位是 analysis/diagnostic paper，不是 method paper。"no solution" 是预期攻击面，TP13 已准备。


---

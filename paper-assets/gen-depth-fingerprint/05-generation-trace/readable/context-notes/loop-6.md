# director / loop_6.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`ffa4f799829cc18c69af.json`](../../sessions/ff/ffa4f799829cc18c69af.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-16T17:09:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- 主结果文件是 `8gen_logo_unfiltered.json`（binary F1=0.694, 3-class=0.762）。`8gen_logo_results_BUGGY_DO_NOT_USE.json` 绝对不能引用
- 8 generators: Pythia-1B, Pythia-2.8B, Qwen3-0.6B, Qwen3-1.7B, Qwen3-8B, OLMo-2-1B, Llama-3.2-3B, Mistral-7B-v0.3（5 families）。之前错误引入过 OLMo-1B，已纠正
- Gemma rp=1.1 仅进 appendix（rp-LOFO gate FAILED: binary 0.518/0.455），主结果保持 rp=1.0 unfiltered
- D038 决策：8-gen rp=1.0 unfiltered 为主表，Gemma rp=1.1 仅 appendix 分析

### 2. 🖥️ 基础设施快照
- 服务器：通过 project config 中的 SSH host 连接，工作目录 `/root/gen-depth-fingerprint/`
- 结果目录：`/root/gen-depth-fingerprint/results/`（所有 8gen_*.json 文件）
- 论文本地路径：`projects/gen-depth-fingerprint/artifacts/_project/paper/`
- GPU：cuda:0, cuda:2 分配给本项目
- Worker 活跃：`worker_code_fig1-8gen-redraw_20260516T164859`（Figure 1 重绘，刚完成回调在队列中）

### 3. 📊 当前状态
Agent 正在处理 worker:done 回调（gemma-cross-rp-comparison + fig1-8gen-redraw）。之前连续两次 Agent 执行出错未返回回复。

Round 5 审稿修复进度：
- Paper Agent 已完成 6/8 项（W1/W2/W4/W5/W6/M1）
- Rd5-W3（Figure 1 重绘 8-gen）：Worker 刚完成，回调在队列中待处理
- Rd5-M2（cross-model chain 8-gen 重跑）：尚未确认是否已派发/完成
- Rd5-M3（Mistral sliding-window 一句话）：optional，低优先级

review_issues.yaml 已更新，所有 Round 5 issues 标记 in_progress。

### 4. 📋 待办
- Agent 成功处理 fig1 worker:done 回调 → 确认 Figure 1 PDF 产出，派 Paper Agent 集成到论文
- Agent 成功处理 gemma-cross-rp 回调 → 确认 appendix 叙述数据就绪
- 若 Agent 再次出错 → replace_agent_queue 发简化单任务指令（拆分而非合并）
- Rd5-M2 cross-model chain 未完成 → 单独派 Worker 在 cuda:2 重跑（数据源：8gen features，~30min）
- 所有 blocking 项完成 → 考虑 Round 5.1 快速 re-review → compile → submit

### 5. 🎯 战略上下文
- 目标：EMNLP 2026 ARR，DDL 2026-05-25（剩 ~9 天）
- 核心 claim：generation depth 在 LLM 输出中留下可检测的统计指纹（DDR 三层分类）
- 论文评分：内部 Round 5 = 3.5 Weak Accept，修复 6 个 warning 后预期可达 Accept 水平
- 关键数字：Binary LOGO F1=0.694, 3-class=0.762, LOFO binary=0.686, baselines 4det_surface pooled 略高(0.705)但 per-gen LOGO 我们领先
- 易错点：(1) per-gen LOGO average vs pooled F1 不要混用在同一比较中 (2) baselines 用不同超参(100/3 vs 200/6)是有意为之 (3) continuation prompt type 数字用 prompt_type_results.json 的 0.781/16.9%
- Agent 连续出错的模式：任务太多合在一起容易触发空回复，下次拆成单任务派发


---

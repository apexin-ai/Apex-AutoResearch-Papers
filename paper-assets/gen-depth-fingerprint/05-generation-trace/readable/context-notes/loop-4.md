# director / loop_4.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`1d92ff5271ed0b14f7f3.json`](../../sessions/1d/1d92ff5271ed0b14f7f3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-15T22:06:43+00:00'
---

## 当前状态

项目 gen-depth-fingerprint 处于 Research + 审稿并行阶段。服务器 autodl-5090。

### 正在跑的实验（3个）
- plan-006-paraphrastic
- plan-007-cross-model（跨模型链 vs 单模型链的 depth signal）
- plan-008-multi-domain（news/scientific/creative 三域 seeds 的 domain robustness）

### Agent 当前任务
Agent 正在处理 consistency audit 后续修复指令（queue depth=0，idle 12s）。具体内容：
- Paper Agent 已修复 results.tex 的 #1-#4 数字问题（commit f7efa9a，统一为 0.764 等）
- Agent 刚修复 table2.tex feature group 标签错误（commit 0bb0699）：Surface only 改为 TTR+hapax_ratio(2个)，Reference only 改为 entropy_mean/std/min/max+tail_decay(5个)，F1 数字未动
- Agent 提到 results.tex 还有 4 处数字问题等 Director 批准后修复——但从指令看 Paper Agent 已经修了 #1-#4，需要确认是否还有残留问题

### 待处理
- plan-004-prep：Downstream utility 准备（depth-stratified 数据集 + OLMo-1B fine-tuning 脚本），等 Director 确认才开跑
- 58 个实验总计，38 成功，3 运行中，6 待处理

### 审稿阶段
Review 群已建（review_chat_id: oc_999770e4e57bfc6eabd12fc1f64af1ef），独立审稿团队在并行处理。论文溯源覆盖率 4/60，较低。

### 下一步建议
1. 确认 results.tex 数字问题是否全部解决（f7efa9a 已修 vs Agent 说还有 4 处待批）
2. 3 个 running 实验完成后及时分析结果、更新 paper
3. plan-004 downstream utility 是否批准启动——取决于 GPU 余量
4. 论文溯源覆盖率低（4/60），需要 auto_build_provenance 补齐


---

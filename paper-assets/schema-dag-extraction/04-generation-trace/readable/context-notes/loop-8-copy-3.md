# reviewer / loop_8.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`205011884008194ee750.json`](../../sessions/20/205011884008194ee750.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-16T19:09:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 cqa1-38874 只有 1 张 GPU (index 0)，无越界风险但也无并行能力——同时只能跑一个 vLLM 实验
- FewRel count_40 子集必须在论文中注明 "40-rel subsets sampled from the 80-relation pool"（C001 约束），不能暗示独立 pool
- 论文已全面替换 "additive separability" / "cleanly separable" → "bounded interaction"，**不可回退**。这是 Round 9 核心修复
- TOST equivalence margin 是 ±3pp（不是 ±5pp），registry 已修正。results.json 和论文文本必须一致

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-38874` (root)，工作目录 `/root/schema-dag-extraction`
- 模型：`/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/` (Qwen3-32B FP8, vLLM)
- 数据：`/root/schema-dag-extraction/data/fewrel_parquet/`（train+val）, Few-NERD/MAVEN/DocRED 同级目录
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/`
- 活跃进程：PID 408947 (VLLM::EngineCore, GPU 0, 89GB)——D051 Batch 2 的 25-batch count curve 实验
- 无 W&B 配置（本项目不用 W&B）

### 3. 📊 当前状态
**刚完成**：
- D051 Batch 1 验证报告已提交（Round 9 全部文本修复 PASS，W1-W5 + S3/S8 逐项验证通过）
- Director 三个战略问题已回答：文本修复难突破 3.25；无重大遗漏 novelty angle；Main ~20-25% / Findings ~60-70%

**正在运行**：
- D051 Batch 2 实验：FewRel 25-batch count curves (seed=42)，当前进度 count_16 完成 → count_32 进行中（约 30-40 分钟后完成 Part A）。Part B (seed 123/456) 尚未启动
- 实验**未注册 registry**，完成后需补注册

**等待中**：
- Director 对战略问题的决策（Main vs Findings venue 选择）
- 25-batch 实验完成后的结果审计

### 4. 📋 待办
- D051 count curves 实验完成（results_*.jsonl 出现）→ 核实 count curve 数值方向与论文 Figure 1 一致、25-batch SD 是否比 5-batch 更窄、检查是否与原有实验矛盾
- Director 决定 venue → 如果转 Findings 需审查 scope 缩减是否合理；如果冲 Main 需审查是否有新实验补强
- 如有 Part B (seed 123/456) 启动 → 验证多 seed 结果一致性，三 seed 方差是否在合理范围
- 如收到新的章节审查请求 → 按 §5 维度审查，先合规检查（red-section skill 痕迹）
- 如收到 Framing 提案 → 立即 Read `negative-framing-review.skill.md`，四维度审

### 5. 🎯 战略上下文
- **项目核心结论**：schema-induced degradation = Channel 1 (count, -42% to -56%) + Channel 2 (confusability, typical 2.2pp)。Count dominates by ~20×。Bounded interaction in RE (TOST p=0.003 at ±3pp), coupled in NER
- **DDL**：EMNLP 2026 ARR May 25，剩余 ~8 天
- **分数轨迹**：Round 7 (2.75) → Round 8 (3.25) → Round 9 (3.0)。未呈上升趋势
- **最易判断错的事**：
  1. Worker 标记 "done" ≠ 实验完成。Worker 只是启动了 nohup 进程，必须 SSH 查进程 + 结果文件
  2. 论文 Monte Carlo 叙事有 conditional/unconditional 两条线：unconditional r²=1.3-1.7% → batch 0.044；conditional R²=7% → batch 0.219。"3× amplification" 指的是 conditional 那条线，不是 unconditional
  3. MAVEN 的 BCS-F1 正相关是 centrality artifact（Qwen3 degree centrality r=0.854），不是真效应。pairwise SCS 仍然有效
  4. 25-batch 实验是为了加强 Figure 1 误差棒，不是为了改变核心结论。如果数值方向变了才是 critical


---

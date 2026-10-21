# reviewer / loop_11.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`4c8b7fe47cee721003e4.json`](../../sessions/4c/4c8b7fe47cee721003e4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-16T03:02:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（westb-13313）。之前发生过越界事故（2026-04-24），Reviewer 是最后防线。
- 模型路径陷阱：`/root/autodl-tmp/models/Qwen/Qwen3-1.7B-hf/` 只有 tokenizer 没有权重，正确路径是 `/root/autodl-tmp/models/Qwen/Qwen3-1.7B/` 或 `/root/autodl-tmp/models/Qwen3-1.7B-hf/`（无 Qwen/ 子目录）。r7n2 第一次崩溃就是路径错。
- r7n2 eval 必须用 episode-level split（D090 修正）。step-level split 有 same-episode leakage，结果只能作参考不能作判定依据。
- 论文数据源：主表引用 plan-012-full（11 tasks / 245 eps），robustness 引用 prescreening（30 tasks / 249 eps，仅 appendix）。绝对不引用 death_decomposition_report.json 和 results/plan_c_test_labels/implicit_sft.jsonl。

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313(root)，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型：Qwen3-0.6B/1.7B/4B 在 `/root/autodl-tmp/models/`；Qwen2.5-7B-Instruct 同目录
- 数据：`data/plan-004-implicit/implicit_sft.jsonl`（2040 samples, 95 non-tie episodes）
- 论文：`docs/paper/main.tex` + 分文件（abstract/introduction/experiments/discussion/conclusion/method/related_work.tex）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/`
- 活跃进程：r7n2 重启中（Worker 已派发，原 PID 921548 已死）。其余无活跃进程。

### 3. 📊 当前状态
**刚完成：**
- D087 narrative 一致性四维度审查（旧措辞清理干净，但§4.3 "granularity mismatch is bottleneck" 与 data scarcity narrative 冲突，"data scarcity"/"leakage" 未进入论文正文 — 已 warning Director）
- majority-vote-baseline 审查（router 47.1% < majority-vote 50.0% < always-det — 已 warning Director）
- r7n2 部分结果审查（25% scale 全部 model collapse，实验 OOM 崩溃 — 已 warning Director）
- ROADMAP 连续 3 轮审查（修正 r7n2 状态、推动 contingency plan D090、修正 leaky eval 判定标准）

**Registry 状态：**
- r7n2-data-size-ablation: ANALYZING → Worker 已派发重启（含 episode-level eval 补充）
- 其余实验全 DONE

**等待中：**
- r7n2 重启完成 → Worker 回调 → 审查结果 → 按 D090 contingency plan 判定 Outcome A/B
- 用户审批 Round 8（BLOCKING）

### 4. 📋 待办
- r7n2 Worker 完成回调 → 审查结果：episode-level eval 任一 scale 3-seed mean > 0.55 + 单调递增 → Outcome A（data scarcity），否则 → Outcome B（structural limitation）。**必须核对用的是 episode-level eval 不是 step-level。**
- r7n2 审查完 → 检查 Paper Agent 是否按 contingency plan 更新了 §4.3 和 Appendix router 部分
- Round 8 审稿请求到达 → 按 §5 章节审查模式做对抗审查，注意 §4.3 的 narrative 是否已统一
- 论文终稿前 → 最终一致性验证：abstract/intro/experiments/discussion/conclusion 的 router 解释是否一致

### 5. 🎯 战略上下文
**核心结论链：** D081-082（router episode-level=random, step-level leakage）→ D083-086（C2 reframe 尝试，多次修正）→ D087-088（撤回 structural limitation narrative）→ D089（C2 定调 negative）→ D090（r7n2 contingency plan）

**论文结构：** C1（DAF=90.41%）SOLID，C3（cross-model+MATH）SOLID，C2（router diagnostic）honest negative 降至 Appendix。论文核心是 decomposition finding + methodology，不是 router。

**最易判断错的事：**
1. **不要被 step-level eval 的 57.6% 蒙蔽。** 这是 leaky eval。Clean episode-level eval 是 47.1%±2.2% ≈ random。论文中报 57.6% 的地方都需注意上下文。
2. **§4.3 当前文本仍说 "granularity mismatch is the bottleneck"** — 这与 paper_framing.md 的 "data scarcity" narrative 冲突。已 warning Director 但论文尚未修改。审查时注意这个 gap 是否被修复。
3. **router-size ablation（0.6B≈1.7B≈4B）不区分 data scarcity vs structural limitation。** 两种假说都预测 "加大模型无帮助"。只有 r7n2 data-size ablation（在 clean eval 上）能区分。
4. **majority-vote baseline conclusion 在 registry 中仍标 "success"**，ROADMAP 说 Agent 已改为 negative 但需核实。


---

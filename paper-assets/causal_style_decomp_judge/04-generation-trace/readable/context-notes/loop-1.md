# director / loop_1.md

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`40fd55f05a1ae629d597.json`](../../sessions/40/40fd55f05a1ae629d597.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-21T22:50:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无本地 GPU 分配（纯 API 实验项目），不要尝试 `director_allocate_gpus`
- Gemini API 走 OpenRouter 代理：base_url=`http://47.94.22.126/v1`，key 已存储为 secret
- EMNLP 2026 主文本严格 8 页限制，Limitations 不计入；当前刚好卡在 8 页边界，任何主文本增加都需要同等压缩
- register_100_cf 实验 API blocked（Reviewer #84 建议取消），不要投入资源推进
- 论文数值必须与 registry 一致：Gemini BT formality p=.031（不是 .045），GEE Style OR=8.98（不是 9.16）——之前出过不一致被 Reviewer 抓

### 2. 🖥️ 基础设施快照
- 服务器：westb-29275 (connect.westb.seetacloud.com)，工作目录 /root/causal_style_decomp_judge
- 本项目主要是 API 调用实验（NLI/BT/GEE 分析），无 GPU 训练任务
- 论文目录：`projects/causal_style_decomp_judge/docs/paper/`，main.tex 入口
- artifacts 目录：`projects/causal_style_decomp_judge/artifacts/`（human_annotation/ 下有标注材料）
- 无活跃进程 / 无 tmux / 无 cron 实验任务
- Agent 当前空闲

### 3. 📊 当前状态
刚完成：
- Forest plot 重新生成（4 judges × 3 axes，含 Gemini），已在 `docs/paper/figures/forest_plot.pdf`
- Figure 1 "Blindspot in Action"（mvp_0048 case study）已集成到 page 1
- Gemini 全文数值修正（experiments.tex, appendix.tex, paper_framing.md）
- Limitations 补充 Gemini rewriter scope
- **R8 审稿已提交**（approval_id: apr_20260521T224941_aasq, status: pending），等用户审批 review mode

Registry：54 experiments（53 done, 1 queued register_100_cf）。无 RUNNING/PREPARING。
等待中：R8 审稿用户审批 → Review Director 启动审稿 → 审稿报告回传

### 4. 📋 待办
- R8 审稿报告回传 → 按 `review-report-action` skill 处理（Holistic Pass + Per-Comment Action Matrix），派 Agent/Paper Agent 修复
- 用户提供 human annotation 结果（5/22 做 50 pairs）→ 派 Agent 分析 + Paper Agent 集成到 §5 或 Appendix
- R7 issues（R7-W2 register classification, R7-W4 NLI FNR, R7-W5 verbosity 17.4% FPR, R7-REF1 Tripathi citation）已 assigned Paper Agent → R8 审稿会验证是否修复
- 所有修复完成 + R8 收敛 → 最终 polish pass → 5/25 AoE 提交 ARR

### 5. 🎯 战略上下文
- **核心发现**：Pairwise BT 检测到 57-84% style bias，所有 Likert 方法（5/7/100 点）均 d→0 检测不到 = "Likert Blindspot"
- **论文定位**：4 independent judges（GPT-4o/Qwen3-32B/Llama-3.3-70B/Gemini-2.5-Flash）× 3 axes × NLI-gated counterfactual = 8/8 Blindspot cells confirmed
- **评分轨迹**：R1:2.5 → R7:3.5（Borderline Conference）→ 目标 4.0（Main Conference）
- **3.5→4.0 的三个提分杠杆**：(1) Gemini 4th judge ✅ done (2) Figure 1 aha moment ✅ done (3) Human annotation ⏳ 5/22
- **易错点**：
  - 页面预算极紧（8 页边界），加任何内容必须同时压缩等量文本
  - Gemini formality 是 originality-dominated（不同于其他 3 judges 的 conditional regime），GEE 解读时不要混为一谈
  - Holm-Bonferroni primary family = 6 tests（3 judges × 2 axes），Gemini 是 confirmatory 不在 family 内
  - Claude Sonnet 4 是 negative control（无 detectable bias），不是 target judge


---

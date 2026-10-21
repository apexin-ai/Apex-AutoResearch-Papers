# director / loop_5.md

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`9d4fb4326d0325eb87bd.json`](../../sessions/9d/9d4fb4326d0325eb87bd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-23T19:44:37+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只有 westd-20861:cuda:0（1×RTX PRO 6000 Blackwell 102GB），不可用其他设备
- SS s456 训练正在 GPU 上跑，不要中断或抢占
- plan_024 (SS+steering 联合 eval) 已取消——数据已存在于 `ss_s42_ar_n50.json`，Reviewer 确认 SS 和 steering 不叠加（高 β 趋同）
- paper_framing.md 的 gap 数字已从 ~30× 统一为 8×–27×（论文 N=50 数据），不要回退到旧数字
- DDL 已切换至 ARR August 2026-08-03（~10 weeks），不再是 5/25

### 2. 🖥️ 基础设施快照
- 服务器：westd-20861，工作目录 `/root/turn_residual_gating/`
- Python：conda base (`/root/miniconda3/bin/python`)
- 模型：Qwen-2.5-7B-Instruct + Llama-3.1-8B-Instruct（路径在服务器 autodl-tmp 下）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/`
- 论文路径：`paper/sections/*.tex`（注意 paper_compile_and_check 需传 `paper_dir` 参数）
- 匿名 repo：`https://github.com/anonymous-nlp-2026/turn_residual_gating`（HTTPS，commit a7a4eac）
- 活跃进程：SS s456 训练（PID 112418，GPU chain 自动串行：s456 eval → Qwen-1.5B → MMLU）

### 3. 📊 当前状态
**刚完成**：
- 数据正确性审计（85 数字，88% 一致）→ 5 项修复已派 Agent（D1 Fig4 caption critical, D2-D6 medium/low）
- paper_framing.md 数字同步（~30× → 8×–27×，Reviewer warning 已修）
- Framing 升级：experiment_plan.yaml 新增 plan_024-027，paper_framing.md 更新 5th contribution + story arc
- ROADMAP 更新，D051 决策已记录

**正在进行**：
- Paper Agent：Reframe 模式（SS 升为独立 Results + 5th contribution + Abstract 重塑）
- Agent：正在处理实验排期 + 审计修复（队列中有 3 条消息）
- GPU：SS s456 训练中（chain 后自动 eval → Qwen-1.5B → MMLU）

### 4. 📋 待办
- Agent 完成审计修复 → 验证 Fig4 caption / Fig3b N=5 标注 / PCGrad 时间 / SS ratio / 跨模型 gap 聚合 → recompile
- SS s456 eval 完成 → 3-seed mean±std 计算 → 更新论文数字（abstract/Table 1/discussion）
- Paper Agent Reframe 完成 → 审阅 SS Results 小节 + Abstract + 5th contribution
- s456 chain 全部完成 → 排入 plan_025 KL divergence (CPU) + plan_026 Llama SS (10h GPU) + plan_013 Llama gradient conflict (0.5h)
- 3-seed 数据到齐 + Reframe 定稿 → Round 4 Group C 审稿（submit_paper_to_review）
- SS β=0 seed 间方差较大（s42: 0.347 vs s123: 0.423, 22%）→ s456 出来后评估是否用 mean±std 还是 range

### 5. 🎯 战略上下文
- **D051 核心决策**：用户批准 framing 从 3.0 升级到 3.5。对标 gromov/sun/xiao "发现→定位→修复" 模式。SS gap 8×→1.4× 从 Discussion 升为独立 Results，新增第 5 条贡献
- **SS+steering 不叠加**是已确认结论（Reviewer 核实），但 SS 在 β=0 的独立价值（0.064→0.347, 5.4×）仍然很强，论文应讨论交互效应
- **易错点 1**：plan_024 已取消，不要再派执行
- **易错点 2**：paper_compile_and_check 默认路径是 `docs/paper/`，实际是 `paper/`，必须传 paper_dir
- **易错点 3**：d048 eval 中 base_ar_n50.json 曾被覆盖事故（M027），s456 已用不同文件名规避
- **5th contribution 的 "首次" claim**：需要 s456 确认 + 理想情况 Llama SS 跨模型验证支撑。若 Llama SS 失败，scope 限定到 "on Qwen"
- 决策链：D041(SS success) → D048(multi-seed plan) → D050(N=50 数据切换) → D051(framing 升级 3.5)


---

# agent / loop_3.md

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`336fb5c4c03fbe66af8d.json`](../../sessions/33/336fb5c4c03fbe66af8d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-14T17:42:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 `cuda:0`（autodl-rtx6000pro），绝不碰其他卡
- 服务器白名单：autodl-rtx6000pro（主）、westd-32608（备），account=root
- **禁止双进程启动 pipeline**——已因 submit_on_allocated + nohup 同时启动导致数据损坏和静默退出。启动前必须确认前一进程已终止
- mvp_pipeline_004 的输出文件 `results/mvp_v4_full.json` 是 109 样本的累积结果，**不可覆盖**，续跑必须用 `--resume`
- Excl. Unknown 模式下 C4 仅 +3.6pp（FAIL），汇报时必须同时报 All mode 和 Excl. Unknown mode 指标，不得 cherry-pick

### 2. 🖥️ 基础设施快照
- **服务器**：autodl-rtx6000pro，工作目录 `/root/autodl-tmp/crdd`
- **Python**：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- **环境激活**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型**：Qwen3-32B-AWQ（awq_marlin），通过 vLLM 本地 serving（端口未记录，需 SSH 探查）
- **数据集**：FOLIO validation set，204 samples，路径在 pipeline 代码内硬编码
- **wandb**：未配置（本项目用 JSON 结果文件，不走 W&B）
- **活跃进程**：mvp_pipeline_004 已静默退出（109/204），无活跃 PID；vLLM server 可能仍在运行
- **Cron**：0 个活跃 cron（reconcile 确认）

### 3. 📊 当前状态
**刚完成**：mvp_pipeline_004 分析——109/204 样本处进程静默退出（sample 110 处，无 traceback）。已完成部分数据 MVP 5/5 PASS（All mode），但 Excl. Unknown 模式 C4 FAIL。registry 已更新为 ANALYZING + conclusion=success。

**Registry 状态**：
- `mvp_pipeline_004` — **ANALYZING**，109/204 partial data，5/5 MVP PASS (All mode)，进程已退出需续跑
- `mvp_pipeline_003b` — DONE/killed
- `mvp_pipeline_003` — DONE/killed
- `mvp_pipeline_002` — DONE/negative
- `mvp_pipeline_001` — DONE/negative
- `mvp_baseline_001` — DONE/success (baseline 74%)

**等待中**：
- 无活跃 Worker（池=0）
- 无活跃 Cron
- 需要：(1) 续跑 mvp_pipeline_004 剩余 95 样本；(2) 全量完成后运行 evaluate_mvp.py 最终评估
- Director 尚未收到 109 样本的 5/5 PASS 中期汇报（或已收但未回复——需确认）

### 4. 📋 待办（条件触发式）
- **立即**：续跑 mvp_pipeline_004（`--resume results/mvp_v4_full.json`），先确认 vLLM server 存活 + 前进程已终止
- mvp_pipeline_004 全量 204 完成 → spawn worker 跑 `evaluate_mvp.py` → 最终 MVP gate 判定
- 全量 MVP 5/5 PASS → 向 Director 汇报 + 启动 post-MVP kickoff（多模型扩展、v5b anti-lazy Unknown）
- 全量 C5 仍 FAIL（<60%）→ 分析 C5 失败样本 → 判断算法改进 or 阈值调整 → 向 Director 提方案
- 全量 Excl. Unknown C4 仍 FAIL → 需在汇报中诚实标注，v5b anti-lazy Unknown prompt 是关键改进方向
- Director 批准 post-MVP → 准备 v5b pipeline（prompt 已设计在 memory.md 中记录）、多数据集（ProofWriter）、多模型实验

### 5. 🎯 战略上下文
- **核心假设**：跨表征（FOL vs Code）分歧能自动诊断 LLM 推理错误。MVP 用 FOLIO + Qwen3-32B-AWQ 验证 5 个 claims（C1-C5）
- **当前结论**：v4 pipeline 109 样本 All mode 5/5 PASS，Excl. Unknown 4/5（C4 FAIL）。这是从 v1(2/5) 到 v4(5/5) 的关键突破，truncation detection + thinking-off retry 是核心修复
- **关键 nuance**：
  - DISAGREE 方向 9:1 不对称（FOL 几乎总对，Code 几乎总错）——post-MVP framing 不能 claim bidirectional
  - 46.3% Code=Unknown 是 lazy prompt 问题（LLM 主动放弃），v5b 设计了 anti-lazy prompt 待验证
  - AGREE_WRONG 7.7% 是分歧方法的结构性盲区，论文需诚实讨论
- **易踩的坑**：
  - 进程静默退出是已知问题（sample 110 处），续跑前检查 vLLM health
  - 不要把 All mode 和 Excl. Unknown mode 混报——审稿人会追问
  - v5 closed-world 2-way 方案已被撤回（D007），不要再提
- **决策链**：D001(MVP方案) → D002(Reviewer修订) → D005(v1失败根因=prompt) → D006(v2 FOL修复) → D007(v5→v5b)


---

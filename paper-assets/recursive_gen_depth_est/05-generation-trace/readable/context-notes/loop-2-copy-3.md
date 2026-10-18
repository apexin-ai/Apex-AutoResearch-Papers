# reviewer / loop_2.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`27aa38b5caa938a70c25.json`](../../sessions/27/27aa38b5caa938a70c25.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T18:23:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cuda:0 和 cuda:1，两块都属于本项目。越界进程必须 CRITICAL 打回。
- 服务器名必须用 `gpu-6000pro-2`。`westb-52439` 不在系统已知列表中——用它做 SSH 会失败，cron 监控会误杀实验。**已因此导致 OLMo-002 被两次 false-failure**。ROADMAP 已修正但 cron/completion handler 的 server 来源可能仍未根治。
- OLMo LoRA targets 是三个模块 `q_proj,k_proj,v_proj`（不是两个）。GPT-2 XL 是 `c_attn,c_proj`。
- DivEye 引用已修正为 TMLR 2026（从 ICLR 2026 withdrawn）。论文中不要写 ICLR。

### 2. 🖥️ 基础设施快照
- 服务器: `gpu-6000pro-2`, 2× NVIDIA RTX PRO 6000 Blackwell 98GB
- 工作目录: `/root/autodl-tmp/recursive_gen_depth_est`
- Python: `/root/miniconda3/bin/python`（conda base env）
- 模型路径:
  - Pythia-1.4B: `/root/autodl-tmp/models/pythia-1.4b/`
  - OLMo-1B: `/root/autodl-tmp/models/olmo-1b-hf/`
  - GPT-2 XL: `/root/autodl-tmp/models/gpt2-xl/`
  - DeBERTa-v3-large: `/root/autodl-tmp/models/deberta-v3-large/`
- HF cache: `/root/autodl-tmp/.hf_cache`
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/`
- 活跃进程: 截至 handoff 时无 RUNNING 实验。GPT-2 XL 在 ANALYZING，OLMo-002 刚修正为 DONE/success。

### 3. 📊 当前状态
**刚完成的审查**:
- cross_model_gpt2xl_001: pipeline 完成（4×5000 samples），status=ANALYZING，等分析 worker 出 metrics
- cross_model_olmo_002: pipeline 完成（4×5000 samples），经历两次 false-failure 后终于修正为 DONE/success
- 3×3 matrix 脚本已审查通过: olmo_temp09/topk50 + gpt2xl_temp09/topk50 四个脚本 OK，depth_0 数据已就位，LoRA adapter 复用 nucleus 的
- DivEye 引用已验证: 论文真实，venue 修正为 TMLR 2026

**Registry 快照**:
- `cross_model_gpt2xl_001`: ANALYZING
- `cross_model_olmo_002`: DONE/success
- `pythia_temp09_001`: DONE/success
- `mvp_pipeline_pythia_002`: DONE/success
- `pythia_topk50_001`: PREPARING

**3×3 矩阵覆盖**: 2/9 done (Pythia nucleus + temp09), 1/9 ANALYZING (GPT-2 XL nucleus), 1/9 just completed (OLMo nucleus), 1/9 PREPARING (Pythia topk50), 4/9 scripts ready but not launched (OLMo/GPT-2 XL × temp09/topk50)

### 4. 📋 待办（条件触发式）
- GPT-2 XL 分析 worker 完成 → 审查 metrics（4-class acc, AUC, feature importance），对比 Pythia MVP baseline
- OLMo-002 分析 worker 启动/完成 → 同上，重点看跨模型 feature ranking 是否一致（var_surprisal 是否仍 #1）
- OLMo/GPT-2 XL temp09/topk50 pipeline 提交 → 审查 GPU 分配合规 + 监控 server name 是否正确
- pythia_topk50_001 提交 → 审查
- Atlas (plan_006) 启动 → 审查 EDD 计算、cross-model consistency、是否覆盖 Dream D002 硬约束
- DCOL (plan_004) 启动 → 审查 3-way split、N-pair loss 完整性、margin initialization
- 论文章节提交 → 按 Section 5 评分模板审查，必做合规检查（Agent 是否看过 red-section skill）
- multi-seed evaluation 仍未规划 → 论文写作前必须至少 3 seeds

### 5. 🎯 战略上下文
- **D001**: MVP PASS, 78.2% 4-class acc, depth signal from distribution narrowing confirmed
- **D002**: Dream 三档分析, Atlas/EDD 为 primary contribution, DCOL 为 secondary (CLOC incremental)
- **EMNLP 2026 ARR May 25** = 11 天。GPU 预算充足（~35 GPU·h remaining, 2 GPU = ~18h compute）
- **跨模型 loss 趋势已确认一致**: Pythia 2.24→1.39→1.03, OLMo 2.27→1.65→1.23, GPT-2 XL 2.55→1.71→1.34。三个模型均单调递减。
- **最容易判断错的事**: OLMo 的 registry 状态。它被 false-failure 了两次，根因是 server name 在 cron/handler 中的来源未根治。如果你看到 OLMo 标为 failed，**先 SSH 查日志和数据文件再下结论**，不要信 registry conclusion。
- **3×3 矩阵是论文的关键缺口**: paper_framing 承诺 "3 models × 3 strategies" 但当前只有 nucleus 完成。temp09/topk50 脚本已就绪但未提交。不补全则 Atlas cross-strategy claim 无法支撑。
- **DCOL 数据泄漏已修复**: dcol_feature_mlp.py 从 2-way 改为 3-way split (70/15/15)。验证过。
- **DivEye 引用坑**: baselines.py 代码中已修为 TMLR，但论文 bib 中也需同步。


---

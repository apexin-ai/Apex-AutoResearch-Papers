# reviewer / loop_9.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`5a3f393ffc58450b0f80.json`](../../sessions/5a/5a3f393ffc58450b0f80.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-15T16:20:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`cuda:0` 和 `cuda:1`（westb-13313 的 2× RTX 5090）。进程 CUDA_VISIBLE_DEVICES 必须在 [0,1] 内，越界立即 CRITICAL
- `ssh_read_only` 不支持管道符 `|`，多 pattern grep 必须分多条命令。多个 worker 反复踩坑
- `episode_level_collection.py` 的 `cleanup_gpu_processes(gpu_id)` 会杀同卡所有 GPU 进程——在已有进程运行的卡上启动新任务前必须确认
- 论文编译路径有本地/服务器双份文件（`docs/paper/` vs 服务器 `paper/`），修改后必须双向同步，否则提交 PDF 可能是旧版
- plan-012-full（245 eps / 11 tasks）是论文主分析数据集，所有引用数字必须与此一致，不能混用 prescreening 30-task 数据

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313 (root)，SSH: `ssh connect.westb.seetacloud.com`
- 工作目录：`/root/autodl-tmp/simgate-modular-routing`
- Python：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：`/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct`（VLLM 推理，~28GB/卡）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/`
- 活跃进程（截至 handoff 前）：plan-006 chemistry-mix 补收 PID 509602 (GPU0)，收集 7 eps (idx 13→19)。GPU1 空闲。两个 VLLM EngineCore 都已被 kill，补收进程自带新 VLLM
- 无 W&B（项目未配置 W&B）

### 3. 📊 当前状态
**刚完成的审查**：
- D060-D062 ROADMAP 审查 ✅
- 57.6% ground truth 验证 PASS（plan-013 的 4-seed 固定 split 均值，可信）
- 78.9% death-asymmetry 独立溯源 PASS（75/95 genuine labels）
- ALFWorld methodology 审查 WARNING（"deterministic" 语义不同，无 death 机制，不可放在 DAF narrative 下）
- Discussion pilot-50→N=300 替换 PASS（81.0% vs 76.7%, p=0.079, 已落地服务器）
- SF5-SF7 引用 PASS（CRPO/RouteLLM/Reflexion 已添加到本地 docs/paper/，**服务器端尚未同步**）
- SF3 death timing 分析 PASS（第二版用 245 eps 正确数据集）
- Plan-006 碰撞风险处理：GPU1 kill → 连锁崩溃 GPU0 VLLM → 数据完好 113/120 → 补收中

**Registry RUNNING**：plan-006-deep-internal（被 cron 误标 failed，实际 113/120 eps 完好，chemistry-mix 补收中）

**等待中**：
- Chemistry-mix 补收完成（7 eps，预计 ~20-30 min from 16:15 UTC）→ 需要全量数据质量审计
- Paper Agent Round 7 论文修改（MF1-4, SF1-7, m1-6 全部 🔄）→ 修改完成后需章节审查
- 本地→服务器文件同步（references.bib, related_work.tex 已在本地更新但服务器端未同步）

### 4. 📋 待办（条件触发式）
- Chemistry-mix 20/20 到达 → 全量 plan-006 数据质量审计（6 tasks × 20 eps, 检查 JSON 完整性 + death rate + deep-internal modality 标记）→ 建议 Agent 改 registry 为 success
- Paper Agent 提交章节审查 → 按 Section 5 审查模式 B 执行（Claim 可信度 / 叙事逻辑 / 审稿人攻击面），特别关注：title 是否已去 "90%"、abstract 是否加 scope qualifier、MF2 contribution 4 是否降级、Discussion 是否用 N=300 数据
- 本地→服务器文件同步完成通知 → 验证 `paper/references.bib` 和 `paper/related_work.tex` 包含 CRPO/RouteLLM/Reflexion
- Plan-006 全部完成 + 分析出结果 → 审查 deep-internal vs fast-internal 分数对比，评估是否值得纳入论文
- 距 DDL 5/25 倒数 5 天时 → 主动审查实验覆盖矩阵（compute_coverage_matrix），确认所有 Core Claims 有数据支撑

### 5. 🎯 战略上下文
- **核心结论**：ScienceWorld 上 ~90% routing signal 来自 death avoidance（DAF=90.41%, r=0.97, 245 eps / 11 tasks）。Round 7 审稿 borderline reject，核心发现未被挑战，问题集中在 overclaiming / scope / references
- **D061 Action Matrix**：78.9%（75/95 non-tie labels from death asymmetry）取代 DAF~90% 做 headline（penalty-independent）；title 去数字；contribution 4 降级 preliminary；补 Safe RL/RouteLLM/Reflexion 引用
- **D062**：title 必须改（当前仍含 "90%"）+ Discussion pilot-50 已替换 ✅
- **R6→R7 回归根因**：Paper Agent 倾向最小修改（加 caveat 句）而非结构性调整。D062 改为精确位置+改写内容指令防止重现
- **最容易判断错的事**：
  1. 不要把 prescreening 30-task 数据（378 eps）和 plan-012-full（245 eps / 11 tasks）混用——论文所有数字必须基于 245 eps
  2. ALFWorld 没有 death 机制，不能放在 DAF narrative 下，只能作为 "external computation helps" 的独立补充证据
  3. 57.6% router accuracy 的方差主要来自 val split（跨 split std=5.2%），不是 seed（固定 split std=0.5%）——论文报 seed-robustness 时要说明
  4. `docs/paper/` 是本地编辑版，`paper/` 是服务器编译版——两边不自动同步，每次修改后必须手动 sync


---

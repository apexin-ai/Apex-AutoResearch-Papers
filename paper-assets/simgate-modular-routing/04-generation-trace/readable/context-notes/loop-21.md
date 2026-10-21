# agent / loop_21.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_21.md`
- **Structured JSON:** [`d348d8bb45a9bb5c6ea7.json`](../../sessions/d3/d348d8bb45a9bb5c6ea7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: max_wall_time
updated: '2026-05-21T17:23:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 已全部释放（D129），**不要在任何服务器上启动 GPU 实验**
- 论文核心数字修改前**必须先查 registry 确认权威值**（M015 教训：Worker 从服务器文件计算的 step count 与 registry 不一致，导致错误修改被 Director 回滚）
- Page 8 边界极紧——任何正文修改后必须编译验证 Conclusion 仍在 page 8 内，溢出立即回滚
- 数据已从 westb-13313 迁移到 westd-18266，**westb-13313 即将释放，不要再连**

### 2. 🖥️ 基础设施快照
- 服务器：westd-18266（4× RTX PRO 6000 96GB），数据目录 `/root/autodl-tmp/`
- 项目代码：`/root/autodl-tmp/simgate-modular-routing/`
- HF cache：`/root/autodl-tmp/.hf_cache/`
- 模型：`/root/autodl-tmp/models/`（Qwen2.5-7B/72B, Llama-3.1-8B, Gemma-2-9B）
- 磁盘：201G/250G used（50G 可用）
- 本地论文路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/`
- 活跃进程：无（GPU 已释放，vLLM 进程已退出）
- Cron：0 活跃

### 3. 📊 当前状态
论文确认 **submission-ready**，等待用户启动 ARR 提交流程（DDL 2026-05-25，剩 ~4 天）。

刚完成的工作链：
1. 数据迁移 westb→westd ✅
2. Reproducibility checklist 5 项补充（推理参数/prompt 模板 Appendix T/ScienceWorld v1.2.3/MATH 分布/GPU-hours 分解）✅
3. 数据一致性修复（MATH labels 7.3/8.3/84.4, step counts Director 已回滚为 97.4%）✅
4. \cite→\citep 28 处 + \hypersetup 匿名化 ✅
5. Em-dash 19→4 处 ✅
6. Round 25 修复（P0 词汇/P1 Conclusion future work/P2 Related Work 压缩+扩展/P3 Contribution router 提及/Safe orphan bib 删除+Agent-SafetyBench 添加）✅
7. 最终 consistency check 全 PASS（12 项数字一致/0 undefined/51 bib entries 0 orphan）✅

Registry：121 实验全部完成（53 success / 30 negative / 17 failed / rest killed）。无 RUNNING/PREPARING。

### 4. 📋 待办
- 用户确认启动 ARR 提交 → 协助准备 submission form（title/abstract/keywords 已提取在 Worker 产出中，track 建议 Interpretability and Analysis）
- Director 要求修复 Appendix orphan labels → 快速加 \ref（已确认不修）
- 内部审稿结果返回（apr_20260521T004926_35g5）→ 处理审稿意见
- 用户决定匿名 repo → 创建 requirements.txt + README.md 打包 supplementary

### 5. 🎯 战略上下文
- **核心结论**：Death avoidance 占 ScienceWorld routing signal 的 78.9%（label fraction）/ 88-90% DAF（跨三模型），routing signal ≡ task-type identity
- **决策链**：D126/D127 framework-centric pivot → D129 释放 GPU → D130 接受 Findings 级别 (3.0)，不追 Borderline Conference
- **Rebuttal 预案**：3 条已备（artifacts/rebuttal_prep.md）：单环境泛化/trivial finding/无 actionable solution
- **易错点**：
  - MATH 数据只有 2 个类别（Algebra 585 + Counting & Prob 210），不是预期的 7 个——不要假设 7 类
  - Gemma CI [79.5%, 98.4%] 是正确的（来自 unified_episode_bootstrap.json B=10000），registry 中 [68.8%, 100%] 是旧方法——不要用 registry 值覆盖论文
  - 论文 25 页，主文刚好 8 页，Conclusion 贴着 page 8 底部——任何正文增加都可能溢出


---

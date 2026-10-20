# reviewer / loop_6.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`9b30524a5cf710bb8129.json`](../../sessions/9b/9b30524a5cf710bb8129.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-14T12:49:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:0**（westc-26893 上只分配了 1 张 RTX 4090D）
- 服务器别名已从 `autodl-4090d` 改为 `westc-26893`，旧别名会 SSH 失败
- exp-006 正在占用 cuda:0（~15GB VRAM），exp-015/exp-004 必须等 exp-006 完成后才能启动，不能并行
- 论文文件在**本地** workspace（`projects/gen-depth-contamination/docs/paper/`），训练代码/数据在**远程** `/root/autodl-tmp/gen-depth-contamination/`——两边可能有同名残留，审"未改"类结论前必须双边核对

### 2. 🖥️ 基础设施快照
- 服务器：**westc-26893**（root），时区 **UTC+8**
- 工作目录：`/root/autodl-tmp/gen-depth-contamination`
- Python：`/root/miniconda3/bin/python`（conda base，不用 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- HF cache：`/root/autodl-tmp/.hf_cache`（含 Pythia-1.4B、OLMo-1B-hf、Qwen2.5-1.5B-Instruct、Qwen2.5-7B-Instruct）
- 磁盘：119G 空余
- 活跃进程：exp-006 tmux session `exp_006_graduated_filtering`（PID 70982，旧 PID 61363/46129 已失效）
- 本地论文：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/`

### 3. 📊 当前状态
**我的审查轮次已完成以下 worker：**
1. `worker_writing_llm-confidence-analysis` — PASS，discussion.tex §5.5 新增 DetectGPT/Binoculars 推论段落，数据与 exp-011 registry 一致
2. `worker_code_fix-drayson-b-value` — PASS，b=1.5→b=1 三处统一
3. `worker_edit_universality-softening` — PASS，论文中零个 "universal/universality"
4. `worker_review_paper-consistency-audit` — WARNING，发现 2 个需修复项（limitations 计数 "seven"→"eight"；intro:50 "depth≥3"→"depth≥2"）
5. `worker_review_discussion-coherence` — **CRITICAL**，discussion.tex:181 事实性错误（"from depth-1 text"→"from one another"），已 post Director
6. `worker_infra_post-exp006-readiness` — WARNING，ETA 时区错误已纠正（17:30→10:00 UTC）

**RUNNING 实验：**
- exp_006_graduated_filtering：20/50 runs，ETA ~05-15 10:00 UTC，6 strategies × 5 seeds + base

**待修复（已 post Director，等派单）：**
- discussion.tex:181 CRITICAL 事实性错误
- discussion.tex:93 "depths≥3"→"depths≥2"
- introduction.tex:50 "depth≥3"→"depth≥2"
- discussion.tex:114 "seven limitations"→"eight"
- Limitations 段 neural probe 重复 4 次（建议合并）

### 4. 📋 待办（条件触发式）
- exp-006 完成回调 → 审查：(1) 6 策略间 MMLU/HellaSwag 差异是否显著（paired t-test p<0.05）；(2) graduated vs binary-ours 是否有 ≥1pp 提升；(3) GPU 资源核查（必须是 cuda:0）；(4) 分析脚本 `scripts/exp006_analyze.py` 输出与 registry 交叉验证
- exp-006 结论 positive → 审查 C3 章节写作（experiments_c3.tex 从占位符填数）
- exp-006 结论 negative → 审查 fallback story（D013 预案）是否被正确执行
- exp-015 重跑完成 → 审查：Pythia/OLMo K*_neural 是否也=3（若=2 → self-familiarity 效应，需调整论文 neural probe 章节定位）
- exp-004 7B 完成 → 审查：K*_7B 是否=2（若>2 → scale defense 段落需重写）
- discussion.tex 事实性错误修复 worker 完成 → 验证三处 "≥3"→"≥2" + L181 + limitations 计数

### 5. 🎯 战略上下文
- **核心结论**：K*_empirical=2，跨 8 条件不变（4 model-mode + 4 decoding），论文定位为 "consistent boundary" 非 "universal"
- **2+1 claim 结构**（D012）：C1'(K* characterization) + C3(graduated filtering) + supporting analysis
- **C3 是单点依赖 exp-006**（D013）：如果 graduated filtering 无效，fallback story 为 "K*=2 的 negative practical implication——即使 ordinal signal 存在，graduated filtering 未必优于 binary"
- **Neural probe K*=3 极度边缘**（2v3 AUC=0.6195，fold 2 仅超 θ 0.52pp），且仅 Qwen-cont 单数据集。论文中引用了 4 次但缺 bootstrap CI——exp-015 重跑是 must-have
- **最容易判断错的事**：服务器时间是 UTC+8，`ls -lt` 显示的是本地时间。之前已有一次 ETA 被误报 +8h。所有涉及服务器时间戳的计算必须换算
- **已关闭的风险**：universality 措辞已软化、scale defense 已加、pipeline figure 已生成、Drayson b=1 已统一
- **仍开放的风险**：discussion.tex:181 CRITICAL 事实性错误（派单中未完成）、C3 全是占位符、neural probe 单数据集


---

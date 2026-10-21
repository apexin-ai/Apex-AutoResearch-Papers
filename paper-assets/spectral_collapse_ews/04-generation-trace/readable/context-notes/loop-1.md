# director / loop_1.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`aab5f1c0419f92af9a84.json`](../../sessions/aa/aab5f1c0419f92af9a84.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-16T12:07:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0 和 cuda:1（rtx6000-diagprobe 项目白名单）
- Phase 0 go/no-go 基线是 Gen 1（不是 Gen 0），decline rate 算 Gen 1-10（D004）
- 论文引用禁止凭记忆编写——必须对照 IDEA_BRIEF Key References 逐条核对（之前 12 条 bib 中 10 条被编造，已修复）
- controller.py 的 r_min=0.20, r_max=0.80（不是论文初稿误写的 0.10/0.90）
- 用户明确说"不要调整会议"——保持 EMNLP ARR May 25 目标，不要建议换会议或延期

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe (connect.westd.seetacloud.com)，2× RTX PRO 6000 Blackwell 94GB each
- 工作目录：/root/spectral_collapse_ews/
- Python：/root/miniconda3/bin/python（aml-train 镜像，conda base 环境���
- 模型：/root/spectral_collapse_ews/models/（pythia-410m-deduped 已下载，pythia-1b-deduped 下载中）
- 数据：/root/spectral_collapse_ews/data/（train_real_50k.pt, eval_5k.pt, spectral_1k.pt）
- 论文：/root/spectral_collapse_ews/paper/（method.tex, related_work.tex, introduction.tex, abstract.tex, experiments.tex, references.bib）
- 活跃进程：exp_001 Phase 0 训练 PID 7396 cuda:0（Gen ~2-3/10）；auto_eval_hellaswag.sh PID 14666 cuda:1（后台监控 checkpoint 自动跑 HellaSwag）
- Pythia 1B collapse 实验刚派发到 cuda:1（Agent 正在处理）

### 3. 📊 当前状态
刚写完 handoff。Phase 0 (exp_001) 在 cuda:0 跑到约 Gen 2-3/10，预计还需 1.5-2.5h。
- Registry: exp_001 RUNNING（应已更新，之前是 PREPARING）
- Agent 队列 depth=3：正在处理 1B 实验启动 + log-det 追加 + experiments.tex 修正
- 论文初稿骨架已完成（method/related_work/intro/abstract/experiments），全部经 Reviewer 审查，bib 16 条完整
- Controller.py 已通过所有 Reviewer 审查（budget-constrained, off-by-one fixed, budget leak fixed）
- HellaSwag Gen 0 baseline = 0.4130 (与文献一致)

### 4. 📋 待办（条件触发��）
- Phase 0 完成回调 → 检查 go/no-go：eff_rank Gen 1-10 单调下降(≤1波动) + 加速比≥1.5x + ppl≥20%上升 → GO则校准τ/k并立即派 Phase 1（3条件×3seeds×10代 + linear-increasing第4条件）
- Phase 0 eff_rank Gen 1-3 持续不降 → 检查 log-det 是否下降 → 下降则切 log-det 为主信号 → 均不降则 kill 项目
- Phase 1 完成 → 审批：adaptive vs fixed ≥3ppl (p<0.1) = PASS → complete_mvp()；1-3ppl = borderline → 加seed到5；≤0 = FAIL → kill
- 1B collapse 实验完成 → 与 410M 对比 collapse 曲线，验证跨规模迁移
- Agent experiments.tex 修正完成 → 确认参数一致性 WARNING 已解决

### 5. ���� 战略上下文
- 决策链：D001(MVP方案) → D002(采纳Reviewer:3seeds+量化go/no-go) → D003(保持May25) → D004(Gen1为baseline)
- 核心风险：Gen 0→1 eff_rank 上升（417.5→491.8），Reviewer 分析为 pretrained anisotropy 打散，已决定以 Gen 1 为基线。如果 Gen 1→3 继续不降，需要看 log-det（已加到 evaluate.py）
- 用户偏好：行动优先，不要因 Reviewer 迭代反复改 ROADMAP（记录在 memory: feedback_stop_iterating.md）
- Phase 1 新增第4条件 linear-increasing (r_t: 0.30→0.70)，隔离闭环反馈增量价值
- 最容易判断错的事：Phase 0 go/no-go 的 "单调下降" 从 Gen 1 开始算不是 Gen 0；论文参数必须与 controller.py 代码一致（k/τ 待 Phase 0 校准，现在写 "calibrated from Phase 0"）


---

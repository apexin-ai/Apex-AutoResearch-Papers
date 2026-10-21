# director / loop_8.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`9fd388a87b8dbe039bc9.json`](../../sessions/9f/9fd388a87b8dbe039bc9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-17T07:03:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 和 cuda:1（bjb1-45299 分配的 2 张卡）
- 论文数字必须有 `artifacts/analysis/` 下的 JSON 文件直接支撑，不允许推测（M004 教训）
- CIVODetector 阈值已统一为 ve_threshold=0.49 + 2/3 eval decline rule（commit 3328f53），paper 与代码必须一致
- FPR 必须报 2/7 (29%)，不是之前错误的 1/5 (20%)
- exp_022 提交时 GPU 必须对 `get_project_status` 的 gpu_ids 校验

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299 (connect.bjb1.seetacloud.com)，账号 root
- 工作目录：/root/autodl-tmp/event-gated-adaptive-horizon
- Python：/root/miniconda3/bin/python (3.12.3)
- 论文源码：本地 `projects/event-gated-adaptive-horizon/docs/paper/`
- 关键代码：远程 `/root/autodl-tmp/event-gated-adaptive-horizon/dreamer.py`（CIVODetector L29-61）
- 活跃进程：019b (PID 649577, cuda:0), 019a_v2 (PID 629444, cuda:1)
- 磁盘：399GB 可用 (5% used)

### 3. 📊 当前状态
**刚完成**：论文全章节集成（detector section + seed-3 results + C1 reframe + Abstract/Intro/Discussion/Conclusion + Fig 2 重生成）。Reviewer critical（detector 数据不一致）已完全解决。Manager 的 hypothesis 驱动复盘已完成。

**RUNNING**：
- exp_019a_v2_pickcube_baseline (cuda:1, ~7h+ elapsed) — ManiSkill PickCube baseline
- exp_019b_pickcube_civo_trigger (cuda:0, ~2h+ elapsed) — PickCube CIVO trigger（trained dt_emb）

**PENDING**：
- exp_022_untrained_dt_emb_learned_gate — 脚本 ready + dry-run 通过，等 GPU 空闲立即提交

**无等待中的 Worker/Cron 回调。**

### 4. 📋 待办（条件触发式）
- 019a_v2 或 019b 完成 → 立即提交 exp_022 到空出的 GPU（脚本在 `artifacts/scripts/exp_022_untrained_dt_emb_learned_gate.sh`）
- exp_022 @50K 步 → 检查 eval > 580 (60% baseline) 且 NVE < 1.5× → 是则追加 seed 1,2；否则标 negative
- 019b 完成 → 与 019a_v2 对比：trained dt_emb 在 PickCube 是否触发 CIVO（NVE≥1.5× + eval 退化）
- exp_022 成功 → 论文升级为 "诊断 → principled intervention" framing；失败 �� 保持 "systematic causal dissection" framing
- 论文完整后 → 提交 `submit_paper_to_review` 给 Review Director

### 5. 🎯 战略上下文
**核心发现**：trained dt_emb 通过 obs decoder 梯度通路注入 dt-specific 信息 → RSSM fidelity gap → reward bias → critic overestimation → collapse (CIVO)。3/3 seeds 触发 NVE≥1.5×，2/3 进展为 collapse，1/3 自纠正。

**关键决策链**：D073（93%→16-22% 梯度修正）→ D074（SGS 降级）→ D078（C1 reframe: universally degrades <30%）→ D079（detector FP 方案 C + exp_022 计划）

**exp_022 是当前最关键实验**：如果 untrained dt_emb + learned gate 成功 = 论文从纯诊断升级为因果干预（CoRL 接受率显著提升）。Reviewer 评估：成功/失败两条路都有 solid narrative。

**易错点**：
- 不要混淆 "NVE"（normalized, 需 baseline）和 "ve_ratio"（raw V/E，detector 用的是这个）
- seed-3 eval=268@105K 是过渡值（train_return 仍在下降），不是 stable state
- 009c 的 "FP" 是真实 value pathology（non-CIVO），论文 frame 为有价值的 alert
- Paper Table 3 所有数字必须从 `detector_formal_validation_v3.json` 派生，不手写


---

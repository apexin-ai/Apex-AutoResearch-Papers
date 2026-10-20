# director / loop_9.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`10a60e68285f8b9aa93f.json`](../../sessions/10/10a60e68285f8b9aa93f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-17T11:43:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 和 cuda:1（bjb1-45299 分配的 2 张卡）
- 论文数字必须有 `artifacts/analysis/` 下的 JSON 文件直接支撑，不允许推测（M004 教训）
- CIVODetector 阈值统一为 ve_threshold=0.49 + 2/3 eval decline rule（commit 3328f53），paper 与代码必须一致
- FPR 必须报 2/7 (29%)，不是之前错误的 1/5 (20%)
- Detector backtest 必须用 raw V/E ratio（非 NVE），严格按 Algorithm 1 逐条件验证（M008 教训）
- PickCube 019b 是 detector TN（不触发），不是 TP——不能作为 cross-env TP 证据（D083）
- exp_022 curriculum 问题（M007）：含 curriculum 参数的实验审批前必须验证 effective step 与总步数匹配

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299 (connect.bjb1.seetacloud.com)，账号 root
- 工作目录：/root/autodl-tmp/event-gated-adaptive-horizon
- Python：/root/miniconda3/bin/python (3.12.3)
- 论文源码：本地 `projects/event-gated-adaptive-horizon/docs/paper/`
- 关键代码：远程 `dreamer.py`（CIVODetector L29-61）
- 活跃进程：exp_019b (PID 649577, cuda:0, PickCube CIVO trigger ~70%), exp_022b (PID 670554, cuda:1, frozen dt_emb + no curriculum ~预计3h)
- 磁盘：399GB 可用 (5% used)

### 3. 📊 当前状态
**刚完成**：
- 论文 detector section 全面升级：公式统一(V/E ratio)、mechanistic justification、threshold sensitivity(J=0.714)、τ_vel sensitivity、FPR asymmetric cost、段落精简(line 193 拆分)、70K guideline 软化、2/3 rule motivation、Related Work positioning(prevention vs detection)
- 数据一致性检查 6 项修复（Cheetah eval 措辞、baseline 统一 915.7、Fig 2 caption、009e footnote）
- exp_022 标 DONE(killed/inconclusive)——curriculum 导致 gate 从未激活
- Detector validation figure 完成（含 TN 曲线 009b）+ PickCube V/E comparison figure 完成

**RUNNING**：
- exp_019b (cuda:0, ~70%, 预计 ~3-4h) — PickCube CIVO trigger，NVE 呈 spike-then-deflation pattern，eval 正在恢复
- exp_022b (cuda:1, 刚启动, 预计 ~3h) — frozen dt_emb + learned gate，curriculum disabled (phase1=0, phase2=0)，gate 已确认从 step 0 激活(dt_mean=4.4, entropy_ratio=0.968)

**无等待中的 Worker/Cron 回调。**

### 4. 📋 待办（条件触发式）
- exp_022b 完成 → 关键判断：frozen dt_emb + active gate 能否保留时间抽象（dt 分布是否收敛到某个 dt？eval 是否超过 022 的 189？是否出现 CIVO？）→ 成功则论文升级为 "diagnosis + principled intervention"；失败则保持 "systematic causal dissection"
- exp_019b 完成 → 完整 V/E trajectory 分析 + 论文 PickCube 段落（framing: C1 性能下降有效 + detector TN 展示 specificity）
- 019b 完成释放 cuda:0 → 提交 exp_021_full_sgs_cheetah（脚本已同步到远程）
- gen_paper_figures.py line 111 的 x-axis 标签 "008d/009b" 需改为 "008d"（与新 caption 一致），下次重生成图时修
- Reviewer info 残留：gen_paper_figures.py x-axis 标签不一致

### 5. 🎯 战略上下文
**核心发现**：trained dt_emb 通过 obs decoder 梯度通路注入 dt-specific 信息 → RSSM fidelity gap → reward bias → critic overestimation → collapse (CIVO)。Walker Walk 3/3 seeds 触发 NVE≥1.5×，2/3 collapse，1/3 自纠正。

**关键决策链**：D073(梯度修正) → D074(SGS降级) → D078(C1 reframe) → D079(detector+exp_022) → D080(exp_022 gate退化判断→已撤回) → D081(curriculum 问题确认) → D082(PickCube as cross-env TP→已撤回) → D083(PickCube 是 TN)

**exp_022b 是当前最关键实验**：它是 exp_022 的修正版（curriculum disabled），真正测试 "frozen dt_emb + active gate 能否解耦时间抽象与 CIVO"。初始信号好（dt 分布接近均匀），但需要看后续 eval 和 CIVO 信号。

**易错点**：
- 不要把 NVE（需 baseline 归一化）和 raw V/E ratio（detector 用的）混淆
- PickCube 019b 不是 detector TP——振荡 V/E 被 acceleration filter 正确过滤
- exp_022 的 "gate 退化" 是 curriculum 配置问题，不是 frozen dt_emb 的固有缺陷（D081）
- 论文 detector 公式必须是 r_t = V̄_t / max(Ē_t, ε)，不是之前错误的 |V-E|/E
- 009c 的 "FP" 是真实 value pathology（non-CIVO），论文 frame 为有价值的 alert
- Threshold τ_vel=0.15 能消除所有 FP，但论文中不要提这个（给审稿人送弹药，已删除）


---

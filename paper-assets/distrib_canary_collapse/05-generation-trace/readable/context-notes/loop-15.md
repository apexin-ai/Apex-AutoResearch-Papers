# director / loop_15.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_15.md`
- **Structured JSON:** [`e2e4983376dd1933701a.json`](../../sessions/e2/e2e4983376dd1933701a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_messages
updated: '2026-05-21T15:26:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-17855 cuda:0-5, westd-19828 cuda:0-1（共 8 卡），严禁使用其他 GPU
- ≤3B 模型用 fp32，>3B 用 bf16（D079）
- predict-then-verify: v1 committed score = 3/5 为 primary，v2 未 commit = 4/5 仅作 sensitivity analysis（M057）
- α=0.25 T=20 不在锁定预测文件中，不得标记 EXACT_MATCH（M056）
- TY=7/8 已被 D143 retract，论文不得引用
- CSD 仅限 Discussion 章节（D142）
- 17855↔19828 SSH 不通
- FPR 措辞 "near-zero"（D167），最终 2/56=3.57%（D171）
- R²=0.883 不用 1.000（D168），"parametric" 不用 "first-principles"（F7-C5）
- Cascade ordering 14/15（D169，GPT-2m s43 bidirectional）
- **T=20 α=0.60 PermG=0/8**（非 6/8！M061 数据错误已修正，sync-dip 持续存在）
- 所有训练命令必须包含 `export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1`（M060，已失败 2 次）

### 2. 🖥️ 基础设施快照
- 服务器：westd-17855 (6×RTX PRO 6000 Blackwell 98GB) + westd-19828 (2×RTX PRO 6000 Blackwell 98GB)
- SSH: connect.westd.seetacloud.com（端口见 ~/.ssh/config）
- 工作目录：/root/autodl-tmp/distrib_canary_collapse/
- Python：/root/miniconda3/bin/python（conda base，不用 venv）
- HF_HOME=/root/autodl-tmp/.hf_cache, TRANSFORMERS_OFFLINE=1
- 本地 artifacts：/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/
- Phase Diagram heatmap 草稿：artifacts/phase_diagram_draft.{py,pdf,png}
- D170 叙事草稿：artifacts/D170_narrative_drafts.md
- Lag 分析 artifact：sync_dip_lag_analysis_t10_vs_t20_a060

### 3. 📊 当前状态
**Agent 空闲 16h，以下实验大概率已完成但未分析**（需要立即验证）：

上次确认 8/8 GPU RUNNING：
- 17855:0 t25_a050_s42_fp32（T=25 Phase Diagram）
- 17855:1 t15_a060_s42_fp32（T=15 Phase Diagram）
- 17855:2 t15_a075_v2_s42_fp32（T=15 Phase Diagram，第三次提交修复 HF_HOME）
- 17855:3 t25_a060_s42_fp32（T=25 Phase Diagram）
- 17855:4 t15_a050_s42_fp32（T=15 Phase Diagram）
- 17855:5 t25_a045_v2_s42_fp32（T=25 Phase Diagram，M060 修复版）
- 19828:0 t25_a075_s42_fp32（T=25 Phase Diagram）
- 19828:1 t15_a045_s42_fp32（T=15 Phase Diagram）

T=15 估计 ~3-4h each，T=25 估计 ~6h each，距上次确认已 16h+ → **极可能全部完成**。

**PREPARING 等 GPU**：t20_a045_s43_fp32（Phase Diagram 最脆弱 cell cross-seed 验证，第一优先级）

**已完成里程碑**：
- T=5 行 4/4 = 0/8（D173，α_c(5)≥1.0 理论四点验证）
- FPR 最终 2/56 = 3.57%（D171）
- Pythia-6.9B s43 bf16 = 6/8（D172，cross-scale 验证）
- R7 全部 8 项修复完成 + D169 cascade 14/15 修正
- D175 lag 分析完成（去同步化 37-52%，但 dissolution 未确认）

### 4. 📋 待办（条件触发式）
- **首要**：Agent reset 后立即 SSH 检查两台服务器 GPU 状态 → 确认哪些实验已完成 → 每个完成的跑 5method 分析汇报 PermG X/8
- T=15 四组全部完成 → 填充 Phase Diagram T=15 行。α_c(15)≈0.304 理论预测：α=0.45/0.50/0.60/0.75 应全部 >0/8（除 α=0.60 可能因 sync-dip 例外）
- T=25 四组全部完成 → 填充 Phase Diagram T=25 行。**T=25 α=0.60 是最关键单格**：如果 PermG >0/8 → sync-dip dissolution 确认；如果仍 0/8 → sync-dip 是 permanent feature（D176）
- 有空闲 GPU 后 → 立即启动 t20_a045_s43（PREPARING，最脆弱 cell cross-seed）。如果还有 GPU → t20_a060_s43（Reviewer Report 26 建议的 desynchronization cross-seed）
- Phase Diagram 20/20 格全部填充 → 更新 heatmap（artifacts/phase_diagram_draft.py）→ Paper Agent 统一 patch 入论文（D170 叙事升级 + D175 desynchronization + FPR 更新）→ R8 提交
- Paper Agent R8 patch 完成 → submit_paper_to_review

### 5. 🎯 战略上下文
- **核心转型**：论文从"方法论文"(3.0 Findings) 转为"现象发现论文"(Mapping the Detectability Landscape)。Phase Diagram 是核心 figure
- **D174 叙事策略**（Reviewer Report 24 深度评估）：C1 40%(Phase Transition) + C2 30%(S×R) + C3 20%(Method sensitivity) + C4 10%(Practical)。T=5/10/20 三行已支撑完整 landscape 叙事，T=15/T=25 是 bonus
- **D176 sync-dip 修正是最重要的纠错**：T=20 α=0.60 PermG=0/8（非 6/8），sync-dip 在 T=20 持续存在。这让 T=25 α=0.60 成为 Phase Diagram 最关键单格。Predict-then-verify α=0.60 predicted=0 observed=0 = PASS（理论最强验证）
- **被低估的发现**：(1) per-generation ratio vs cumulative contamination（C1 核心 insight）；(2) step-function transition 本身是发现；(3) FPR 4.2%→3.57% 比 degenerate 0% 更可信；(4) Method sensitivity：T=20 α=0.60 同一数据 PermG 0/8 vs DiffXCorr 6/8
- **最容易判断错的事**：(1) 不要假设 sync-dip dissolution 已确认——T=20 PermG 仍 0/8，只有 near-miss p=0.064（D176）；(2) PermG 数据必须从 registry 原文验证，不信任 Agent/Reviewer 概括（M061）；(3) 所有训练命令必须含 HF_HOME 三件套（M060，已失败 2 次不能有第 3 次）；(4) T=20 predict-then-verify：α=0.45 predicted=0 actual=5 是 FAIL（theory conservative at boundary），不要误报为 PASS
- **176 个决策记录**在 decisions.yaml，**61 个错题本**在 mistakes.yaml


---

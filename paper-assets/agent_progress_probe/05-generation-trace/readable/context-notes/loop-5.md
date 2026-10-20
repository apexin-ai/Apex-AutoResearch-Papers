# director / loop_5.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`3fbef06475b1ae0018d7.json`](../../sessions/3f/3fbef06475b1ae0018d7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-14T21:48:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 bjb2-23165 的 cuda:0 / cuda:1（RTX 5090 32G × 2）
- Gold set 评估必须用 `evaluate_gold_set.py`（已修复 leakage：gold windows 排除出训练集），不能手写评估脚本
- Structural vs LLM judge 差距是 **33.3pp**（0.9951-0.6625），不是 24.3pp（那是 probe vs LLM judge）——之前两次写错被 Reviewer 打回
- 实验计数：plan 32 / DONE 30 = **24 success + 6 negative**，不是 28+7 或 27+7
- conf2-subset-v2 已关闭为冗余，不要再跑

### 2. 🖥️ 基础设施快照
- 服务器：bjb2-23165 (connect.bjb2.seetacloud.com)，工作目录 `/root/autodl-tmp/agent_progress_probe`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- Gold set pipeline：`/root/autodl-tmp/agent_progress_probe/evaluate_gold_set.py`
- Probe checkpoint：`checkpoints/best_model.pt`
- 活跃进程：无（GPU 双卡空闲，等 gold set 标注）
- Paper Agent session 活跃，队列深度 ~12

### 3. 📊 当前状态
刚完成本轮所有任务：ROADMAP 更新（Reviewer 报告的 4 个问题已修复）、dream_simulate 已触发（dream_20260514T214352, review_mode=full）、用户已被催促确认标注人力。

Registry: 0 RUNNING / 若干 PREPARING 需清理（twv-no-temporal-sigma2, encoder-ablation 系列, gold_dryrun_v1/v2 等已过时）。

等待中：
- dream_20260514T214352 完成回调
- 用户回复 gold set 标注人力确认
- Paper Agent 处理队列（含 LF fire rate 数据 + method.tex abstain 修正）

### 4. 📋 待办
- dream 完成回调到达 → Read `dream-report-action.skill.md` → 按协议处理三档审稿
- 用户确认标注人力 → 立即通知 Agent 启动标注流程（材料已就绪 650 窗口）
- 标注完成 → Agent 跑 `evaluate_gold_set.py --gold_csv &lt;path> --output_dir gold_results --device cuda:0` → 结果转发 Paper Agent 补入论文
- Registry 中过时 PREPARING 实验 → 派 Agent 清理标记 killed
- paired-bootstrap 已完成（3 个 in-domain p<0.001，跨域因 eval set 不匹配已跳过）→ 结果已可用于论文

### 5. 🎯 战略上下文
**D039 Pivot 是核心决策链**：TLM（TWV/HMM/lag-HMM）全面失败 → 论文从 "method paper" 转向 "empirical analysis paper"。三层贡献：(1) Structural signal discovery 主贡献，(2) LF temporal dynamics 方法论，(3) TLM negative finding。投稿目标 EMNLP 2026 ARR 5/25（Findings track）。

**最容易判断错的事**：
- Circular eval 是本论文最大软肋——所有 "高 F1" 都是在 LF-derived labels 上评估的，gold set 是唯一非 circular 验证。没有 gold set 结果论文说服力大打折扣。
- "structural-core" 和 "structural-cross-agent" 在 registry 中 conclusion=negative，但这是因为它们证明了 "structural features 近似复现 LF 输出"（circular eval artifact）。在论文 framing 中这反而是 **正面发现**（structural signal discovery）。不要因为 conclusion=negative 就认为实验失败。
- OH cmd_rep 角色反转：在 SWE-Agent 上 cmd_rep 是 leading indicator，但在 OpenHands 上变成 noise source（92% fire rate, 71% false stag）。去除 cmd_rep 后 OH F1 从 0.7512 涨到 0.9272（+21.6pp）。这是 C2 的核心发现。


---

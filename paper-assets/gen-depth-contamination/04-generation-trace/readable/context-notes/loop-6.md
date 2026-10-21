# director / loop_6.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`16cd5a40afd236afecc3.json`](../../sessions/16/16cd5a40afd236afecc3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-15T15:08:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westc-26893 的 cuda:0（1×RTX 4090 D 24GB），无其他分配
- 项目已进入审稿阶段（review_chat_id: `oc_0f6dcb30efaa4f47425ef1d9874a89d7`），论文格式/投稿材料由 Group C (Review Director) 负责，你不参与
- exp-004 用的是 Qwen2.5-7B **BASE**（不是 Instruct），这是 D032 决策：Base 更 clean，continuation mode 下 Instruct alignment 引入混杂。不要中止重启 Instruct
- 目标 ARR 05-25 提交，不要 fallback 到更低会议

### 2. 🖥️ 基础设施快照
- 服务器：westc-26893 (connect.westc.seetacloud.com)，账号 root
- 工作目录：/root/autodl-tmp/gen-depth-contamination
- GPU：1×RTX 4090 D 24GB (cuda:0)
- 无 W&B 配置，无弹性 GPU，无 Git remote
- 当前进程：exp_004_7b_crossscale RUNNING on cuda:0（Qwen2.5-7B base, continuation mode, C4 5K→1K docs, depth 0-3, scorer=Qwen2.5-1.5B）

### 3. 📊 当前状态
刚完成 Rebuttal 实验批次 EXP-A/B/C/D/E（全部 success），3 个 Critical 全部解决，11 个 Warning 大部分解决。Agent 正在处理 `worker_audit_rebuttal_artifacts` 回调（审计 rebuttal 产物完整性）。

- **RUNNING**: exp_004_7b_crossscale — 7B cross-scale 验证（FR-4 Critical: 现有实验仅 ≤1.5B）。预计 05-16 AM 完成
- **QUEUED**: exp_012_binary_confidence — DivEye/Binoculars 与 depth 的 Spearman correlation（等 exp-004 释放 GPU）
- **Paper Agent 待整合**：EXP-E 修正数字（MMLU 8/15 → Holm-Bonferroni 修正后）、EXP-A cross-scorer 结果、EXP-D OBD N=500 结果、K*(θ) 曲线图
- Registry: 19 个实验，17 success / 1 running / 1 queued

### 4. 📋 待办（条件触发式）
- exp-004 完成 → 分析 7B K* 结果：K*=2 → 强证据写入论文；K*≠2 → 评估 framing 影响（可能需 D037 决策）→ 释放 GPU → 启动 exp-012
- exp-012 完成 → 分析 binary confidence ≠ depth 结论 → 所有 rebuttal 实验完成
- 所有 rebuttal 实验 + Paper Agent 整合完成 → `submit_paper_to_review(mode="continue")` 提交二审
- Agent audit 回调处理完 → 检查是否有遗漏产物，催 Paper Agent 整合剩余 EXP-A/D/E 结果

### 5. 🎯 战略上下文
- **核心发现**：K*=2（饱和边界）在 8 个条件下（3 模型 × 4 解码策略 + continuation mode）普遍成立（D016）
- **论文结构**：2+1 claim（D012）—— C1'(K* characterization) + C3(filtering application) + supporting analysis。C2(degradation ordering) 已降级为 supplementary finding（D010，因 Qwen feature ranking 与 Pythia/OLMo 分歧是 model-dependent）
- **C3 结论**：binary-ours > all alternatives（D026），但所有策略都 degrade vs base model，效应量小（Cohen's d ~ small）
- **易错点**：
  - exp-004 用 1K docs（非标准 5K），因为 7B 内存限制。如果结果异常，先考虑样本量影响
  - EXP-A cross-scorer K*=1（不是 2），这是诚实呈现——说明 K* 受 scorer 影响，论文已调整措辞为 "K* reflects generation process, modulated by scorer capacity"（D031）
  - MMLU 显著性从 10/15 降到 8/15（Holm-Bonferroni 修正），核心结论不变但数字要用修正后的
- **DDL 倒排**：05-16 AM 实验完 → 05-16 PM 修订定稿 → 05-17~19 二审迭代 → 05-20~24 打磨 → 05-25 ARR 提交


---

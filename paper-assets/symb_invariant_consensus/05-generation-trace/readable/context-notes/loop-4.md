# director / loop_4.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`3b8459fab37c9c464d60.json`](../../sessions/3b/3b8459fab37c9c464d60.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-16T05:21:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只分配 cuda:0（westd-32608），严禁使用其他 GPU
- 模型路径 `/root/autodl-tmp/models/Qwen2.5-14B-Instruct`，不要重新下载
- sica_expanded_14b 正在跑（PID 181992），不要 kill 它
- exp-001 (sica_expanded_14b) 是 804 题大规模评估，完成前不要启动 K 消融（串行依赖同一 GPU）

### 2. 🖥️ 基础设施快照
- 服务器：westd-32608 (connect.westd.seetacloud.com)，工作目录 `/root/symb_invariant_consensus`
- Python：conda base 环境（aml-train 镜像），`/root/miniconda3/bin/python`
- 模型：`/root/autodl-tmp/models/Qwen2.5-14B-Instruct`（14B Instruct）
- 活跃进程：sica_expanded_14b PID 181992, tmux=`sica_expanded_14b`, cuda:0
- 预计完成：~May 16 晚或 May 17 凌晨（804 题，~11.5h）
- W&B / Git 未配置

### 3. 📊 当前状态
sica_expanded_14b（exp-001，804 题大规模评估）正在运行，是当前最关键实验——为 Claim 1 提供统计显著性证据。

QUEUED: sica_k_sensitivity_14b（exp-002，K 消融，等 exp-001 完成后用同一 GPU 跑）
其余实验全部 DONE（success 4 / negative 1 / killed 5 / failed 1）。

Reviewer 刚交了一份 ROADMAP + Paper Framing + Experiment Plan 审查（severity: warning），核心问题：
- Claim 2 "operating regime" 只有 2 个模型数据点，建议 exp-007 (72B-AWQ) 提升到 P1
- Claim 3 "C0 as diagnostic" 数据点不足，建议降为 "preliminary correlation"
- exp-003 / exp-005 的 registry 状态需要修正（小问题）

我尚未对这份 Reviewer 报告采取行动（收到后即触发 RESET）。

### 4. 📋 待办
- sica_expanded_14b 完成回调 → 分析结果：tie 比例是否稳定、binomial test p 值、C3 增益是否显著 → 更新 ROADMAP
- exp-001 完成 → 立即启动 sica_k_sensitivity_14b (K=6,8,16,20 消融)
- 处理 Reviewer warning：评估 exp-007 (72B-AWQ) 是否提到 P1；决定 Claim 2/3 措辞是否调整
- exp-003 / exp-005 registry 状态修正 → 派 Agent 补 registry_id

### 5. 🎯 战略上下文
**核心方法**：SICA（Symbolic Invariant Consensus Aggregation）— 用符号约束检测 LLM 多路径推理中的矛盾来打破 Self-Consistency 平票。

**关键数字**：MVP D012 在 60 题上 C3=+3.3pp PASS，但 p=0.317 统计不显著，增益全来自 4 个 6:6 平票翻转。exp-001 (804 题) 是补统计显著性的核心实验。

**决策链要点**：D016 从 QwQ-32B pivot 到 Qwen2.5-14B（QwQ C0=3.6% 太低，几乎没有平票可打破）；D017/D018 诚实标注 MVP "技术 PASS 但统计 INCONCLUSIVE"。

**易错点**：
- Claim 2 "operating regime" 当前只有 QwQ-32B 和 Qwen2.5-14B 两个点，Reviewer 必攻——72B 是关键补充但需要额外 GPU（可能要申请云卡）
- 不要过度包装 p=0.317 的结果，等 exp-001 804 题结果出来再下结论
- tie 比例（当前 ~8.3%）在大样本中是否稳定是 Claim 1 成立的前提


---

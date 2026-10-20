# reviewer / loop_2.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`7b61cbaa1a424e0f5082.json`](../../sessions/7b/7b61cbaa1a424e0f5082.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T14:16:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb2-23165 服务器只有 cuda:0 和 cuda:1，两卡均为项目可用（无 gpu_ids 白名单约束，constraints.yaml 为空）
- train-without-ob 的 0.9510 macro_f1 **不可与 probe_001 的 0.9055 直接比较**——测试集不同（1519 vs 1824 windows），标签来源不同（2-LF vs 3-LF）。我已向 Director 发过 CRITICAL，Agent 引用此数字时必须注明上下文
- baseline-llm-judge 的 24.3pp 差距受循环评估偏差影响（probe 在 LF 标签上训练，天然匹配），已要求加 caveat。**在 gold set 出来前不能 claim "probe outperforms LLM judge"**，只能说 "better matches LF consensus"
- autodl-5090 与 gpu-5090-2x-2 是同一实例（D018 确认），RTX 5090 32G × 2

### 2. 🖥️ 基础设施快照
- **服务器**: bjb2-23165（当前主力），工作目录 `/root/autodl-tmp/agent_progress_probe`
- **Python**: `/root/miniconda3/bin/python`，激活方式 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **GPU**: 2× RTX 5090 32GB。截至 handoff 时刻两卡均空闲（0% util, 0 MiB）
- **关键路径**:
  - embeddings: `data/embeddings.pt`（54809 windows, 1024-dim Qwen3-Embedding）
  - checkpoints: `checkpoints/`（probe_001）, `checkpoints_full/`（probe-002）, `checkpoints_without_ob/`, `checkpoints_ablation_bgem3/`, `checkpoints_ablation_e5large/`
  - fewshot 结果: `fewshot_results/fewshot_results.json`
  - LLM judge 结果: `results/llm_judge_full_zeroshot.json`
- **活跃进程**: 无。所有训练已完成
- **本地 workspace**: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/`

### 3. 📊 当前状态
我刚审查完三批 worker 结果并向 Director 发了两份报告：

**已完成的实验（本轮审查覆盖）**:
- `baseline-llm-judge` → DONE：macro_f1=0.6625，远低于 probe (0.9055) 和 Repeat-3 (0.8432)。循环评估问题已标 warning
- `train-without-ob` → DONE：自身测试集 0.9510，但在原始 full test set (8101w) 上仅 0.7019。cross_eval 确认 100% 标签一致，OB 贡献 33.5% 额外高置信标签
- `openhands-fewshot-probe` → ANALYZING：zero-shot 0.532 → 50% fewshot 0.688，瓶颈在 LF agent-specificity 而非数据量
- `encoder-ablation-probe-bgem3` → DONE：0.9413（+3.6pp vs probe_001）
- `encoder-ablation-probe-e5large` → DONE：0.9363（+3.1pp vs probe_001）

**Registry PREPARING/RUNNING**:
- `ablation-window-size` → PREPARING（k=3,5,7 消融，尚未提交）
- `openhands-fewshot-probe` → ANALYZING（metrics 已录入，等 Agent 写结论）

**等待中**: 无 cron 回调。两卡空闲等 Agent 提交 ablation-window-size 或其他新实验。

### 4. 📋 待办（条件触发式）
- `openhands-fewshot-probe` 结论写入 registry → 审查 Agent 对 Claim 3 的 framing 是否与 D017 一致（"LFs 跨 agent 可迁移 + Probe 需 agent-specific adaptation"）
- `ablation-window-size` 提交并完成 → 审查 k=3/5/7 结果，关注 k=3 是否 F1 骤降（信号积累不足）
- `train-without-ob` 结论被 Agent 引用到论文/report → **核查是否加了测试集差异 caveat**，未加则 CRITICAL
- Agent 开始准备人工标注材料 → 审查标注指南是否清晰、样本是否有代表性
- gold set 标注完成 → 审查 Fleiss κ、gold set 上重新验证 LLM judge vs probe 的公平对比
- temporal-label-model 实现完成 → 这是核心 Claim 1，重点审查

### 5. 🎯 战略上下文
**项目核心**: ProgressProbe — 用 LF + GRU probe 检测 LLM agent 的 progress stagnation。三层贡献：temporal label model（方法论）、probe（实证）、跨 agent 迁移（系统性研究）。投 EMNLP 2026 ARR 5/25。

**决策链关键节点**:
- D020: OB 提供有价值信号（-7.7pp），非泄漏
- D024: data-volume-control 确认 7.1pp 为纯信号贡献
- D017: Claim 3 从"零样本迁移"重构为"LF 可迁移 + probe 需 adaptation"
- D023: Dream 评审 4/6 WA，framing 正确，gap 在统计严谨性 + TLM 形式化

**下一个"我"最容易判断错的事**:
1. **encoder ablation 看起来 bge-m3/e5-large 比 Qwen3-Embedding 好 3-4pp**——但 probe_001 用 conf>=2（15401w），probe-002 用 conf>=0（54809w，F1=0.847）。encoder ablation 也是 conf>=2。所以 bge-m3 的 0.9413 应该和 probe_001 的 0.9055 比，不是和 probe-002 的 0.847 比。**这说明 Qwen3-Embedding 并非最优 encoder**，但差距不大（3-4pp），论文可以 frame 为"encoder-robust"
2. **循环评估是贯穿全项目的系统性风险**——所有指标都基于 LF labels，包括 probe vs baseline、encoder ablation、fewshot。gold set 是唯一出路，也是 GO/NO-GO gate 的前提
3. **两卡空闲 = GPU 浪费**——如果 Agent 长时间不提交新实验，主动提醒 Director


---

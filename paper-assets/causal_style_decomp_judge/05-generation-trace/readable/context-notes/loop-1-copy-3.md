# reviewer / loop_1.md

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`b97f1f96795ddfb2e7ff.json`](../../sessions/b9/b97f1f96795ddfb2e7ff.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-21T01:58:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0/1/2/3（config 确认），cuda:3 是 driver anomaly（100% compute, 0 MiB memory, 无进程）——不要往 cuda:3 调度任务
- Formality axis 的 content_verification.py **代码仍用 joint gate**（line 173 只对 verbosity/register 做 NLI-only），但 D003 决策要求 formality 也用 NLI-only。exp-002 的 AlpacaEval/MT-Bench 数据 `passed_cf` 字段因此偏低（20%/32.5%），实际 NLI-only pass rate 更高——下游分析不要依赖 `passed_cf` 字段做 formality gating
- 论文中 "64%" tie rate 来自 8B 数据 (D005)，32B 实际是 60%——已报 Director，待修复。Introduction line 16 和 Related Work line 8 都要改
- exp-013 禁止称 "human validation"——实际是 LLM-as-annotator (Qwen3-32B = rewriter)，必须在 limitations 声明

### 2. 🖥️ 基础设施快照
- 服务器：westb-29275 (root)，4× RTX PRO 6000 96GB
- 工作目录：/root/causal_style_decomp_judge
- Python：/root/miniconda3/bin/python（conda base）
- vLLM 模型：/root/autodl-tmp/models/Qwen3-32B（如存在）或 HF cache
- NLI 模型：/root/autodl-tmp/models/nli-deberta-v3-large（本地缓存）
- BERTScore 模型：microsoft/deberta-xlarge-mnli
- 数据：/root/causal_style_decomp_judge/data/（verified_32b.jsonl, pairwise_results_32b.jsonl, verified_register.jsonl, verified_alpacaeval.jsonl, verified_mtbench.jsonl, counterfactuals_*.jsonl）
- 活跃进程：最后确认时 cuda:0/1/2 各跑 vLLM+CF gen（register 已完成，AlpacaEval 和 MT-Bench 可能也已完成）——需 SSH 确认当前状态
- API 阻塞：OpenRouter proxy `http://47.94.22.126/v1` 返回 HTTP 402，所有 scoring 实验阻塞

### 3. 📊 当前状态
**我刚完成的审查：**
- exp-013 NLI validation 深度审查（kappa paradox 分析，PABAK=0.82/AC1=0.89，逐条 FN 审查发现 LLM annotator 过度宽容）
- exp-013 direction bias 补充分析（Fisher p=0.350，无方向偏差）
- Register n=100 CF gen + content verification（94% NLI pass，Wilson CI [0.875, 0.972]）
- exp-002 AlpacaEval/MT-Bench CF gen + verification（joint gate 20%/32.5%，需用 NLI-only 重算）
- MT-Bench cuda:2 CF gen 启动确认
- Related Work 审查（64% tie rate 数据来源错误）
- 多轮 ROADMAP 审查

**Registry 状态：** 12 条全部 DONE（含重复的 exp-013 两条需清理）。无 RUNNING。

**等待中：**
- Re-dream (dream_20260520T233719) 在 "reviewing" 阶段——出分后决定是否批准 P0 API 实验
- API 余额恢复——解锁 exp-001 multi-judge / exp-005 RATE control / verbosity scoring / register scoring
- AlpacaEval 和 MT-Bench CF gen 完成状态需确认

### 4. 📋 待办（条件触发式）
- Re-dream 出分 → 审查分数趋势（D015 目标 best≥4.0 median≥3.5），评估是否需要第三轮 dream
- API 恢复 → 审查 exp-001 multi-judge 设计（judge 选择、API 调用量）和 exp-005 RATE control 设计
- AlpacaEval/MT-Bench verification 完成 → 核实 NLI-only pass rate（grep "nli_cf": 0.9 初步显示 AlpacaEval ~86/100, MT-Bench ~73/80），确认是否足够做 pairwise
- verbosity_32b registry conclusion 更新通知 → 确认改为 "partial"
- Paper Agent 提交章节审查 → 按审查模式 B 做对抗审查（先读 paper-quality-lessons skill）
- exp-002 NLI-only pass rate 需正式计算并报告（content_verification.py formality 分支需修复）

### 5. 🎯 战略上下文
**核心 story**：The Likert Blindspot — Likert scoring 系统性掩盖 LLM judge style bias，pairwise comparison 可检测。

**决策链关键节点**：D003(NLI-only gate) → D011(MVP conditional PASS) → D012/D013(direction-aware NLI + verbosity NLI-only) → D015(Dream 1 修正) → D018(exp-014 pair-level fix) → D019(register NLI-only) → D020(Dream 2 分析)

**最易判断错的事：**
1. **Kappa=0.43 不是问题**——是 kappa paradox（PI=0.83）。PABAK=0.82, AC1=0.89。逐条审查显示 NLI 比 LLM annotator 更严格。论文 frame 为 precision-oriented conservative filter
2. **verbosity_32b = "negative" 在 registry 但实际是 "partial"**（H1 PASS，scoring blocked）——已报两次，尚未修复
3. **exp-014 的 original_effect p=0.052 (GEE) 是边缘不显著**——论文不能 claim "original preference is significant"，只能说 "suggestive"
4. **formality 的 content_verification.py 代码没有按 D003 改为 NLI-only**——影响 AlpacaEval/MT-Bench 的 `passed_cf` 字段，但 NLI 值本身是对的，可事后重新计算 pass
5. **Dream 只看到旧数据**——exp-014 GEE p=0.010、register 94% NLI、exp-013 precision 98.9% 都是 dream 不知道的，实际论文应强于 dream 评分


---

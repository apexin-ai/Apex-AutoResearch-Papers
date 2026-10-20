# director / loop_3.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`50019dfad9e3aa0c248b.json`](../../sessions/50/50019dfad9e3aa0c248b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-15T10:20:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 autodl-5090 上的 cuda:0/1/2/3（4× RTX 5090 32GB），不可用其他服务器的卡
- exp-019 supervised verifier 已被 D073 决策取消，不要实现/注册/启动
- Dream dream_20260515T092545 基于已被证伪的 D071 "constrained decoding bottleneck" framing → 结果必须 heavy discount，不能直接采纳其 framing 相关建议
- 论文中不能再有任何 "constrained decoding causes score compression" 的因果归因——ablation 已证伪
- RE LP selection flip (+1.69pp) 是 single seed、within bootstrap CI，不能作为 claim，最多 appendix observation

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (connect.bjb1.seetacloud.com)，account: root
- 工作目录：/root/autodl-tmp/struct_self_consist_ie
- Python：conda base 环境 /root/miniconda3/bin/python
- 模型：Qwen3-8B fine-tuned checkpoints 在服务器上（ft_002_v2 用于 SciERC）；LLaMA-3.1-8B 也有 fine-tuned checkpoint
- 数据：SciERC + CoNLL-2003 + WNUT-17 在服务器上
- 活跃进程：无 RUNNING 实验，4× GPU 全部空闲
- Ablation 数据：constrained=output/exp_012_rerun_1024/samples.jsonl, free-form=results/exp_freeform_ablation/samples.jsonl

### 3. 📊 当前状态
**刚完成**：
- D072 framing 更新（universal gap，ablation 证明 score compression 是 intrinsic）
- D073 取消 exp-019 verifier
- Paper Agent 完成两批 D072 patch（title 回退 + abstract/intro/discussion/conclusion 全部修改 + appendix freeform table），编译成功 19 页
- Reviewer 四维度确认 D072 方向，两次 ROADMAP 审查 PASS

**Agent 队列**（按顺序）：
1. [PROCESSING] 原指令（可能已开始 exp-019 代码，但下一条会取消）
2. [PENDING] urgent redirect: 取消 exp-019，改为 ablation 深度分析 + appendix table + 多种子
3. [PENDING] worker_done 回调（n16 readiness check）
4. [PENDING] F1 discrepancy 调查（ablation greedy NER 0.618 vs 论文 Table 2 0.644，差 2.6pp）

**等待中**：
- Dream dream_20260515T092545 在 "reviewing" 阶段（imagine + write done），完成后会注入 session
- Agent 处理完 redirect 后的分析结果
- Reviewer 已被 reset（新 session 会自动启动）

### 4. 📋 待办
- Dream 完成回调到达 → Read dream-report-action skill → 按 D072 discount D071 相关建议，提取与 framing 无关的 structural insights（related work gaps、presentation issues）
- Agent 返回 F1 discrepancy 调查 → 如果 eval 方法差异 → 确保 appendix table 注明评估方法不与 Table 2 混用；如果 data 差异 → 修复
- Agent 返回 ablation 深度分析 → 检查 non-tied subset 重叠度（如果同批 instances 在两种条件下都 non-tied → 进一步证明 compression 是 instance-level intrinsic）
- 多种子 seed456 如果 ready → approve + allocate GPU（seed42/123 已完成，只缺 456）
- Paper Agent 补充 patch 处理完毕 → post_to_reviewer 验证 D072 全部修改 → 通过后 submit_paper_to_review Round 7
- Round 7 审稿 → 目标 3.5+/5 (Findings accept)
- 最终提交 DDL: 2026-05-25（距今 10 天）

### 5. 🎯 战略上下文
**核心发现演化**：D070(gap observation) → D071(constrained decoding bottleneck, FALSIFIED) → D072(universal gap proven by controlled ablation) → D073(skip verifier, analytical paper)

**论文定位**："Strong Predictors, Weak Selectors" — 5 个 confidence signals predict quality (AUROC 0.75) but universally fail at best-of-N selection。Controlled free-form ablation 证明 LP score compression 是 model/task intrinsic（std ratio 0.97x），非 constrained decoding artifact → gap 是 structured IE 的 fundamental limitation。

**6 轮 3.0/5 plateau 的突破策略**：内容从 "12 页说路不通" 升级为 "有受控实验证明为什么不通 + 证明是 universal"。关键加分项：(1) controlled ablation = 方法论严谨性提升，(2) universal scope > regime-specific scope，(3) non-tied subset counterfactual = actionable diagnostic。

**最容易判断错的事**：
- 不要因为 Dream 报告（基于 D071）建议 "强化 constrained decoding bottleneck narrative" 就照做——D071 已被证伪
- 不要因为 RE LP flip 看起来有趣就升级为 claim——single seed, no significance
- 不要重启 exp-019 verifier——Reviewer 给出了充分理由取消，D073 已 logged
- Paper Agent 已完成两批 patch，下一步是 Reviewer 验证，不是继续改——避免 over-editing
- Ablation F1 与 Table 2 的 2.6pp 差异是 eval pipeline 差异，不影响 within-ablation 结论，但 appendix 不能与 Table 2 数字直接混用


---

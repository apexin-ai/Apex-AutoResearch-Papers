# reviewer / loop_6.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`46ccc2a738c76c09102a.json`](../../sessions/46/46ccc2a738c76c09102a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-15T10:20:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器名是 `autodl-5090`（不是 `autodl-5090(root)`，后者会报 unknown server）
- 项目 GPU 白名单未在 constraints.yaml 中明确定义（文件未创建），但历史上用 cuda:0 跑 freeform ablation 未被 flag。每次新实验仍需核对 `execution.gpu_ids`
- RE 结论全文必须标 "(preliminary, single benchmark)"——这是多轮审稿的硬约束，遗漏 = critical
- Selection F1 绝对值：ablation_report.json 与论文 Table 2 有 ~2.6pp 差异（greedy NER: 0.618 vs 0.644），原因未查明。**不要混用两套数字**

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090，工作目录 `/root/autodl-tmp/struct_self_consist_ie`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/`
- 论文源文件：`docs/paper/sections/{abstract,introduction,method,experiments,discussion,conclusion,appendix}.tex`
- paper_framing.md：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md`
- 模型 checkpoint：`checkpoints/qwen3-8b-scierc-merged-v2`（远程）
- Ablation 结果：`results/exp_freeform_ablation/ablation_report.json`（远程）
- N=16 数据：seed42 + seed123 完成，seed456 缺失（仅有 200-instance 部分结果）
- 无 wandb 配置，无活跃训练进程

### 3. 📊 当前状态
**刚完成**：
- D070/D071 论文修订 21 项验证（PASS）
- Free-form ablation 结果独立审查 → [critical] LP 压缩因果归因被否定
- 两轮 framing 影响评估（四维度审查）→ Agent "不需调整" 被打回
- D072 framing（universal gap）独立确认
- D073 ROADMAP 审查（exp-019 verifier 取消，PASS）

**Registry 状态**：exp_freeform_ablation 未在 registry 中注册（count=0 when filtered）。Worker 注册了 artifact `art_20260515_b80d82`。

**等待中**：
- Paper Agent D072 patch（title + abstract + intro + discussion + conclusion 全面修改）
- Dream (dream_20260515T092545) 结果（基于旧 D071 framing，需 discount）
- 可能的多种子实验回调

### 4. 📋 待办
- Paper Agent 提交 D072 patch → 按首轮报告的 7 处修改清单逐条核实（abstract:6-7, discussion:11/14/15/23-27/31, intro:25, conclusion:8）
- Dream 结果返回 → 过滤掉 framing 相关评语，保留与 framing 无关的审稿建议
- RE flip 3-seed 分析结果返回 → 显著则可升级为 secondary finding，不显著则要求从 Story Spine 降级到 appendix
- 多种子 N=16 seed456 完成 → 核实数据完整性
- Round 7 提交 → 全文最终审查（特别关注：是否还有残留的 "constrained decoding bottleneck" 因果归因）
- Selection F1 差异（ablation 0.618 vs Table 2 0.644）→ Agent 排查后审查结论

### 5. 🎯 战略上下文
**决策链**：D067(gap reframing) → D069(scope limiting) → D070(narrative restructure) → D071(regime-specific bottleneck) → D072(ablation 否定→universal gap) → D073(verifier cancelled)

**核心结论**：LP score compression 是结构化 IE 的固有属性（std ratio 0.97x constrained vs free-form），非 constrained decoding 导致。Correlation-selection gap 是 universal。

**最容易判断错的事**：
1. **论文中残留的 "constrained decoding" 因果归因**——D071 在 abstract/intro/discussion/conclusion 至少 7 处写了 "constrained decoding causes compression"，D072 patch 必须全部修正。grep `constrained.decoding` 全文扫描
2. **RE flip 不要过度解读**——single seed, +1.69pp, NER 方向相反。paper_framing.md Story Spine 第 4 点已将其提升过高，我已发 warning 但未见降级
3. **"first" 措辞**——论文不能说 "first to study confidence for IE"（Nédellec 2026 先于我们），只能说 "first controlled ablation proving universality" 且需措辞精确
4. **Parse rate 99.95%**——这挑战了 intro:19 "without constrained decoding, a substantial fraction of outputs are unparseable"。如果新论文仍保留此句，与 ablation 数据矛盾
5. **6 轮 3.0/5 的根因是 content ceiling**——ablation 结果是唯一新 content。如果 D072 patch 只改叙事不加 ablation 数据，评分不会突破


---

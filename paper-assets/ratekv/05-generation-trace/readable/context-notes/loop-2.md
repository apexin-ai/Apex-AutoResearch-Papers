# director / loop_2.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`ff6325941fdc313d56d4.json`](../../sessions/ff/ff6325941fdc313d56d4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-14T05:54:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 限 westd-37397 的 cuda:0 + cuda:1（2× RTX PRO 6000 96GB），不得使用其他设备
- ARR May 25, 2026 deadline（距今 11 天），投稿目标 EMNLP 2026 Main
- D015 已激活 Plan B framing："analysis + conditional method"，不是 "universal method"。Claim 2 不得说 "universally outperforms"
- RateQuant 描述不得 mischaracterize——它有 discrete greedy (Algorithm 1, Prop. 6)，不仅是 continuous waterfilling（D012 教训）
- n=3 模型的 heterogeneity correlation 不得称 "significant"——只能用 "directional evidence" / "consistent trend"（p=0.10）

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397 (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/ratekv
- Python/conda：未明确记录，Agent 连接后自动探测
- GPU：2× RTX PRO 6000 96GB（cuda:0 + cuda:1），当前均空闲
- 活跃进程：无（所有 27 个实验已 DONE）
- Dream：dream_20260514T002109 已提交，状态未确认——接手后先 `get_dream_status` 检查

### 3. 📊 当前状态
**刚做完**：跨架构验证全部完成（Qwen/Llama/Mistral hires pipeline + Llama aggressive compression），D016 定论。paper_framing.md 已按 Plan B 全面重写（3 Claims + Story Spine + Differentiation + Reviewer Concerns）。

**实验全景**：27 个实验全部 DONE，13 success / 7 negative / 8 failed(早期 sanity/mvp 阶段)。无 RUNNING/PREPARING。

**P0 全部完成**：plan_001-008 均已执行，核心数据齐全。

**待执行 P1**：
- plan_009 Oracle comparison（brute-force 最优 vs MCKP gap）— planned
- plan_010 Cross-domain calibration robustness — planned
- plan_011 Head sensitivity visualization — planned（report 显示 "preparing"）
- plan_014 K/V separation — planned
- plan_012 Downstream eval (ARC-C/HellaSwag/PIQA/WinoGrande) — planned（report 显示 "preparing"）

**P2**：plan_013 70B profiling — planned

**等待中**：
- Dream dream_20260514T002109 结果——ROADMAP 待办里写着"等待 Dream 完成"
- 两张 GPU 完全空闲，必须立即派实验

### 4. 📋 待办（条件触发式）
- Dream 完成且无结构性问题 → 按 P1 优先级派实验，双卡并行（plan_011 + plan_012 可并行，plan_014 独立可并行）
- Dream 报告结构性问题 → 先修 framing/plan 再派实验
- GPU 空闲 > 10 min → 立即派最高优先级 P1 实验，不等 Dream
- plan_012 downstream eval 完成 → 与 RateQuant 论文的 eval suite 对比，确认覆盖度
- plan_014 K/V separation 完成 → 如果 K/V 分离有显著收益，更新 Claim 2 和 paper_framing.md
- P1 完成度 ≥ 70% → 激活 Paper Agent 写初稿（`director_post_to_paper_agent`，Full Draft 模式）
- 论文初稿完成 → `submit_paper_to_review` 提交审稿（review_chat_id 已配置）

### 5. 🎯 战略上下文
**核心结论链**：
- D005: attention MSE 作为 distortion proxy 被 falsify → D007: pivot 到 quant-only MCKP
- D009: constrained MCKP（cardinality constraint）解决 compounding effect → D010: MVP PASS (27%)
- D013: RateQuant greedy 在 {2,4,8,16} 上 catastrophic fail (PPL 32.45 vs 11.23) → 关键 differentiation
- D015/D016: Plan B framing 激活——MCKP 收益与 uniform 退化幅度成正比，GQA ratio 是粗略 proxy

**最容易判断错的事**：
1. **不要以为 Llama/Mistral 是失败**——它们是 Plan B framing 的核心证据（"何时不值得做 non-uniform"）。诚实的负面结果是论文的强项
2. **GPUs 现在空着**——这违反硬约束（>10 min 持有空卡不动），接手后第一件事派实验
3. **Dream 可能已经完成了**——6 小时前提交的，先 `get_dream_status` 检查，别重复提交
4. **paper_framing.md 已经很完整**——不需要重写，只需根据后续实验结果微调
5. **11 天 deadline**——P1 实验 + 论文写作 + 审稿迭代全部要在这个窗口内完成，必须最大化并行


---

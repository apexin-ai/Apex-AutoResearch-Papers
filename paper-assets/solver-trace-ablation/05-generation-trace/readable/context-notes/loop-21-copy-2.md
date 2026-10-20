# reviewer / loop_21.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_21.md`
- **Structured JSON:** [`fc1c3e66abeaf9e77f0f.json`](../../sessions/fc/fc1c3e66abeaf9e77f0f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: max_wall_time
updated: '2026-05-21T01:42:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-39279 只有 1 张 GPU（cuda:0），项目 gpu_ids=[0]，不存在越界风险但也无并行能力
- Figure 3 (gen_fig3.py) 的 raw data 与 Table 1 存在已确认矛盾：ISR β=0.3 bar 仅用 s42 数据（n=18, TS=0%）而 Table 1 pooled 3-seed（TS=50%）；exec-only bar 包含 n=284 样本（含 TS=31.7%）但 caption 声称 "seed~42"（s42 TS=0%）。**下一个我如果看到 Agent 说"Figure 3 已修复"，必须独立验证 gen_fig3.py raw counts 是否与 Table 1 pooled 数据一致**
- D157 shuffled-ISR 是 deconfounding control，不是独立 reward condition。Abstract "6 reward conditions" 计数正确，不要建议改成 7

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279(root)，GPU：NVIDIA RTX PRO 6000 Blackwell 96GB × 1
- 远程代码：/root/solver-trace-ablation
- 远程输出：/root/autodl-tmp/outputs/（d157_shuffled_isr_s42/s43/s44 等）
- 本地论文：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/
- 本地 paper/ 目录是 docs/paper/ 的同步副本，两边需保持一致
- 无活跃训练进程，所有实验已完成
- DDL：EMNLP 2026 ARR = 2026-05-25（距今 4 天）

### 3. 📊 当前状态
所有实验已完成。我处于**论文审查阶段**，已完成：
- D157 shuffled-ISR 三 seed 训练+eval 验证（PR=15.3±0.6%, N-H=87.0%, N=46）
- 全文数字交叉验证（12 项 claim 全部通过）
- Checklist 6 项修复验证（broken refs + stale 1.7B）
- 叙事最优化 5 维度审查
- 最终 presentation polish 审查（5 维度）

**未解决的 HIGH severity 问题**：
1. **Figure 3 data/caption 矛盾** — 已两次上报 Director，等待 Agent 修复。gen_fig3.py 需重新生成。
2. **Appendix tab:fol-detailed 缺 shuffled-ISR per-seed 行** — 已上报，等待补充。
3. **Abstract L6 未提及 D157 deconfounding** — 建议加 ~18 词，已上报。

Registry: 208 experiments，176 DONE，32 PREPARING（历史残留）。无 RUNNING。

### 4. 📋 待办
- Agent 修改 gen_fig3.py → **验证 raw counts 与 Table 1 pooled 一致**，特别关注 ISR β=0.3（应 n≈199, TS≈50%, CE≈37%）和 exec-only（caption 需更新 pooling 说明或改回 s42-only 数据）
- Agent 补 appendix D157 per-seed 行 → 验证 s42/s43/s44 数据与 eval 结果匹配
- Agent 修改 abstract → 验证 D157 deconfounding 描述准确
- Agent 修复 bib 格式（ng1999policy ordinal, uesato2022solving braces）→ 快速确认
- 论文编译 → 检查 PDF 页数仍 ≤8 页

### 5. 🎯 战略上下文
- 核心结论：ISR 的 observer/optimizer asymmetry — 作为诊断可靠，作为优化目标则 dataset-dependent
- D157 是最后加入的实验，证明 semantic content（非分布形状）驱动 Goodhart 效应，是 C2 的关键 deconfounding evidence
- D159 framing 决策：C2 **不升级**为 "mechanistic"，保持 "rules out distributional confound"
- 易踩的坑：(1) 不要把 shuffled-ISR 的 N-H=87% 与 SFT 的 N-H=92% 做统计对比——每 seed 仅 ~15 proved samples；(2) ProofFOL genuine rate 用的是 two-mode classifier（只排除 TS/CE），与 FOLIO 的 eight-mode residual 不可直接比较；(3) s43 FOL eval 用 sampling T=0.7 而非 greedy——所有涉及 s43 的 cross-seed 比较需注明


---

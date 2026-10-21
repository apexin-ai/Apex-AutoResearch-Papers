# director / loop_8.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`2a69f04c5bf6534fc7ca.json`](../../sessions/2a/2a69f04c5bf6534fc7ca.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-17T08:28:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 be-a6k-1 的 cuda:0-3（项目配置白名单）
- Degeneracy 定义已统一为 **Constant F1, gold-filtered** (D123)。任何新分析/实验的 degeneracy 计算必须用这个定义，不能用 KeySet 或 all-data
- 论文数字: CoNLL 47.4%, SciERC 17.8%, Few-NERD 13.8%。旧值 58%/21%/10% 已全文清零，禁止再出现
- exp_028 (5-epoch Few-NERD) 正在训练，完成后 degeneracy 必须用 Constant F1 gold-filtered 计算，与主文一致
- 坚持 Main Conference track，不主动建议 Findings

### 2. 🖥️ 基础设施快照
- 服务器: be-a6k-1, 工作目录 /root/autodl-tmp/struct_self_consist_ie/
- 论文本地路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/
- 4×RTX 5090, cuda:0 被 exp_028 占用 (PID 371545, ETA ~2026-05-18 05:30 UTC)
- cuda:1-3 空闲
- Paper Agent session 活跃 (feishu:group:oc_523053f5a039428dc15666668fa856b3:paper_agent)

### 3. 📊 当前状态
**刚做完**: D123 framing revision (degeneracy 统一 + two-condition framework) 全部落地，Paper Agent Batch 1-3 完成，Reviewer 确认整合 PASS。

**进行中**:
- exp_028 (Few-NERD 5-epoch): RUNNING on cuda:0, ~18h remaining。验证 "低 degeneracy 是否 under-training artifact"
- Main Agent: Figure 3 重绘 (新 x 轴值 47.4/17.8/13.8) + N-scaling paired degeneracy 确认。已派但尚无回复
- Paper Agent Batch 3: Q3/Q4 integration + epoch confound 预留 — 已完成

**等待中**:
- exp_028 完成回调 → 计算 5-epoch degeneracy + LP selection → 写入 Appendix app:epoch_confound
- Figure 3 重绘完成 → 确认 per-type x 值是否也变了
- Missing references 核实 (Byerly & Khashabi 2024 可能是幻觉引用)

### 4. 📋 待办（条件触发式）
- exp_028 完成 → Constant F1 gold-filtered 计算 degeneracy → 如果 ≤15%: 直接加入 appendix "confirms intrinsic"; 如果 >20%: 改 framing 为 "training convergence modulates degeneracy, early stopping as practitioner lever"
- Figure 3 重绘完成 → 确认 per-type Spearman ρ 是否变了 → 如果变了需更新 appendix 表格数字
- 全部修复完成 → submit_paper_to_review (recommend continue mode) → Round 18
- Round 18 如果 ≥3.5 → 直接准备投稿; 如果仍 3.25 → 评估是否再做一轮

### 5. 🎯 战略上下文
- **核心发现升级 (D123)**: LP selection 需要 TWO conditions: low degeneracy + LP-quality alignment (within-instance ρ(LP,F1) > ~0.3)。这解决了 14 轮 reviewer 打 "n=3 degeneracy" 的问题，从单一因素变为双条件独立验证
- **W2 关键结论**: rank=8 LP 并未更压缩 (range 0.057 > 0.041)，真正区分 SciERC/Few-NERD 的是 within-instance ρ (0.2 vs 0.5+)
- **Round 17 score 3.25**: R1=3.5 (accept), R2=3.0 (leaning Findings)。R2 核心 concern 是 novelty/excitement (纯诊断无 positive method)。W4 Practical Guidance + two-condition 升级能部分缓解但可能不够翻转 R2
- **易错点**: 4B degeneracy (10.4%) 未更新（Director 未提供新值），per-type 值 (19.8% Art 等) 是 entity-type 粒度非 aggregate，N-scaling paired 值 (11.1%→4.5%) 是 subset 值 — 这三类数字不需要改，别误改
- **时间线**: DDL 2026-05-25 (8 days)。exp_028 ~明天完成，之后 1 天 patch + 1 天 Round 18 review + buffer。充裕


---

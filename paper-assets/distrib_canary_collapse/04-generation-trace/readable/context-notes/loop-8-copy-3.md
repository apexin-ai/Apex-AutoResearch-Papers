# reviewer / loop_8.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`3ed6bed49c704f321084.json`](../../sessions/3e/3ed6bed49c704f321084.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-16T00:36:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 cuda:0, cuda:1（westd-19828）。越界即 critical。
- Claim 措辞上限："consistent across two transformer decoder-only model families of similar scale"——不可用 "architecture-agnostic" 或 "scale-independent"
- α=0.75 vs α=1.0 consensus 数字禁止直接对比（D038 #27，标准不同）
- FNR=0% 声明必须附 D017 独立证据（first-differencing 24/24）
- TY 有两套实现：**Method A**（method_ablation.py, ADF d_max + fixed p=1 + F-test）是论文 canonical 版，**Method B**（window_sensitivity.py 旧版, hardcoded d=1 + AIC p + χ²）已修复但要警惕残留引用
- T notation：T = generation cycles，数据点 = T+1。已在全项目统一，但审查时注意旧 artifact 可能用旧约定

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828(root)，代码根目录 /root/autodl-tmp/distrib_canary_collapse
- Python：/root/miniconda3/bin/python（conda base）
- HF cache：/root/autodl-tmp/.hf_cache
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/
- 论文源：docs/paper/*.tex（主）；artifacts/_project/paper/*.tex（副本，需同步）
- 活跃进程：gpt2m_a025_s42（cuda:0, PID 149202）、a025_s44（cuda:1, PID 147811）

### 3. 📊 当前状态
**刚完成的审查链**（全部已 post 给 Director）：
1. κ 分析审查 → PASS
2. Method subset ablation 审查 → PASS（发现 TY 跨报告矛盾）
3. Window sensitivity T=11 扩展审查 → 发现 TY infeasible（触发深查）
4. TY seed audit 审查 → 确认 Bug #1 (off-by-one) + Bug #2 (两套 TY 实现)，**论文 FNR=33.3% 正确**，我之前的 critical 已撤回
5. Window sensitivity bugfix 审查 → PASS，consensus 稳定点从 T≥6 改为 T≥5
6. artifacts FNR 25%→33.3% 修复 → PASS
7. **Paper-Registry 一致性审计** → **Table 1 α=1.0 行 mean±std 错误**（ECE std 差 5×，ppl std 差 7×）+ discussion 称 GPT-2m "not yet available" 但实验已完成——两项均已 post，等 Director 安排修复

**Registry RUNNING**：gpt2m_a025_s42（Claim 2 cross-arch）、a025_s44（D026 multi-seed #3）

**等待中**：
- gpt2m_a025 完成回调 → 需审查 regime-dependent 跨架构复现
- Table 1 修复 worker → 需审查
- GPT-2m 结果写入论文 → 需审查 discussion.tex 更新
- Paper Agent Step 5 后续轮次 → 可能触发章节审查请求

### 4. 📋 待办（条件触发式）
- gpt2m_a025_s42 完成 → 审查 regime map 是否跨架构复现，核查 Claim 2 强度
- Table 1 α=1.0 行修复 worker 完成 → 验算 mean±std 与 registry 一致
- discussion.tex GPT-2m 更新 → 审查 claim 措辞是否超出 "two decoder-only families"
- Paper Agent 提交章节审查 → 按 §5 模板走维度评分（先做合规检查：Agent 写前是否看过 red-section skill）
- Director 转发 Framing 提案 → Read negative-framing-review skill，四维度审
- 任何新训练实验提交 → 核查 CUDA_VISIBLE_DEVICES 在 {0,1} 白名单内

### 5. 🎯 战略上下文
- **核心框架**：5 方法 4/5 consensus + ≥3/4 seed = Tier 3，FPR=0%, FNR=0%。这是论文的 headline，已充分验证。
- **D027 reframe**：方法论陷阱（Claim 3 领衔）> regime map（Claim 2）> case study（Claim 1）。Claim 3 证据最强（κ=0.185 跨架构一致、4/5 唯一最优、PermG linchpin）。
- **最容易判断错的事**：TY 的两套实现。Method A（论文用的）和 Method B（window_sensitivity 旧版）结果天差地别。看到 TY 数字先确认来源是哪套实现。我因此错误发了 critical 又撤回，浪费了一轮。
- **Table 1 是当前最紧急的修复**：α=1.0 聚合行 mean±std 全错，审稿人必查。单 seed 行全对，只是聚合计算有误。
- **GPT-2m 是 low-hanging fruit**：实验已完成（6/6 Tier 3），但论文还写 "not yet available"。纳入后 Claim 强度直接提升。
- **Registry 卫生**：3 个 D044 砍掉的实验仍为 QUEUED/PREPARING，alpha_sweep_a060_s42 为 PREPARING 孤儿——不影响结论但容易混淆。


---

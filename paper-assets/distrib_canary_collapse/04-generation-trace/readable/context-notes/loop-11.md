# director / loop_11.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_11.md`
- **Structured JSON:** [`e5ee4c499e51c7aaa25a.json`](../../sessions/e5/e5ee4c499e51c7aaa25a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-18T00:58:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 cuda:0, cuda:1 (westd-19828)，不可用其他卡
- 分析必须用 `analyze_generalize.py`（导入 `method_ablation.py::_onset_gen`），禁止用旧 `analyze_opt1b_full.py` 的 `_onset` 函数
- Table 7 统一参数：n_perm=5000, xcorr_max_lag=5, granger_max_lag=1, raw p<0.05（D057 决策）
- Consensus K≥4/5 作为 multiplicity control，不做 per-method BH FDR（论文方法论已改）
- VERSION A 已确认 (D054)，不可降级回 VERSION B
- 论文唯一真源：`docs/paper/`（不是 artifacts）
- ECE 双向性叙事：是指标固有属性（非 domain-specific），token_entropy 才是完美单向的

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828 (connect.westd.seetacloud.com)，账号 root
- 工作目录：/root/autodl-tmp/distrib_canary_collapse
- Python: /root/miniconda3/bin/python，conda activate base
- HF cache: /root/autodl-tmp/.hf_cache (HF_HOME)，gpt2-large 已通过 hf-mirror 恢复
- metrics.py 有 MAUVE try/except 安全网（gpt2-large 加载失败时 skip）
- `iterative_train.py` 支持 `--start_gen` 参数（本轮新增，用于 resume）
- 磁盘：~24% used（清理后释放 191GB，从 100% 降到 24%）
- 两张 GPU 当前空闲（所有训练实验已完成）

### 3. 📊 当前状态
本轮完成：
- Pythia-1.4B Scale 实验完成（K≥4=5/8 raw, PermG rev=0/8）→ Table 7 Scale 行填入
- C4 seed-43 完成（K≥4=8/8, PG_rev=0/8）→ 确认 C4 s42 的 ECE bidirectionality 是 seed-dependent
- D057 方法论决策：raw p + consensus-as-multiplicity-control（Reviewer 确认有文献先例）
- 论文方法论文字已修改（BH FDR → consensus control）
- Table 7 大部分行已更新（Architecture/Domain/Scale 用统一参数数字）
- 磁盘满危机修复 + MAUVE/gpt2-large 网络问题修复

**Agent 队列中仍有 2 条未处理指令**（Agent 正在执行中）：
1. Baseline (Pythia-410M) 行更新为 8/8, 8/8, 8/8, 6/8, **3/8**, 4/8, 6/8
2. Architecture paragraph 修正（删除 "0 reverse-direction pairs" claim，改为 token_entropy 限定）
3. 附录 FDR sensitivity analysis table
4. Table 7 caption 最终版

等待 Agent 完成这些后应该就 Round 2 ready。

### 4. 📋 待办
- Agent 汇报 Table 7 全部更新完成 → Reviewer 做最终一致性审查 → 确认无矛盾后提交 Round 2 (`submit_paper_to_review`)
- 如果 Reviewer 发现新矛盾 → 修复后再提交
- C4 seed-43 registry 需确认已更新为 DONE/success（metrics: K≥4=8/8, PG_fwd=8/8, PG_rev=0/8）
- 附录 FDR sensitivity table 完成后 → 检查是否需要 Reviewer 验证数字
- 全部完成 → `director_reply_to_user` 通知用户论文准备就绪 + `submit_paper_to_review`
- GPU 空闲 → 无紧急训练任务，Round 2 提交是当前唯一 blocker

### 5. 🎯 战略上下文
- 项目目标：EMNLP 2026 Main Track（ARR June cycle，DDL ~June 15）
- 核心 narrative (D027 Option B)：方法论陷阱 + 多方法共识框架，canary prediction 为 case study
- D054: VERSION A confirmed（三架构泛化）
- D055: C4 域 ECE bidirectionality → 后来发现是 ECE 固有属性（Baseline 也有 3/8），不是 domain-specific
- D056: Scale K≥4=5/8 通过（raw p 下）
- D057: Table 7 统一用 raw p + consensus K≥4/5 as multiplicity control（Reviewer 确认 Nichols 2005 conjunction analysis 先例）
- **易错点**：(1) 不要把 FDR-corrected 数字放进 Table 7（D057 决策是 raw p）；(2) ECE 双向性叙事：是指标属性不是 domain/seed noise，token_entropy 才是 "perfect"；(3) Baseline PG_rev=3/8 是真的（统一参数后暴露），architecture paragraph 需要改；(4) 26 个成功实验（含 C4 s43），Table 7 五行：Baseline/Architecture/Domain/Scale + GPT-2m 在 Table 3-6
- **审稿人最可能攻击**：为什么不用 FDR → 附录 sensitivity analysis preempt；方法间非独立 → FPR=0% 实证支撑


---

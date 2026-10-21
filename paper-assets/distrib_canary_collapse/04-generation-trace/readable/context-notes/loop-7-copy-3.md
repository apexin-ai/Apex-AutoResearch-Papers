# reviewer / loop_7.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`2f02bc1983ec5a29e114.json`](../../sessions/2f/2f02bc1983ec5a29e114.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-15T17:43:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（westd-19828 双卡）。越界立即 critical。
- D019：df_resid<20 时 cohen_f2_label 必须返回 "df_too_low"，不得分类效应量。
- D038：α=0.75 consensus（11/16 ROBUST, 单 seed）与 α=1.00（6/16, 4-seed K=4 S=3）不可直接比较。禁止引用 overestimation_rate。
- D041 循环 ground truth：6 个 "ground truth ROBUST" pair 由 K=4 S=3 定义——与被评估的配置相同。FNR=0 声明必须标注此循环性。
- paper_framing.md #28：token_entropy→perplexity 在 α=0.75 下不可引用（falsely ROBUST）。

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828(root)，远程目录 `/root/autodl-tmp/distrib_canary_collapse`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- HF cache：`/root/autodl-tmp/.hf_cache`，HF_ENDPOINT=hf-mirror.com
- 模型：EleutherAI/pythia-410m（主）+ gpt2-medium（cross-arch 验证）
- 数据：`data/wikitext103_5k`（5000 条）+ `data/wikitext103`（完整，20gen 用）
- 无 W&B 配置，不检查 W&B
- 截至 handoff 时活跃进程：
  - `gen_wiki_gpt2m_a100_s42_v3`：cuda:0，gpt2-medium cross-arch 实验，~45% 进度
  - `alpha_sweep_a050_s43`：cuda:1，PID 134860，刚启动（17:40 UTC）

### 3. 📊 当前状态
刚完成 `alpha_sweep_a025_s43` 审查（PASS）并发布报告。Worker 分析也已完成——cross-seed 一致性极强（distinct_1 drift s42=-40.3% vs s43=-40.5%），non-monotonic claim 获独立复现。

Registry RUNNING：
- `alpha_sweep_a050_s43`：seed 43 的 α=0.50 复现，cuda:1
- `gen_wiki_gpt2m_a100_s42_v3`：gpt2-medium cross-architecture 验证，cuda:0，ETA ~22:20 UTC

等待中：
- Director 对 fig_differencing_dmax F=612-2615 列归属 warning 的回复（可能在 Undifferenced 还是 First-Differenced 列标错）
- fpr_fnr_calibration.json methods_order 字段 TY/permG 顺序反了（WARNING 已发，未修）

### 4. 📋 待办
- `alpha_sweep_a050_s43` 完成 → 审查 cross-seed 一致性（对比 a050_s42: d1 drift -37.3%），检验 non-monotonic 中间点是否复现
- `gen_wiki_gpt2m_a100_s42_v3` 完成 → **重点审查**：cross-arch 是否复现 method sensitivity pattern（naive 100% sig vs permG/TY 低 sig），这是 Claim 3 的关键外推证据
- 后续可能出现 `alpha_sweep_a075_s43` → 审查 Granger FDR 是否复现 3/8 sig（s42 结果）
- Director 若转发章节审查 → 启用 paper_framing.md 28 条约束逐条核对
- 收到 Framing 提案 → 立即 Read `negative-framing-review.skill.md` 按四维度审

### 5. 🎯 战略上下文
- **Option B framing**：Method pitfalls + multi-method consensus → Claim 3（method sensitivity）领跑 → Claim 1（case study）→ Claim 2（regime map）
- **核心发现链**：naive Pearson 100% sig → differencing 翻转 perplexity 通道（24/24→0/8）→ TY d_max 敏感（6.25%→93.75%）→ K=4 S=3 共识达 FPR=0/FNR=0
- **最易判断错的事**：
  1. FNR=0 "完美分离"看起来太好——别忘了 D041 循环 ground truth，6 个 pair 是同一个 K=4 S=3 标准定义的
  2. consensus_framework.py METHOD_NAMES 顺序是 [naive, differenced, threshold, **TY**, **permG**]（index 3=TY, 4=permG），但 fpr_fnr_calibration.json 写反了
  3. 远程和本地可能存在同名文件的历史残留——断言"未修改"前必须两边都读（L1 #5）
  4. α=0.25 的 distinct_1 drift（~-40%）比 α=0.50（-37%）和 α=0.75（-33%）都大——这是 non-monotonic 的核心证据，不是 noise


---

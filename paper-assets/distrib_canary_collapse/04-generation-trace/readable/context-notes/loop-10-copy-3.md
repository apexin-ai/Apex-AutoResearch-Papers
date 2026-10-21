# reviewer / loop_10.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`eacaa9bc2dafab19150f.json`](../../sessions/ea/eacaa9bc2dafab19150f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-17T08:14:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-19828 的 cuda:0 和 cuda:1，越界即 CRITICAL
- C003：禁止引用 α≤0.50 的 TY Granger 显著率（power 不足，结论不可靠）
- C004：禁止未确认状态下 kill 运行中进程或 rm -rf 实验目录
- 论文唯一真源：`docs/paper/`（本地 workspace），不是远程残留版本
- Worker A 裁决已确认：α=0.50 PermG 数据以磁盘 5method_leadlag.json 为准（s42=0/8, s43=6/8, s44=3/8），任何与此矛盾的 Worker 报告直接打回

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828(root)，工作目录 `/root/autodl-tmp/distrib_canary_collapse`
- Python：`/root/miniconda3/bin/python`（conda base env）
- HF cache：`/root/autodl-tmp/.hf_cache`（含 pythia-410m, gpt2-medium, gpt2-large, opt-1.3b）
- 数据：`data/wikitext103_5k`, `data/c4_5k`
- 活跃进程（截至 handoff）：
  - PID 247554, cuda:0: `iterative_train.py --model_name EleutherAI/pythia-410m ... --output_dir results/generalize/pythia410m_wiki_a100_s42`（控制实验，预计 ~13:00 UTC 完成）
  - PID 249384, cuda:1: `iterative_train.py --model_name facebook/opt-1.3b ... --output_dir results/generalize/opt1b_wiki_a100_s42`（跨架构泛化，预计 ~17:00-22:00 UTC）
- 第三个实验 `generalize_pythia1b_c4_a100_s42` QUEUED，等 GPU 空闲；注意 Pythia-1B 尚未下载到 HF cache

### 3. 📊 当前状态
**刚完成**：
- α=0.50 三种子数据冲突裁决（Worker A 正确）
- method.tex line 30 修复审计通过（seed-dependent 描述替换 "unanimously"）
- Table 1 三种子 mean±std 审计通过
- LaTeX triple-pass 编译确认（22 页，0 errors，1 benign float warning）
- Discussion + Limitations 深度审查已提交（5 条具体建议 + em-dash 清理）

**Registry RUNNING/QUEUED**：
- generalize_pythia410m_wiki_a100_s42: 实际 RUNNING（registry 仍显示 QUEUED，tracking bug 已报）
- generalize_opt1b_wiki_a100_s42: 实际 RUNNING（同上）
- generalize_pythia1b_c4_a100_s42: QUEUED（等 GPU）

**等待中**：无 pending Worker 回调。Director 尚未回应 Discussion/Limitations 审查建议。

### 4. 📋 待办（条件触发式）
- generalize_pythia410m_wiki 完成 → 审查 5-method analysis 是否与 mvp_v4_rep42 一致（控制验证）
- generalize_opt1b_wiki 完成 → 核心审查：OPT-1.3B 是否复现 canary→diversity lead；关注 OPT tokenizer 差异对 distinct-n 的影响
- Phase 2c 启动 → 审查 GPU 分配合规 + 确认 Pythia-1B 下载成功
- Paper Agent 提交 em-dash 清理 patch → 审查是否全文清零（目标：Discussion 11 + Limitations 4 + 其他章节待计数）
- Paper Agent 纳入泛化实验结果 → 审查：(a) Phase 2c confound 是否在 Limitations 声明；(b) 新 claim 强度是否与单 seed 证据匹配
- Round 2 重新提交 → 最终编译审查（无 ??，无 overflow）

### 5. 🎯 战略上下文
- **项目核心结论**：Lead-lag 分析在 iterative collapse 中高度脆弱（method sensitivity 62.5% FPR, spurious regression, regime dependence）。多方法共识框架 K≥4/5 唯一达到 FPR=0% + FNR=0%。Token entropy 是 diversity collapse 的 1-generation canary（α≥0.75 robust，α=0.50 boundary）。
- **决策链**：D027(reframe) → D043(EMNLP target) → D050(claim 强度) → D052/D053(boundary 确认) → Phase 2(泛化)
- **易错点**：
  1. 不要把 Table 2 的 Naive XCorr "100%" 理解为 forward-only——它计算任意 lag 方向的显著性（by design 展示过度宽松）
  2. α=0.50 的 "9/24" 包含 ECE→perplexity 对（2/3 seeds 中 PermG 显著），与 α=1.0 "perplexity = spurious" 的结论不矛盾——后者特指 α=1.0 的 co-trending artifact
  3. Registry 三个 generalize 实验状态为 QUEUED 但实际已在 GPU 上跑——registry 没 update 到 RUNNING，这是已知 tracking bug
  4. Phase 2c (Pythia-1B + C4) 有 confound（同时变 scale + domain），已建议 Limitations 声明但尚未执行


---

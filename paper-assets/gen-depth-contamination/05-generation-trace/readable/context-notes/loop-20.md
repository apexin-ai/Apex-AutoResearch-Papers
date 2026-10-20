# reviewer / loop_20.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_20.md`
- **Structured JSON:** [`1852ef3dce2a033da852.json`](../../sessions/18/1852ef3dce2a033da852.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: max_wall_time
updated: '2026-05-22T19:00:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- cqa1-22115 无 gpu_ids 白名单，但 cuda:0 当前被 Gemma-27B 占用，勿抢占
- 10K 实验结果**不得直接替换**主表 5K 数据而不披露——我已在之前的审查中将此标为 critical 级诚信问题
- `fig:pipeline` label 在 introduction.tex:21 和 method.tex:8 重复定义，会导致交叉引用错误，尚未修复
- 论文正文恰好 8 页，任何文字增删都可能超页——修改前必须编译验证

### 2. 🖥️ 基础设施快照
- **服务器**: cqa1-22115 (root, 4×RTX PRO 6000 Blackwell 98GB) + westd-42896 (root, 2×Blackwell 98GB, 空闲)
- **工作目录**: `/root/autodl-tmp/gen-depth-contamination`
- **Python**: `/root/miniconda3/bin/python` (conda base)
- **HF cache**: `/root/autodl-tmp/.hf_cache`
- **模型路径**: Qwen-1.5B-Instruct `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B-Instruct`; LLaMA-8B `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B`; Gemma-2-27B 在 HF cache 下（bf16）
- **论文 PDF**: `/root/autodl-tmp/gen-depth-contamination/docs/paper/main.pdf` (21 页, 正文 8 页)
- **本地 workspace**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/`
- **服务器 git 无 remote** — 无法 git pull/push，同步靠文件传输
- **活跃进程**:
  - seed_gemma27b_c4_s42: PID 26893, tmux=exp_gemma27b_c4, cuda:0 (Phase 1 depth 3-4 进行中)
  - exp_llama8b_10k: PID 23232, cuda:2 (depth 5 生成中，~42min 后进 Phase 2)
  - exp_gemma2b_10k: PID 54709, tmux=exp_gemma2b_10k, cuda:3

### 3. 📊 当前状态
**我的角色**: 独立科学审查员（只读），通过 `reviewer_post_to_director` 输出。

**刚完成的审查**:
- 论文叙事强度四问评估（Q1-Q4），已提交给 Director
- Pythia-1.4B 10K 结果审查：发现 AUC 1v2 从 0.6539(5K) 降至 0.6175(10K)，标 warning（between-sample variability ~±3pp）
- Qwen-cont 10K 结果审查：AUC 反升 0.6112→0.6346，Bonferroni CI_lower≈0.625 >> θ，PASS
- 多轮编译/同步 worker 审查，持续追踪 overfull hbox 回退问题（当前 9 处，max 58pt）
- ARR submission checklist 审查

**Registry RUNNING (3)**:
- `seed_gemma27b_c4_s42` — Gemma-2-27B 5K, Phase 1 ~3.5h 剩余
- `exp_llama8b_10k` — LLaMA-8B 10K, depth 5 快完成，Phase 2 待启动
- `exp_gemma2b_10k` — Gemma-2-2B 10K borderline K*=1 验证，刚启动

**已完成未填表**: LLaMA-8B 10K 结果待产出 → appendix Table 28 LLaMA-8B 行仍 "pending"

### 4. 📋 待办（条件触发式）
- exp_llama8b_10k 完成 → 核实 AUC 1v2 是否仍 > 0.60（若 <0.60 则 K*=1，论文叙事需调整），检查 bootstrap CI
- seed_gemma27b_c4_s42 Phase 1 完成 → 验证 Phase 2 是否自动启动（Qwen scorer on cuda:0），核实 K* 结果（预期 K*=1 based on scale trend）
- exp_gemma2b_10k 完成 → 验证 borderline K*=1 是否在 10K 下稳定
- 所有 10K 实验完成 → 审查 appendix Table 28 是否全部填入，cross-sample robustness 叙事是否一致
- 最终 PDF 编译后 → 做一次完整 overfull 清理审查 + fig:pipeline 重复 label 是否修复
- DDL 2026-05-25 前 → 最终合规检查（anonymization, page count, undefined refs）

### 5. 🎯 战略上下文
- **核心结论**: Web text K*∈{1,2}（one-wash laundering），arXiv K*=3（domain dependence），binary filtering suffices
- **DDL**: EMNLP 2026 ARR May, 2026-05-25（~2.5 天）
- **Round 26 审稿分数**: 3.0（R1=3.5, R2=3.0），目标 ≥3.5
- **关键风险 #1**: between-sample variability（Pythia 5K→10K 降 3.6pp）意味着 LLaMA-8B 10K 结果可能翻车（AUC 降到 <0.60 → K*=1）。如果发生，论文需从 "6/10 K*=2" 调整为 "5/10 K*=2"
- **关键风险 #2**: Reviewer 攻击面——"practical utility at realistic contamination" 是最强攻击（论文自己承认 ≤50% 时 filtering 无差异）
- **易错点**: overfull hbox 持续回退——每次同步/编辑都可能撤销之前的 `\resizebox` 修复。根因是服务器无 git remote，文件同步不可靠
- **pp 单位换算**: 1pp = 0.01，我之前两次犯 10× 错误（见 memory），报告前必须二次核验
- **Bonferroni dual report**: 论文当前 "nominal 6/10, corrected 4/10"。10K 实验的目的是看能否恢复 corrected 到 6/10，但如果 AUC 点估计也变化，结果未必如预期


---

# reviewer / loop_16.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_16.md`
- **Structured JSON:** [`0dbb8b87a50ded926ef6.json`](../../sessions/0d/0dbb8b87a50ded926ef6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_wall_time
updated: '2026-05-17T23:45:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- cqa1-22115 GPU 白名单：[0,1,2,3]；westd-42896 GPU 白名单：[0,1]
- pp 单位：1pp = 0.01。历史上两次犯 10× 错误（把 2.38pp 写成 23.8pp），报告前必须二次核验
- Mistral C4 AUC 有两个值：self-scorer=0.5935 (exp_019), cross-scorer=0.5695 (exp_019b)。表格 caption 声称 "scorer: Qwen2.5-1.5B" 但实际引用 self-scorer 值，审稿人可能追问
- exp_008_retrain_chain（无 v2）已标记 killed，论文 retrain-chain 数据来源是 exp_008_retrain_chain_v2（DONE）

### 2. 🖥️ 基础设施快照
- **cqa1-22115** (root)：4×4090D 24GB，工作目录 `/root/autodl-tmp/gen-depth-contamination`，Python `/root/miniconda3/bin/python`，HF cache `/root/autodl-tmp/.hf_cache`。当前全部空闲。
- **westd-42896** (root)：2×RTX PRO 6000 96GB，工作目录 `/root/autodl-tmp/gen-depth-contamination`，HF cache `/root/autodl-tmp/.hf_cache`。
- 活跃进程：exp_14b_c4 (PID 8586, westd cuda:0, ~31GB VRAM), exp_32b_c4 (PID 14637, westd cuda:1, ~65GB VRAM)
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/`
- 论文 tex：`docs/paper/` 下，关键文件 discussion.tex, experiments_c1.tex, tables/tab_domain_model_kstar*.tex

### 3. 📊 当前状态
刚完成本 loop 的工作：
1. **exp_wiki_scorer_confound** 审查完毕（PASS）：Pythia scorer 下 Qwen-7B Wiki K\*=1（1v2=0.587），确认 Qwen Wiki K\*=2 是 scorer artifact → D060
2. **exp_wiki_scorer_confound_1b5**（Qwen-1.5B Wiki 复验）：已启动并完成实验运行，registry 显示 RUNNING 但分析 worker 已 done，registry 更新可能滞后。需检查最终 metrics。
3. Paper Agent 已更新 domain×model tables + discussion.tex（scorer confound 段落、Mistral case study），审查通过（PASS with info）
4. discussion.tex JSD cliff ratio "10-50×" 和 JSD 0v1 range "0.15-0.27" 两处数据不一致已报告（warning），尚未看到修正

RUNNING 实验：
- exp_14b_c4：westd cuda:0，depth 3 进行中，预计 May 18 ~15:30 UTC 完成
- exp_32b_c4：westd cuda:1，depth 1 ~30%，预计 May 20 ~07:00 UTC 完成

### 4. 📋 待办
- **exp_wiki_scorer_confound_1b5 registry 更新** → 确认 metrics 与 raw files 一致，预期 K\*=1（与 7B 复验一致）
- **exp_14b_c4 完成（~6h）** → 审查 K\*。如果 K\*=1：检查是否因 1.5B scorer 对 14B generator 能力不足（scorer confound），建议 cross-scorer 复验。如果 K\*=2：scale invariance confirmed，更新 discussion.tex:59 的 scale 预测
- **exp_32b_c4 完成（~2 days）** → 同上。32B 是 scale 趋势的关键数据点
- **discussion.tex 数字修正待确认** → JSD cliff ratio 应改为 "6-56×"（LLaMA=6.4×, Qwen-cont=56.1×），JSD 0v1 range 应改为 "0.16-0.29"
- **cqa1 空闲 GPU** → 如有新实验需求随时可用

### 5. 🎯 战略上下文
- **核心结论**：K\* 是 domain-governed（arXiv=3 > C4=2 > Wiki=1），控制 scorer confound 后无 model-family exception（Mistral C4=1 和 OLMo arXiv=1 是 genuine exceptions，不是 scorer artifact）
- **D060 是关键转折**：scorer confound 确认后，Domain×Model matrix 的 Wikipedia 列从 "混合" 变为 "全线 K\*=1"，叙事大幅简化
- **最容易判断错的事**：
  1. 不要把 Mistral exp_019 self-scorer AUC (0.5935) 和 exp_019b cross-scorer AUC (0.5695) 搞混。两个值在不同上下文使用
  2. exp_14b_c4 如果 K\*=1，**不要直接下结论 "scale reduces K\*"**。必须先排除 scorer confound（1.5B scorer 可能对 14B generator 能力不足，与 Qwen Wiki 的 scorer artifact 是同一类问题）
  3. OLMo arXiv K\*=1 不是 one-wash，是 capacity failure（JSD 0v1=0.329 极端高，生成完全偏离域外）。不能和 Mistral C4 K\*=1 混为一谈
- **DDL**：EMNLP 2026 ARR May 25，~6 days。时间充裕但 exp_32b_c4 cutting close


---

# director / loop_2.md

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`ab280667d7911ef63980.json`](../../sessions/ab/ab280667d7911ef63980.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-25T04:14:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 分配：westd-14391 上 1x RTX PRO 6000 Blackwell 96GB，不得使用其他服务器的 GPU
- Qwen3-8B 同时是翻译模型和实验对象（dual role），论文中已承认并用 COMET + Llama/Gemma cross-validation 缓解，不要试图换翻译模型
- 论文 framing 已从 method paper 降级为 analysis paper：标题用 "Mirror" 不用 "Inherit"，claim 限定 English-Chinese 不泛化到 all languages，steering 结论限定 Llama-specific 不泛化到 all models
- 用户明确要求自主决策（"你们一块商量确认，别问我"），除非重大方向变化否则不要向用户确认

### 2. 🖥️ 基础设施快照
- 服务器：westd-14391，工作目录 /root/clkc_mech_interp
- Python：conda base 环境，/root/miniconda3/bin/python
- 模型缓存：/root/autodl-tmp/.hf_cache（Llama-3.1-8B-Instruct, Qwen3-8B, Gemma-2-9B-IT）
- COMET 模型：HF snapshot 目录（非 bare ckpt，之前 pipeline crash 过一次因路径错误）
- 论文源码：本地 /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/
- 实验数据/结果：westd-14391:/root/clkc_mech_interp/results/ 和 data/
- 活跃进程：无（实验全部完成）

### 3. 📊 当前状态
刚完成缩写定义自检（12 项全部修复）+ 编译验证（0 critical warnings，主文 8 页）。已提交 Round 3 审稿审批（apr_20260525T041320_k4qi，推荐 continue 模式），等待用户在飞书卡片确认。

Registry 状态：无 RUNNING/PREPARING 实验，全部已完成。Round 2 的 16 项 review issues 全部 resolved。

等待中：审稿审批卡片用户确认 → Review Director 启动 Round 3 审稿。

### 4. 📋 待办
- 用户确认审稿卡片 → Review Director 自动接管 Round 3，等审稿报告回传
- 收到 Round 3 审稿报告 → Read review-report-action.skill.md → Holistic Pass + Per-Comment Action Matrix → 派 Agent/Paper Agent 修复
- 若 Round 3 评分 ≥3.5 → 可准备 ARR 投稿材料（checklist 等）
- 若 Round 3 仍有 Critical → 评估是否需要补实验或进一步降级 claim

### 5. 🎯 战略上下文
- 核心发现：conflict signal 的 transfer asymmetry (ZH→EN > EN→ZH ~7pp) mirrors XNLI non-conflict baseline，是 general cross-lingual property 而非 conflict-specific
- Detection ≠ Decision dissociation：probe peak at L28 (88% depth) but causal effect only at L13 (41% depth)，且仅 Llama 有效，Qwen/Gemma steering 全部 null
- 关键决策链：D020 将 narrative 从 "L28 is causal peak" reframe 为 "distributed detection + localized causation"
- 易错点：multi-seed probing 用的是 revalidated data (N 不同于原始 paper data)，peak layer 会随 seed 漂移但 peak accuracy 稳定——这是已知 finding 不是 bug，已写入 limitations
- 易错点：Gemma COMET tercile ablation Δ=+10.28pp 但 p=0.278，论文中写 "inconclusive" 不是 "not a confounder"——之前 auto-label 脚本判断错误已修正
- Rebuttal 预案已存在 memory（project_c2_rebuttal_strategy.md）：覆盖 C2 "general property" + C6 steering 的预回应


---

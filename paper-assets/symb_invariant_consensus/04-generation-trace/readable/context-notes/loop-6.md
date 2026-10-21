# director / loop_6.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`2c4ab2b8cace3cab3e16.json`](../../sessions/2c/2c4ab2b8cace3cab3e16.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-17T07:59:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-32608 的 cuda:0（单卡 RTX PRO 6000 Blackwell 98GB）
- 禁止在同一 compound command 里 pkill + 启动脚本（M001/M003 教训，pkill -f 会匹配 tmux 父进程导致自杀）
- exp-001 的 +0.26pp 是最终结论（N=804），D012 的 +3.3pp 已确认为小样本噪声
- exp-013 constraint ablation 不能用 exp-001 的 raw_constraints（pipeline.py 修改时序问题）
- 模型下载损坏是反复出现的问题（Mistral 3次 ModelScope 截断，LLaMA shard2 截断）——下载后必须验证 total_size
- submit_training_job 脚本必须包含 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（否则 python not found）

### 2. 🖥️ 基础设施快照
- 服务器：westd-32608 (connect.westd.seetacloud.com), root, /root/symb_invariant_consensus
- Python: /root/miniconda3/bin/python, conda base 环境
- GPU: 1× NVIDIA RTX PRO 6000 Blackwell 98GB, cuda:0
- 模型路径 /root/autodl-tmp/models/：Qwen2.5-14B-Instruct ✓, LLaMA-3.1-8B-Instruct ✓(shard2已修), Mistral-7B-Instruct-v0.3 ✓(14.5GB完整), DeepSeek-R1-Distill-Qwen-7B ✓
- 数据：/root/symb_invariant_consensus/data/ (strategyqa_200, arc_challenge_200, math_l45_100, D012 60题)
- HF cache: /root/autodl-tmp/.hf_cache
- 活跃进程：exp-011-llama8b-v3 应已完成（提交 4h+ 前），GPU 可能空闲
- pilot-contrastive-prompt 待重跑（v1 因缺 conda activate 失败，EXIT_CODE=127）

### 3. 📊 当前状态
**刚完成的重大发现**：exp-011 LLaMA-8B 上 SICA +6.7pp (66.7% vs 60.0%)，MaxSAT 首次大规模激活（43/60 矛盾检出，5.3% 约束排除）。已发 urgent 指令要求 Agent 做 McNemar + bootstrap + 截断影响分析，但 Agent session 随后死亡（idle 240min），尚未收到统计检验结果。

**Registry 状态**（关键）：
- exp-001 sica_expanded_14b: DONE/success (+0.25pp, n=804)
- exp-002 sica_k_sensitivity_14b: DONE/success (SICA≤SC all K)
- exp-011-llama8b-v3: 应 DONE（需确认 conclusion + 录入 metrics）
- exp-017-strategyqa-v3: DONE/success (+3.3pp n.s.)
- exp-018-arc-v2: DONE/success (-1.67pp)
- exp-013/016/005/009: DONE
- pilot-constraint-filtering: DONE/negative
- pilot-contrastive-prompt: DONE/failed (conda bug，需 v2)
- exp-010-mistral: DONE/failed (pkill 自杀 bug，需 v3)

**用户最新指令**："再给你一次机会，按照最高ceiling来"——要求以最高质量标准推进，不惜资源。

### 4. 📋 待办（条件触发式）
- Agent 恢复 → 首先确认 exp-011 统计检验结果（McNemar p-value + bootstrap CI + 截断影响）
- p<0.1 且排除截断后 gap 持续 → **重大升级**：论文 story 变为"Operating Regime Characterization"，立即设计 LLaMA-8B 扩大验证（n=200+），更新 paper_framing.md
- p>0.1 或 gap 消失 → 回退 D025 analysis paper，LLaMA-8B 作为 suggestive evidence
- pilot-contrastive-prompt 需重跑（加 conda activate），排在统计检验之后
- exp-010-mistral-v3 需修复（pkill 分离后重提交），排在 contrastive pilot 之后
- contrastive pilot discriminative ratio >70% → 进入 full-scale Method C 验证
- 所有 cross-family + cross-domain 完成 → 更新 paper_framing.md + re-dream

### 5. 🎯 战略上下文
**决策链**：D025(pivot to analysis)→D026(exp-001 confirm)→D027(exp-013 C1)→D028/D029(K-ablation)→D030(pivot to methods paper，用户要求)→pilot negative→用户"按最高ceiling来"

**核心转折**：exp-011 LLaMA-8B 的 +6.7pp 可能重新定义项目。之前所有 Qwen-14B 数据说"SICA 无效"，但 LLaMA-8B 说"SICA 在弱模型上可能有效"。如果统计显著，最高 ceiling 的论文是：
> "Characterizing When Symbolic Consensus Helps: Operating Regime Analysis showing SICA benefits weak models (high diversity + detectable contradictions) but not strong models (no diversity)"

这比纯 analysis 或纯 methods 都更有深度——既有诊断（为什么 SICA 在强模型上失败）又有发现（SICA 在弱模型上有效的条件）。

**易错点**：
1. 不要因为 +6.7pp 就回退到"SICA 有效"的老叙事——D012 的 +3.3pp 就是这样被 exp-001 debunk 的。必须等统计检验。
2. 44 条 truncated traces (6.1%) 可能是 artifact 来源——如果 gap 主要来自 truncated 题，效应不真实。
3. exp-010 Mistral 的 pkill 自杀 bug：必须分两步（先 kill，确认死了，再启动），不要 compound command。
4. 用户态度："methods paper 会更受欢迎" + "按最高ceiling来"——不要保守，但也不要在未验证时就 overclaim。


---

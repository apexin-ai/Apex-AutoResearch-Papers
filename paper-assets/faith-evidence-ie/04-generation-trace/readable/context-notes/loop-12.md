# director / loop_12.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_12.md`
- **Structured JSON:** [`0789f9d597a989cbcb09.json`](../../sessions/07/0789f9d597a989cbcb09.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_messages
updated: '2026-05-22T18:10:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：rtx5090-4x cuda:0-3 **only**。用 `GPU=X` 环境变量（不是 CUDA_VISIBLE_DEVICES）
- 4B 模型路径异常：`/root/autodl-tmp/models/Qwen3-4B`（无 `Qwen/` 子目录），其他模型都在 `/root/autodl-tmp/models/Qwen/Qwen3-XXX`
- Evidence tax 符号约定：tax = ign_f1(no_evi) - ign_f1(with_evi)。正=代价，负=收益
- fair_tax 必须用 matched@2048 协议（both conditions @2048），旧 @1024 mismatched 数据已废弃
- 论文 ign_f1 和 rel_f1 是不同指标（之前 Reviewer 混淆过），对比时确认同一指标
- 4B RSFT 用 v2 retrained checkpoint（原 checkpoint 因服务器存储故障丢失，论文脚注已披露）
- "1.7B approaches 8B SFT"（p=0.65 不显著），禁止写 "surpasses" 或 "more accurate in mean"

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (connect.westd.seetacloud.com)，root 用户
- 工作目录：`/root/autodl-tmp/freige`（代码+论文）
- 论文 sections：`/root/autodl-tmp/freige/sections/`（abstract.tex, introduction.tex, experiments.tex, appendix.tex, conclusion.tex, analysis.tex）
- 模型路径：`/root/autodl-tmp/models/Qwen/Qwen3-{1.7B,8B,14B}`, `/root/autodl-tmp/models/Qwen3-4B`, `/root/autodl-tmp/models/meta-llama/Llama-3.1-8B-Instruct`
- SFT/RSFT outputs：`/root/autodl-tmp/sft_output_*`, `/root/autodl-tmp/rsft_output_*`
- 数据：`/root/autodl-tmp/data/docred`（DocRED），Re-DocRED 同目录
- bjb2-12179：备用服务器，当前 nvidia-smi permission denied，不可用

### 3. 📊 当前状态
**刚做完**：D147 evidence tax test 5/5 完成 + D148 LLaMA fair_tax 修正 + 论文叙事升级 P1-P7（Reviewer 通过）+ plan_010 NLI large 数据确认正确（+1.10pp）

**RUNNING 实验**（4/4 GPU 满载）：
| GPU | exp_id | 内容 | ETA (UTC) |
|-----|--------|------|-----------|
| cuda:0 | test_eval_14b_rsft_s42_no_evi | 14B RSFT no-evi test | ~17:30 |
| cuda:1 | plan017_14b_sft_s43 | 14B SFT s43 训练（2nd seed pipeline 第 1 步）| ~18:30 |
| cuda:2 | test_eval_1_7b_rsft_s42_no_evi | 1.7B RSFT no-evi test | ~22:00 |
| cuda:3 | test_eval_8b_rsft_s42_no_evi | 8B RSFT no-evi test | ~16:40 |

**已预授权级联**（Agent 自动执行，无需审批）：
- cuda:3 空出 → LLaMA RSFT no-evi test eval
- cuda:0 空出 → 4B RSFT no-evi test eval
- cuda:1 SFT s43 完成 → continue 14B RSFT s43 pipeline（generate → CED score → train → eval）

### 4. 📋 待办（条件触发式）
- 8B RSFT no-evi test 完成 → 收集 ign_f1，计算 RSFT test tax = no_evi - with_evi（with_evi=0.3353）
- 14B RSFT no-evi test 完成 → 同上（with_evi=0.3849）
- 5 模型 RSFT test tax 全部齐全（~22:00 UTC）→ Paper Agent patch appendix（新增 RSFT test evidence tax 行）→ 最终编译 → submit_paper_to_review
- 14B SFT s43 pipeline 全部完成（~24h）→ 收集 14B RSFT s43 ign_f1，对比 s42 的 0.5886，汇报 2-seed mean±std → rebuttal ammunition
- 所有 supplementary 完成 + paper 定稿后 → submit_paper_to_review 给 Review Director 做最终审

### 5. 🎯 战略上下文
- **论文当前状态**：Reviewer 评估"实验已完备，无 submission-blocking 缺口"。Dream v2 分数 best=3.0/median=2.5——叙事升级后可能改善，但尚未 re-dream
- **3 贡献**：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (GRPO catastrophic > DPO gradual > RSFT none) (3) Evidence tax landscape + variance compression (7.5-31×)
- **当前跑的都是 supplementary/rebuttal**——不阻塞投稿，但完善 RSFT test tax 表 + 14B 2nd seed 会增强论文
- **易错点**：SFT evidence tax 的 test 数据已全部完成并写入论文（appendix.tex），但 RSFT evidence tax 的 test 数据还在收集中——不要混淆两张表
- **易错点**：analysis.tex 的 NLI large +1.10pp 是 ign_f1 指标（不是 rel_f1），已确认正确
- **D148 教训**：fair_tax 文件必须交叉验证 metrics.json，之前 @1024 mismatched 导致 LLaMA tax 方向翻转
- **CodaLab 不需要**：Re-DocRED test labels public，本地 eval 即最终结果
- **用户期望**：用户希望"把实验价值体现出来，叙事升级"——P1-P7 已完成但用户可能有更高期望


---

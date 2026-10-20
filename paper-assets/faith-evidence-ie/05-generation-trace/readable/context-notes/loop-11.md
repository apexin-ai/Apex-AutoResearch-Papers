# director / loop_11.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_11.md`
- **Structured JSON:** [`bebf60981e6c98aa979f.json`](../../sessions/be/bebf60981e6c98aa979f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_messages
updated: '2026-05-21T23:16:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：rtx5090-4x 的 cuda:0/1/2/3（4× RTX PRO 6000）。bjb2-12179 也在配置中但当前所有实验跑在 rtx5090-4x
- M027 教训：所有 no-evidence eval 必须验证 adapter 路径指向正确的 SFT checkpoint + --no_evidence flag，不能用错 adapter（之前全部 Qwen no-evi 数据因 adapter 错误作废）
- M028 教训：任何训练任务必须走 [APPROVAL NEEDED] 流程，Agent 不得自行启动训练
- D147 约束：evidence tax threshold claim 仅限 observational（不做因果解释），cross-architecture variation 放 supplementary（不进 Abstract），evidence tax 标注为 dev-set finding
- matched@2048：所有 evidence tax 对比必须用 matched@2048 protocol（with-evi 和 no-evi 同 2048 token budget）

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x，工作目录 /root/autodl-tmp/faith-evidence-ie（推测，需确认）
- SFT 模型路径：/root/autodl-tmp/sft_output_seed42, sft_output_seed43, sft_output_seed44（1.7B/4B/8B），sft_output_14b/checkpoint-144（14B），sft_output_llama/（LLaMA-8B）
- RSFT 训练数据：rsft_train.jsonl（2718 CED k=1 samples，已存在）
- 4B RSFT checkpoint：❌ 丢失（bjb2 备份确认缺失），retrain_4b_rsft_ced_s42_v2 已审批
- Re-DocRED test set：500 docs，gold density 34.7 triples/doc（vs dev 12.3）
- 活跃进程：需 Agent 重启后 SSH 确认（Agent idle 16h，进程状态未知）

### 3. 📊 当前状态
**刚完成**：paper_framing.md M027 数据修正（12+ edits）、Paper Agent 11-item LaTeX patch、D147 Reviewer framing pre-review

**实验状态**（Agent idle 16h，以下为最后已知状态，需验证）：
- cuda:0: test_eval_1_7b_sft_s42 — 可能已完成（16h+ 前 RUNNING）
- cuda:1: test_eval_14b_sft_s42 — 可能已完成
- cuda:2: retrain_4b_rsft_ced_s42_v2 — ALLOCATED 但 Agent idle 未启动
- cuda:3: test_eval_llama_sft_s42 — 已完成（ign_f1=0.3420）；指令发了 14B no-evi test eval 但 Agent 未处理

**Test table 进展**：
| Scale | SFT test | RSFT test | Δ | SFT trunc% | RSFT trunc% |
|-------|----------|-----------|---|------------|-------------|
| 1.7B | pending confirm | 29.33 | — | — | 73.8% |
| 4B | 22.32 | ❌ retrain needed | — | 64.6% | — |
| 8B | 31.06 | 33.53 | +2.47 | 82.0% | 1.8% |
| 14B | pending confirm | 38.49 | — | — | 13.4% |
| LLaMA | 34.20 | 35.99 | +1.79 | 65.4% | 56.6% |

### 4. 📋 待办
- Agent 重启后 → 立即 SSH 检查 cuda:0/1/2/3 实际进程状态，确认哪些 test eval 已完成
- 1.7B/14B SFT test 已完成 → 收集结果，更新 test table
- retrain_4b_rsft_ced_s42_v2 未启动 → 重新指令 Agent 在 cuda:2 启动（已 ALLOCATED）
- retrain 完成（~66min）→ 提交 4B RSFT test eval
- 有空闲 GPU → 提交 D147 no-evi test spot-check：14B SFT no-evi test（最高优先），1.7B SFT no-evi test（次优先）
- 全部 SFT test 完成 → Paper Agent patch 更新 test table SFT 列
- 全部 test 完成 → CodaLab 提交获取 official ign_f1

### 5. 🎯 战略上下文
- 项目目标：EMNLP 2026 Main（ARR July，~55 天），empirical analysis paper 研究 RSFT 在 document-level IE 中的效果
- 核心 narrative（D145 后）：3 贡献 = C1 RSFT framework + C2 NLI quality scoring + C3 evidence tax landscape + variance compression
- C3 关键数据：within-family threshold（1.7B fair_tax=-5.63pp 受益，4B+ 趋零 mean=+0.25±0.47pp），cross-arch variation（Qwen 8B ~0 vs LLaMA 8B seed-dependent），RSFT variance compression 7.5-31×
- 8B truncation 对比（SFT 82% vs RSFT 1.8%）是强 paper 证据，支持 RSFT format robustness 叙事
- test vs dev gap ~20pp 是系统性的（gold density 差异），论文已有解释段落
- 易错点：adapter 路径命名不规范（sft_output_seed42 vs sft_output_qwen3_4b_bf16_s44 不存在），提交前必须 ssh_read_only 验证实际路径


---

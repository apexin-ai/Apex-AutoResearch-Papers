# reviewer / loop_18.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_18.md`
- **Structured JSON:** [`3f1c291f3540b1067c74.json`](../../sessions/3f/3f1c291f3540b1067c74.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: max_wall_time
updated: '2026-05-22T18:10:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3（rtx5090-4x 四张卡）。进程跑在白名单外 → 立即 critical 打回 + 要求 kill
- 论文 Ign-F1 vs Rel-F1 容易混淆：CED s42 Ign-F1=44.23, Rel-F1=45.17。D076 协议用 rel_f1，ablation table 用 Ign-F1。对比数字前必须确认指标口径
- Evidence tax 符号：tax = no-evi − with-evi，正值=代价，负值=收益。别搞反
- "more accurate in mean"（1.7B RSFT vs 8B SFT）p=0.65 非显著，论文已改为 "approaches"。如果有人再写 "surpasses" 立即 flag

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (root)，4× RTX PRO 6000 96GB
- 远程代码：/root/autodl-tmp/freige
- 远程数据：/root/autodl-tmp/data/docred（dev）、/root/autodl-tmp/data/re-docred-repo/data（test）
- 模型路径：/root/autodl-tmp/models/Qwen/Qwen3-{1.7B,4B,8B,14B}、/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B
- RSFT checkpoints：/root/autodl-tmp/rsft_output_ced_s42_v2（4B v2）、rsft_output_qwen3_{1_7b,8b}_k1、rsft_output_14b
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/
- 论文：docs/paper/main.tex → sections/{abstract,introduction,related_work,method,experiments,analysis,conclusion,limitations,appendix}.tex
- 活跃进程：plan017_14b_sft_s43 (PID 189766, cuda:1), test_eval_1_7b_rsft_s42_no_evi (PID 189480, cuda:2), test_eval_8b_rsft_s42_no_evi (cuda:3), test_eval_14b_rsft_s42_no_evi (cuda:0)

### 3. 📊 当前状态
**刚完成：**
- D147 evidence tax test 5/5 全量验证通过
- D148 LLaMA fair_tax matched@2048 修正验证通过
- Narrative upgrade P1-P7 全文审查通过（1 warning 已修）
- dev_eval_4b_rsft_ced_s42_v2：ign_f1=0.4388（vs 原 0.4517，差 1.29pp < 2pp 阈值 PASS）
- test_eval_4b_rsft_s42_v2_reeval：ign_f1=0.2501，与原 test 完全一致 ✅
- NLI large +1.10pp 数字确认正确（我之前误 flag 已撤回）
- 论文完整性评估：结论"实验已完备，无 submission-blocking 缺口"

**RUNNING（4 个）：**
1. test_eval_14b_rsft_s42_no_evi (cuda:0) — RSFT inference-time tax on test，配对 with-evi 0.3849
2. plan017_14b_sft_s43 (cuda:1) — 14B 2nd seed SFT 训练，rebuttal 弹药，~24h
3. test_eval_1_7b_rsft_s42_no_evi (cuda:2) — 1.7B RSFT no-evi test，配对 with-evi 0.2933
4. test_eval_8b_rsft_s42_no_evi (cuda:3) — 8B RSFT no-evi test，配对 with-evi 0.3353

### 4. 📋 待办（条件触发式）
- 8B RSFT no-evi test 完成 → 核对 ign_f1，计算 RSFT test tax = no-evi − 0.3353。Dev tax 是 -0.78pp，SFT 在 8B 有 dev-test 方向不一致（dev +0.04 vs test -1.71），看 RSFT 是否也有
- 14B RSFT no-evi test 完成 → 核对 ign_f1，计算 RSFT test tax = no-evi − 0.3849。Dev tax 是 -4.54pp（最大），这是最重要的验证点
- 1.7B RSFT no-evi test 完成 → 核对 ign_f1，计算 RSFT test tax = no-evi − 0.2933。Dev tax 是 -7.75pp
- 三个 no-evi test 全完成 → Agent 应 patch appendix 加 RSFT test evidence tax table。验证数字一致性
- plan017_14b_sft_s43 完成 → 后续有 RSFT gen + CED score + RSFT train + eval 全 pipeline（可能 24h+）。完成后验证 14B 2-seed std，看是否需要更新论文

### 5. 🎯 战略上下文
- 投稿目标：EMNLP 2026 Main (ARR July cycle, ~55 天)，时间充裕
- 3 贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Evidence tax landscape + variance compression
- D147 核心结论：within-family capacity threshold——1.7B evidence helps, ≥4B neutral。test 5/5 全部验证一致
- D148：LLaMA fair_tax 从 mismatched@1024 修正为 matched@2048，方向从不稳定→全部 negative
- 论文 4B RSFT 用 v2 retrained checkpoint（原 checkpoint 因服务器存储故障丢失），footnote 已披露
- 14B 是单 seed（plan017 正在补 s43），这是论文已知最弱点
- **易踩坑**：Ign-F1 和 Rel-F1 是两个不同指标，CED s42 分别是 44.23 和 45.17。Registry 的 ign_f1 字段对应 Ign-F1，f1 字段对应 Rel-F1。之前我就混淆过一次
- **易踩坑**：dev evidence tax 用 matched@2048 fair subset，test tax 用全量 500 docs。两者评估协议不同，小幅方向不一致（如 8B）是可接受的


---

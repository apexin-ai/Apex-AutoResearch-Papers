# reviewer / loop_20.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_20.md`
- **Structured JSON:** [`8e89a9fb1eec5c0b286c.json`](../../sessions/8e/8e89a9fb1eec5c0b286c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: max_wall_time
updated: '2026-05-19T12:06:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-39279 只有 **1 GPU (cuda:0)**。ROADMAP 曾错误写 2 GPU，已修正。所有实验串行。
- 训练数据必须用 `data/train_500_seed42.jsonl`（C001），禁止 `proofwriter_fol_train.jsonl`。D142-ext registry 的 data_path 字段填错了这个文件名（实际训练正确），注意不要被 registry 误导。
- Eval 必须显式指定 `--data_path data/proofwriter_fol_100.jsonl`（C008），禁止依赖默认值。
- D142 gated ISR 论文 claim 已从 "eliminates TS entirely (0/3)" 修正为 "suppresses TS in 5/6 seeds"。**不要回退到旧 claim**。s55 证明 exec reward alone 可驱动 TS。

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279(root)，1×RTX PRO 6000 Blackwell 96GB
- 代码根目录：`/root/solver-trace-ablation`
- Python：`/root/miniconda3/bin/python3`
- 模型路径：`/root/autodl-tmp/models/Qwen3-4B`（1.7B 同目录）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/`
- 论文：`{workspace}/paper/*.tex`
- D142-ext 输出：`/root/autodl-tmp/d142_gated_isr_s{52-57}/`（classify.json + eval_results.json 均在）
- GPU 当前**空闲**（0% util, 0 MiB）。D142-ext pipeline 已完成。无活跃训练进程。
- D143 ProofWriter 数据准备和 D144 LLaMA 下载状态未知——需 SSH 核实。

### 3. 📊 当前状态
**刚完成**：
- 验证 D142-ext 6-seed 数据（s55 TS=82% 发现 → 推翻旧 claim → 论文已修正）
- 验证 conclusion.tex + appendix §G.4 6-seed 更新的数据准确性：全部 PASS
- R14 审稿修复方案审查（5 条方案全部审核，数据准确性确认）
- ROADMAP GPU 数量错误发现 → 已修正

**Registry RUNNING/QUEUED**：
- d142-gated-isr-s55/s56/s57: registry 可能仍显示 RUNNING/QUEUED，但**实际已全部完成**（pipeline log: "ALL RUNS COMPLETE, failures: 0", 11:12 UTC）。需要 Agent 更新 registry。

**等待中**：
- D143 ProofWriter 9 experiments（cuda:0, ~18h serial）
- D144 LLaMA-3.2-3B 9 experiments（cuda:0, ~18h serial, after D143）
- 云 GPU 扩容申请结果

### 4. 📋 待办（条件触发式）
- D143 ProofWriter 任一 seed 完成 → 验证 classify.json 数据，检查 Goodhart collapse 是否跨数据集复现
- D144 LLaMA 任一 seed 完成 → 同上，检查跨模型复现
- D143/D144 全部完成 → 审查论文新增 Table 和跨维度分析段落的数据准确性
- 论文提交前 → 最终一致性审查：abstract/intro/experiments/conclusion/appendix 数字一致性 + 新增实验数据是否正确引用 registry
- 若 D143/D144 结果为 negative（无 collapse）→ **立即报 Director**，这会削弱而非增强论文，需要讨论是否纳入或降级 claim

### 5. 🎯 战略上下文
- **核心结论链**：D134 确立 TS deterministic attractor (5/5 ISR seeds, Fisher p=0.004) → D142 gated ISR 展示 whack-a-mole (block TS → PG emerges) → D142-ext 6-seed 修正为更 nuanced 的故事（5/6 suppress TS, 1/6 TS via exec reward, 3/6 PG migration）→ D143/D144 尝试跨数据集+跨模型泛化
- **R14 评分 3.0 (Findings)**，ceiling 来自单模型+单数据集。D143/D144 是突破 ceiling 的唯一路径。
- **最容易判错的事**：(1) s55 的 TS 是 gate 失败的证据——不是。Gate 正确阻断了 ISR bonus（gate_pass≈0），TS 通过 exec reward 维持。这证明 ISR bonus is sufficient but not necessary for TS。(2) Table 2 (tab:hacking-taxonomy) 混合了单 seed 和 pooled 数据，caption 有标注但 body 内不直观——审稿人 W-m2 已提过这个问题，至今未完全解决。(3) N-H (non-hacking) 始终是 upper bound——undiscovered modes 会降低真实率。s54 的 96.7% N-H 在 S-NH 下约 62%（35.2% content-independent）。
- **DDL**：May 25，D143+D144 串行需 ~36h GPU time → May 21 完成训练 → 2-3 天 paper integration + review cycles。可行但零容错。


---

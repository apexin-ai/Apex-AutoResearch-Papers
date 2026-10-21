# reviewer / loop_13.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`8bf909a7e6d4694911eb.json`](../../sessions/8b/8bf909a7e6d4694911eb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-16T20:38:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 仅 cuda:0/1/2/3（4× 5090 32GB）。rng_state 文件数 = GPU 数，用此验证 DDP 合规。
- 项目 greedy baseline 有两套：0.645（529 gold-filtered, 2-seed mean, Table 2 用）和 0.614（551 inst, seed=42, N-scaling 用）。验证数字时必须区分场景。
- AUROC 已从 cross-dataset 比较表移除（仅保留 ρ 和 Δ）。原因：三套脚本用三种不同 AUROC 定义（sample-level / instance-F1=1.0 / median），不可跨数据集比较。若 Agent 重新加回 AUROC 到 cross-dataset 表，立即 critical。
- exp-027 MLP verifier 用 N=16 数据训练，但论文写 N=8。此不一致已报 Director，尚未解决。验证论文数字时注意。

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090(root)，工作目录 `/root/autodl-tmp/struct_self_consist_ie`
- 代码：`/root/autodl-tmp/struct_self_consist_ie/code/`
- 输出：`/root/autodl-tmp/struct_self_consist_ie/output/`
- exp-021 checkpoint：`/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_full/checkpoint-6177/`（adapter 349MB）
- 分析脚本：`code/analyze_fewnerd_results.py`（Few-NERD）、`code/analyze_exp017_5signal.py`（SciERC）
- 本地论文：`projects/struct_self_consist_ie/docs/paper/sections/`
- 活跃进程：**无**（训练完成后 4 卡空闲，推理未启动）

### 3. 📊 当前状态
刚完成：
- exp-021 训练完成核实（PASS，3 epochs, eval_loss=0.0275）
- Appendix 结构审查（posted：2 个孤儿 section 需加引用 — app:lp_failure_stability, app:llama3b）
- Related Work 审查（posted：缺 Fomicheva 2020 TACL 基础引用）

等待中：
- exp-021 推理启动（GPU 空闲中，等 Agent/Director 下一步操作）
- exp-027 N=8 vs N=16 不一致的 Director 决策
- Related Work Fomicheva 引用的 Director 决策
- Appendix 孤儿引用修复

### 4. 📋 待办（条件触发式）
- exp-021 推理完成 → 核实 `analyze_fewnerd_results.py` 输出，检查 Few-NERD 三场景（A: selection works / B: QE works but selection fails / C: both fail），对照 paper_framing.md 验证 narrative
- exp-021 Few-NERD 结果写入论文 → 审查数字一致性 + cross-dataset 表是否仍无 AUROC
- Director 回复 exp-027 N=8/N=16 决策 → 确认论文相应修正
- 论文章节提交审查 → 按 5.1 维度 + 合规检查（Agent 是否看过 red-section skill）

### 5. 🎯 战略上下文
- 核心结论：**correlation-selection gap** — 信号能预测质量（ρ≤0.45, AUROC≤0.82）但无法在 N 个 candidate 中选出更好的，因为 instance degeneracy（21-58% 样本 F1 相同）消除了可选择的 headroom。
- Few-NERD 是最后一个跨数据集验证点。CoNLL 高退化（58%）、SciERC 中等（21%）、WNUT 信号崩溃。Few-NERD 的退化率将决定 paper 的 generalization claim 强度。
- 易错点：LP compression（median within-instance range = 0.041 nats）是 NER 特有的现象描述；RE 中 LP 反而是最强 selection signal（free-form decoding 下 +1.8pp）。不要把 NER 结论直接套用到 RE。
- 易错点：paper 用 macro F1 作标准指标。CoNLL 的 entity-level micro F1（~91%）和 macro F1 不同，验证时注意区分。
- Decision chain: D001 选定 structured IE + self-consistency → D002 确定 5 信号框架 → pivot 到 negative framing（selection fails）→ 当前 story 是"QE works, selection doesn't, degeneracy is why"。


---

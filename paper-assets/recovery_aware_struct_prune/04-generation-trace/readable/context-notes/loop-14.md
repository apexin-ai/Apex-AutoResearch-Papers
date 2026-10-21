# director / loop_14.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_14.md`
- **Structured JSON:** [`66c19e5d22832ef83161.json`](../../sessions/66/66c19e5d22832ef83161.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_messages
updated: '2026-05-19T08:59:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-29022 cuda:0-3, westb-23072 cuda:0-1（共 6 张）。C005 约束。
- westb 磁盘紧张（91%, 24GB free）。seed123 训练写 checkpoint 需 ~12GB，不要在 westb 上启动新的大模型下载或训练。
- Standard/RASP fair GRPO checkpoint 的真实路径是 `grpo_stage2_standard_20_fair/` 和 `grpo_stage2_rasp_20_fair/`（不是 `grpo_standard_20_fair`）。之前因路径错误导致 HumanEval eval 崩溃（M009 相关）。
- `eval_humaneval.py` 已修复（`sys.executable` 替代裸 `python`），但所有 tmux session 仍应确保 conda 激活。
- **SFT CKA-only HumanEval 0% 是 PATH bug 假结果（M009）**。v2 正在重跑。在 v2 结果出来前，D071 叙事中所有 "SFT CKA-only 0%" 的 claim 标记为 UNVERIFIED。不要在论文中使用未验证的 0%。
- Standard GRPO 100步 GSM8K 58.91% 是 phantom number（无结果 JSON，bootstrap CI 记录 "no n=1319 eval"）。正在 cuda:0 重跑验证。paper_framing.md 已标 ⚠️。

### 2. 🖥️ 基础设施快照
- **westd-29022**：4×GPU, 工作目录 `/root/autodl-tmp/recovery_aware_struct_prune/`, Python `/root/miniconda3/bin/python`
- **westb-23072**：2×GPU, 同路径, 磁盘 24GB/250GB (91%)
- 模型路径（westd）：`sft_cka_only_20/`, `sft_standard_20/`, `sft_rasp_20/`, `grpo_cka_only_20/`, `grpo_stage2_standard_20_fair/`, `grpo_stage2_rasp_20_fair/`, `grpo_cka_only_20_extended_300/`, `grpo_standard_20_extended_300/`
- 模型路径（westb）：`grpo_cka_only_20_seed123/`(训练中), `pruned_unstructured_20/`(可删)
- 代码：`/root/recovery_aware_struct_prune/src/` (eval_humaneval.py 已修复 sys.executable)
- W&B：project `recovery_aware_struct_prune`
- 活跃进程：
  - westd cuda:0: GSM8K Standard fair baseline eval（刚启动）
  - westd cuda:1: HumanEval SFT CKA-only v2（PATH 修复版重跑，**CRITICAL 等待结果**）
  - westd cuda:2: HumanEval GRPO Standard fair v3
  - westd cuda:3: HumanEval GRPO RASP fair (PID 74303)
  - westb cuda:0: 空闲（等 seed123 完成后跑 GSM8K eval）
  - westb cuda:1: grpo_cka_only_20_seed123 训练 (~29/100, ~7h remaining)

### 3. 📊 当前状态
本轮完成了大量 paper_framing.md 更新和实验收割：
- **E2 300步 complete**: CKA-only 64.37% = 100步, Standard 59.29% ≈ 100步。E2 叙事完全闭环。
- **Unstructured GRPO GSM8K**: 87.64%（vs pre-GRPO 87.87%），confirms collapse = structural damage
- **MATH-500 全表 complete**: CKA-only 29.0/29.2% >> Standard 25.8/26.4% >> RASP 22.6/24.0%. All GRPO-SFT |Δ| < 2pp.
- **HumanEval GRPO CKA-only final**: 20.12% (33/164)
- **D071 (C1 task-dependent reframing)**: 完成但部分 UNVERIFIED（SFT CKA-only 0% 待 v2 确认）
- **Reviewer 刚 RESET**（16h 达限），新 Reviewer session 需要 bootstrap

等待中：
- HumanEval SFT CKA-only v2（最高优先级，决定 D071 是否成立）
- HumanEval GRPO Standard fair v3 + RASP fair（决定 "CKA-only specific" claim 强度）
- GSM8K Standard fair baseline（验证 phantom 58.91%）
- seed123 GRPO 训练（~7h）

### 4. 📋 待办（条件触发式）
- **SFT CKA-only HumanEval v2 完成** → 如果 ~0%: D071 叙事验证，更新 paper_framing.md 为 ✅；如果 5-10%: D071 "extreme specialization" 叙事大幅弱化，需要降级 claim
- **GRPO Standard fair HumanEval 完成** → interim 5% 很低。如果 final <10%，CKA-only 20% vs Standard <10% 差距更大（利好）。如果 ~15%（接近 RASP），"CKA-only specific" 仍成立但弱化
- **GRPO RASP fair HumanEval 完成** → interim ~15%。与 CKA-only 20% 差距仅 ~5pp。综合 Standard/RASP fair 数据后固定 D071 最终 framing
- **GSM8K Standard fair baseline 完成** → 如果 ≈58-59%: 更新 paper_framing.md 替换 phantom 58.91%；如果差距大: 调查原因
- **所有 HumanEval 数据就位** → 派 Agent 做 output pattern analysis（SFT vs GRPO 对比 case study，3-5 个典型样本），然后通知 Paper Agent 做 patch
- **seed123 GRPO 完成** → westb cuda:0 跑 GSM8K eval，验证 CKA-only GRPO 可复现性
- **所有 P0 数据就位** → 派 Paper Agent 做 comprehensive patch（D071 reframing + unstructured + MATH-500 + HumanEval + stats），然后 submit_paper_to_review

### 5. 🎯 战略上下文
- **目标**: EMNLP 2026 Main (ARR May 25)，~5 天。
- **核心结论**: 结构化剪枝准则决定 GRPO recovery capacity。CKA-only（纯多样性保留）>> importance-based methods。Recovery capacity gradient: CKA-only >> Random >> Standard ≈ RASP。
- **决策链**: D058(fair v5 config) → D063(E2 extended) → D065(C1→supporting, C2+E3=dual core) → D067(unified C1 decoupling) → D069(C2 stats restructure) → D071(C1 task-dependent, **partially UNVERIFIED**)
- **最容易判断错的事**:
  1. **不要信 SFT CKA-only HumanEval 0%**——这是 PATH bug 假结果，v2 还在跑。D071 整个叙事悬而未决。
  2. **Standard GRPO 100步 58.91% 是 phantom number**——正在重跑验证。论文中引用前必须等 verified 数据。
  3. **checkpoint 路径是 `grpo_stage2_*_fair/`** 不是 `grpo_*_fair/`——已经因此崩溃过一次。
  4. **HumanEval GRPO Standard fair interim 5% 极低**——20 samples 方差大，不要在 final 出来前下结论。
  5. **paper_framing.md 是真源**——所有 claim/evidence/framing 的权威文件。每个实验完成后必须更新。Reviewer 会交叉核对。


---

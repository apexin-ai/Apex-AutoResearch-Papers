# reviewer / loop_19.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_19.md`
- **Structured JSON:** [`18813251a2df009d17e6.json`](../../sessions/18/18813251a2df009d17e6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_wall_time
updated: '2026-05-23T19:45:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C005：westb-23072 只能用 cuda:0/1，westd-32935 只能用 cuda:0/1/2/3。越界即 CRITICAL。
- eval_math500 必须使用 fixed 版本脚本（2026-05-23 22:53 更新的 eval_math500.py），不能用 eval_math500_buggy.py。所有 MATH-500 结果必须用同一脚本版本，否则不可比。
- grpo_random_20_retrain_v2 结果（max_completion_length=512）Director 已决定可用于论文，但必须在论文中披露 512 vs CKA-only/Standard 的 1024 差异。v3 已被 Director 取消。
- dose-response 实验（α=0.5,2.0,3.0,4.0）统一使用 max_completion_length=512（Director 决策，内部一致性）。
- beta 参数：20% GRPO "fair" 实验统一用 beta=0.01（默认），我之前关于 beta=0.04 的 warning 基于读错进程 cmdline，已撤回。

### 2. 🖥️ 基础设施快照
- **westb-23072** (root)：工作目录 `/root/recovery_aware_struct_prune`，模型存储 `/root/autodl-tmp/recovery_aware_struct_prune/`，conda base env `/root/miniconda3/bin/python`
- **westd-32935** (root)：同上路径结构，eval 脚本已同步 fixed 版本
- 关键模型路径（westb）：sft_cka_only_20, sft_random_20, grpo_cka_only_20/checkpoint-100, grpo_random_20_retrain/checkpoint-100
- 关键模型路径（westd）：grpo_stage2_standard_20_fair, sft_standard_20, sft_rasp_20_westd（注意 _westd 后缀）, sft_standard_25, grpo_stage2_rasp_20_fair
- wandb run IDs：grpo_random_20_retrain_v2 = 9c16hnf7, grpo_standard_25 = 16vqw4e6
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/`

### 3. 📊 当前状态
刚完成审查：grpo_random_20_retrain_v2（success, reward=0.2875）、grpo_standard_25_retrain_v2（OOM killed）、eval_math500_sft_cka_only_20_fixed_v2（27.4%）。

**RUNNING（5个）**：
- eval_math500_grpo_cka_only_20_fixed (westb:0) — GRPO CKA-only MATH-500，刚启动
- eval_math500_sft_random_20_fixed (westb:1) — SFT Random MATH-500，刚启动
- eval_math500_sft_standard_25_fixed (westd:0) — SFT Standard 25% MATH-500
- eval_math500_grpo_rasp_alpha1p0_20_fixed (westd:1) — ~60% done，预计还 2-3h
- eval_math500_grpo_standard_20_fixed (westd:2) — ~60% done
- eval_math500_sft_standard_20_fixed (westd:3) — ~57% done

**PREPARING 关键项**：
- grpo_rasp_alpha3p0_20_retrain — 等 GPU，用 512 (Director 决策)
- eval_math500_grpo_random_20_fixed — 依赖 grpo_random_20_retrain 完成（已完成，等 GPU）

**已完成的 MATH-500 fixed 结果**：
- SFT CKA-only 20%: 27.4%
- SFT RASP α=1.0 20%: 21.6%

### 4. 📋 待办（条件触发式）
- eval_math500_grpo_standard_20_fixed 完成 → 交叉验证 accuracy vs buggy 版本（26.4%），检查 reward-accuracy decoupling 在 MATH-500 上是否成立
- eval_math500_sft_standard_20_fixed 完成 → 与 SFT CKA-only（27.4%）对比，验证 diversity-preserving 优势
- eval_math500_grpo_rasp_alpha1p0_20_fixed 完成 → 与 SFT RASP（21.6%）对比，验证 GRPO vs SFT 差距
- eval_math500_grpo_cka_only_20_fixed 完成 → 关键数据点：GRPO CKA-only MATH-500，与 SFT CKA-only（27.4%）对比验证 decoupling
- 所有 MATH-500 fixed evals 完成 → 全表一致性审查：确认所有行用同一脚本版本
- grpo_standard_25 有新 v3 提交 → 检查是否解决了 OOM（需减 batch_size 或 num_generations）
- 任何新论文章节提交审查 → 加载 paper-quality-lessons skill，按模式 B 审查

### 5. 🎯 战略上下文
**核心论文叙事**：Recovery-Aware Structured Pruning (RASP)。两大 claims：
- C1 Reward-accuracy decoupling：diversity-preserving pruning 下 GRPO ≈ SFT accuracy（方法无关）
- C2 Recovery capacity spectrum：CKA-only(0.354) > Random(0.288) > Standard(0.081) >> RASP(0.010)

**易错点**：
1. grpo_cka_only_20 的模型权重只在 checkpoint-100/ 子目录，base dir 没有 model.safetensors。之前 verify eval 因此出现 64.06% vs 64.37% 差异。
2. sft_rasp_20 在 westd 上路径有 _westd 后缀（sft_rasp_20_westd），在 westb 上没有。跨服务器路径不一致。
3. paper_provenance.yaml 严重过时（所有 claim deprecated），不可依赖。
4. Abstract 的 "4.4×" = CKA-only/Standard（0.354/0.081），方法框架图右端应标 0.081 不是 0.061（此 bug 已报告，待修复）。
5. grpo_standard_25 两次都坍塌（v1 reward=0.0075, v2 reward=0.000625+OOM），这支持论文但没有 checkpoint 可做 MATH-500 eval。


---

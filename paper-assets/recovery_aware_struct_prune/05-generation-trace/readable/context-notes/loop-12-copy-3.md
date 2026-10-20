# reviewer / loop_12.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`7b583cecb9be0ca41762.json`](../../sessions/7b/7b583cecb9be0ca41762.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-17T07:18:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C004: westb-23072 cuda:0/1 + westd-11672 cuda:0/1/2/3（共 6 卡）。越界 → severity:critical + kill
- `run_scoring_ablation.sh` 内部 `export CUDA_VISIBLE_DEVICES=$GPU` 会覆盖外层设置。传参时直接 `bash script.sh 1`，不要外层再设 CUDA_VISIBLE_DEVICES
- westd 数据盘 `/root/autodl-tmp`，代码 `/root/recovery_aware_struct_prune`。westb 同结构
- `load_pruned_model` 不支持 non-uniform attention heads（只支持 non-uniform MLP）。已通过 `--skip_attention` 临时绕过，未根治

### 2. 🖥️ 基础设施快照
- **westb-23072** (root): Python `/root/miniconda3/bin/python`, conda base, 2×A800 96GB
  - 活跃进程: eval_unstructured_20 (PID 680604, tmux=eval_unstructured_20, cuda:1, N=1319, ~10min elapsed)
  - 活跃进程: scoring_ablation_batch_v2 (PID 681296, cuda:0, magnitude method Step 2/4 eval, 55/200 ~1.5h in, ~100s/it 极慢因共享 GPU)
  - 活跃进程: multiseed_serial (PID 682422, cuda:0 共享, RASP seed=123 评估中 152/200)
- **westd-11672** (root): 4×A800 96GB, 刚从宕机恢复（uptime ~1h18m）
  - cuda:0: eval_math500_unpruned (PID 3331, 17667 MiB)
  - cuda:1: eval_math500_sft_rasp_20 (PID 3335, 12967 MiB)
  - cuda:2: eval_math500_sft_standard_20 (PID 3333, 12967 MiB)
  - cuda:3: eval_humaneval_unpruned 已完成; 可能有新进程
- 模型路径: `/root/autodl-tmp/recovery_aware_struct_prune/` 下 sft_*/grpo_*/pruned_*
- 基础模型: `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`（两台服务器都有）

### 3. 📊 当前状态
**刚完成的关键结果:**
- eval_grpo_rasp_25: **acc=53.15%** (N=1319, stderr=1.37pp), pre-GRPO=52.99%, Δ=+0.16pp → **C1 在 25% sparsity 完美确认**
- eval_humaneval_unpruned: pass@1=1.83% (3/164) — 模型不擅长代码，HumanEval 无价值
- eval_humaneval_grpo_rasp_20: pass@1=10.37% (17/164) — 比 unpruned 高但绝对值太低

**RUNNING 实验:**
- scoring_ablation_batch_v2 (westb cuda:0): magnitude eval 55/200, ~100s/it 极慢（与 multiseed 共享 cuda:0），预计还需数小时。之后 gradient → random → cka_only 各含 prune+eval+SFT+eval
- multiseed_serial_westb (westb cuda:0): RASP seed=123 正在 152/200，后续还有 Standard seed=123 + RASP/Standard seed=456
- eval_unstructured_20 (westb cuda:1): N=1319 全量 eval，运行 ~11min
- eval_math500_unpruned/sft_rasp_20/sft_standard_20 (westd cuda:0/1/2): MATH-500 评估中

**已报告给 Director 但未收到回复的:**
- scoring_ablation load_pruned_model attention head bug (已临时 fix)
- westd 宕机 + multi-seed 需重试 (已在 westb serial 运行)
- --output_path 缺失 bug (westb serial 已修复)

### 4. 📋 待办（条件触发式）
- multiseed_serial 完成 → 核实 4 组结果 (seed 123/456 × RASP/Standard)，计算 CI，报告 Director
- scoring_ablation_batch_v2 magnitude eval 完成 → 核实 post-prune acc，监控 SFT 步骤内存/loss
- scoring_ablation gradient/random/cka_only → 检查是否也剪了 attention groups（理论上 --skip_attention 已生效，但验证）
- eval_unstructured_20 完成 → 读结果，对比 structured pruning (RASP 31% / Standard 27% post-prune)
- MATH-500 三个 eval 完成 → 核实 RASP vs Standard vs Unpruned，评估 C1 跨 benchmark 证据
- westd 再次失联 → 立即报 Director，检查 MATH-500 是否需重跑
- 任何实验使用非白名单 GPU → severity:critical 立即报告

### 5. 🎯 战略上下文
**项目核心:**
- C1 (primary): GRPO reward-accuracy decoupling 是 universal + cosmetic。**已在 2 模型 × 2 sparsity × 2 benchmark 全面确认**。所有 Δ < 0.5pp
- C2: Collapse severity gradient (RASP > Standard > Unpruned)。Unpruned 完全不 collapse (reward=0.66)，确认 collapse 是 pruning-specific
- C3: Recovery method conditions optimal pruning strategy (SFT vs RLVR)

**关键数据 @ 20% sparsity (N=1319):**
- Post-SFT: RASP 61.56% vs Standard 59.29% (Δ=+2.3pp)
- Post-GRPO: RASP ~61.87% vs Standard 58.91% (collapse 不影响 acc)
- Unpruned: SFT 81.27%, GRPO 81.27%

**易踩的坑:**
1. alpha ablation 结果: α=0.0 (=Standard) post-SFT 64% > α=1.0 post-SFT 57%（N=100 noise，但表面上 CKA weighting 伤了恢复）。N=1319 full eval 才是可信数据
2. westd 的 SFT 模型命名带 `_westd` 后缀（如 `sft_rasp_20_westd`），westb 不带。两者是独立训练的 reproductions，结果一致
3. scoring_ablation 极慢因为与 multiseed 共享 cuda:0 — 这是已知的，不是 bug
4. experiment_plan.yaml 的 registry_id 链接严重过期，compute_coverage_matrix 报 5.6% 是假的，实际覆盖率远高于此
5. HumanEval 对这个模型族无价值（unpruned 只有 1.83%），不要在上面花 GPU 时间


---

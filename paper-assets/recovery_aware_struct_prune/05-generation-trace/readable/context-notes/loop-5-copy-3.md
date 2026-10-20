# reviewer / loop_5.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`92c7ab22cce4f9664a3c.json`](../../sessions/92/92c7ab22cce4f9664a3c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-15T01:48:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 cuda:0 和 cuda:1（C001），越界立即 critical
- 所有模型/checkpoint/大文件只写 `/root/autodl-tmp/`（C002），根分区 30GB 禁止写大文件
- 服务器 westb-23072 用 conda base 环境（不是 venv）：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 存在两个易混淆脚本：`src/run_graspune.sh`（旧版，GRASPrune 工具）vs `src/run_grasp_prune.sh`（新版，GraSP baseline）——我曾因文件名混淆误报，注意区分

### 2. 🖥️ 基础设施快照
- 服务器：westb-23072 (root)，代码根 `/root/recovery_aware_struct_prune`
- Python：`/root/miniconda3/bin/python`，conda base
- 模型路径：`/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`（原始），剪枝/SFT/GRPO 产出均在 `/root/autodl-tmp/recovery_aware_struct_prune/` 或 `/root/autodl-tmp/pruned_*`
- HF cache：`/root/.cache/huggingface/`（GSM8K 已缓存，网络不通但有 local cache）
- W&B：project `recovery_aware_struct_prune`，用户 `xiaoyucorynne`
- 活跃进程：GRPO Stage 2 双卡并行
  - `grpo_stage2_rasp_20`：PID 263888, cuda:0, wandb run `ve3er9un`
  - `grpo_stage2_standard_20`：PID 263966, cuda:1, wandb run `mqu3sg7j`

### 3. 📊 当前状态
**GRPO Stage 2 是当前核心实验**，刚启动（09:14 UTC），500 steps，预计 7-10h。

Registry RUNNING：
- `grpo_stage2_rasp_20`：SFT-warmed RASP → GRPO RLVR recovery（cuda:0）
- `grpo_stage2_standard_20`：SFT-warmed Standard → GRPO RLVR recovery（cuda:1）

我最后提交了 Claim 3 叙事逻辑审查报告（severity: warning），等 Director 回复。

已完成的关键审查：
- 三个 worker 脚本产出（run_graspune.sh 修复、run_grpo_stage2.sh、run_sft_eval.sh）— 全部 PASS
- SFT 100 样本 eval 结果：**Standard 64% > RASP 57%**（critical 已报告，Director 判定不构成假设否定，GRPO Stage 2 是决定性实验）
- 自纠：之前误把 `run_graspune.sh` 的问题归到 `run_grasp_prune.sh`，已纠正

### 4. 📋 待办
- GRPO Stage 2 前 10-20 步出 log → 立即检查 reward/grad_norm/clipped_ratio，确认不是零梯度重演（之前 D009/D010/D013 反复出现此问题）
- GRPO 早期 reward 出现分化（RASP vs Standard）→ 报 Director，附 W&B run ID + 具体数据
- GRPO 出现 RASP ≈ Standard 或 Standard > RASP → **立即 critical**，触发 pivot 讨论
- GRPO 任一实验 reward_desert_patience 触发早停 → 报告并建议是否需要调参重跑
- Director 可能要求 full GSM8K (1319 samples) eval → 需等 GRPO 结束释放 GPU

### 5. 🎯 战略上下文
**决策链**：D005(降 sparsity 到 20%)→D006(RASP 29% vs Standard 1%)→D009/D010/D013(GRPO 反复失败，根因是 sampling 无 EOS)→D013(SFT warmup 修复 EOS)→D015(SFT Standard>RASP 不改方向，GRPO Stage 2 是决定性实验)

**最易判断错的事**：
1. SFT 结果 Standard 64% > RASP 57% **不等于假设被否定**。核心 claim 是关于 RLVR (GRPO) 恢复，不是 SFT。Director 已明确判定（D015）
2. Registry 中 sft_rasp_20 和 sft_standard_20 的 metrics **未更新为 100 样本结果**（仍是 3-5 样本旧数据）。真实数据在 `results/eval_sft_*_combined.json`
3. 之前所有 GRPO 尝试（grpo_*_fast, grpo_*_4096）都因零梯度失败。Stage 2 是 SFT-warmed 模型首次 GRPO——如果前 10 步仍然零梯度，问题可能更深层（train_grpo.py 本身？）
4. Claim 3 "排序反转"叙事在 SFT 那一行（57% vs 64%）p≈0.32 不显著。即使 GRPO 出正面结果，仍需 full eval + 多 seed 加固


---

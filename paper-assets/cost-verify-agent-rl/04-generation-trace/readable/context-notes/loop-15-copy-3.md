# reviewer / loop_15.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_15.md`
- **Structured JSON:** [`cbe4b582e20e09c15704.json`](../../sessions/cb/cbe4b582e20e09c15704.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_wall_time
updated: '2026-05-19T09:07:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单 C006**: bjb1-17606 只能用 cuda:0,1；westd-47453 可用 cuda:0,1,2,3
- **westd 根分区只有 30G**（overlay），已修复 TMPDIR/RAY_TMPDIR/TMUX_TMPDIR 指向 `/root/autodl-tmp/`，但磁盘仍然紧张。任何大文件（checkpoint、optimizer state）必须写数据盘 `/root/autodl-tmp/`（250G）。之前 4 次进程崩溃全因磁盘满。
- **optimizer_offload bug**: `optimizer_offload: true` 在 checkpoint resume 时会触发 device mismatch（cuda vs cpu）。hsweep_h10 用了 `resume_mode: disable` 绕过，但新实验如需 resume 要注意。
- **exp029_seed2 OOD eval 仍未完成**（3 次崩溃均因磁盘满），是论文必需数据点。

### 2. 🖥️ 基础设施快照
- **bjb1-17606**: `/root/cost-verify-agent-rl`，Python `/root/miniconda3/bin/python`
  - 活跃: hsweep_h20_seed1 (tmux=hsweep_h20_seed1, cuda:0,1, W&B qi8g4f86, step ~3-4/15, ~22min/step)
- **westd-47453**: `/root/cost-verify-agent-rl`，Python `/root/miniconda3/bin/python`
  - 活跃: 7b_cell_a_h2 (tmux=7b_cell_a_h2, PID 849089, cuda:0,1,2,3, W&B irxgmlm2, 刚启动 val_before_train)
  - ScienceWorld SFT 生成: PID 755742 (CPU only, 16/30 tasks done, ~1750 trajectories)
  - `.bashrc` 已设: TMPDIR/RAY_TMPDIR→`/root/autodl-tmp/tmp`, TMUX_TMPDIR→`/root/autodl-tmp/tmux`
- **模型路径**: 
  - 1.7B SFT: westd `/root/autodl-tmp/checkpoints/` 下各实验子目录
  - 8B SFT: westd `/root/autodl-tmp/qwen3_8b_sft_v1/checkpoint-231/` (7 safetensors, 完整)
  - 8B base: westd `/root/autodl-tmp/models/Qwen3-8B/`
- **W&B**: entity=xiaoyucorynne-, project=cost-verify-agent-rl

### 3. 📊 当前状态
**刚完成**: 审查 7B Cell A 训练启动（westd 全 4 GPU，W&B irxgmlm2），确认正常初始化。此前审查了 westd 崩溃根因（磁盘满）、7B zeroshot eval（0.75%）、8B SFT eval（80.6% OOD）、ScienceWorld 适配器代码、h=20 step 3 数据（train 40.6%）。

**Registry RUNNING**: 
- `hsweep_h20_seed1` — bjb1, step ~3-4/15, train success 20.3%→13.3%→40.6%
- `exp029_seed2_ood_reeval` — 状态标 RUNNING 但实际进程已死（3 次崩溃），需重启

**等待中**:
- h=20 step 5 val → cliff figure 最终数据点（预计 ~12:00-13:00 UTC）
- 7B Cell A step 1 train metrics → 确认 8B step-independent 是否也崩溃
- exp029_seed2 OOD eval 需第 4 次重启（现在 westd 全 4 GPU 被 7B Cell A 占用，需等其完成或用 bjb1）

### 4. 📋 待办（条件触发式）
- **h=20 step 5 val 出来** → 提取 val success，与 h=10 (6.25%) 对比，确定 cliff 精确位置，报告 Director
- **7B Cell A step 1-3 出来** → 检查是否 collapse（如 1.7B Cell A 那样）；若 8B SFT 80.6% baseline 下仍 collapse，这是强证据
- **7B Cell A 完成/崩溃** → 释放 westd 4 GPU → 立即重启 exp029_seed2 OOD eval（用 cuda:0,1，必须在 tmux 内）+ 启动 7B Cell C
- **ScienceWorld SFT 生成完成** → 检查数据质量和条数，评估是否足够做 SFT+RL
- **Director 问 plan_002 h=5 数据** → plan_002 notes 里 "h=5 DONE (28.1%)" 是错误标注，无 registry 条目；h=5 证据来自 γ-sweep（4 个 γ 全 collapsed）

### 5. 🎯 战略上下文
**核心论证**: step-independent windowing 导致 sign misattribution → RL 崩溃。3-cell factorial（A=collapse, B=ceiling 0.75%, C=works ~28-31%）+ γ-sweep 全坍缩 + h-sweep cliff + 52% per-sample sign agreement 实证。

**Cliff figure 数据**: h=2 ✗, h=5 ✗ (γ-sweep), h=10 ✗ (val=6.25%=baseline), h=20 ⏳ (train 40.6% 很强), h=full ✓ (28-31% val)。h=20 step 5 val 是最后一块拼图。

**8B 天花板陷阱**: SFT baseline 80.6%，RL 改进空间小。审稿人可能质疑"7B 上 RL 只提高了 5pp 有什么意义"。正确的 framing 是：step-independent 是否在高 baseline 下仍导致退化，而非 RL 能提升多少。

**易错点**:
- westd 磁盘会反复满，任何新进程启动前检查 `df -h / && df -h /root/autodl-tmp`
- exp029_seed2 OOD eval registry 标 RUNNING 但进程早已死，不要信 registry 状态
- plan_002 notes 中 h=5 数据有误，论文引用 h=5 结果时只能引 γ-sweep 数据


---

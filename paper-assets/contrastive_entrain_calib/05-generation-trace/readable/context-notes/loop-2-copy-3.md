# reviewer / loop_2.md

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`19ef4a15d3e6ced8aeed.json`](../../sessions/19/19ef4a15d3e6ced8aeed.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-21T07:52:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-29046 只能用 cuda:0, cuda:1；westd-28034 可用 cuda:0-3（项目白名单）
- 28034 今天已发生 **三次进程冲突**（多 worker 独立提交 eval 无互斥），提交 eval 前必须先 `nvidia-smi` 确认目标 GPU 空闲
- exp-003 seed1 日志 `exp003_v2.log` 在 step 3760 后停更（tee buffer 问题），**不能依赖日志判断训练状态**，必须看 checkpoint 时间戳
- 28034 上 checkpoint 有两种存储结构：`/root/autodl-tmp/checkpoints/exp003/` (seed1) 和 `/root/autodl-tmp/checkpoints/exp003_s2/` (seed2)，29046 上分别叫 `exp003_r3only_seed1` 和 `exp003_r3only_seed2`，名字不一致

### 2. 🖥️ 基础设施快照
- **westd-29046** (root): 训练服务器，2× RTX PRO 6000 (98GB)
  - 工作目录: `/root/contrastive_entrain_calib`
  - Python: `/root/miniconda3/bin/python`
  - 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`
  - seed1 checkpoints: `/root/autodl-tmp/checkpoints/exp003_r3only_seed1/` (500-7500)
  - seed2 checkpoints: `/root/autodl-tmp/checkpoints/exp003_r3only_seed2/` (500-3500)
  - 活跃: seed1 PID 70649 (cuda:1, tmux), seed2 PID 237437 (cuda:0)

- **westd-28034** (root): eval 服务器，4× RTX 5090 (32GB)
  - 工作目录: `/root/contrastive_entrain_calib`
  - Python: `/root/miniconda3/bin/python`
  - Eval 脚本: `eval/eval_unified_preset.py`
  - seed1 checkpoints: `/root/autodl-tmp/checkpoints/exp003/` (1000-7000)
  - seed2 checkpoints: `/root/autodl-tmp/checkpoints/exp003_s2/` (500-3000)
  - 结果目录: `results/exp003_d027_eval/` (seed1), `results/exp003_s2_unified_eval/` (seed2)
  - 活跃 eval: PID 497834 (ckpt5000-v2, GPU0), 498446 (ckpt6000, GPU1), 498584 (ckpt6500, GPU2), 500594 (ckpt7000-v2, GPU3，利用率 0% 需关注)

### 3. 📊 当前状态
**刚做完**: 审查了一系列 worker ops — SCP 传输修复、进程冲突清理、eval 重提交。Table 1 NoF 修复（0.945→0.961）已验证通过。Paper D045 narrative fix 已验证。

**RUNNING 实验**:
- exp-003 (seed1): ~step 7636/8000，ckpt-7500 已出，预计 ~18:30 CST 完成
- exp-003-s2 (seed2): step 3524/8000，预计 May 23 ~05:00 完成
- 4 个 eval 在 28034 并行跑（ckpt-5000-v2/6000/6500/7000-v2），预计 ~1.5h 完成

**已完成 eval**: seed1 ckpt-1000/2000/3000/4000/4500/5500; seed2 ckpt-500/1000/1500

**等待**: 4 个 eval 完成回调；seed1 ckpt-7500/8000 SCP+eval；seed2 ckpt-2000/2500/3000/3500 eval

**GPU 3 风险**: PID 500594 (ckpt7000-v2) 最后一次观察利用率 0%、VRAM 13GB，可能卡住，需要跟进

### 4. 📋 待办
- 4 个 eval 完成 → 交叉验证 SYCONScore 与已有 trajectory（0.074→0.085→0.095→0.114→0.134→0.114→...），ckpt-6000/6500/7000 应该延续 0.114 plateau
- GPU 3 ckpt7000-v2 仍 0% → 检查日志，可能需要 kill+restart
- seed1 完成 (ckpt-8000) → SCP 到 28034 + eval，这是最终 checkpoint
- seed2 ckpt-2000/2500/3000/3500 → 当 28034 GPU 空闲时提交 eval（已 SCP 到位）
- 任何 eval 结果异常（SYCONScore 偏离 trajectory 预期）→ 立即 [severity: warning] 报 Director
- Paper Agent 整合 mechanistic analysis → 可能触发新一轮写作审查

### 5. 🎯 战略上下文
**核心结论链**: d_syc AUROC 0.827 (Qwen) / 0.779 (Llama) → 但 d_syc-based GRPO 全部失败 → 三层解耦（representation stable + reward saturated + behavior regresses）→ vanilla ceiling（R3-only GRPO peak=vanilla 0.134 at ckpt-4500, regress to 0.114）→ SFT (ACT) 能突破 vanilla 但 GRPO 不行

**决策链**: D027 (unified eval) → D042 (三层区分) → D045 (vanilla ceiling narrative with ckpt-4500)

**易判错的事**:
1. exp-004 是 **SFT/ACT**（看 train_log.jsonl 有 sft_loss），不是 GRPO。之前有人反复混淆
2. ckpt-4500 SYCONScore=0.1337 ≈ vanilla 0.1335，是"match"不是"exceed"——论文用"transient recovery to vanilla ceiling"表述
3. R3 reward 饱和在 ~0.98（KS p=0.308/0.703），reward 信号本身没问题，是 GRPO 在 flat landscape 上 drift
4. 28034 没有 auto-pipeline cron，所有 eval 都是手动/agent 触发的，checkpoint 不会自动评估
5. seed2 还需要 ~38h 才完成，距 DDL May 25 有 buffer 但紧张


---

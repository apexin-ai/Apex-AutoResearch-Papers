# agent / loop_20.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_20.md`
- **Structured JSON:** [`5896061a6440e5d9fe5b.json`](../../sessions/58/5896061a6440e5d9fe5b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: max_wall_time
updated: '2026-05-17T10:58:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0 和 cuda:1（westd-39279 上分配给本项目的两张 RTX PRO 6000 96GB）
- 服务器 SSH alias 是 `westd-39279`，不是 `autodl-1`（后者不在 resources 列表，worker 会报错）
- 磁盘刚清理完（85G/250G），每个实验 checkpoint ~31G，最多同时存 4-5 个实验产出
- sweep-isr-b005-s42 是已完成实验（DONE/negative, 100% H7），不能重跑——Director 曾混淆 s42/s43
- Registry 状态机 DONE→RUNNING 需要链式转换：DONE→PREPARING→PENDING→QUEUED→ALLOCATED→RUNNING

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279，工作目录 /root/solver-trace-ablation
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 输出目录：/root/autodl-tmp/outputs/
- Eval archive：/root/autodl-tmp/eval_archive/（已备份的旧实验 eval JSON）
- 模型：Qwen/Qwen3-4B（HF cache，已下载）
- 数据：/root/solver-trace-ablation/data/train_500_seed42.jsonl (500 samples)
- Eval 数据：/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl (100 samples)
- 活跃进程：
  - sweep-isr-b005-s44: PID 281848, tmux=sweep-isr-b005-s44, cuda:0 — **已完成（DONE/negative）**
  - sweep-random-b005-s43: PID 246587, tmux=sweep-random-b005-s43, cuda:1 — **可能已完成或接近完成**
- Cron 注册：sweep-isr-b005-s43 (PID 246667), sweep-random-b005-s43 (PID 246587)
- Worker 可能还在跑：worker_ops_wave2-progress-check_20260517T103719（检查进度+eval）

### 3. 📊 当前状态
刚完成 sweep-isr-b005-s44 分析（86.9% H7, genuine=10.1%），已汇报 Director。β=0.05 ISR 三 seed 全部确认 H7 collapse（"no safe dose"）。

Registry RUNNING：
- sweep-random-b005-s43 (Random β=0.05 s43, cuda:1) — 应该接近完成或已完成

等待中：
- Worker progress-check 回调（可能带 sweep-random-b005-s43 eval 结果）
- Director 决策：cuda:0 下一步跑什么（1.7B exec-only s43 按 pipeline，或 random β=0.05 s44 做第三个 control）

### 4. 📋 待办
- progress-check worker 回调 → 读取 sweep-random-b005-s43 结果，更新 registry，汇报 Director
- sweep-random-b005-s43 完成 → eval + classify_h7 → 与 ISR β=0.05 对比（关键：s43 random 崩溃前 train PR=87.5%，可能非零！与 s42 的 0% 完全不同）
- Director 指定 cuda:0 下一实验 → 立即提交（如果是 1.7B，需确认 config 和模型是否就绪）
- cuda:1 空出后 → 按 pipeline 或 Director 指令填充
- 两实验都完成 → 更新 memory.md β=0.05 对比数据 + 汇报完整 dose-response 表

### 5. 🎯 战略上下文
- **核心发现**：Dose-response 非单调。β=0.05/0.2/0.3 = deterministic H7 collapse；β=0.1 = bimodal (stochastic bifurcation, 3/5 retain genuine)。β=0.1 是唯一有 genuine 窗口的剂量。
- **Paper framing (D120)**：Goodhart inevitable at all doses, β controls timing not destiny。D119 Critical Threshold 叙事。
- **DDL**：EMNLP 2026-05-25（剩 8 天）
- **易错点**：
  - Random β=0.1 s43 数据有两个版本：r2 (PR=88, H7=0) 和 **r3** (PR=94, H7=36)。论文用 r3。
  - Random β=0.05 s42 = 0% PR（完全失败），但 s43 崩溃前 train PR=87.5%——seed 间方差极大，最终 eval 结果很重要
  - ISR β=0.05 的 s42 之前被意外改为 PREPARING，实际已 DONE/negative
  - 磁盘容量紧张：每次跑完实验要关注是否需要清理旧 checkpoint


---

# director / loop_6.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`413a7f8ce214d975784e.json`](../../sessions/41/413a7f8ce214d975784e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-15T13:27:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-39279 的 cuda:0 和 cuda:1（gpu_constraint 白名单）
- plan002-additive 系列 conclusion 已修正为 negative（D078），不要再改回 success
- SFT 训练脚本 `train_sft.py` 的 `--gpu N` 会覆盖 CUDA_VISIBLE_DEVICES，必须用 `--gpu` 指定物理 GPU 编号，不能靠外部 export

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279 (connect.westd.seetacloud.com)，账号 root
- 工作目录：/root/solver-trace-ablation
- Python：conda base 环境（aml-train 镜像）
- 两张 GPU 均在跑实验，cron 自动监控

### 3. 📊 当前状态
刚完成的工作：
- kill 了 GPU 1 幽灵进程 PID 352975，r3 速度从 1.7s→0.8s/step
- 修正 plan002-b01-s42 registry：genuine_count→14, conclusion→negative（D078）
- SFT s42-1000 genuine=92.3%, s43-1000 genuine=90.9%（均 success）

RUNNING 实验：
- cuda:0: plan001-exec-only-s43-1000（exec-only GRPO, seed=43, 1000步，PID 356071，~90min）
- cuda:1: plan009-sft-baseline-s44-1000-r3（SFT, seed=44, 1000步，PID 353656，接近完成）

QUEUED：
- plan001-exec-only-s44-1000：等 cuda:1 空出后自动提交

### 4. 📋 待办
- s44-r3 完成 → eval genuine_count → 提交 exec-only-s44-1000 到 cuda:1
- exec-only-s43-1000 完成 → eval → 报告 genuine_count（预期 ~0%）
- exec-only-s44-1000 完成 → eval → 3-seed exec-only 1000步全部就位
- 3-seed SFT + 3-seed exec-only 都完成 → 向 Director 汇报 Goodhart collapse 统计结论（SFT ~91-92% vs GRPO ~0%）

### 5. 🎯 战略上下文
核心结论正在成型：**Goodhart collapse 是 GRPO 特有现象**——1000步时 GRPO 所有条件（exec-only/ISR/random）genuine→0%，SFT 维持 ~92%。当前在补多 seed 统计支撑。

1000步全景表（s42 完整）：exec-only 0%, ISR β=0.1 3%, random 0%, ISR β=0.3 0%, **SFT 92.3%**。

项目已进入审稿阶段（review_chat_id 已配置），Review Director 在 Group C 独立审稿。研究侧继续补实验加强证据链。

易错点：experiment_plan 中 P0/P1 已基本做完，新实验需要 Director 决策方向（是否扩更多 seed、扩更多 GRPO 条件的 1000步、还是进入写作）。


---

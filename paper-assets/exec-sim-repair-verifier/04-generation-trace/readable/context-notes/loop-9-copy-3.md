# reviewer / loop_9.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`140823158a2ffbe7b9af.json`](../../sessions/14/140823158a2ffbe7b9af.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-14T17:20:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd GPU 分配：cuda:0/1 = eval，cuda:2 = CWM 8B 训练，cuda:3 = CLS 8B s123 训练。**不要在已占用 GPU 上启动新进程**（今晚已因此 OOM 杀死 CLS 主训练一次）
- **kill 进程前必须 `ps -o ppid= -p &lt;PID>` 确认不是其他训练的 DataLoader 子进程**（今晚 Worker 误杀 DataLoader workers 导致两个 8B 训练同时崩溃）
- 多个 Worker 不得同时操作同一 GPU。今晚因 Worker 间无协调，GPU 3 上发生了 CLS 恢复进程 OOM + 杀死主训练的级联故障
- CLS ckpt-400/600（seed123 8B）已永久丢失（备份脚本晚启动 2.5h）。恢复需从 ckpt-200 resume 单独训练，但必须在独占 GPU 上做，不能与主训练共 GPU

### 2. 🖥️ 基础设施快照
- **westd** (seetacloud-westd-4x5090, root): 项目路径 `/home/sonny/exec-sim-repair-verifier`
  - conda: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
  - 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/` (8B), `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B` (4B)
  - 数据: `/home/sonny/exec-sim-repair-verifier/data/swebench_full/`
  - Checkpoints: `/root/autodl-tmp/checkpoints_repo_{cls,cwm}_8b_{seed123_,}conda/`
  - 备份: `/root/autodl-tmp/checkpoints_backup_{cls_8b_seed123,cwm_8b}/`
  - 活跃进程: PID 195531 (CWM eval seed123 GPU0), PID 195668 (CWM eval v12 GPU1), PID 245775 (CWM 8B train GPU2), PID 248041 (CLS 8B s123 train GPU3)
- **home** (home-1x5090, sonny): 项目路径同上
  - 活跃: 8B s42 ckpt-400 val@5120 eval (PID 3137889, GPU0)
- 无 W&B（`--no_wandb`）

### 3. 📊 当前状态
刚完成一轮密集审查：8B 训练崩溃根因（Worker 误杀 DataLoader 子进程）→ 多次重启失败 → 最终恢复 → val unparseable 根因定位（2 个 problem_id）→ 截断逻辑修复 → val-test inversion 最强证据（ckpt-800 val+4.5pp test-6.5pp）。

**westd 运行中：**
- CWM 4B eval seed123: 89%, acc=59.1%, ETA ~02:30 UTC May 15
- CWM 4B eval v12: 90%, acc=57.8%, ETA ~02:15 UTC May 15
- CWM 8B train: step ~1500/6633 (22.6%), ETA May 15 22:00-May 16 04:00
- CLS 8B s123 train: step ~2917/6633 (44%), ETA ~May 15 13:00 UTC

**home 运行中：**
- 8B s42 ckpt-400 val@5120: ~17% done, ~30min remaining; ckpt-3000 排队

### 4. 📋 待办
- CWM 4B eval 完成（~02:15-02:30 UTC）→ 独立验证最终 accuracy（seed123 ~59.1%, v12 ~57.8%），用 `analyze_cwm_eval.py` 和 `analyze_cwm_errors.py` 分析错误模式，注册结果到 registry
- CLS 8B s123 训练完成（~13:00 UTC）→ checkpoint sweep eval（注意 ckpt-400/600 丢失，只有 ckpt-200 + 1800-6633 range）
- CWM 8B 训练完成（~22:00 UTC+）→ checkpoint sweep eval
- 8B val@5120 eval 完成（home）→ 收集结果，对比 val@2048/4096
- CWM 4B eval 完成后 westd GPU 0/1 空闲 → 可用于 8B checkpoint sweep 或 CLS ckpt-200 恢复训练
- 截断逻辑修复后重跑 val eval → 验证 unparseable 是否降为 0

### 5. 🎯 战略上下文
- **核心 claim C1**: CLS > CWM。4B 数据：CLS ~80% vs CWM ~58%（差距 ~22pp，非常显著）。8B 结果待出。
- **D065/D066**: 弃用 val-based checkpoint selection，改用 mean±std across valid checkpoints。今晚证据：ckpt-800 val 最优但 test 最差（11pp 排名差），根因是 val pass rate 75.9% vs test 73.0% + 截断 artifact
- **D076/D077**: Val 20.2% unparseable 由 2 个 problem_id 的长 prompt 导致（100% = truncated）。已修复截断逻辑（截 code 不截 prompt）。westd 上 eval 脚本已改为 val 自动用 8192 seq_len
- **易错点**: (1) val 指标不可用于 checkpoint selection 但仍需报告，不要混淆 (2) CWM v10 的 ~70% accuracy 全靠 majority fallback（93% unparseable），真实分类能力接近零；v12/seed123 用了 max_new_tokens=1024 应该好很多 (3) 8B 训练用了 `--dataloader_num_workers 0` workaround，速度略慢但稳定


---

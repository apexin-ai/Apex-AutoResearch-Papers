# diagnose exp029 seed8

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp029_seed8_20260521T205756_result.json`
- **Structured JSON:** [`a0b237ba43885b4d1419.json`](../../sessions/a0/a0b237ba43885b4d1419.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 崩溃直接原因：磁盘满导致 checkpoint 写入失败

**不是 OOM，不是 response inflation。** 实际崩溃链：

1. `/root/autodl-tmp/` 分区（250GB）使用率超过 95%，Ray raylet 连续报警：可用空间从 6.4MB → 4.1MB → 0.6MB
2. 训练完成 step 9 的 validation（耗时 140.8s），进入 step 10 的 checkpoint 保存
3. `torch.save(optimizer_state_dict, ...)` 写入失败 → `RuntimeError: basic_ios::clear: iostream error`
4. 第二个 worker 同样失败 → `RuntimeError: [enforce fail at inline_container.cc:668] unexpected pos` (zip 文件损坏)
5. Ray task 异常退出，EXIT_CODE=1

崩溃点：`fsdp_checkpoint_manager.py:244` 的 `torch.save(optimizer_state_dict, optim_path)`

### GPU 状态

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 90467 MiB | 100% | **被其他进程占用** |
| 1 | 0 MiB | 0% | 空闲 |
| 2 | 0 MiB | 0% | 空闲（exp029_seed8 已释放） |
| 3 | 0 MiB | 0% | 空闲（exp029_seed8 已释放） |

cuda:2,3 已空闲可用。GPU 0 被另一个实验占用。

### 孤儿进程

有残留，**未 kill**：

- **PID 462990**: tmux session `exp029_seed8` — 外壳仍存活
- **PID 763475 的子进程树**: ~60+ 个 `ray::IDLE` worker + 1 个 `ray::TaskRunner.run`(PID 768713) + 1 个 `ray::WorkerDict`(PID 769407) + wandb 进程(PID 770156, 770189) — 这些在 04:50 启动，可能是 GPU 0 上另一个实验的 Ray 集群，也可能是 exp029_seed8 残留
- **PID 118779/118781**: checkpoint_watchdog（seed5/seed6 的清理脚本），持续运行中

### 磁盘现状

`/root/autodl-tmp/`: 208G/250G used (84%)，当前有 43G 可用 — 比崩溃时已恢复（崩溃时几乎 0 可用），可能是 Ray 临时文件被清理。

### 结论

根因是磁盘空间不足。checkpoint watchdog 只覆盖了 seed5/seed6，没有覆盖 seed8，导致 seed8 的 checkpoint 积累把磁盘写满。重跑前需要确认：(1) 清理旧 checkpoint 腾出空间 (2) 把 seed8 加入 watchdog 或手动清理策略 (3) 确认 GPU 0 上跑的是什么。

---

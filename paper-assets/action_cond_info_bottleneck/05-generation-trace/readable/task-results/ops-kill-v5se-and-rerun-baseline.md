# ops kill v5se and rerun baseline

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-v5se-and-rerun-baseline_20260516T021252_result.json`
- **Structured JSON:** [`562d7f543fa1f2306faf.json`](../../sessions/56/562d7f543fa1f2306faf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 执行结果

### 1. v5_stopgrad_entropy kill ✅
- PID 694348（wrapper）已 kill
- PID 694353（实际 GPU 训练进程，PPID=694352 已不存在）也已 kill
- GPU 1 释放 16256 MiB

### 2. baseline_plus libero_10 没有崩溃 ⚠️

**任务前提有误**，不需要诊断或重跑。

证据：
- PID **675231** 还在运行 `lerobot-eval --policy.path=lerobot/smolvla_libero_plus --env.task=libero_10 --output_dir=.../baseline_plus_v2/libero_10`，已跑 **49 分钟**，在 GPU 0（6601 MiB）
- main.log 中 **0 处** error/exception/traceback/oom
- 日志显示 libero_10 已构建 10 个 task 的 vec env（task_id=0~9），当前正在跑 task 0 的某个 episode，进度 295/520 steps（57%）
- libero_10 单 suite 包含 10 个 task × 50 episodes × 最长 520 steps，自然比其他 suite（300 steps）慢得多
- 已完成的 suite：libero_spatial ✅, libero_object ✅, libero_goal ✅（都有 eval_info.json）

**结论：不应该重跑** — 会覆盖现有进度。让它继续跑完即可。

### 3. baseline_std eval 进度
- PID 508625 还在跑（2h38m），当前 suite: libero_goal
- 已完成：libero_spatial ✅, libero_object ✅
- 剩余：libero_goal（进行中）, libero_10

### 4. GPU 当前状态
```
GPU 0: 22843/97887 MiB  | 682233 (v5_div_reg 训练 16214) + 675231 (baseline_plus libero_10 eval 6601)
GPU 1:  2120/97887 MiB  | 508625 (baseline_std libero_goal eval 2120)
```

GPU 1 现在几乎空闲，可以启动新任务。是否要在 GPU 1 上启动 v5_stopgrad_entropy 之外的其他训练，或者继续等待两个 eval 完成？

---

# eval per task t04 check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_per-task-t04-check_20260519T143626_result.json`
- **Structured JSON:** [`3d705e2e3127eb0d7af7.json`](../../sessions/3d/3d705e2e3127eb0d7af7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

**进程仍在运行**：PID 171794, elapsed ~20 min, GPU 0 使用中 (39.6GB, 29% util)

**详情**：
- 命令：`CUDA_VISIBLE_DEVICES=0,1 python eval_per_task_type.py 2>&1 | tee /root/autodl-tmp/tmp/exp029_per_task_t04.log`
- 脚本确认 `TEMPERATURE = 0.4`
- 结果将写入 `/root/autodl-tmp/tmp/exp029_per_task_type_breakdown_t04.json`（尚未生成）
- 日志仅有初始化信息（46行），eval 进度被 Python stdout 缓冲，未 flush 到文件
- 上次 T=0.0 run 134 episodes 大约耗时 30-40 分钟，预计还需 ~10-20 分钟完成

**之前的 run**（PID 154798）在 episode 23/134 时 vLLM EngineCore 崩溃（`Engine core proc EngineCore died unexpectedly`），当前 run 是重启后的。

**下一步**：等 ~15 分钟后再查，到时结果 JSON 应该已生成，可以读取 per-task breakdown 与 T=0.0 对比。

---

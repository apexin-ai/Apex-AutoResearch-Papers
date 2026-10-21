# diagnose retrain gemma2 d100 s0

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_retrain_gemma2_d100_s0_20260521T023007_result.json`
- **Structured JSON:** [`43417d19453aacbf65e5.json`](../../sessions/43/43417d19453aacbf65e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结果：训练已成功完成，这是监控误判。**

关键事实：
- 训练 4159/4159 步全部完成，exit code=0，耗时 ~4h7m
- Adapter 文件完整（216MB safetensors，lora_alpha=32 正确）
- 脚本自带验证输出 `SUCCESS: adapter verified`
- **失败原因**：`train_sft.py` 既没有 W&B 集成也没有写 sentinel 文件，监控系统 5 次检查都找不到活跃信号，自动标记为 failed
- GPU cuda:0 当前空闲，无残留进程

**建议操作**：将实验状态改为 completed，直接用该 checkpoint 进行下游 eval/signals 任务。

---

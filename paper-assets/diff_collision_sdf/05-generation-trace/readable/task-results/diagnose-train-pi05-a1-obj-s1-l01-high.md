# diagnose train pi05 a1 obj s1 l01 high

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_train_pi05_a1_obj_s1_l01_high_20260527T100106_result.json`
- **Structured JSON:** [`6bb6a8ae98e73db32edd.json`](../../sessions/6b/6bb6a8ae98e73db32edd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。**两个实验都没有失败，是监控系统误判。**

核心发现：

1. **训练 (seed1, λ=0.1)**: 已完成全部 30000 steps（耗时 ~34h），checkpoint 已保存到 `30000/`。最终 loss=0.0171。不需要 resume。

2. **评估 (seed0, λ=0.1)**: 已完成全部 4 个 tasks。**Avg TSR=47.0%, Avg CAR=58.0%**。结果已保存到 JSON 文件。

3. **根因**: 进程正常退出后 PID 消失，监控系统找不到 sentinel/W&B 信号，连续 5 次检测后误判为 failed。

4. **GPU 状态**: GPU 0/1 在跑新的 eval，GPU 3 在跑 LoRA baseline 训练，**GPU 2 完全空闲可用**。

报告已写入 `artifacts/diagnose_l01_failures.md`。

---

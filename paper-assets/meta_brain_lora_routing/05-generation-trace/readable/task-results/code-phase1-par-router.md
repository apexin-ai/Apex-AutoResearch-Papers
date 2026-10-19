# code phase1 par router

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase1-par-router_20260515T160424_result.json`
- **Structured JSON:** [`e5c15f3ed4c0b0c99507.json`](../../sessions/e5/e5c15f3ed4c0b0c99507.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。结果汇总：

**已创建文件：**
- `/root/meta_brain_lora_routing/phase1/train_par_router.py` — PAR Router 训练脚本
- `/root/meta_brain_lora_routing/phase1/par_router.py` — Router 推理模块

**Dry-run 验证（cuda:2）：**
- 数据加载：5 类扰动各 20 steps，共 100 samples（class 分布 60:20:20）
- 5-fold CV macro-F1：**0.9878 ± 0.0244**（4 折完美 1.0，1 折 0.939）
- Checkpoint 保存成功 → `checkpoints/phase1/par_router/best_router.pt`
- 训练曲线 + confusion matrix → `phase1/outputs/`
- Router 推理模块加载 checkpoint 并完成 forward pass，softmax 输出 sum=1.0

**sensor_noise 数据为空**，已自动跳过。

---

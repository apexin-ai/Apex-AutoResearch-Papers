# diagnose eval direct correction r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-direct-correction-r2_20260517T030028_result.json`
- **Structured JSON:** [`df95aa4e17eb7bfb1221.json`](../../sessions/df/df95aa4e17eb7bfb1221.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 根因：被外部 SIGTERM 杀死（非 OOM、非代码 bug）

**证据：**

1. **r2 run log** (`~/runs/.../eval-direct-correction-object-seed42-r2.log`):
   - 模型加载成功，正常开始评估
   - 在第 1 个 task 的 rollout 5/10 时收到 `Terminated` → `EXIT_CODE=143`
   - 终止时间：`2026-05-17T02:58:21Z`

2. **r1 run log** (`~/runs/.../eval-direct-correction-object-seed42.log`):
   - 同样正常加载和运行，完成了第 1 个 task（0/10 success）
   - 日志在此处截断，无 "Terminated" 字样 → 可能是 SIGKILL（无缓冲输出机会）
   - 无 exit file

3. **排除 OOM**：
   - SIGTERM (143) 不是 OOM killer 行为（OOM 发 SIGKILL → exit 137）
   - 该实验 GPU 显存仅 ~3.8GB / 24GB，远未满载
   - 同机其他 5 个 GPU 进程正常运行至今

4. **排除代码 bug**：评估代码本身运行正常，无异常/traceback

### 结论

**被实验管理系统或其他 agent 主动 kill 了。** GPU 4 现在完全空闲（2MiB），其他 GPU (0,1,2,3,5) 都在跑别的实验。两次 kill 行为一致，指向调度层面的冲突。

### 额外问题

`/root/acr-vla-conformal-refinement/logs/eval_direct_correction_object_seed42.log` 中内容是 `bash: line 1: python: command not found`——这是第三次尝试的结果（11:00 local），启动脚本未正确激活 conda 环境。

### 建议

1. **值得重试**——代码本身没有问题
2. 重试时确保：
   - 启动命令包含 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
   - 确认 GPU 4 没有被其他调度系统征用
   - 使用 agent-ml 的 tmux+trap 模式启动（与其他成功实验一致），而不是裸 python 调用

---

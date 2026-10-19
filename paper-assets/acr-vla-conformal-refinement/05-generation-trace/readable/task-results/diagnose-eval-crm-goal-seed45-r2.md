# diagnose eval crm goal seed45 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-crm-goal-seed45-r2_20260519T232457_result.json`
- **Structured JSON:** [`df31f293f192b5290e21.json`](../../sessions/df/df31f293f192b5290e21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

**结论：两个实验实际上已成功完成，监控系统误报。**

### 发现

1. **实验实际完成了**，结果文件在项目目录下：
   - `seed44-r2`: 64.0% overall success (64/100) → `/root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed44_r2.json`
   - `seed45-r2`: 65.0% overall success (65/100) → `/root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed45_r2.json`
   - 两个实验都完整跑完了 10 tasks × 10 rollouts，日志和 JSON 结果都齐全。

2. **误报原因**：这两个实验没有通过 `submit_training_job` 提交，而是直接用 `ssh_execute` 跑的 `python -u src/evaluate.py ...`。因此：
   - `~/runs/acr-vla-conformal-refinement/` 下无对应 log 文件
   - `/tmp/agent-ml-exit/` 下无 sentinel/exit 文件
   - 无 W&B run
   - 监控系统在这三个位置都找不到存活信号，判定为 "process dead 5× → failed"

3. **`--checkpoint` 参数无问题**：`--checkpoint` 和 `--crm_checkpoint` 是等价的（后者是前者的 alias，见 evaluate.py:320-322）。当前正在运行的 seed46/seed47 也用的 `--checkpoint`，正常工作。

4. **GPU 状态正常**：GPU 2 已空闲（seed45-r2 早已跑完退出），GPU 1/3 分别在跑 seed46 和 seed47。

### 建议
- **不需要修复**，结果已经存在，可以直接使用。
- 后续 CRM eval 实验统一用 `submit_training_job` 提交，避免监控系统误报。

---

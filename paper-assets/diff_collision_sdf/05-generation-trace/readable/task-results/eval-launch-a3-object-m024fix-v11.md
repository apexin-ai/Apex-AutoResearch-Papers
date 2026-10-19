# eval launch a3 object m024fix v11

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_launch_a3_object_m024fix_v11_20260522T165502_result.json`
- **Structured JSON:** [`c245d2885542bc6027e0.json`](../../sessions/c2/c245d2885542bc6027e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

1. **M024 修复验证**：已确认 `next_ee = current_ee + action[:3]` 在 eval_safelibero.py 中部署

2. **Eval 启动确认**：
   - PID: 780772
   - tmux session: `eval_a3_m024fix`
   - GPU 2: 已占用 8580 MiB
   - 日志正常，已加载 Task 0（pick up the orange juice and place it in the basket），safety level II

3. **日志前几行**：模型加载成功（a3_grad_refine_object_pudding），norm stats 正确加载（safelibero_object），已开始 eval 第一个 task

4. **Registry**: `eval_a3_object_m024fix_v11` → RUNNING，cron 监控已注册（120s 间隔）

注意：任务描述中的 CLI 参数有误（`--scene`/`--level`/`--checkpoint_dir`/`--ckpt_step`/`--output_path` 均不存在），已修正为脚本实际支持的参数（`--suite`/`--safety_level`/`--checkpoint`/`--output_prefix`/`--save_dir`）。

---

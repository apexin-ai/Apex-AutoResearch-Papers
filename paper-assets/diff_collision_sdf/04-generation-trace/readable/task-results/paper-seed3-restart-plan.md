# paper seed3 restart plan

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_seed3-restart-plan_20260529T150143_result.json`
- **Structured JSON:** [`42b75a82de77ad146673.json`](../../sessions/42/42b75a82de77ad146673.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已生成并注册: `artifacts/seed3_restart_plan.md` (art_20260529_0c2a0f)

核心要点:
- **westd-35807** (lora_baseline_s3_v2): v2 启动后跑了至少 8 steps，可能已跑完（预估 12.5h）。需上线后检查 checkpoint。LeRobot 4 处 patch 需验证
- **westd-45947** (a1_obj_s3_l01_v2): v1 确认保存 step 2000 checkpoint (11G)，v2 从此 resume 后断连。磁盘 250G 满，需清理 50-90G 再重跑
- 两台服务器恢复后第一步：更新 SSH 端口 → 检查 checkpoint → 清理磁盘 → tmux 启动训练

---

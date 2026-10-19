# ops fix restart pi05 baseline eval

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_restart_pi05_baseline_eval_20260526T044259_result.json`
- **Structured JSON:** [`8acc75ac841fc7b925fe.json`](../../sessions/8a/8acc75ac841fc7b925fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

1. **Symlink 修复**：两台服务器（westd-45947、westd-35807）均创建 `scripts/serve_policy.py` → `vlsa-aegis/scripts/serve_policy.py` symlink，import 验证通过
2. **额外修复**：首次重启发现 `./checkpoints/pi05_libero` 缺失，创建 symlink 指向 `/root/autodl-tmp/openpi_weights/pi05_libero`
3. **Eval 已重启**：PID 132718，westd-45947 cuda:1，tmux session `eval_pi05_baseline_reeval_disp`。模型加载中，无错误，无 ImportError
4. **Registry 已更新**：spec 更新为正确命令，notes 记录了 v1 kill 原因、两次 symlink 修复过程

---

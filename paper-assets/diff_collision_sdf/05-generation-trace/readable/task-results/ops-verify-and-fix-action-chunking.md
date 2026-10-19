# ops verify and fix action chunking

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_and_fix_action_chunking_20260522T105355_result.json`
- **Structured JSON:** [`5cb3d365c7242022e0b1.json`](../../sessions/5c/5cb3d365c7242022e0b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成。结果：

| 指标 | 值 |
|------|-----|
| TSR | 0.0% (0/3) |
| CAR | 66.7% (2/3) |
| Avg smoothness | 0.003058 |
| Avg max displacement | **0.0076m** |

**与 v10 对比**：v10 的 avg max displacement 是 0.048m，现在 v11（带 action chunking）降到 0.0076m，改善了约 6.3 倍。CAR 从 v10 数据也有改善。

**验证总结**：

1. **修复状态**：action chunking 确实完全丢失，已重新实现
2. **实施的 9 项修改**：
   - `PYTHONUNBUFFERED` 环境变量
   - `from collections import deque` + `from PIL import Image`
   - `--replan_steps` (default=5) + `--output_prefix` argparse 参数
   - `get_action_from_policy` 返回完整 action chunk（移除 `actions[0]`）
   - `deque` 缓存 + 每 replan_steps 步重新推理
   - 10 步 warm-up（gripper closed）
   - 图像 resize 224×224
   - 输出文件支持 output_prefix
   - 保存 config 包含 replan_steps
3. **额外修复**：baseline 的 norm_stats 加载——从 checkpoint assets 自动发现子目录（与 M022 同理）
4. **保留的修复**：M019（rotvec L579）和 M022（a3_norm_stats）均完好
5. **Dry-run 成功**：3 episodes 全部完成，displacement 显著下降
6. **cuda:0 未受影响**：训练仍在运行

---

# code fix critical bugs training

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_critical_bugs_training_20260519T182717_result.json`
- **Structured JSON:** [`2f786e5959f86d45343b.json`](../../sessions/2f/2f786e5959f86d45343b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**Bug 1 (train_baseline.py)**: 添加了 `openpi/` 根目录到 sys.path，`from scripts.train_pytorch import train_loop` 路径解析正确。完整 import 需要 `lerobot` 包（尚未安装）。

**Bug 2 (eval_safelibero.py)**: 原始描述的 OBSTACLE_NAMES 实际是正确的（MuJoCo body 命名验证通过，6/6 全部找到）。但发现了 3 个更严重的运行时 bug：
- `torch.load` weights_only 不兼容 PyTorch 2.6+（init_states 加载直接崩溃）
- `env._get_observations()` 方法不存在
- `env._check_success()` 应为 `env.check_success()`

另修复了 joint fallback typo (`_jnt0` → `_joint0`) 并添加了 0-obstacle 警告。

**Dry-run**: eval 环境加载、obstacle 检测、碰撞检测、success 判断全部验证通过。完整训练/评估 dry-run 无法执行（缺 lerobot + 训练数据）。

报告已写入 `/root/colliforce-vla/data/bugfix_report.txt`。

---

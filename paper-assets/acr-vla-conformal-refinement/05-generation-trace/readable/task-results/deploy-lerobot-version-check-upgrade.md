# deploy lerobot version check upgrade

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_lerobot-version-check-upgrade_20260521T105540_result.json`
- **Structured JSON:** [`c66d8eae4d920f168838.json`](../../sessions/c6/c66d8eae4d920f168838.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PyPI（清华镜像和官方源都查过）上 lerobot 最高只有 0.5.1，没有 0.5.2 版本。

### 报告
| 服务器 | 原始版本 | 升级后 |
|--------|---------|--------|
| bjb2-28827 | 0.5.1 | **失败** — PyPI 无 0.5.2 |
| bjb1-18228 | 0.5.1 | **失败** — PyPI 无 0.5.2 |

PyPI 现有 lerobot 版本：`0.1.0, 0.3.2, 0.3.3, 0.4.0, 0.4.1, 0.4.2, 0.4.3, 0.4.4, 0.5.0, 0.5.1`。

可能原因：
1. 0.5.2 尚未发布到 PyPI，vision_tower key 映射修复只在 GitHub main 分支
2. 版本号信息有误（也许是 0.5.1 之后的某个 commit）

请确认是否从 GitHub 源码装（如 `pip install git+https://github.com/huggingface/lerobot.git`，或指定 commit），还是核实正确的版本号？

---

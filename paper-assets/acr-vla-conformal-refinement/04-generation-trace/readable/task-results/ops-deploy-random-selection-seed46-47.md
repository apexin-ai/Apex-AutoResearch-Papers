# ops deploy random selection seed46 47

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-random-selection-seed46-47_20260519T013449_result.json`
- **Structured JSON:** [`79f71c6f7e6d17a7899e.json`](../../sessions/79/79f71c6f7e6d17a7899e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程存活，tmux session 正常运行。LIBERO 环境初始化需要几分钟。

**部署结果：**

| 项目 | 详情 |
|------|------|
| 服务器 | bjb2-40593 GPU 0 |
| Session | `eval-random-selection-seed46-t16` |
| 命令 | `--mode random_selection --benchmark object --n_rollouts 10 --seed 46 --K 10` |
| 输出 | `logs/eval_object_random_selection_seed46.json` |
| Timeout | 16h (57600s) |
| GPU 内存 | 5485/24564 MiB（与 eval-scalar-seed45-r2 共存） |

**说明：**
- bjb1-32546 代码版本旧，缺少 `random_selection` 模式且 GPU 3 已满
- bjb1-18228 四卡全满
- 最终部署在 bjb2-40593，需要显式设置 `HF_HOME=/root/autodl-tmp/.hf_cache`（首次启动因缺少该变量失败）
- 不需要 `--crm_checkpoint`，random_selection 只用 VLA 模型生成 K 个候选后随机选一个

---

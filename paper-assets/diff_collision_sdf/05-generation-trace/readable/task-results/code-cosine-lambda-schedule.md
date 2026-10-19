# code cosine lambda schedule

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cosine_lambda_schedule_20260525T094220_result.json`
- **Structured JSON:** [`571b44bfaa2f63d8f147.json`](../../sessions/57/571b44bfaa2f63d8f147.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**`--lambda_schedule` 参数已出现在 help 中**，支持 `constant`（默认）和 `cosine` 两个选项。

**cosine decay 功能正确**：
| step | constant | cosine |
|------|----------|--------|
| 0 | 0.005 | 0.005 |
| 10000 | 0.005 | 0.005 |
| 20000 | 0.005 | 0.0025 |
| 30000 | 0.005 | 0.0000 |

修改汇总：
- `import math` 新增
- `--lambda_schedule` 参数（`constant`/`cosine`）
- `SdfAuxHooks.get_lambda_sdf(global_step)` 方法实现 cosine decay
- `on_loss_computed` 中用动态 lambda 替代静态 `self.lambda_sdf`
- `aux_info` 新增 `lambda_sdf_current` 指标用于 wandb logging
- 顶部 docstring 补充说明

---

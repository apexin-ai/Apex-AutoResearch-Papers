# code lambda cli param

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lambda_cli_param_20260528T192037_result.json`
- **Structured JSON:** [`58342920d935444c8fd8.json`](../../sessions/58/58342920d935444c8fd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 汇报

| 项目 | 结果 |
|------|------|
| **修改前状态** | 已暴露为 draccus dataclass 字段（第 92 行：`occ_loss_weight: float = 0.01`） |
| **修改内容** | 无需修改 |
| **MD5 验证** | westd-34685 = `188d7f040bd2d4d65ae764ff26ac2db5`，westd-10894 = `188d7f040bd2d4d65ae764ff26ac2db5` ✓ 一致 |
| **westd-13654** | 该服务器不存在。可用服务器仅有 westd-10894 / westd-34685 / westd-19957 / bjb2-23165 |

**CLI 用法**：
```bash
torchrun ... vla-scripts/finetune.py --occ_loss_weight 0.001
```

λ₀ sweep 三组值直接传参即可：`--occ_loss_weight 0.001`、`--occ_loss_weight 0.01`（默认）、`--occ_loss_weight 0.1`。exponential decay 公式 `cfg.occ_loss_weight * exp(-batch_idx / cfg.occ_loss_decay_steps)` 会自动使用传入的值。

---

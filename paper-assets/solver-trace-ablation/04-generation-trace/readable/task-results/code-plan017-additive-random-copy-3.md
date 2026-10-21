# code plan017 additive random

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan017-additive-random_20260514T024850_result.json`
- **Structured JSON:** [`e2be723136b77d50ab99.json`](../../sessions/e2/e2be723136b77d50ab99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。验证结果：

| 检查项 | 状态 |
|--------|------|
| `additive_random` 在 argparse choices | ✓ |
| `_fast_fn` 调用残留 | ✓ 无残留（L161/164 仅为变量赋值，所有实际调用已改为 `_full_fn`） |
| 所有 config data_path = `data/train_500_seed42.jsonl` | ✓ 7/7 |
| `grpo_additive_random.yaml` 存在且正确 | ✓ |

修改内容：
1. **`_fast_fn` → `_full_fn`**（L174，`random_reward` 分支）— 现在所有模式统一用 full STA 计算 ISR
2. **5 个 config 文件** data_path 统一为 `data/train_500_seed42.jsonl`
3. `additive_random` 模式和对应 config 已在之前实现，无需额外修改

---

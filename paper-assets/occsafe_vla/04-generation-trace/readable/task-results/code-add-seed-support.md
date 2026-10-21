# code add seed support

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_add-seed-support_20260520T071245_result.json`
- **Structured JSON:** [`03a47c8b6aba150f2ea4.json`](../../sessions/03/03a47c8b6aba150f2ea4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`--help` 在 draccus 格式化时报错，这是预存问题，与我们的修改无关。核心验证已通过。

修改完成：

1. **FinetuneConfig** 第 99 行：添加了 `seed: int = 7`（在 `batch_size` 之后）
2. **finetune()** 第 818-819 行：添加了 `from prismatic.util.torch_utils import set_global_seed` 和 `set_global_seed(cfg.seed)`（在 print 之后、`get_run_id` 之前）

验证结果：`seed` 字段和 `set_global_seed` 调用均存在，默认值为 7。

---

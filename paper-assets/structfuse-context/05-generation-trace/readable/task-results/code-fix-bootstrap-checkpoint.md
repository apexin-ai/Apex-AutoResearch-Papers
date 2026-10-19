# code fix bootstrap checkpoint

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_bootstrap_checkpoint_20260515T150138_result.json`
- **Structured JSON:** [`41e95643b74a7abd5ce2.json`](../../sessions/41/41e95643b74a7abd5ce2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，dry-run 验证通过。

**修改内容** (`/root/structfuse/scripts/bootstrap_paired_test.py`)：

1. 新增 `_is_adapter_only(ckpt_dir)` — 通过文件大小 (<500MB) 或 `adapter_config.json` 存在检测 adapter-only checkpoint
2. 重写 `load_model` 的加载逻辑：
   - **Adapter-only** (如 embedding_distance_s43, 32MB)：`strict=False` 加载，验证无 unexpected keys，验证 missing keys 只是 backbone 权重（非 backbone 的 missing key 会 raise）
   - **Full-model** (如 random_s43, 5.9GB)：`strict=False` 加载，warning 提示异常
3. 加载时打印 checkpoint 类型和大小，方便排查

**Dry-run 验证**：
- adapter-only checkpoint (`embedding_distance_s43/best_by_recall_at_1`, 32MB) — 加载 149 adapter keys, 434 base-model keys 从 pretrained 获取，embedding shape [1,256], norm=1.0
- full-model checkpoint (`random_s43/best_by_recall_at_1`, 5918MB) — 583 keys 全部匹配，embedding shape [1,256], norm=1.0

---

# code checkpoint auto cleanup

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_checkpoint_auto_cleanup_20260518T071535_result.json`
- **Structured JSON:** [`73cdaec96c5d3a61f98b.json`](../../sessions/73/73cdaec96c5d3a61f98b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**Diff 摘要（相对 .bak）：**

1. **L28**: 添加 `import shutil`
2. **L277-283**: checkpoint 保存后插入清理逻辑：
```python
        # Auto-cleanup: keep gen_0 + last 2 checkpoints
        if gen >= 3:
            old_gen_dir = os.path.join(args.output_dir, f"gen_{gen - 2}")
            old_ckpt = os.path.join(old_gen_dir, "checkpoint")
            if os.path.isdir(old_ckpt):
                shutil.rmtree(old_ckpt)
                print(f"  Cleaned up old checkpoint: {old_ckpt}")
```

**语法验证**: `OK`

**保留策略验证**（10 gen 为例）：
- gen 0-2: 不触发清理
- gen 3: 删 gen_1/checkpoint
- gen 4: 删 gen_2/checkpoint
- ...
- gen 10: 删 gen_8/checkpoint
- **最终保留**: gen_0, gen_9, gen_10 的 checkpoint + 所有 gen 的 metrics.json 和 synthetic_data

注：diff 中还包含 .bak 之前已有的 `gradient_checkpointing` 和 `optim` 参数差异，这些是 .bak 备份时点之后的已有改动，不是本次引入的。

---

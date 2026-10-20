# ops add save total limit

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_add_save_total_limit_20260524T215342_result.json`
- **Structured JSON:** [`d616273926cae3494b1d.json`](../../sessions/d6/d616273926cae3494b1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器修改一致，验证通过。

### Diff

在 `save_training_checkpoint(...)` 调用后插入：

```python
                # Checkpoint rotation: keep only the latest 3 checkpoints
                if not cfg.save_latest_checkpoint_only and distributed_state.is_main_process:
                    import glob, shutil
                    all_chkpts = sorted(glob.glob(str(run_dir) + "--*_chkpt"), key=os.path.getmtime)
                    if len(all_chkpts) > 3:
                        for old_ckpt in all_chkpts[:-3]:
                            print(f"Removing old checkpoint: {old_ckpt}")
                            shutil.rmtree(old_ckpt)
```

### 逻辑说明

- 仅在 `save_latest_checkpoint_only=False`（多 checkpoint 模式）且 rank 0 时执行
- 按 mtime 排序所有 `*_chkpt` 目录，保留最新 3 个，删除其余
- 在 checkpoint 保存成功后才执行删除（先存后删）
- westd-34685: 第 1278 行 / westd-10894: 第 1280 行

---

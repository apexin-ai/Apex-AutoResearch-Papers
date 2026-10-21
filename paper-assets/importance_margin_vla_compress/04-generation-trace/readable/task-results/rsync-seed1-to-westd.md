# rsync seed1 to westd

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_rsync_seed1_to_westd_20260517T071126_result.json`
- **Structured JSON:** [`3142509537a530e64594.json`](../../sessions/31/3142509537a530e64594.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

第一个 rsync 已完成。`checkpoint.pt` 已就位：

- 文件大小：**1,319,625,623 bytes (~1.23GB)**
- 时间戳：May 17 12:30（源文件时间）

第二个 rsync 仍在跑但不影响，完成后会覆盖（内容相同）。

rsync 成功，checkpoint 已在 westd-27271 就绪：
```
/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_full_ft_seed1/step_099999/checkpoint.pt  (1.23GB)
```

---

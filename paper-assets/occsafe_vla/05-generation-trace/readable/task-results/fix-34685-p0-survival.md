# fix 34685 p0 survival

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_34685-p0-survival_20260527T211909_result.json`
- **Structured JSON:** [`f7a412c76cb1bb81a555.json`](../../sessions/f7/f7a412c76cb1bb81a555.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

```
清理前可用: 60G
清理后可用: 110G （释放 ~50G）
save_total_limit: 有 — 保留最近 3 个 checkpoint（line 1282-1287 的 rotation 逻辑，>3 时自动删旧的）
cuda:2 存活: ✓ (92% util, 62209 MiB)
cuda:3 存活: ✓ (43% util, 62203 MiB)
```

删除了：
- `detach_ln_v2_s2` 不完整 20000_chkpt (~7.5G)
- `vanilla_object_s0` 不完整 15000_chkpt (~7.5G)
- `full_occ_ln_v2_s3` 旧 10000_chkpt (~15G)
- `detach_ln_v2_s3` 旧 10000_chkpt (~15G)

110G 可用空间充裕，每个 checkpoint ~7.5G，加上代码已有 3-checkpoint rotation，不会再因磁盘满崩溃。

---

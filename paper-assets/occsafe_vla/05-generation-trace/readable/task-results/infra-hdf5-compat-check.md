# infra hdf5 compat check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_hdf5_compat_check_20260521T022309_result.json`
- **Structured JSON:** [`44551ca3237730c5039f.json`](../../sessions/44/44551ca3237730c5039f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

问题定位清楚了。汇报：

```
westd-10894: h5py=3.16.0, HDF5=2.0.0
westd-34685: h5py=3.16.0, HDF5=2.0.0
版本完全一致，不是版本问题。
```

**根因：westd-10894 上 4 个 HDF5 文件被截断/损坏。**

文件大小对比：

| 文件 (简称) | westd-10894 | westd-34685 | 状态 |
|---|---|---|---|
| `next_to_the_cookie_box` | 2,845,119 | 5,174,045 | **截断** |
| `next_to_the_ramekin` | 2,842,763 | 5,171,222 | **截断** |
| `on_the_ramekin` | 2,803,883 | 4,458,225 | **截断** |
| `on_the_stove` | 2,789,730 | 5,398,563 | **截断** |
| `between_plate_and_ramekin` | 4,132,936 | 4,132,936 | 一致 ✓ |
| `from_table_center` | 4,583,724 | 4,583,724 | 一致 ✓ |
| `in_top_drawer` | 6,030,363 | 6,030,363 | 一致 ✓ |
| `next_to_the_plate` | 4,584,519 | 4,584,519 | 一致 ✓ |
| `on_the_cookie_box` | 4,087,033 | 4,087,033 | 一致 ✓ |

验证：10894 上截断文件报 `bad object header version number`，相同大小的文件正常读取 `['data']`。34685 上全部文件正常。

**结论：文件损坏（生成时截断），不是 h5py 兼容性问题。**

**建议修复方案：** 从 westd-34685 scp 这 4 个损坏文件到 westd-10894，或在 10894 上重新生成。

---

# infra sync preload to 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_sync_preload_to_34685_20260520T121141_result.json`
- **Structured JSON:** [`0163c13f57aeebf68b49.json`](../../sessions/01/0163c13f57aeebf68b49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。同步结果：

| 文件 | 状态 | 验证 |
|------|------|------|
| `datasets.py` | 已同步 | `_occ_cache`(L47/93/225）、`_preload_occ_data`（L55/59）均存在 |
| `finetune.py` | 已同步 | `occ_detach: bool = False`（L94），默认值正确 |
| `evaluate_safelibero.py` | 已同步 | 文件头确认为 SafeLIBERO 评估脚本 |

（通过在 34685 上设置到 10894 的 SSH 密钥互信完成 SCP 传输。）

---

# ops disk cleanup westd34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-westd34685_20260521T190405_result.json`
- **Structured JSON:** [`e1df67423d7ec8696799.json`](../../sessions/e1/e1df67423d7ec8696799.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。汇总：

| 步骤 | 删除目录 | 释放空间 |
|------|---------|---------|
| Step 1 | `occ_s1/` | 90G |
| Step 2 | `vanilla_s0/`, `vanilla_s1/`, `vanilla_s2/` | 45G |
| Step 3 | `occ_s1_fresh/--2500_chkpt/`, `--5000_chkpt/` | 30G |
| **合计** | | **~165G** |

**最终磁盘状态**：350G 总量，113G 已用，238G 可用（33%），从 79% 降至 33%。

**剩余 checkpoints**：
- `occ_s0/` — 16G
- `occ_s1_fresh/` — 60G（保留 7500/10000/12500/15000 + latest）
- `occ_s2/` — 16G

**occ_s1_fresh 当前 step ~16074**，训练正常运行中，未中断。

---

# emergency disk full rescue

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_emergency_disk_full_rescue_20260516T131857_result.json`
- **Structured JSON:** [`6d3d8014f051b8cc8ec7.json`](../../sessions/6d/6d3d8014f051b8cc8ec7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| Step | 结果 |
|------|------|
| 1. checkpoints → 数据盘 | ✓ symlink 生效，exp_001 下次写 checkpoint 自动落到 `/root/autodl-tmp/` |
| 2. checkpoints_1b 清理 | ✓ 释放空间 + symlink 就绪 |
| 3. 根分区 | **100% → 84%**，5.1G 可用 |
| 4. exp_002 重启 | ✓ PID=25232，日志 `~/runs/spectral_collapse_ews/exp_002.log` |

---

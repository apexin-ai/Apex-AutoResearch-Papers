# ops westd27271 disk cleanup p0

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd27271-disk-cleanup-p0_20260520T183833_result.json`
- **Structured JSON:** [`f31c66b278930443a08a.json`](../../sessions/f3/f31c66b278930443a08a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

## 磁盘清理结果

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 235G (94%) | 192G (77%) |
| 可用 | 16G | **59G** |
| 释放 | — | **43G** |

**清理内容：**
- `openvla_sc_m128_seed42/`: 删除 3 个中间 checkpoint（~38.8G），保留最终 `checkpoint.pt`
- `baseline/`: 删除 5 个旧 step + latest 副本（~7.2G），保留 `step_029999`
- OFT 残留 JSON 已清除
- 7天以上旧日志已清除

**M32 训练存活：** PID 921279，已运行 7h53m，正常。

未达到 100G 目标。剩余大占用：HF cache datasets/lerobot 共 67G，但 M32 训练可能正在读取，不能在训练期间删除。`openvla_sc_m128/` (19G) 和 `openvla_sc_m32_seed42/` (38G) 分别只有 1 个 checkpoint 和活跃训练目录。59G 可用空间足够 M32 训练继续运行。

---

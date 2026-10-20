# code download libero long checkpoint

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_download_libero_long_checkpoint_20260521T004512_result.json`
- **Structured JSON:** [`28b78104d95ff3fe31f2.json`](../../sessions/28/28b78104d95ff3fe31f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件持续增长（136MB → 146MB），进程活跃。下载正在稳定进行（`du` 因为 sparse file 未刷盘显示的更新不够频繁，但 `stat` 可以确认文件大小在变）。

**状态总结：**
- PID 513449 后台下载 `moojink/openvla-7b-oft-finetuned-libero-10`
- 当前已下载约 563MB（含 .cache 中的 incomplete 文件）
- 下载速度 ~2MB/s，预计完成需约 2 小时
- 不占用 GPU，可与其他训练任务并行
- 日志文件：`/tmp/hf_download_libero10.log`
- 轮询检查命令：`du -sh /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10/` 和 `ps -p 513449 -o pid=`

---

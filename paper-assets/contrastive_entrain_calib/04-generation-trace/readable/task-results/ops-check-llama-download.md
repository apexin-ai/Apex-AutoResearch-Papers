# ops check llama download

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-llama-download_20260520T044223_result.json`
- **Structured JSON:** [`38474c3c611799445692.json`](../../sessions/38/38474c3c611799445692.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**下载状态：进行中，未完成。**

| 分片 | 大小 | 进度 | 预计剩余 |
|------|------|------|----------|
| model-00001-of-00004.safetensors | 4.63G | 13% (619M) | ~2h43m |
| model-00002-of-00004.safetensors | 4.66G | 13% (626M) | ~2h39m |
| model-00003-of-00004.safetensors | 4.58G | 14% (637M) | ~2h41m |
| model-00004-of-00004.safetensors | 1.09G | 55% (616M) | ~19m |

- **PID 214625** 运行中，已运行 20 分钟
- 下载速度 ~440-450 kB/s/stream，4 路并行总速度 ~1.76 MB/s
- 模型总大小 ~15 GB，预计还需 **~2h40m** 完成
- 磁盘空间充足：/root/autodl-tmp/ 剩余 296G
- 模型目录已创建，config/tokenizer 已下载完毕，safetensors 权重文件尚在下载中

**结论：** 不能现在启动 exp-012，需等约 2.5-3 小时下载完成后再验证模型加载。

---

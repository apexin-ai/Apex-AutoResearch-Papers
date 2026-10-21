# ops download progress check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_download-progress-check_20260518T144808_result.json`
- **Structured JSON:** [`3846cdcc6cc9e1c7cce0.json`](../../sessions/38/3846cdcc6cc9e1c7cce0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 模型 | safetensors 完成/总数 | 目录大小 | incomplete 文件 | 状态 |
|------|----------------------|---------|----------------|------|
| **Phi-4** | 3/6 | 22G | 3 (2.1G, 2.6G, 2.7G each ~4.7G target) | 正常下载中，log 显示 12/21 files 57%，ETA ~50 min |
| **OLMo-2** | 4/6 | 25G | 2 (2.2G active, 4.4G **停滞 2h** since 20:55) | 有 timeout 错误，ETA ~3h14m，4.4G 文件疑似卡住 |
| **Gemma-2-9B** | 6/8 | 33G | 2 (3.5G last mod 22:14, 4.0G active) | 有 timeout 错误，速度极慢 ~4500s/file |

**磁盘**: 123G/250G used, 128G 可用，空间充足。

**问题**:
- OLMo-2 的 model-00003-of-00006 (4.4G) 已 2 小时未更新，大概率卡在 xet timeout retry 循环
- Gemma 的 model-00004 (3.5G) 也 34 分钟未写入，可能同样卡住
- 两者都遇到 xet CDN timeout (`The read operation timed out`)

如需干预，可以 kill 卡住的进程并用 `--resume-download` 重启，或者加 `HF_HUB_DISABLE_XET=1`（已设置但可能未生效）。

---

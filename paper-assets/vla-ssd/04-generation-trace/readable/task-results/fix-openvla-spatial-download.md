# fix openvla spatial download

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_openvla_spatial_download_20260522T052447_result.json`
- **Structured JSON:** [`55653bb120697f5d673c.json`](../../sessions/55/55653bb120697f5d673c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载正在进行，让我算下速度和 ETA。

**诊断结果：**

| 项目 | 状态 |
|------|------|
| 主进程 PID 594575 | 运行中，已运行 ~4 小时 |
| 下载进程 PID 594477 | 运行中，有活跃 socket |
| network_turbo | 已激活（proxy 已设置） |
| 下载位置 | `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial/` |

**下载进度：**

| Shard | 大小 | 状态 |
|-------|------|------|
| model-00001-of-00004 | ~4.95 GB | **下载中**，已下载 4.74 GB（~95.7%） |
| model-00002-of-00004 | 4.95 GB | ✅ 完成 |
| model-00003-of-00004 | 4.95 GB | ✅ 完成 |
| model-00004-of-00004 | 251 MB | ✅ 完成 |

**速度测量：** 20 秒内下载了 10,485,760 bytes → **~512 KB/s**

**剩余：** ~198 MB → 预计 **6-7 分钟**完成

**问题根因：** 下载日志显示连接到 `cas-bridge.xethub.hf.co`（HF 的 xet CDN），尽管脚本设置了 `HF_HUB_DISABLE_XET=1`，但仍然走了 xet 通道，导致通过 AutoDL 代理访问时超时重试。

**结论：** 只剩最后 ~200 MB，当前速度下 6-7 分钟可完成，不值得干预。让它自然跑完即可。无需进一步操作。

---

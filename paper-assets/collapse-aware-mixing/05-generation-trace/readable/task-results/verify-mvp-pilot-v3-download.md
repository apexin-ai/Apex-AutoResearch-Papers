# verify mvp pilot v3 download

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_mvp_pilot_v3_download_20260512T124427_result.json`
- **Structured JSON:** [`98628e7827e06dde573c.json`](../../sessions/98/98628e7827e06dde573c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结论：下载卡死，锁被僵尸进程持有。**

## 状态汇报

| 项目 | 状态 |
|------|------|
| **进程存活** | PID 13466 (mvp_pilot_v3) 存活，CPU 1.6%，RSS 889MB |
| **缓存增长** | **未增长**。openwebtext 第4个 blob 0 字节，自 17:18 起未变（3.5+ 小时） |
| **磁盘空间** | 充足。数据盘 221G 可用，根分区 24G 可用 |
| **GPU** | 完全空闲 (0%, 3 MiB) |

## 根因

**PID 2371**（17:13 启动的测试下载命令 `load_dataset('openwebtext', split='train[:1000]')`）持有两把锁：
- `openwebtext/..._builder.lock`（fd5）
- blob download lock `437833e2...lock`（fd7）

该进程下载了 3 个 blob（共 ~870MB），但**第 4 个 blob 下载在 17:18 卡死**（0 字节，3.5 小时无变化）。进程本身 0% CPU，socket 连接可能已断开。

**mvp_pilot_v3 (PID 13466) 被这个锁阻塞**，无法开始加载数据集。

另外还有两个旧的 dryrun 进程（PID 6584、6793）也在运行，可能也在等同一把锁。

## 修复建议

需要 `ssh_execute` 执行：
1. `kill 2371` — 杀掉持锁的僵尸测试进程
2. `kill 6584 6793` — 杀掉旧 dryrun 进程释放资源
3. `rm /root/autodl-tmp/.hf_cache/hub/datasets--openwebtext/blobs/437833e29326c3d88792e834d36368d2c4836e5c5f3535233a88f3cf7dd46aad.incomplete` — 清理残留文件
4. mvp_pilot_v3 应该能自动获取锁并重新开始下载

是否执行修复？

---

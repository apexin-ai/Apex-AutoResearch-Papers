# infra libero assets download

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_libero-assets-download_20260515T140643_result.json`
- **Structured JSON:** [`3a84512de0f6cd3d7a41.json`](../../sessions/3a/3a84512de0f6cd3d7a41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载速度降至 ~200KB/s，ETA ~9小时。代理严重限速。

当前状态汇报：

**下载信息**
- 来源: `https://huggingface.co/datasets/Sylvest/LIBERO-plus` (assets.zip, 6.0GB)
- 方式: aria2c 16连接 + 代理 + 自动重试脚本
- 当前进度: 65MB/5.9GB (1%)
- 当前速度: ~200KB/s（代理限速后稳定值）
- 预计时间: 8-9 小时

**后台进程**
- 下载脚本 PID=135490（带自动重试，失败后自动恢复）
- 解压脚本 PID=135573（自动等待下载完成后解压到 `/root/LIBERO-plus/libero/libero/`）

**检查命令**
```bash
# 查看下载进度
du -h /root/autodl-tmp/libero_plus_assets/assets.zip
# 查看进程是否存活
ps -p 135490 -o pid,state,etime
# 查看解压进度（下载完成后）
tail -20 /tmp/post_download.log
```

**已有 assets 状态**
当前 `/root/LIBERO-plus/libero/libero/assets/` 目录已有 415MB 内容（scenes/lights/ 有 1024 个 XML 文件，textures/ 有 35 个 PNG），但远少于官方完整 6.4GB。下载完成后解压脚本会自动备份现有 assets 并替换为官方完整版本。

**替代方案（如果 8 小时太久）**
1. 在有更快网络的机器上先下载，再 scp 传过来
2. 如果暂时只需要 light scenes，当前的 1024 个 light XML 文件看起来内容完整（60 行的 mujoco XML 含正确的纹理/材质/灯光配置），可能可以先用

---

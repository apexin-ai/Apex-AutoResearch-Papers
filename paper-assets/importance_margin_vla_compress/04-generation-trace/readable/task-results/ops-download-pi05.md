# ops download pi05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_download_pi05_20260517T140308_result.json`
- **Structured JSON:** [`df29e82a2ca7cd012cd1.json`](../../sessions/df/df29e82a2ca7cd012cd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部下载完成。最终报告：

## 下载路径和大小

```
du -sh /root/autodl-tmp/pi05* /root/autodl-tmp/openpi-repo
7.0G    /root/autodl-tmp/pi05-libero-finetuned
14G     /root/autodl-tmp/pi05-libero-base
2.5M    /root/autodl-tmp/openpi-repo
```

## 最终磁盘状态

```
df -h /root/autodl-tmp
Filesystem      Size  Used Avail Use% Mounted on
/dev/md0        250G  209G   42G  84% /root/autodl-tmp
```

- `pi05-libero-finetuned`: 7.0G（model.safetensors 7.0GB，9 个文件，含 normalizer）
- `pi05-libero-base`: 14G（model.safetensors 13.5GB，3.62B float32 参数，7 个文件）
- `openpi-repo`: 2.5M（shallow clone，含 src/examples/scripts/docs 等）
- 剩余磁盘空间：42GB

注意：`pi05-libero-base` 和 `pi05-libero-finetuned` 各有 `.cache` 目录包含下载缓存，如需回收磁盘可删除 `.cache` 子目录。

---

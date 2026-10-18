# download w1 models

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_download_w1_models_20260515T061043_result.json`
- **Structured JSON:** [`e9b259e051709353b3b1.json`](../../sessions/e9/e9b259e051709353b3b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载仍在进行。状态无变化。我停止轮询。

**当前下载进度总结：**
- **Falcon-7B**: ModelScope 下载中，~15%（~2GB/13.5GB），预计还需 ~1.5-2 小时
- **Qwen2.5-14B**: ModelScope 下载中，~71%（~20GB/28GB），预计还需 ~1-1.5 小时
- **Phi-3-medium**: 磁盘不够，**跳过**

**下载完成后需要做的：**
1. 清理 `/root/autodl-tmp/models/falcon-7b/`（不完整的旧文件），创建符号链接指向 ModelScope 缓存
2. 创建 `/root/autodl-tmp/models/Qwen2.5-14B/` 符号链接
3. 验证两个模型的 config.json + safetensors 文件

**检查命令（你可以自己跑）：**
```bash
# 查看是否完成
grep "DONE" /tmp/dl_falcon_ms.log /tmp/dl_qwen14b.log

# 查看进度
tail -1 /tmp/dl_falcon_ms.log
tail -1 /tmp/dl_qwen14b.log
```

需要我继续监控还是你稍后再让我处理完成后的步骤？

---

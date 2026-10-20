# ops westd model download

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-model-download_20260518T062758_result.json`
- **Structured JSON:** [`e2cdd11e3dae5301a8cf.json`](../../sessions/e2/e2cdd11e3dae5301a8cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载正常进行中。4 个 safetensors 分片正在并行下载（190MB + 270MB + 70MB + 180MB = ~710MB 已写入），通过 hf-mirror.com 下载。

**状态汇报：**

| 项目 | 状态 |
|------|------|
| **磁盘** | `/root/autodl-tmp` 250GB 可用，充足 |
| **screen session** | `2216.model_dl` 运行中 |
| **7B 下载** | 4 个 safetensors 分片并行下载中，已写入 ~1.5GB（含小文件） |
| **14B 下载** | 排队中（7B 完成后自动开始） |
| **下载源** | hf-mirror.com（中国镜像） |
| **预计完成** | 7B (~14GB) 约 10-15 分钟，14B (~28GB) 约 20-30 分钟，总计 ~30-45 分钟 |

查进度可用：
```
tail -5 /root/autodl-tmp/models/dl_7b.log
du -sh /root/autodl-tmp/models/Qwen2.5-7B/
```

完成标志：`/root/autodl-tmp/models/DOWNLOAD_DONE.txt` 存在。

---

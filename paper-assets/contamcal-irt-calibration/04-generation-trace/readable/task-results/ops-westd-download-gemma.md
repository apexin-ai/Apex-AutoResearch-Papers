# ops westd download gemma

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-download-gemma_20260518T070704_result.json`
- **Structured JSON:** [`8b09ebf6e89995902090.json`](../../sessions/8b/8b09ebf6e89995902090.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有下载都在进行中。Gemma 有 8 个 incomplete 文件（对应 8 个 safetensors 分片）。

当前状态汇总：

| 模型 | 已下载 | 预计总量 | .incomplete 文件 | 状态 |
|------|--------|----------|-----------------|------|
| **Gemma-2-9B** | ~750M | ~18GB | 8 | 下载中 (screen dl_gemma) |
| Qwen2.5-7B | 9.7G | ~15G | 4 | 下载中 (download_all.sh) |
| Qwen2.5-14B | 9.8G | ~28G | 8 | 下载中 (download_all.sh) |
| Mistral-7B-v0.3 | 3.8G | ~14G | 4 | 下载中 (download_all.sh) |
| Llama-3.1-8B | 68K | ~15G | 0 | 未开始/排队 |

**Gemma-2-9B 下载已成功启动**，在 `screen -r dl_gemma` 中运行。需要的关键修复：必须设置 `HF_ENDPOINT=https://hf-mirror.com` 和 `HF_HUB_DISABLE_XET=1`（该服务器在国内，无法直接访问 huggingface.co）。

磁盘空间充足（226G 可用）。当前下载速度 ~5-10 MB/s（4 个模型共享带宽），Gemma 预计 ~30-40 分钟完成。

验证完成可用：
```bash
# SSH 到 westd-29999 后
grep GEMMA_DONE /tmp/dl_gemma.log
ls /root/autodl-tmp/models/gemma-2-9b/*.safetensors | wc -l  # 应为 8
du -sh /root/autodl-tmp/models/gemma-2-9b/  # 应为 ~17-18GB
```

---

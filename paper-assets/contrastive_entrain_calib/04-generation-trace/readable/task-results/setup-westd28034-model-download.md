# setup westd28034 model download

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_westd28034_model_download_20260518T132211_result.json`
- **Structured JSON:** [`0991d348745c98f48fb5.json`](../../sessions/09/0991d348745c98f48fb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载进度总结：
- **已下载**：主分片 2.9GB（model-00005-of-00005.safetensors），共 5 个大分片
- **速率**：约 2-3MB/s（AutoDL 网络加速代理下）
- **状态**：偶发超时但 huggingface_hub 自动重试恢复
- **进程**：PID 2756 正在运行
- **预计总时间**：~60-90 分钟（从开始算起）

下载在后台稳定运行。你可以先做其他事，我随时可以帮你检查进度。用以下命令查看：
```bash
# 在 westd-28034 上执行：
ls -lh /root/autodl-tmp/.hf_cache/models--Qwen--Qwen3-8B/blobs/*.incomplete | grep -v " 0 "
ls /root/autodl-tmp/.hf_cache/models--Qwen--Qwen3-8B/blobs/ | grep -cv incomplete
tail -5 /tmp/model_download.log
ps -p 2756 -o pid= && echo "RUNNING" || echo "DONE"
```

下载完成后模型路径为：`/root/autodl-tmp/.hf_cache/models--Qwen--Qwen3-8B/snapshots/&lt;hash>/`

---

# infra download qwen3 8b

**error type pref optim** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_download-qwen3-8b_20260514T094718_result.json`
- **Structured JSON:** [`a4ef51018d702ff3d01f.json`](../../sessions/a4/a4ef51018d702ff3d01f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载速度大幅下降到 ~300KB/s，但进程稳定运行中（nohup 后台）。当前进度摘要：

| 文件 | 大小 | 已下载 | 进度 |
|------|------|--------|------|
| model-00001 | 3.72G | 1.1G | 29% |
| model-00002 | 3.72G | 2.1G | 56% |
| model-00003 | 3.69G | 2.4G | 65% |
| model-00004 | 2.97G | 922M | 30% |
| model-00005 | 1.16G | 1.1G | 95% |

总进度约 48%（~7.6G/16G）。当前速度下还需约 2-3 小时完成。

进程 PID 80423 在后台运行，会自动完成。可用以下命令随时检查：
- 进度：`tail -5 /tmp/hf_download.log`
- 进程状态：`ps -p 80423 -o pid=`
- 完成标志：日志中出现 `DOWNLOAD_COMPLETE`

完成后需要执行验证：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python -c "from transformers import AutoTokenizer; tok = AutoTokenizer.from_pretrained('/root/error_type_pref_optim/models/Qwen3-8B'); print(f'Vocab size: {tok.vocab_size}'); print('Qwen3-8B download OK')"
```

模型实际存储路径：`/root/autodl-tmp/models/Qwen3-8B/`，通过符号链接挂载到 `/root/error_type_pref_optim/models/Qwen3-8B`。

---

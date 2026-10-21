# diag lg extract failed

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_lg_extract_failed_20260515T165541_result.json`
- **Structured JSON:** [`33ecbe4a73920e5158a5.json`](../../sessions/33/33ecbe4a73920e5158a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结论

### 失败根因

`extract_features.py:80` 的 `AutoProcessor.from_pretrained(model_path, trust_remote_code=True)` 尝试连接 `huggingface.co` 下载/验证文件，AutoDL 实例无外网访问。

关键错误链：
```
ConnectionError → huggingface.co:443 Network is unreachable
→ LocalEntryNotFoundError (HF cache 中也找不到)
→ 进程崩溃
```

HF 请求的 URL 分别是：
- trained: `https://huggingface.co/openvla-7b/resolve/main/config.json`
- untrained: `https://huggingface.co/openvla-7b-untrained/resolve/main/config.json`

这说明 `--model_path` 传的是 HF repo ID（`openvla-7b` / `openvla-7b-untrained`），而非本地绝对路径。HF 库先尝试网络（失败），再找本地 cache（也没有匹配条目），最终崩溃。

### 本地资源状态：完整，无需下载

| 资源 | 状态 |
|------|------|
| `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/` | 完整（config.json + 3 shards + processor + tokenizer + custom code） |
| `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained/` | 完整（config.json + 4 shards + 全部文件） |
| LIBERO-Goal 数据（10 个 HDF5） | 完整 |

### 修复方案

将 `--model_path` 改为本地绝对路径，并设置离线环境变量：

```bash
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1

# trained
python scripts/extract_features.py \
  --model_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b \
  --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ \
  --mode trained ...

# untrained
python scripts/extract_features.py \
  --model_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained \
  --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ \
  --mode untrained ...
```

修复后可直接重试，不需要下载任何资源。

---

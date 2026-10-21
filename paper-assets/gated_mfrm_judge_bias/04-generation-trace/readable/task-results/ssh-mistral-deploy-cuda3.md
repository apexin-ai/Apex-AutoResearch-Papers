# ssh mistral deploy cuda3

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mistral_deploy_cuda3_20260524T044939_result.json`
- **Structured JSON:** [`54a922af388eb6974c7f.json`](../../sessions/54/54a922af388eb6974c7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

2 个分片完成（4.6G 每个），第 3 个正在下载。进度稳定。

下载正在后台稳定运行，预计还需约 50 分钟（12 个分片 * 4 分钟/分片）。

**当前状态汇总：**

| 步骤 | 状态 |
|------|------|
| **Step 1: 磁盘清理** | 完成。释放 28G (212G → 184G)，可用 67G |
| **Step 2: 下载 Mistral-Large-2-AWQ** | 进行中 (PID 534407)。2/14 分片完成 (~12G/60.5G)，速度 ~13 MB/s，预计 ~50 分钟 |
| **Step 5: Config** | 已创建 `config_mistral-large-2_local_n17.yaml` |
| **Step 3-4, 6: vLLM + collect.py** | 等下载完成 |

下载使用 `aria2c` 16 连接从 `hf-mirror.com` 下载。脚本支持断点续传，失败自动重试。

**监控命令：**
```bash
du -sh /root/autodl-tmp/models/Mistral-Large-Instruct-2407-AWQ/
cat /tmp/download_mistral_v3.log | strings | grep -E "SKIP|OK|FAIL|Downloading" | tail -10
ps -p 534407 -o pid,etime
```

下载完成后需要执行 Step 3 (vLLM 部署) → Step 4 (健康检查) → Step 6 (collect.py)。是否需要我继续轮询等待下载完成并执行后续步骤？

---

# infra setup qwen7b folio cuda2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_setup-qwen7b-folio-cuda2_20260522T234615_result.json`
- **Structured JSON:** [`8bf6ab3d839573ad3fba.json`](../../sessions/8b/8bf6ab3d839573ad3fba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**Qwen2.5-7B-Instruct 不在磁盘上，需要下载。**

磁盘上现有 Qwen 模型：Qwen2.5-14B-Instruct、Qwen2.5-72B-Instruct-AWQ，无 7B。

cuda:2 状态：完全空闲（0 MiB, 0%）。

### 下载信息

- **模型大小估计**：~15 GB（7B 参数，bf16 权重）
- **目标路径**：`/root/autodl-tmp/models/Qwen2.5-7B-Instruct`
- **推荐下载命令**（AutoDL 优先用 ModelScope）：

```bash
source /etc/network_turbo
pip install modelscope
python -c "from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/models/Qwen2.5-7B-Instruct')"
```

或 HuggingFace（AutoDL 上较慢）：
```bash
source /etc/network_turbo
export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_DISABLE_XET=1
huggingface-cli download Qwen/Qwen2.5-7B-Instruct --local-dir /root/autodl-tmp/models/Qwen2.5-7B-Instruct
```

### 其他发现

- `run_cross_dataset_replication.py` 位于项目根目录（不在 scripts/ 下），且是给 ProofWriter/LogiQA 用的，不适用于 FOLIO
- 已有现成脚本 `scripts/multiseed_qwen25_7b_folio_cuda3.sh`，使用 `run_full_mvp.py`，参数完整可复用（改 CUDA_VISIBLE_DEVICES=2 和端口即可）

**下载完成后可继续后续步骤。**

---

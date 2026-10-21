# code prepare unpruned grpo westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-unpruned-grpo-westb_20260515T172540_result.json`
- **Structured JSON:** [`02a6aadf530b66ca83fe.json`](../../sessions/02/02a6aadf530b66ca83fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Base model 状态
**不在 westb。** HF cache 只有 4KB 的 refs 指针（commit `916b56a...`），无实际模型文件。

westd-11672 上有完整的 `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/` (15GB)。

### 传输方案
westb → westd **不能直接 SSH**（hostname 无法解析，AutoDL 实例间无内网互通）。

**推荐方案：westb 上直接用 ModelScope 下载**（AutoDL 国内 CDN 快）：
```bash
source /etc/network_turbo
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python -c "from modelscope import snapshot_download; snapshot_download('deepseek-ai/DeepSeek-R1-Distill-Qwen-7B', cache_dir='/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B')"
```
预估 5-15 分钟（取决于 ModelScope CDN 速度）。下载后需确认路径结构（ModelScope 可能加子目录）。

### 脚本状态
- `run_grpo_unpruned.sh` 已创建于 `/root/recovery_aware_struct_prune/run_grpo_unpruned.sh`
- 参数与 v8 **完全一致**（从运行中的 v8 进程确认：beta=0.01, lr=1e-6, dapo, save_total_limit=3 等）
- model_path 指向 `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`
- `train_grpo_v5.py` 和 `model_utils.py` 都在 `/root/recovery_aware_struct_prune/src/`

### 磁盘
`/root/autodl-tmp/`: **88GB 空闲**（250G 用了 163G）。15GB 模型 + 训练输出绰绰有余。

### 阻塞项
**唯一阻塞：需要下载 base model 到 westb。** 脚本、代码、磁盘都就绪。Kill v8 释放 cuda:0 后，下载完模型即可执行 `bash /root/recovery_aware_struct_prune/run_grpo_unpruned.sh`。

---

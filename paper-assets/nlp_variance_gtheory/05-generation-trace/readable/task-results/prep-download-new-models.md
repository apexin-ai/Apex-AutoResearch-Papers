# prep download new models

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_download_new_models_20260521T095956_result.json`
- **Structured JSON:** [`76e170712fe4e29699a1.json`](../../sessions/76/76e170712fe4e29699a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 当前状态汇报

### 已完成
- **model_paths.py** 已更新（本地 + 服务器），添加了 3 个新模型的路径映射和 display names
- **vLLM 0.9.2 兼容性确认**：
  - `trust_remote_code=True` 已配置
  - `enforce_eager=True` 已配置
  - 3 个模型均应兼容（Yi-1.5 基于 Llama 架构，OLMo-2 标准 transformer，Phi-3.5 需 trust_remote_code）
- **OLMo repo 名修正**：正确名称是 `allenai/OLMo-2-1124-7B-Instruct`（非 `OLMo-2-7B-1124-Instruct`）

### 下载进行中（后台 nohup）

| 模型 | 来源 | 本地路径 | 进度 | 速度 |
|------|------|---------|------|------|
| Yi-1.5-9B-Chat | ModelScope `01ai/Yi-1.5-9B-Chat` | `.hf_cache/01ai/Yi-1___5-9B-Chat` | shard 2/4, 5% | ~500KB/s |
| OLMo-2-7B-Instruct | ModelScope `allenai/OLMo-2-1124-7B-Instruct` | `.hf_cache/allenai/OLMo-2-1124-7B-Instruct` | shard 2/3, 1% | ~475KB/s |
| Phi-3.5-mini | ModelScope `LLM-Research/Phi-3.5-mini-instruct` | `.hf_cache/LLM-Research/Phi-3___5-mini-instruct` | shard 2/2, 9% | ~470KB/s |

预计完成时间（按当前速度）：
- **Phi-3.5**: ~1-1.5h（最小，~7.5GB，只剩最后一个 shard）
- **Yi-1.5**: ~2-3h（~18GB，4 shard 并行下载）
- **OLMo-2**: ~3h+（~14GB，3 shard）

### 待下载完成后
- 验证每个模型 config 可解析
- 确认磁盘空间

### 轮询命令
```bash
tail -2 /tmp/download_yi.log
tail -2 /tmp/download_olmo.log
tail -2 /tmp/download_phi.log
```

下载都在后台运行，不影响 GPU 上的 exp-002。需要我继续轮询直到完成，还是你稍后自行检查？

---

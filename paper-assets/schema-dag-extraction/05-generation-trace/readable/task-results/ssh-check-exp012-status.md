# ssh check exp012 status

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-exp012-status_20260515T164226_result.json`
- **Structured JSON:** [`0b89358b8554a84ae456.json`](../../sessions/0b/0b89358b8554a84ae456.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### 1. exp012_llama_fewnerd_r4 — 已崩溃

- **原始 PID 294443 已死亡**
- 日志 `exp012_llama_8b.log` 显示 **vLLM 启动失败**：GPU 显存不足（仅 7.01GB / 94.97GB 可用），无法分配 85.48GB
- 错误：`ValueError: Free memory on device cuda:0 (7.01/94.97 GiB) on startup is less than desired GPU memory utilization (0.9, 85.48 GiB)`
- **根因**：另一个 vLLM 进程（PID 297093，`VLLM::EngineCore`）占用了 89.5GB 显存，已运行 4 分 38 秒，导致 exp012 启动时没有足够显存

### 2. 已生成的结果文件

`artifacts/exp012/` 目录有产出（应该是之前成功的 run）：
- `predictions_fewnerd_exp1_llama-3.1-8b-instruct.json` (46.8MB)
- `eval_fewnerd_exp1_llama-3.1-8b-instruct.json` (80KB)
- `batch_config` 文件 × 3（含 70b-fp8 和 8b 的配置）
- `artifacts/exp012_dryrun/` 有 dry run 结果

### 3. 磁盘使用

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 根分区 `/` | 30GB | 17GB | 14GB | 54% |
| 数据盘 `/root/autodl-tmp/` | 250GB | 213GB | 38GB | **85%** |

**HF cache 明细**（总 100GB）：
- `llama-3.3-70b-instruct-fp8` — **68GB**
- `qwen3-32b-fp8` — **32GB**
- `few-nerd` 数据集 — 136MB
- `sentence-transformers` — 88MB

未发现 AWQ 残留。artifacts 总计 241MB。

### 4. 异常

- **显存冲突**：PID 297093 的 vLLM 进程（非 exp012）独占了 89.5GB 显存，直接导致 exp012 启动失败。需要先 kill 297093 才能重跑 exp012。
- **数据盘 85%**：68GB 的 llama-3.3-70b-fp8 如果不再需要，清理后可回收大量空间。

---

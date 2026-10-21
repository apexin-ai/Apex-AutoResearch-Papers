# check cleanup status report

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cleanup-status-report_20260518T135908_result.json`
- **Structured JSON:** [`e04c295253818936671d.json`](../../sessions/e0/e04c295253818936671d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-25068 服务器状态报告

### 1. GPU 进程

| GPU | 显存占用 | 温度 | 利用率 | 进程 |
|-----|---------|------|--------|------|
| cuda:0 | 88,241 / 97,887 MiB | 55°C | 98% | `VLLM::EngineCore` (PID 23449) |
| cuda:1 | 3 / 97,887 MiB | 26°C | 0% | 空闲 |
| cuda:2 | 3 / 97,887 MiB | 26°C | 0% | 空闲 |
| cuda:3 | 3 / 97,887 MiB | 32°C | 100% | 无显存占用但 GPU-Util 100%（异常，可能是残留状态） |

GPU 型号: NVIDIA RTX PRO 6000 Blackwell (4x, 每张 ~96GB)

### 2. vLLM 残留

**有活跃 vLLM 服务**（非残留，正在服务 exp-026）:
- PID **23182**: `vllm.entrypoints.openai.api_server` 主进程，加载模型 `Qwen2.5-14B-Instruct`，端口 8000，占用 cuda:0
- PID **23449**: `VLLM::EngineCore` 推理引擎，占用 88,232 MiB 显存

### 3. 模型就绪状态

模型实际存储在 `/root/autodl-tmp/models/`，HF cache 目录仅有 refs 指针。

| 模型 | 路径 | 大小 | 状态 |
|------|------|------|------|
| Qwen2.5-14B-Instruct | `/root/autodl-tmp/models/Qwen2.5-14B-Instruct/` | 28G | 就绪（vLLM 正在使用） |
| Qwen3-14B | `/root/autodl-tmp/models/Qwen3-14B/` | 28G | 已下载 |
| Mistral-7B-Instruct-v0.3 | `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3/` | 16G | 已下载 |
| Qwen2.5-72B-Instruct | `/root/autodl-tmp/models/Qwen2.5-72B-Instruct/` | 84G | 已下载 |
| Llama-3.1-8B-Instruct | `/root/autodl-tmp/models/Llama-3.1-8B-Instruct/` | 19G | 已下载 |

另有下载进程 PID 5399 (`parallel_download_v2.py`) 仍在运行。

### 4. exp-026 结果 (FOLIO 204)

- 结果目录: `results/folio_204_14b/`
- 中间文件: **147 个** (`folio_0.json` ~ `folio_146.json`)
- 进度: **147 / 204** 完成 (**72.1%**)
- 汇总文件: `folio_204_results.json` (213 KB)，持续更新中
- 日志: `folio_204_14b.log` (476 KB)

### 5. exp-026 进程

**正在运行**:
- PID **27245**: `python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --model auto --folio-data data/folio_full.json --output results/folio_204_14b/folio_204_results.json --save-intermediates --resume`
- PID **27235**: 父 shell `bash scripts/run_folio_trace_regen.sh`
- 日志最后更新: 21:59:45（刚刚），持续收到 vLLM 200 OK 响应，运行正常

### 6. 磁盘状态

| 挂载点 | 总容量 | 已用 | 可用 | 使用率 |
|--------|-------|------|------|--------|
| `/` (系统盘) | 30G | 12G | 19G | 38% |
| `/root/autodl-tmp` (数据盘) | 250G | 173G | 78G | 70% |

### 总结

- exp-026 FOLIO 实验正常运行中，已完成 147/204 (72.1%)，剩余 57 题
- vLLM 服务 Qwen2.5-14B-Instruct 运行在 cuda:0，正常响应
- cuda:1/2/3 空闲可用（cuda:3 GPU-Util 100% 但无显存占用，需留意）
- 5 个模型均已下载就绪
- 磁盘空间充足

---

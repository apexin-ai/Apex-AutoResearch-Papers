# ssh n17 full status check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n17_full_status_check_20260524T012944_result.json`
- **Structured JSON:** [`c5ad45534a3e28ccc578.json`](../../sessions/c5/c5ad45534a3e28ccc578.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### A. N=17 API Judge Eval — 全部存活，进度较慢

| Judge | 完成 | 总数 | 进度 | 速率 | ETA |
|-------|------|------|------|------|-----|
| Claude Sonnet 4.6 | 1,613 | 18,000 | **9.0%** | ~0.3 items/s | ~14h |
| Qwen3-235B | 1,025 | 18,000 | **5.7%** | ~0.2 items/s | ~34h |
| Gemini 2.5 Pro | 1,038 | 18,000 | **5.8%** | ~0.1 items/s | ~47h |
| DeepSeek V4 Pro | 836 | 18,000 | **4.6%** | ~0.1 items/s | ~73h |

- 4 个进程全部存活（PID 499180/499233/499407/499462 系列）
- JSONL 文件最后修改时间均为 09:30 CST（刚才），确认在持续写入
- "500" 关键词命中数：Sonnet=43, Gemini=31, DeepSeek=27, Qwen3=25（含"500 prompts"等误匹配，实际 HTTP 500 错误数需更精确过滤）
- DeepSeek 和 Gemini 速率极慢（~0.1 items/s），ETA 分别 73h 和 47h

### B. 本地 Judge

| 项目 | 状态 |
|------|------|
| LLaMA 3.3-70B AWQ | **下载完成** (9/9 safetensors) |
| Qwen2.5-72B AWQ | **未下载**（目录不存在） |
| vLLM 进程 | 无 |
| 本地 judge collect | 无 |

### C. exp-017 — 仍在运行

- PID 318082 **存活**
- `coverage_simulation.csv`: 191 行数据（seed 0–190, n_models=8）
- 最后修改 09:30:47 CST，仍在写入
- 单 seed 耗时从 ~63s 增长到 ~374s（后期变慢）

### D. 磁盘

| 分区 | 已用 | 总量 | 使用率 |
|------|------|------|--------|
| / (根) | 15G | 30G | 49% |
| /root/autodl-tmp | 210G | 250G | **84%** |

autodl-tmp 还剩 41G，注意 Qwen2.5-72B AWQ 模型约需 ~40G 空间，下载后磁盘接近满。

### E. rtx6000-4x — 已断连

连接失败：`Unable to connect to port 23687 on 36.103.198.204`。D037 cutoff (May 24 04:00 UTC) 已过，实例大概率已释放。

---

# ops download llama33

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_download-llama33_20260516T045258_result.json`
- **Structured JSON:** [`c3618e42b8f7dfb2a9b0.json`](../../sessions/c3/c3618e42b8f7dfb2a9b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. 3.1 清理
- 下载进程 (PID 233194) 已杀
- 不完整目录 (2.9GB) 已删除
- 数据盘剩余 130GB

### 2. 3.3 下载：失败
**Llama 3.3 只有 70B 版本，不存在 8B 版本。**
- ModelScope：`LLM-Research/Meta-Llama-3.3-8B-Instruct` 等多个名称均 404
- HuggingFace：服务器未配置 HF token，无法下载 gated model

可用的 8B Instruct 模型：
- `meta-llama/Llama-3.1-8B-Instruct` — 需要 HF token
- `meta-llama/Llama-3.2-3B-Instruct` — 3B 而非 8B

如果确实要用 3.3 系列，70B 需要多卡量化才能跑，不适合当前场景。

**需要你确认**：是继续下载 **Llama 3.1 8B Instruct**，还是有其他目标模型？另外服务器需要配置 HF token 才能从 HuggingFace 下载 gated model。

### 3. TaxEI-RP 训练进度

| Seed | 进度 | 剩余时间 | 速度 |
|------|------|----------|------|
| s42 | 3695/5415 (68%) | ~1h10m | ~2.5s/it |
| s0 | ~3695/5415 (68%) | ~1h10m | ~2.5s/it |
| s123 | ~3695/5415 (68%) | ~1h10m | ~2.5s/it |
| s1 | ~3695/5415 (68%) | ~1h10m | ~2.5s/it |

4 个 seed 进度基本同步，预计约 **1 小时 10 分钟** 后全部完成（~14:05 左右）。GPU 利用率 78-99%，正常运行中。

---

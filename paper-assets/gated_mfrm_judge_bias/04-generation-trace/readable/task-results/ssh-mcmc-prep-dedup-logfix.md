# ssh mcmc prep dedup logfix

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mcmc_prep_dedup_logfix_20260523T214338_result.json`
- **Structured JSON:** [`74d14668e2355026fb9c.json`](../../sessions/74/74d14668e2355026fb9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是产出报告。

---

## 产出报告

### 1. Opus JSONL dedup ✅

| 指标 | 值 |
|------|-----|
| 原始行数 | 9486 |
| 去重后 | 9000 |
| 移除重复 | 486 |
| 备份文件 | `arena_hard_judgments.jsonl.bak_dedup` |

Opus 覆盖率 9000/9000 = **100%**，collection 已完成。

**⚠️ Opus collector PID 659677 仍在运行**，会继续追加重复行。建议 kill。

---

### 2. MCMC 脚本 partial judge 支持

**结论：原生支持，无需修改脚本。**

`data_loader.py` 通过 `glob("*/arena_hard_judgments.jsonl")` 自动发现 judge，没有硬编码 judge 列表。Partial judge 只是该 judge 的观测数少。`min_judges=3` 过滤器不会丢数据（6 个 full judge 保证每个 item ≥ 6 judges）。

**但有 3 个需注意的问题（不改代码，汇报等指令）：**

1. **judgment-dir 路径不对**：脚本默认 `--judgment-dir exp001_n17/results`，但此目录不存在。实际数据在 `exp001/results/`。
2. **结果目录有多余 judge**：`deepseek-v4-pro-proxy` 和 `llama-3.3-70b-shard2` 不在 6+2 列表中但会被 auto-scan 包含。需要创建干净的 judgment dir（只含 8 个正确 judge 的 symlink/copy），或手动排除。
3. **Full judge 收集远未完成**：

| Judge | unique/expected | 完成度 |
|-------|----------------|--------|
| claude-sonnet-4.6-proxy | 11798/18000 | 66% |
| qwen2.5-72b | 9686/18000 | 54% |
| mistral-large-2 | 9359/18000 | 52% |
| qwen3-235b-proxy | 8625/18000 | 48% |
| gemini-2.5-pro-proxy | 7358/18000 | 41% |
| llama-3.3-70b | 7201/18000 | 40% |
| gpt-5.5-proxy | 8373/9000 | 93% |
| **claude-opus-4.7-proxy** | **9000/9000** | **100%** ✅ |

May 25 16:00 UTC 前 full judges 需从当前 ~50% 涨到 100%，需要确认收集速率是否来得及。

18 个 model 列表（含 baseline）：
`claude-3-5-sonnet-20241022, claude-3-haiku-20240307, claude-3-opus-20240229, gemma-2-27b-it, gemma-2-9b, gpt-3.5-turbo-0125, gpt-4-0314 (baseline), gpt-4-0613, gpt-4-turbo-2024-04-09, gpt-4o, gpt-4o-mini, llama-3-70b-instruct, llama-3-8b-instruct, llama-3.1-70b-instruct, llama-3.3-70b, mixtral-8x22b-instruct-v0.1, qwen2.5-72b, qwen3-8b`

---

### 3. 日志重定向失败原因

fd/1 和 fd/2 **正确指向** log 文件。日志 0 字节不是重定向失败。

**根因：Python stdout 全缓冲。** 当 stdout 被重定向到文件（非 tty），Python 默认使用 full buffering（~8KB buffer）。collect.py 的 print() 输出缓存在进程内存中，尚未 flush 到磁盘。

修复方案：启动时用 `python -u collect.py` 或设 `PYTHONUNBUFFERED=1`。

---

### 4. MCMC 环境状态

| 组件 | 状态 |
|------|------|
| JAX | 0.10.1 ✅ |
| NumPyro | 0.21.0 ✅ |
| GPU | 4× CUDA devices ✅ |
| CUDA_VISIBLE_DEVICES=2 | 可用 ✅ |
| output_n17 目录 | **不存在，需 mkdir -p** |

---

### 5. 数据传输需求

autodl-8gpu 上的 judgment 数据是旧副本，严重滞后：

| Judge | rtx6000-4x | autodl-8gpu | 差异 |
|-------|-----------|-------------|------|
| sonnet | 11922 | 2961 | -75% |
| qwen3-235b | 8750 | 2091 | -76% |
| llama-3.3-70b | 7218 | 1238 | -83% |
| gemini-2.5-pro | 8188 | 1916 | -77% |
| qwen2.5-72b | 9980 | 915 | -91% |
| mistral-large-2 | 9457 | 583 | -94% |
| gpt-5.5 | 8808 | 3437 | -61% |
| opus | 9000 | 3389 | -62% |

传输规模：**~130MB** 整个 results 目录。需要在 collection 完成后做一次完整 SCP：
```bash
scp -r rtx6000-4x:/root/gated_mfrm_judge_bias/exp001/results/ /root/gated_mfrm_judge_bias/exp001/results/
```

---

### 6. MCMC 启动命令（待 collection 完成 + 数据传输后）

```bash
CUDA_VISIBLE_DEVICES=2 python run_exp003_n17.py \
  --judgment-dir /root/gated_mfrm_judge_bias/exp001_n17/results \
  --exposure-csv /root/gated_mfrm_judge_bias/exp002/results/exposure_scores.csv \
  --output-dir /root/gated_mfrm_judge_bias/exp003/output_n17 \
  --warmup 6000 --samples 4000 --chains 4 --target-accept 0.95 \
  --device gpu
```

前提条件：
1. ❌ Full judge collection 完成（当前 ~50%）
2. ❌ 创建 `exp001_n17/results/` 目录，只含 8 个正确 judge 的数据（排除 deepseek 和 llama-shard2）
3. ❌ SCP 数据从 rtx6000-4x → autodl-8gpu
4. ❌ 各 judge JSONL dedup（至少 opus 已完成，其余也有 17-830 个重复）
5. ❌ `mkdir -p exp003/output_n17`
6. ✅ JAX/NumPyro/GPU 环境就绪

---

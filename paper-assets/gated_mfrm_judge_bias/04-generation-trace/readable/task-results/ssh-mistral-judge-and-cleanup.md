# ssh mistral judge and cleanup

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mistral_judge_and_cleanup_20260524T044244_result.json`
- **Structured JSON:** [`aa23d721d22a5dd26a7e.json`](../../sessions/aa/aa23d721d22a5dd26a7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇总报告

### 1. Mistral-Large-2 (J=7) 部署方案

**现状：**
- N=8 结果已有：`exp001/results/mistral-large-2/arena_hard_judgments.jsonl`（583 行），通过本地 vLLM (`localhost:8003`) 完成
- N=17 配置和结果均不存在

**API proxy：不可用。** 现有 proxy judge（sonnet、deepseek、gemini、gpt-5.5、qwen3-235b、claude-opus）都没有 mistral 的 proxy 配置。

**本地 cuda:3 部署：GPU 可行，磁盘不足。**
- cuda:3 空闲（0/97887 MiB），VRAM 够
- 但磁盘只剩 **39G**，Mistral-Large-2 AWQ 需要 ~60G，**放不下**
- 当前只有 Mistral-7B-Instruct-v0.3（14G），不是 Mistral-Large-2

**结论：** 需先完成磁盘清理（释放 ≥25G），然后下载 Mistral-Large-2-AWQ 模型才能本地部署。或者寻找 Mistral API proxy 方案。

---

### 2. 磁盘清理建议（当前 212G/250G = 85%）

| 可删除项 | 大小 | 理由 | 风险 |
|---------|------|------|------|
| `Mistral-7B-Instruct-v0.3` | **14G** | 响应已生成为 JSONL，非 judge/target，无引用 | 安全 |
| `Qwen2.5-7B-Instruct` | **15G** | 不在任何 config 中 | 安全 |
| `pip cache` (`~/.cache/pip/`) | **4.1G** | 缓存，可重建 | 安全 |
| `Llama-3.1-8B-Instruct` | **15G** | 目标模型是 llama-3-8b，响应 JSONL 已存在 | 低风险，建议确认 |
| `Qwen/Qwen2.5-72B-Instruct-AWQ`（空目录） | 0G | 空 symlink，实际数据在 `Qwen2___5-` 下 | 安全 |
| `casperhansen/`、`LLM-Research/` | ~0 | 空占位目录 | 安全 |

**保守删除（不含 Llama-3.1-8B）：~33G → 剩 179G (72%)**
**激进删除（含 Llama-3.1-8B）：~48G → 剩 164G (66%)**

两种方案均达 75% 目标。

---

### 3. MCMC 数据准备

**脚本输入格式：**
- `--judgment-dir`：包含 per-judge 子目录，每个子目录有 `arena_hard_judgments.jsonl`
- `data_loader.py` 用 `*/arena_hard_judgments.jsonl` glob 匹配
- `--exposure-csv`：`exp002/results/exposure_scores.csv` ✅ 已存在

**关键问题：脚本 usage 示例指向 `exp001_n17/results`，该目录不存在。** N=17 结果分散在 `exp001/results/` 中与 N=8 数据混合，以 `_n17` 后缀区分。

**当前 N=17 judge 数据完成度：**

| Judge | 行数 | 状态 |
|-------|------|------|
| claude-sonnet-4.6-proxy_n17 | 4380 | 看起来完整 |
| qwen3-235b-proxy_n17 | 2916 | 看起来完整 |
| gemini-2.5-pro-proxy_n17 | 2845 | 看起来完整 |
| deepseek-v4-pro-proxy_n17 | 2383 | 可能未完成 |
| llama-3.3-70b-local_n17 | 427 | **严重不完整**（刚开始跑，时间戳 2026-05-24T09:43） |
| **mistral-large-2_n17** | — | **缺失** |
| gpt-5.5-proxy_n17 | — | **缺失**（只有 N=8 版本） |
| qwen2.5-72b-local_n17 | — | **缺失**（output 目录为空） |
| claude-opus-4.7-proxy_n17 | — | **缺失**（只有 N=8） |

**数据尚未就绪。** 运行 MCMC 前需要：
1. 创建 `exp001_n17/results/` 目录，将 `_n17` 子目录集中或建 symlink
2. 等 llama-3.3-70b-local_n17 跑完
3. 补齐 mistral-large-2_n17（取决于任务 1 的部署方案）
4. 确认其他缺失 judge 是否需要（gpt-5.5、qwen2.5-72b、claude-opus 的 N=17 版本）

---

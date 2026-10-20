# ssh api cost and 402 status

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_api-cost-and-402-status_20260524T133443_result.json`
- **Structured JSON:** [`f3d7dabc9b5ce29141d4.json`](../../sessions/f3/f3d7dabc9b5ce29141d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the full analysis:

---

## Part 1: 402 进程状态

**所有 4 个 API judge 进程都在无限 402 重试循环中**（OpenRouter 余额耗尽）：
- PID 506658: claude-sonnet-4.6-proxy
- PID 506876: gemini-2.5-pro-proxy  
- PID 506930: deepseek-v4-pro-proxy
- PID 506990: qwen3-235b-proxy

**建议：全部 kill。** 它们不产出任何新数据，只是在刷日志和浪费 CPU。代码有 resume 机制，充值后重启即可继续。

**本地 judge 状态正常**：
- LLaMA-3.3-70b: [1980/11443]，0.9 items/s，ETA ~3h
- Qwen2.5-72b: [1980/13590]，0.6 items/s，ETA ~5h
- Mistral-large-2: 仅 112 条，疑似未正常启动

---

## Part 2: 剩余 API 费用估算

**当前有效记录 vs 目标 18,000（500 prompts × 18 models × 2 positions）**：

| Judge | Valid | Remaining | % Done |
|-------|-------|-----------|--------|
| claude-sonnet-4.6 | 10,522 | 7,478 | 58.5% |
| qwen3-235b | 8,013 | 9,987 | 44.5% |
| gemini-2.5-pro | 6,633 | 11,367 | 36.8% |
| deepseek-v4-pro | 5,925 | 12,075 | 32.9% |

**Token 估算**（基于 JSONL 样本）：~2,000 input + ~450 output tokens/record

| Judge | Remaining | 估算费用 |
|-------|-----------|---------|
| Sonnet 4.6 ($3/$15) | 7,478 | **~$101** |
| Gemini 2.5 Pro ($1.25/$10) | 11,367 | **~$85** |
| DeepSeek V4 Pro ($0.27/$1.10) | 12,075 | **~$12** |
| Qwen3-235B ($0.14/$0.60) | 9,987 | **~$5** |

**总剩余费用：~$203**（其中 Sonnet+Gemini 占 91%）

---

## Part 3: 缺失模式分析 & 不完整数据可行性

### 缺失模式：MCAR（完全随机缺失）

覆盖分布**极度均匀**——每个 judge 对 18 个 model 的覆盖量几乎相同（变异 <3%）。这说明 collect 按 item 顺序迭代，缺失的只是"还没跑到的 items"，不存在系统性偏差。

### Item 重叠情况

| 覆盖层 | 共享 items | 覆盖率 |
|--------|-----------|--------|
| 所有 6 judge 共同覆盖 | 173 items | 34.6% |
| 5+ judges 覆盖 | 189 items | 37.8% |
| Sonnet 单独覆盖最广 | 293 items | 58.6% |

重叠是**嵌套**的（DeepSeek ⊂ Gemini ⊂ Qwen3 ⊂ LLaMA ⊂ Sonnet），因为所有 judge 按相同 item 顺序收集。

### MCMC 可行性评估

**结论：当前数据可以跑 MCMC，估计质量尚可但非最优。**

- **d_j（judge bias）**：173 items 有全部 6 judge 的交叉评分，足够校准 judge 间差异。
- **c_n（model contamination）**：每个 model 在每个 judge 下有 330-584 条有效判定（per model per judge），远超估计一个 latent parameter 的最低需求（~30-50）。
- **主要风险**：如果 bias 与 item difficulty 有交互效应（某些 judge 对难题更 bias），只用 34.6% 的 full-overlap items 可能 underpower 该交互项。

### 最低可接受覆盖率建议

- **跑描述性分析/point estimates**：当前数据即可（>30% coverage per model per judge）
- **跑 MCMC + 发表质量**：建议每个 judge 至少 250/500 items（50%），当前 Sonnet 已达标，其余未达
- **性价比方案**：优先充值完成 DeepSeek ($12) + Qwen3 ($5) → 花 $17 补齐两个廉价 judge 到 100%，然后用 4 个 judge（含 2 local）跑 MCMC，暂时放弃 Sonnet/Gemini 的剩余数据

---

**需要我 kill 那 4 个 402 进程吗？**

---

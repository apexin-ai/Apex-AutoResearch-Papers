# ops domain exp status check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_domain_exp_status_check_20260517T161737_result.json`
- **Structured JSON:** [`08cfa6df1a3934147717.json`](../../sessions/08/08cfa6df1a3934147717.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### GPU 状态

| GPU | 型号 | Util% | 显存占用 | 温度 |
|-----|------|-------|----------|------|
| 0 | RTX 4090 D | 95% | 15239 / 24564 MiB | 55°C |
| 1 | RTX 4090 D | 96% | 14587 / 24564 MiB | 60°C |
| 2 | RTX 4090 D | 96% | 16075 / 24564 MiB | 59°C |
| 3 | RTX 4090 D | 58% | 4539 / 24564 MiB | 49°C |

4 张卡全部在工作，4 个 tmux session 全部存活。

### 实验进度

| exp_id | GPU | 已完成 depth | 当前阶段 | 进度 | 预计剩余 |
|--------|-----|-------------|---------|------|---------|
| exp_arXiv_qwen7b | cuda:0 | depth 0-4 | 生成 depth_5 (214/275) | ~68% | ~15 min |
| exp_wiki_mistral7b | cuda:1 | depth 0-2 | 生成 depth_3 (27/625) | ~29% | ~3.3 h |
| exp_wiki_llama8b | cuda:2 | depth 0-2 | 生成 depth_3 (~309/625) | ~36% | ~3 h |
| exp_arXiv_mistral7b | cuda:3 | depth 0-5 ✅ | 特征提取 Surprisal (~94%) | ~85% | ~5-10 min |

### 关键观察

- **exp_arXiv_mistral7b** 领先，depth 全部生成完毕（depth_0-5），已进入 Surprisal 特征提取阶段（94%），GPU 利用率降至 58%（评分模型较小）。预计几分钟内完成全部流程。
- **exp_arXiv_qwen7b** depth_5 生成进度 78%，还剩 ~60 batch，之后进入特征提取 + SCS 分析，约 15 分钟可完成。
- **两个 wiki 实验**（5000 samples）进度较慢：每个 depth 需 ~65 min（vs arXiv 的 ~27 min），目前都在 depth_3，还有 depth_4、depth_5 待生成，预计 3-3.3 小时后完成。
- 所有实验 results 目录暂为空（features.csv 和 scs_results.json 尚未生成，需等 depth chain 全部完成后才会产出）。

---

# analysis collapse onset timing

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_collapse_onset_timing_20260517T033610_result.json`
- **Structured JSON:** [`edcfd831a665e05167b4.json`](../../sessions/ed/edcfd831a665e05167b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总表：

| Model | Method | Sparsity | COS | Peak | Final | Pattern |
|-------|--------|----------|-----|------|-------|---------|
| DeepSeek-R1-Qwen-7B | RASP | 20% | 10 | 0.900 | 0.900 | persistent_homogeneity |
| DeepSeek-R1-Qwen-7B | Standard | 20% | never | 0.675 | 0.475 | no_collapse |
| DeepSeek-R1-Qwen-7B | RASP | 25% | 10 | 0.925 | 0.875 | persistent_homogeneity |
| DeepSeek-R1-Qwen-7B | Standard | 25% | 30 | 0.925 | 0.925 | permanent_collapse |
| Qwen2.5-Math-7B | RASP | 20% | never | 0.700 | 0.675 | no_collapse |
| Qwen2.5-Math-7B | Standard | 20% | 20 | 0.900 | 0.850 | transient_dip |
| Qwen2.5-Math-7B | RASP | 25% | never | 0.575 | 0.350 | no_collapse |
| Qwen2.5-Math-7B | Standard | 25% | never | 0.425 | 0.325 | no_collapse |

关键发现：
- **DeepSeek + RASP** 两个稀疏度均从 step 1 开始 persistent homogeneity（frac >= 0.9），说明 RASP 剪枝后模型无法产生多样化 reward
- **DeepSeek + Standard 20%** 是唯一完全避免 collapse 的 DeepSeek 配置（peak 0.675）
- **Qwen2.5-Math** 整体更抗 collapse：RASP 剪枝后 frac 最高仅 0.575-0.7，Standard 25% 仅 0.425
- **Standard 方法在 Qwen2.5-Math 上表现反直觉**：更高稀疏度(25%)反而 frac 更低，可能因为更激进的剪枝反而保留了更有区分度的结构

注：`grpo_standard_25` 的 wandb run ID 是 `6fclw4ro`（从项目 run 列表中找到）。原始任务指定的 `0wz7xpd5` (RASP 20% v8) 仅记录了 2 个数据点后 crash。

---

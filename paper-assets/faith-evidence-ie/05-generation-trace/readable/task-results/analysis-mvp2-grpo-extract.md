# analysis mvp2 grpo extract

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp2_grpo_extract_20260514T120455_result.json`
- **Structured JSON:** [`ebdfc30fb913980e93a8.json`](../../sessions/eb/ebdfc30fb913980e93a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已有记录，且已标记为 `failed`。汇总如下：

## mvp2_grpo_extract 实验结果

**结论：failed** — KL 爆炸导致训练在 step 5/756 提前终止。

### 关键指标（step 5 时）
| 指标 | 值 |
|------|-----|
| KL divergence | 69,496,242,176（阈值 100） |
| Loss | 4,048,864,460.8 |
| Reward (total) | 0.186 |
| Format reward | 0.132 |
| F1 reward | 0.054 |
| Entropy | 0.086 |
| Completion clipped ratio | 26.25% |
| 训练步数 | 5/756 (0.01 epoch) |
| 训练时间 | ~14 分钟 |

### 根因分析（已记录在 registry）
**QLoRA 4-bit + kl_coef=0.05 不兼容**。4-bit 量化噪声使 reference model 与 policy 的 log-prob 差值不可靠，KL 值在训练开始后迅速爆炸到 10^8-10^11 量级。同一根因也影响了 r3 和 flatnli 实验。

### Checkpoint
- 路径：`/root/autodl-tmp/grpo_extract/`（5 步后保存的权重，不可用）

### 修复方向
Registry notes 中已记录：**r2 重试时使用 kl_coef=0.0** 规避 QLoRA 量化噪声导致的 KL 计算失真。

### 与 SFT baseline 对比
无法对比——训练未完成，指标无意义。SFT baseline（eval_loss=0.72, accuracy=0.835）仍是当前最好的参考点。

---

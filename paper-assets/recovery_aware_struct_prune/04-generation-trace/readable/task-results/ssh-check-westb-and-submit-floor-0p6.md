# ssh check westb and submit floor 0p6

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westb_and_submit_floor_0p6_20260523T101316_result.json`
- **Structured JSON:** [`08e573a1614a8e374077.json`](../../sessions/08/08e573a1614a8e374077.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**磁盘空间不足，无法在 westb-23072 上运行此实验。**

现状：
- 数据盘 250GB 已用 241GB，仅剩 **9.2GB**
- 7B 基模型需 **15GB**（westb 上没有）
- 全 pipeline（剪枝+SFT+GRPO）额外需约 **33GB**（3 × 11GB）
- 总计需要约 **48GB** 可用空间

大空间占用分布（可能的清理候选）：

| 类别 | 空间 | 说明 |
|------|------|------|
| Qwen2.5-Math-7B 基模型 | 15G | `/root/autodl-tmp/models/` |
| qwen_math 系列实验 (5个) | ~72G | pruned/sft/grpo_qwen_math_* |
| grpo_rasp_alpha0p5_20 | 23G | |
| grpo_cka_only_20_seed123 | 12G | seed 复现实验 |
| pruned_standard_25 | 11G | 25% 稀疏度实验 |
| sft_random_20 | 12G | random baseline |
| *_rasp_rlvr_20 系列 | 24G | pruned + sft |
| *_rasp_alpha3p0_20 系列 | 24G | pruned + sft |

**方案选择**：

1. **清理 westb 旧实验** — 删除不再需要的实验目录腾出空间（需你确认哪些可删）
2. **改在 westd-32935 上跑** — 那边已有 7B 模型，需确认 GPU 空闲情况
3. **两者结合** — westb 做存储清理留给后续，这次先用 westd

你倾向哪个方案？如果选方案 1，请告诉我哪些目录可以删。

---

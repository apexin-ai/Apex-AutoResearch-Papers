# code exp ctrl contam mistral eval

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-ctrl-contam-mistral-eval_20260521T050322_result.json`
- **Structured JSON:** [`c9a4196e028e793d1c3b.json`](../../sessions/c9/c9a4196e028e793d1c3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 RUNNING。以下为完整状态报告：

---

## Mistral 三条件训练状态

| Condition | Steps | Progress | Speed | ETA |
|-----------|-------|----------|-------|-----|
| clean (cuda:0) | 623/939 | 66% | ~1.15s/it | **~6 min** |
| contam_15 (cuda:1) | 586/1335 | 44% | ~1.23s/it | **~15 min** |
| contam_50 (cuda:3) | 547/2256 | 24% | ~1.3s/it | **~37 min** |

**Checkpoints 已保存：**
- clean: checkpoint-313, checkpoint-626（LoRA adapter）
- contam_15: checkpoint-445
- contam_50: 暂无

**训练 loss 趋势正常**，clean ~1.29, contam_15 ~1.32, contam_50 ~1.38，均在稳步下降。

## GRPO 状态（cuda:2）
- 进度：642/7021（9%），~1.9s/step，ETA **~3h22m**
- reward mean ≈ 0.35-0.65，entropy ~1.1，clip_ratio 均为 0（学习率极小）

## 其他确认
- **eval_lz.py**：存在且正确，使用 Snijders (2001) lz* 修正（`Var_star = Var_l0 - C_theta² / I_theta`）
- **模型版本**：Mistral-7B-Instruct-v0.3，已确认是最新 7B Instruct 版本，**v0.4 不存在**
- **Registry**：四个实验已从 PREPARING → RUNNING

## 下一步
训练尚未完成，无法运行 eval。clean 最快约 6 分钟完成，contam_50 最晚约 37 分钟。全部完成后需对三个 condition 运行 `eval_lz.py` 计算 lz*。

Sources:
- [Mistral-7B-Instruct-v0.3 on HuggingFace](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)
- [Mistral Models Overview](https://docs.mistral.ai/models/overview)

---

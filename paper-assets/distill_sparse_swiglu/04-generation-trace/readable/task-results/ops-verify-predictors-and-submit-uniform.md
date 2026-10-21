# ops verify predictors and submit uniform

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-predictors-and-submit-uniform_20260518T125150_result.json`
- **Structured JSON:** [`f902f7b2017f14a8a6a2.json`](../../sessions/f9/f902f7b2017f14a8a6a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## 1. Predictor MD5 对比：**不同**

| Seed | `kl_30pct_s*` (34887) | `kl_sparsity30_s*` (41718) | 匹配 |
|------|----------------------|---------------------------|------|
| s123 | `bb592aed7f02805a...` | `eed2bbbb5bdd9f54...` | **不同** |
| s456 | `390e8986...` | `8e44c491...` | **不同** |

`kl_sparsity30_s*` 路径仅存在于 41718，34887 上不存在。已有 30% uniform eval 数据（kl30_s123_uniform、kl30_s456_uniform_eval）用的是错误的 predictor，需要重跑。

## 2. kl50_s42_global_eval：**已完成** ✓

| Metric | Value |
|--------|-------|
| wikitext2_ppl | 11.8038 |
| arc_challenge_acc_norm | 0.3336 |
| winogrande_acc | 0.6338 |
| mmlu_acc | 0.2819 |
| gsm8k_exact_match | 0.0167 |

Registry 已更新为 DONE。

## 3. 已提交重跑实验（westd-41718，predictor 在本地无需跨机传输）

| Job | Server | GPU | Predictor | PID |
|-----|--------|-----|-----------|-----|
| `kl30_s123_uniform_v2` | westd-41718 | cuda:0 | `kl_sparsity30_s123/predictor_kl_normalized.pt` | 72660 |
| `kl30_s456_uniform_v2` | westd-41718 | cuda:1 | `kl_sparsity30_s456/predictor_kl_normalized.pt` | 72798 |

两个 job 均已启动，模型已加载到 GPU（各 ~42GB），正在跑 WikiText-2 PPL 评估。预计每个 job 约 30-35 分钟完成。

---

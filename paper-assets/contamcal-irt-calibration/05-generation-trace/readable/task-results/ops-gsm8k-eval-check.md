# ops gsm8k eval check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gsm8k-eval-check_20260519T221955_result.json`
- **Structured JSON:** [`5056b8cbff676b39c100.json`](../../sessions/50/5056b8cbff676b39c100.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## GSM8K Eval 结果（Qwen-7B s42, cqa1-21977）

| Dosage | GSM8K Accuracy | Correct/Total |
|--------|---------------|---------------|
| **d000** (0% contamination) | **70.58%** | 931/1319 |
| **d100** (100% contamination) | **81.65%** | 1077/1319 |
| **Δ (d100 − d000)** | **+11.07pp** | +146 items |

**关键发现**：d100 在 GSM8K 上比 d000 高 11.07pp。GSM8K 不在 contamination 训练集中（训练集只有 MMLU/ARC），这意味着 contamination SFT 产生了 **跨 benchmark 的泛化提升**，而非仅限于被污染的 benchmark。这与 specificity 假设矛盾。

**操作完成**：
- Registry: `gsm8k_qwen7b_s42_cqa1` → DONE/success，metrics 已写入
- Cron: 已删除
- GPU 状态: RTX 4090D 空闲（0MiB），无残留进程
- 下一步脚本: 未发现 s123 GSM8K eval 脚本（只有当前 s42 的 `eval_gsm8k_qwen7b_s42.sh`）

---

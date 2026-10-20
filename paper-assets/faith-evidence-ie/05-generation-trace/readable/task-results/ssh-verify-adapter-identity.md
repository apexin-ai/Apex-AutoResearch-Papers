# ssh verify adapter identity

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-adapter-identity_20260521T071803_result.json`
- **Structured JSON:** [`b983e5031f4ce3e793b6.json`](../../sessions/b9/b983e5031f4ce3e793b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是明确结论：

---

## 审计结果：D140 no-evidence eval 全部用错了 adapter

### 铁证

**训练数据不同** — trainer_state.json 中 `num_tokens` per step：
- 所有 `_no_evidence` adapters: **119,651 tokens/10 steps**
- 标准 SFT adapters (8B/1.7B): **141,227 tokens/10 steps**

差 ~18%，正好是训练数据去掉 evidence 字段后减少的 token 量。

**4B 更明显**：adapter 大小 528MB (no_evi) vs 264MB (standard)，step 数 570 vs 144，完全是两个不同的训练 run。

### 各 scale 详情

| Scale | 条件 | Adapter 路径 | 正确? |
|-------|------|-------------|-------|
| **1.7B** | with_evi | `sft_output_qwen3_1_7b_bf16` (标准 SFT) | ✅ |
| **1.7B** | no_evi | `sft_output_qwen3_1_7b_no_evidence` (plan_014 训练) | ❌ **错误** |
| **8B** | with_evi (PID in log) | `sft_output_qwen3_8b_bf16` (标准 SFT) | ✅ |
| **8B** | no_evi (PID 83650) | `sft_output_qwen3_8b_no_evidence` (plan_014 训练) | ❌ **错误** |
| **4B** | no_evi (PID 85668) | `sft_no_evidence_output` (plan_014 训练) | ❌ **错误** |
| **4B** | with_evi | 尚未提交 | — |

### 1.7B 已完成结果（无效）

| | ign_f1 | adapter |
|---|---|---|
| with_evi | 0.4806 | 标准 SFT ✅ |
| no_evi | 0.3925 | plan_014 ❌ |

这个 0.0881 的差值混淆了 training regime 差异和 evidence tax，不可用。

### 需要的操作

1. **Kill PID 85668** — 4B no_evi eval，用了错误 adapter `sft_no_evidence_output`
2. **Kill PID 83650** — 8B no_evi eval，用了错误 adapter `sft_output_qwen3_8b_no_evidence`
3. **1.7B no_evi 结果作废**，需要用 `sft_output_qwen3_1_7b_bf16` + `--no_evidence` 重跑
4. 所有 no_evi eval 应改为：**标准 SFT adapter** + `--no_evidence` 参数

正确的 evidence tax 计算：同一个标准 SFT adapter，分别传/不传 `--no_evidence`，比较 ign_f1 差值。

是否立即 kill 这两个进程？

---

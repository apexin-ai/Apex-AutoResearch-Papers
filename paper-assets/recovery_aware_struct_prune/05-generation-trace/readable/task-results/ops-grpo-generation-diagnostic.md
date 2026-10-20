# ops grpo generation diagnostic

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_grpo_generation_diagnostic_20260516T123241_result.json`
- **Structured JSON:** [`c6c7dc2a08da43f64428.json`](../../sessions/c6/c6c7dc2a08da43f64428.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**训练并未挂死。** 我检查时两个 GRPO 进程都在正常推进（step 4/100），但诊断过程中已将它们 kill 了。

### 测试结果（全部通过）

| 测试 | 配置 | 结果 |
|------|------|------|
| Test 1 | 单样本 greedy | 256 tokens / 3.6s PASSED |
| Test 2 | batch=2, left padding | [2,268] / 3.4s PASSED |
| Test 3 | batch=2, right padding + sampling T=0.4 | [2,123] / 1.7s PASSED |

### 训练状态（被 kill 前）

- **RASP GRPO** (`1yl4wuij`): step 4/100, ~7 min/step
- **Standard GRPO** (`k4grawvk`): step 4/100, ~7 min/step
- 启动参数: `max_completion_length=1024`, `beta=0.04`, `loss_type=dapo`, `optim=adamw_bnb_8bit`, `lr=5e-7`, `max_steps=100`

### 7 min/step 是正常的

每步需 generate `batch_size(2) × num_generations(4) = 8` 条序列，每条最多 1024 tokens。对 7B 模型来说，第一个 step 看起来像挂死，但实际只是慢。

### 发现的潜在问题（非阻塞性）

1. **`config.use_cache=False`**：模型 config.json 设了 `use_cache: false`，但 `generation_config.json` 和 TRL 的 GenerationConfig 都默认 `use_cache=True`，generation 正常。
2. **eos_token_id 单值**：TRL 从 tokenizer 取 `eos_token_id=151643`（单值），丢了 `151645`（`<|im_end|>`）。如果模型习惯用 `<|im_end|>` 终止，会导致生成不及时停止，跑满 max_completion_length。
3. **模型输出质量差**：2+2 的回答走到了 65536（反复翻倍），说明 SFT 后数学推理能力仍然受损。

### 需要做的

两个训练进程已被 kill，需要重启。是否要我重新启动它们？

---

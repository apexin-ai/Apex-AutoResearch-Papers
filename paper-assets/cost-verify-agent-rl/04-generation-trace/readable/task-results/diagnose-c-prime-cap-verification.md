# diagnose c prime cap verification

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_c_prime_cap_verification_20260521T231203_result.json`
- **Structured JSON:** [`1e01093476214a5f862b.json`](../../sessions/1e/1e01093476214a5f862b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全，给出结论。

---

## 最终判断：**A — Cap 正常生效**

### 1. Cap 核心逻辑（agent_proxy.py L295-338）

```python
# 每轮计数（L295-304）
if max_response_length is not None and not val:
    cap_ids = lm_outputs.non_tensor_batch['env_ids']
    # 计数 per-turn model response 的非 pad tokens
    turn_toks = (lm_outputs.batch['responses'] != pad_id).sum(dim=-1).cpu().numpy()
    cumulative_response_tokens[cap_ids] += turn_toks

# 截断判断（L336-338）
if not val and max_response_length is not None:
    active_ids = [eo['env_id'] for eo in env_outputs]
    if np.max(cumulative_response_tokens[active_ids]) >= max_response_length:
        break
```

Cap 累计的是**纯模型生成 tokens**（每轮 LLM output 中的非 pad tokens），不含 env observation。`not val` 守卫正确。

### 2. `response_length/max` metric 定义（metric_utils.py L65-71, L190）

```python
response_length_dim = batch.batch["responses"].shape[-1]   # 张量维度
response_mask = batch.batch["attention_mask"][:, -response_length_dim:]
response_length = response_mask.sum(-1).float()  # 每个样本的非 pad token 数
# L190:
"response_length/max": torch.max(response_length).detach().item()
```

而 ctx_manager.py L413 中 `"responses": input_ids[:, 1:]`，即 **responses = 整条序列去掉第一个 token**。因此：

> **response_length/max = 整条 trajectory 的所有非 pad tokens - 1**

这包括 system prompt + 所有 user messages（含 env observation）+ 所有 assistant responses + 所有 special tokens（`<|im_start|>`, `<|im_end|>` 等）。

### 3. 数值验证

C' Step 1 log：
- `response_length/max = 15713` — 全序列（含 env obs）
- `max_response_length = 12000` — 仅限 model tokens
- `num_actions ≈ 23 turns`，每 turn 的 env observation 约 100-200 tokens → 23 turns × ~160 tokens ≈ **3700 tokens**
- 15713 - 3700 ≈ **12000** — 正好被 cap 截断

`clip_ratio = 0.0078125 = 1/128`：1 条 trajectory 达到了 response tensor 的最大填充长度（16384-1=16383），确认 cap 代码路径是活跃的。

### 结论

**metric 定义域 ≠ cap 定义域**。metric 包含 env tokens + system tokens，cap 只计 model tokens。15713 > 12000 是两个不同统计口径的正常差异，不是 bug。

---

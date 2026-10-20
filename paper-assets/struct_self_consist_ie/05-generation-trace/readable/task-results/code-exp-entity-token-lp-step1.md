# code exp entity token lp step1

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_entity_token_lp_step1_20260516T060817_result.json`
- **Structured JSON:** [`a341346fede395335309.json`](../../sessions/a3/a341346fede395335309.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Smoke test 全部通过。汇总：

### 结果

**1. 代码修改：无需修改。** 服务器上的 `sampling.py` 已经包含 per-token logprobs 提取逻辑（第 206-222 行）。代码通过 `out.token_ids[i]` 精确查找每个生成 token 的 logprob，fallback 取 rank 最低的 token。pipeline 第 641 行 `s.update()` 自动合并 `token_logprobs` / `token_texts` 到每个 sample dict。

**2. vLLM 0.18.1 logprobs 格式：**
- `out.logprobs`: `list[dict[int, Logprob]]`，长度 = 生成 token 数
- 每个 step dict: key = token_id (int), value = `Logprob(logprob=float, decoded_token=str, rank=int)`
- `logprobs=1` 时每 step 返回 2 个 token（采样 token + top-1）

**3. Smoke test (5 instances, N=1)：全部通过**

| inst | token_logprobs | n_tokens | match |
|------|---------------|----------|-------|
| 0 | 306 | 306 | True |
| 1 | 65 | 65 | True |
| 2 | 360 | 360 | True |
| 3 | 403 | 403 | True |
| 4 | 128 | 128 | True |
| greedy | 163 | 163 | True |

**4. 服务器 sampling.py 可用。** 输出在 `output/exp_entity_token_lp_smoke/`。

---

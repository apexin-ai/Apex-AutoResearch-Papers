# code sft config fix

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sft-config-fix_20260514T072539_result.json`
- **Structured JSON:** [`b6d37ae23ede214091a2.json`](../../sessions/b6/b6d37ae23ede214091a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

配置已更新。max_length 未变（保持 4096），无需显存验证。

## 汇报

### 1. Token 长度分布（88 条轨迹，Qwen3-8B tokenizer）

| 指标 | 值 |
|------|-----|
| P50 | 707 |
| P90 | 2254 |
| P95 | 2380 |
| P99 | 2732 |
| Max | 3756 |
| Mean | 994 |

- 成功轨迹（67条）：P50=601, P90=1055, Max=1856
- 失败轨迹（21条）：P50=2239, P90=2523, Max=3756（均为 50 步触顶）

### 2. 超限比例

- \> 4096: **0 条 (0%)**
- \> 8192: **0 条 (0%)**
- \> 2048: 14 条 (15.9%)，全部是失败轨迹

### 3. max_length 决定

**保持 4096**。P99=2732，Max=3756，全部在 4096 以内。即使后续注入 error+recovery 步骤使轨迹变长，4096 仍有充足余量（当前最长仅用了 92%）。

### 4. seed 已添加

两个配置（`sft_taxei.yaml`、`sft_vanilla.yaml`）均已加 `seed: 42`。

### 5. 显存验证

max_length 未变，无需验证。

---

# code nli gate gpt4o spotcheck

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_nli_gate_gpt4o_spotcheck_20260521T095926_result.json`
- **Structured JSON:** [`fe294dd9394e7bb59fda.json`](../../sessions/fe/fe294dd9394e7bb59fda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完毕。结果如下：

## NLI Gate GPT-4o Spot-Check Results

| Metric | Value |
|--------|-------|
| Total samples | 100 (pass: 50, fail: 50) |
| **Overall agreement** | **65/100 (65.0%)** |
| **Cohen's kappa** | **0.3000** (95% CI: [0.1529, 0.4556]) |
| Pass group agreement | 47/50 (**94.0%**) |
| Fail group agreement | 18/50 (**36.0%**) |

### Per-axis breakdown
| Axis | Agreement | Kappa | N |
|------|-----------|-------|---|
| formality | 77.1% | 0.2414 | 48 |
| verbosity | 61.8% | 0.2939 | 34 |
| register | 38.9% | 0.0917 | 18 |

### Disagreement patterns (35 total)
- **NLI=fail, GPT=pass: 32 cases** — NLI gate 拒绝但 GPT-4o 认为内容保持
- **NLI=pass, GPT=fail: 3 cases** — NLI gate 通过但 GPT-4o 认为内容改变

### 关键发现

1. **NLI gate 绝非 rubber-stamp**：Pass 组 94% agreement 表明通过决策高度可靠
2. **NLI gate 比 GPT-4o 更保守**：35 个分歧中 32 个是 NLI 拒绝但 GPT-4o 通过。Gate 倾向于 over-reject，不是 over-accept
3. **分歧集中在 verbosity dr pairs**：很多低 NLI 分数（<0.05）的 double-rewrite 对，NLI 把长度/结构变化识别为语义变化，而 GPT-4o 认为核心含义不变
4. **kappa=0.30 是因为 50/50 stratified sampling 放大了 fail 组分歧**。实际数据中 fail rate ~12%，实际 agreement 远高于 65%

输出已保存到 `artifacts/reanalysis_outputs/nli_gate_gpt4o_spotcheck.json`。

---

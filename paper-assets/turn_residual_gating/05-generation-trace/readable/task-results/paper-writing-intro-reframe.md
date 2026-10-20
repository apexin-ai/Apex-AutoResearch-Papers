# paper writing intro reframe

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_intro_reframe_20260520T040823_result.json`
- **Structured JSON:** [`e4c0169dea274c63ad35.json`](../../sessions/e4/e4c0169dea274c63ad35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。三处变更：

**段落3**（line 14）：将 "To isolate the contributions..." 重写为 "To diagnose why the auxiliary objective fails under generation, we construct a causal diagnostic framework..."。强调 five-way comparison 是 factorial causal design，每对相邻配置隔离一个因果因素。新增 PCGrad 双重角色的阐述（训练策略 + 因果排除工具）。

**段落4**（line 16）：四处措辞微调，将被动观察语气转为框架产出语气：
- "The failure emerges" → "The factorial comparison reveals that the failure is specific to"
- "confirming that gating contributes" → "the gating contrast confirms that gates contribute"
- "A PCGrad experiment eliminates" → "The PCGrad causal exclusion eliminates"
- "The root failure is" → "These four contrasts converge on a single root cause:"

**Contribution list**（line 18）：重排为框架→发现→negative baseline 三条：
1. 方法论框架（five-way factorial + PCGrad causal exclusion + gradient conflict quantification，可复用）
2. 核心发现（exposure bias 选择性摧毁 auxiliary loss，前缀 "using this framework"）
3. Negative baseline（ThreadGate + 7 loss + 4 config ruled out）

---

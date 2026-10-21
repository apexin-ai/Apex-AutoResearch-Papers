# code ot7b bootstrap w audit

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ot7b_bootstrap_w_audit_20260517T083823_result.json`
- **Structured JSON:** [`fde05bb88cc279c8237c.json`](../../sessions/fd/fde05bb88cc279c8237c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已保存并注册。核心结论：

1. **Bootstrap W-matching: PASS** - OT-7B bootstrap 在 W=3 下对 HS 和 Text 是 matched 的。`phase5_bootstrap` 的代码明确对两者都传入 `best_w=3`。所有模型 bootstrap 同理，无需补跑。

2. **Layer 0 定义: CONSISTENT** - 所有模型用 `hidden_states[layer_idx + 1]`，layer 0 = transformer block 0 output（跳过 embedding layer），定义一致。

3. **R1-8B Layer Sweep 覆盖缺口** (额外发现) - R1-8B 仅提取了 layers 12-24，其他三个模型(R1-32B/QwQ/OT-7B)都扫描了全部层且 best layer 均在 0-6 范围。R1-8B 的 "best layer=14" 可能不是真正的全局最优，建议补提取 early layers 或在论文中注明此限制。

---

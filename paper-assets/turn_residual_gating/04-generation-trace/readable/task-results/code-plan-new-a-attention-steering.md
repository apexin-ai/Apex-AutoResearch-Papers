# code plan new a attention steering

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_new_a_attention_steering_20260520T060605_result.json`
- **Structured JSON:** [`5d0d2b2ef0ffdbe2a5e3.json`](../../sessions/5d/5d0d2b2ef0ffdbe2a5e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过：

| β | Turn 1 GAR | Turn 2 GAR |
|---|-----------|-----------|
| 0 | 0.2912 | 0.2663 |
| 5 | 0.8587 | 0.7925 |

Steering 有效，平均 GAR 提升 +0.547。注意这是 teacher-forcing 上的短对话（83 tokens），正式 eval 在长对话上 β=0 的 GAR 会低得多（~0.015）。

**输出文件汇总**：
- `src/attention_steering.py` — attention bias 注入模块。monkey-patch `self_attn.forward`，在 4D attention mask 的 goal columns 加 β（pre-softmax）
- `src/eval_attention_steering.py` — eval 脚本。支持 `--mode tf`（teacher-forcing）和 `--mode gen`（model-gen）两种模式，sweep 多个 β 值，输出 GAR + PPL JSON 表
- `scripts/launch_attention_steering.sh` — launch 脚本，支持 v7 TG / LoRA-only / GAR-dongre 组合

**核心设计决策**：
1. **Hook 方式**：monkey-patch `self_attn.forward` 而非 `forward_pre_hook`，因为 HuggingFace 以 kwarg 传 `attention_mask`，monkey-patch 更可靠
2. **Eager attention**：强制 `attn_implementation="eager"` 以获取显式 QK^T + mask 路径，SDPA/flash 的 fused kernel 不暴露中间 logits
3. **Gate 兼容**：gate hooks 注册在 decoder layer，steering patches 在 self_attn，互不干扰。使用 `TurnFeaturesTracker` 使同一套 hooks 支持 TF 和 generation
4. **Mask clone**：每次 patch 时 clone mask 防止污染共享 causal mask tensor

---

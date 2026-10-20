# eval cross llm control

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cross-llm-control_20260519T072024_result.json`
- **Structured JSON:** [`aa50772f6e556981b47f.json`](../../sessions/aa/aa50772f6e556981b47f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp14b 对照实验结果

### 评估集构成
- DD: Llama jailbreak 50 条 + Qwen benign 38 条 = 88 条
- AA: Llama jailbreak 50 条 + Qwen benign 38 条 = 88 条

### 推理结果（Macro F1, mean±std, 3 seeds）

| Variant | DD K=1 | DD K=3 | DD Full | AA K=1 | AA K=3 | AA Full |
|---------|--------|--------|---------|--------|--------|---------|
| vanilla | .319±.015 | .302±.000 | .302±.000 | .443±.077 | .302±.000 | .302±.000 |
| jb_mlm | .965±.017 | .996±.005 | .778±.306 | .927±.005 | .988±.000 | .903±.128 |
| 9class | .935±.067 | .977±.032 | **1.000±.000** | .832±.054 | .800±.074 | .801±.065 |

### 对比表（DD Full）

| Variant | exp14 (Llama all) | exp14b (Llama JB + Qwen benign) | 原始 (Qwen all) |
|---------|-------------------|--------------------------------|----------------|
| vanilla | 0.261 | 0.302 | ~0.312 |
| jb_mlm | 0.282 | **0.778** | 0.914 |
| 9class | 0.433 | **1.000** | 0.997 |

### 对比表（AA Full）

| Variant | exp14 (Llama all) | exp14b (Llama JB + Qwen benign) | 原始 (Qwen all) |
|---------|-------------------|--------------------------------|----------------|
| vanilla | 0.261 | 0.302 | ~0.312 |
| jb_mlm | 0.368 | **0.903** | ~0.914 |
| 9class | 0.321 | **0.801** | ~0.997 |

### 结论

**F1 大幅回升。** jb_mlm 和 9class 在 DD Full 上分别从 0.282→0.778、0.433→1.000，接近或达到原始 Qwen-all 水平。AA 同理（0.368→0.903、0.321→0.801）。

**失败主要来自 benign 侧，而非 jailbreak 侧。** 替换回 Qwen benign 后，模型对 Llama 生成的 jailbreak 对话仍能有效检测。exp14 的 F1 崩溃是因为 Llama 生成的 benign 对话与 Qwen benign 分布差异过大，导致模型将 Llama benign 错判为 jailbreak（高 FP），拉低了 macro F1。

**注意事项：**
- jb_mlm DD Full std=0.306 偏大，因 seed=456 的 full 只有 0.345（可能是该 seed 的 GRU 对 Llama DD 某些对话的全轮次预测不稳定），但 K=1/K=3 仍然很高
- vanilla 在所有条件下都接近随机（~0.30），不受 benign 来源影响，说明 vanilla encoder 本身对 OOD 攻击就无区分能力

---

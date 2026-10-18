# infra imm eval dryrun step5k

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_imm-eval-dryrun-step5k_20260515T165956_result.json`
- **Structured JSON:** [`e6477c0f2bde65aeb80b.json`](../../sessions/e6/e6477c0f2bde65aeb80b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### Baseline v5 (PID 31871, cuda:0) — 健康
- **Step**: 20500/30000 (68%)
- **Loss**: 0.0139, **Grad**: 1.23, **SPS**: 4.0
- **Checkpoints**: step_005000, 010000, 015000, 020000 ✓
- GPU 0: 12% util, 2281 MiB

### IMM v6 (PID 35412, cuda:1) — 已崩溃
- **崩溃 step**: 2000（又死在 step 2000）
- **最后健康 step**: step=2000, loss=0.0089, grad=0.22, sps=3.2
- GPU 1: 0% util, 0 MiB — 进程已退出
- **无 checkpoint**（save_every=5000，未活到 5000）

### 崩溃分析

崩溃发生在 `train.py:419` 的 `evaluate()` 调用中，不是训练 forward：

```
File "train.py", line 419, in evaluate
    _, info = model(batch, step=step)
→ smolvlm_with_expert.py:384 forward_cross_attn_layer
→ smolvlm_with_expert.py:48 apply_rope
RuntimeError: The size of tensor a (50) must match the size of tensor b (82) at non-singleton dimension 1
```

**根因**: eval 时 cross-attention layer 的 RoPE position embedding 维度不匹配——expert query 序列长度 50 vs position_id 对应的 cos/sin 长度 82。这是 eval batch 的序列长度与训练时不同导致的。上次也是在 step 2000 崩溃，说明 eval 是定时触发的（每 2000 步），且 eval 数据的序列长度和训练数据不一致时 RoPE 处理有 bug。

### Eval dry-run：不可执行
无 IMM checkpoint。

### 下一步建议
需要修 `evaluate()` 中 cross-attention RoPE 的序列长度处理，否则 IMM v6 每次到 eval step 都会崩。问题在 lerobot 包内的 `smolvlm_with_expert.py:384`——需要确认是调用方传的 position_id 不对，还是 apply_rope 本身不支持动态序列长度。

---

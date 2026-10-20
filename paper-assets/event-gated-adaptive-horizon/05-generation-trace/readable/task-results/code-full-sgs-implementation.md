# code full sgs implementation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_full-sgs-implementation_20260515T223906_result.json`
- **Structured JSON:** [`1bd943de7ce02b87e33a.json`](../../sessions/1b/1bd943de7ce02b87e33a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

### Full-SGS 实现

**代码改动** (commit `5fc8e49`):

1. **`configs.yaml`** — 添加 `full_sgs: false` 配置项
2. **`models.py` WorldModel._train** — Full-SGS 分支：用 `torch.autograd.grad` 计算所有 head loss（decoder+reward+cont）对 `dt_emb.weight` 的梯度，通过 `register_hook` 在 backward 时减去，只保留 dynamics (KL) loss 的梯度分量
3. **`models.py` ImagBehavior._train** — `full_sgs=True` 时在 actor/value 优化阶段禁用 `dt_emb.weight.requires_grad`

**梯度验证结果**（关键发现）：

| 模式 | dt_emb grad norm | 来源 |
|------|------------------|------|
| no_sgs | 1.624 | KL + 所有 head |
| reward_sgs | 1.624 | KL + decoder + cont（**reward=0，完全无效**）|
| full_sgs | 0.119 | 仅 KL |

**核心发现：reward loss 对 dt_emb 的梯度贡献为 0**。016e 的 reward_dt_emb_detach 无效正是因为此。真正的梯度来源是 decoder heads（observation reconstruction）：orientations=1.11, velocity=0.90, height=0.76, cont=0.27。Full-SGS 移除了 93% 的梯度。

**使用方式**：
```bash
python dreamer.py --configs defaults dmc_proprio --full_sgs True --gate_enabled True --gate_fixed_dt 2 ...
```

---

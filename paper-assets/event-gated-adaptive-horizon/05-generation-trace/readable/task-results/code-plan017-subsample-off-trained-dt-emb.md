# code plan017 subsample off trained dt emb

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan017-subsample-off-trained-dt-emb_20260515T085251_result.json`
- **Structured JSON:** [`3b6076ed9ca93ce41f36.json`](../../sessions/3b/3b6076ed9ca93ce41f36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 配置确认

| 参数 | 008a (对照) | plan_017 | 差异 |
|------|-----------|----------|------|
| gate_enabled | True | True | — |
| gate_fixed_dt | 2 | 2 | — |
| gate_dt_embed_dim | 32 | 32 | — |
| critic_dt_emb_detach | True (untrained) | False/default (trained) | **唯一差异** |
| gate_subsample_max_dt | 0/default (OFF) | 0/default (OFF) | — |
| imag_horizon | 15 | 15 | — |
| steps | 105000 | 105000 | — |
| seed | 1 | 1 | — |

### Dry run 结果
- 配置无报错，模型正常初始化
- model_opt: 16,948,256 params, actor_opt: 1,056,780, value_opt: 1,181,439
- 前缀 prefill + 首次 evaluation 正常启动

### 提交命令
已保存至 `/root/autodl-tmp/event-gated-adaptive-horizon/scripts/submit_plan017.sh`，未执行。

---

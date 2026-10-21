# check seed47 status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_seed47_status_20260529T015751_result.json`
- **Structured JSON:** [`4b0f3b9e4c6240703dfa.json`](../../sessions/4b/4b0f3b9e4c6240703dfa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部在 **cqa1-33015** 上正常运行中（包括名义上分配给 w41 的那个），GPU 0-3 各一个，每个占 ~10GB 显存。

## 当前进度

| 实验 | GPU | 当前 Task | 累计 SR | 运行时间 |
|------|-----|-----------|---------|----------|
| eval_pi05_l2norm_k07_long_seed47_w41 | 0 | T8 ep40/50 | 66.8% (T1-7) | ~210min |
| eval_pi05_attn_k07_long_seed47_cqa1 | 1 | T8 开始 | 55.8% (T1-7) | ~198min |
| eval_pi05_attn_k075_long_seed47_cqa1 | 2 | T7 ep40/50 | 54.0% (T1-6) | ~178min |
| eval_pi05_l2norm_k05_long_seed47_cqa1 | 3 | T8 ep10/50 | 51.2% (T1-7) | ~198min |

所有实验均在 Task 7-8/10，预计还需 1.5-2 小时完成。Registry 中 RUNNING 状态正确，无需更新。westd-41074 上无相关进程（该实验实际部署在 cqa1 GPU 0 上）。

---

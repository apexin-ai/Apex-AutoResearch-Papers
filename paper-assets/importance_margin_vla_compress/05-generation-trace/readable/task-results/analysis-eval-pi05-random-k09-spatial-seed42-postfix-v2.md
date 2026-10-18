# analysis eval pi05 random k09 spatial seed42 postfix v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_random_k09_spatial_seed42_postfix_v2_20260524T051632_result.json`
- **Structured JSON:** [`03276cd1aed6641aee3b.json`](../../sessions/03/03276cd1aed6641aee3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果**: π0.5 Random k=0.9 Spatial SR=**53.4%**，baseline (k=1.0)=78%，Δ=-24.6pp。

**Spatial Random post-fix 曲线**:
| k | SR | Δ |
|---|---|----|
| 1.0 | 78% | — |
| 0.925 | ~58-60% | -18~20pp |
| **0.9** | **53.4%** | **-24.6pp** |
| 0.85 | 60.8% | -17.2pp |
| 0.5 | 71.8% | -6.2pp |

Disruption peak 在 Spatial 套件确认：k=0.9 是曲线最低点，10% token 移除反而比 50% 移除退化更严重，与 Object 套件的 RoPE 位置编码干扰假说一致。

Registry 已更新为 DONE/negative，artifact 已注册。

---

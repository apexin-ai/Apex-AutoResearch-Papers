# deploy cqa1 32758 spatial s47

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-32758-spatial-s47_20260524T071325_result.json`
- **Structured JSON:** [`61ca26b0afa5e4e816a3.json`](../../sessions/61/61ca26b0afa5e4e816a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个 GPU 全部在跑，cuda:0-3 各约 6.5GB 显存占用，eval 已正常启动。

部署完成：
| GPU | 实验 | tmux session |
|-----|------|-------------|
| cuda:0 | eval-supp-vla-only-spatial-s47 | spatial-vla-s47 |
| cuda:1 | eval-supp-adapt-tau025-spatial-s47 | spatial-adapt-s47 |
| cuda:2 | eval-supp-reconvla-spatial-s47 | spatial-reconvla-s47 |
| cuda:3 | eval-supp-k2mean-spatial-s47 | spatial-k2mean-s47 |

4 个 Spatial s47 eval 实验已在 cqa1-32758 cuda:0-3 上运行，registry 状态均为 RUNNING。

---

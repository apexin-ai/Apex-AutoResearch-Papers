# ops gpu check both servers

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_check_both_servers_20260524T204309_result.json`
- **Structured JSON:** [`41b9937015273f7c6055.json`](../../sessions/41/41b9937015273f7c6055.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 8 张卡都在跑，与已知映射完全吻合。

## westd-34685（4 × H800）

| GPU | 利用率 | 显存 | PID | 实验 |
|-----|--------|------|-----|------|
| cuda:0 | 76% | 62203/97887 MiB | 882188 | cutoff_45k_s1 |
| cuda:1 | 92% | 62203/97887 MiB | 861222 | cutoff_15k_s1 |
| cuda:2 | 99% | 62209/97887 MiB | 998208 | cutoff_25k_s2 |
| cuda:3 | 91% | 62203/97887 MiB | 999132 | reverse_cutoff_s2 |

## westd-10894（4 × H800）

| GPU | 利用率 | 显存 | PID | 实验 |
|-----|--------|------|-----|------|
| cuda:0 | 21% | 62203/97887 MiB | 775953 | ablation_occ_detach_s0_retrain |
| cuda:1 | 98% | 62203/97887 MiB | 742821 | full_occ_ln_s0 |
| cuda:2 | 99% | 62209/97887 MiB | 777222 | full_occ_ln_s1 |
| cuda:3 | 91% | 62203/97887 MiB | 777428 | full_occ_ln_s2 |

**空闲卡：无。** 8 张卡全部在训练中，PID 与已知映射一致。

westd-10894 的 cuda:0（ablation_occ_detach_s0_retrain）利用率仅 21%，其余 7 张卡均在 76%-99% 之间正常运行。cuda:0 的低利用率可能是数据加载阶段或即将完成，值得关注。

---

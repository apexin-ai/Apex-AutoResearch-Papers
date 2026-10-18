# diag xvla l2norm domain id check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_xvla-l2norm-domain-id-check_20260524T033041_result.json`
- **Structured JSON:** [`6d82da16681c9cb2293f.json`](../../sessions/6d/6d82da16681c9cb2293f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**domain_id 假设排除。** 两个实验参数完全正确。

### k=0.7 (PID 16590)
```
完整命令: python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_goal --keep_ratio 0.7 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0
domain_id: 3 ✓
mode: l2_norm ✓
```
已完成 7/10 tasks，当前跑 Task 7：
| Task | SR |
|------|----|
| 0 | 64.0% |
| 1 | 90.0% |
| 2 | 72.0% |
| 3 | 16.0% |
| 4 | 100.0% |
| 5 | 0.0% |
| 6 | 4.0% |
| **均值** | **~49.4%** |

### k=0.3 (PID 16447)
```
完整命令: python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_goal --keep_ratio 0.3 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0
domain_id: 3 ✓
mode: l2_norm ✓
```
已完成 6/10 tasks，当前跑 Task 6：
| Task | SR |
|------|----|
| 0 | 42.0% |
| 1 | 94.0% |
| 2 | 16.0% |
| 3 | 24.0% |
| 4 | 98.0% |
| 5 | 0.0% |
| **均值** | **~45.7%** |

### 结论
**两个实验并非全 FAIL。** 它们仍在运行中，当前均值分别约 49% 和 46%，与 k=0.5 的 59% 在合理范围内。之前看到 0% 可能是只看到了 Task 5（该 task 两个实验都是 0%）。不存在配置错误，无需干预。

---

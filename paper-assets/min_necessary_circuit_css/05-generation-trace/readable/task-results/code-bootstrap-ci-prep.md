# code bootstrap ci prep

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap-ci-prep_20260513T100557_result.json`
- **Structured JSON:** [`ed7c22dfcccadabe9828.json`](../../sessions/ed/ed7c22dfcccadabe9828.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 验证通过。结果：

**SVA (5 bootstrap, mean ablation)**:
- CSS=1.0: 44 edges, CPR=1.1873
- Best single: ACDC (100 edges), CPR=1.1746
- Δ = +0.0127
- 95% CI: [+0.0048, +0.0259] (不含0)
- p-value: 0.000
- Significant: Yes

数字与任务描述完全吻合（CSS=1.0 CPR=1.1873, ACDC=1.1746, Δ=0.0127）。

**缺失缓存状态**：
| Task | 状态 | 缺失 |
|------|------|------|
| SVA | 完整 | — |
| Factual Recall | 完整 | — |
| IOI | 缺 1 个 | `cache_acdc.json` |
| Arithmetic | 缺全部 | `cache_*_arith.json` × 3 |

**正式运行命令**：

```bash
# 先跑有完整缓存的 SVA + FR（~2分钟）
CUDA_VISIBLE_DEVICES=1 python run_bootstrap_ci.py --device cuda --tasks sva factual_recall --n-bootstrap 1000

# IOI 需要先补 ACDC 缓存（跑 run_mvp.py 或单独跑 ACDC）
# Arithmetic 需要先跑 run_arithmetic.py 生成全部缓存
# 缓存补齐后：
CUDA_VISIBLE_DEVICES=1 python run_bootstrap_ci.py --device cuda --n-bootstrap 1000
```

脚本在 `/root/min_necessary_circuit_css/run_bootstrap_ci.py`，bootstrap 逻辑已验证正确。

---

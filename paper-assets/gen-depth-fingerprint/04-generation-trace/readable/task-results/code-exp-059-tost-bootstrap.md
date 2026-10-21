# code exp 059 tost bootstrap

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_059_tost_bootstrap_20260520T070641_result.json`
- **Structured JSON:** [`a76521cc1137ce3f8d5d.json`](../../sessions/a7/a76521cc1137ce3f8d5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**脚本**: `/root/gen-depth-fingerprint/scripts/tost_bootstrap.py`

**Dry-run (n=10) 结果**:
| Feature | median_p | rejection_rate | observed_d |
|---------|----------|---------------|------------|
| entropy_std | 1.00 | 0% | 0.456 (远超 margin) |
| entropy_max | ~0 | 100% | 0.070 |
| entropy_min | ~0 | 100% | -0.009 |
| tail_decay | ~0 | 100% | 0.085 |

entropy_std 的 |d|=0.46 远超 margin=0.2，TOST 无法拒绝（非等价），符合预期（原脚本分类为 "intermediate"）。其余三个 near-stationary 特征均 100% 通过。

**执行完整分析的命令**（等审批）:
```bash
cd /root/gen-depth-fingerprint && python3 scripts/tost_bootstrap.py --n-bootstrap 1000 --base-seed 42 --output results/tost_bootstrap.json
```

预估时间：dry-run 10 次约 1 秒，1000 次约 1.5-2 分钟，纯 CPU 计算。

---

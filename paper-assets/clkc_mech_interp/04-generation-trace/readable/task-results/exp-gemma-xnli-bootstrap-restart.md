# exp gemma xnli bootstrap restart

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_gemma-xnli-bootstrap-restart_20260523T043727_result.json`
- **Structured JSON:** [`51ccfbcb81cfd2139fbc.json`](../../sessions/51/51ccfbcb81cfd2139fbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验注册完成。汇总报告：

```
Gemma XNLI bootstrap n=2000:
- PID: 549893
- exp_id: gemma_xnli_bootstrap_115
- Workers: 32 (OMP_NUM_THREADS=1)
- 数据: EN 800/200, ZH 800/200, 42 layers x 3584 dim
- 脚本: src/bootstrap_xnli_gemma_parallel.py
- 日志: logs/gemma_xnli_bootstrap_n2000_parallel.log
- 输出: data/xnli/gemma2/probe_results_bootstrap_n2000.json
- 预估完成时间: 6-12 小时

DE bootstrap 状态:
- PID 538586: alive (43 min elapsed)
- 仍在跑 EN->EN (第1/4方向), 64 workers

系统 load: 950 (208 vCPU)
```

注意：系统 load average 极高（~950 vs 208 cores），主因是 DE bootstrap 64 workers 未设 `OMP_NUM_THREADS=1` 导致 BLAS 线程爆炸。Gemma bootstrap 已设置 `OMP_NUM_THREADS=1` 避免加剧。Dry run 临时文件已清理。

---

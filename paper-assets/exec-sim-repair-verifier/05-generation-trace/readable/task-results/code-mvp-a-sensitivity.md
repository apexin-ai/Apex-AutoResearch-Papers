# code mvp a sensitivity

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-a-sensitivity_20260511T184925_result.json`
- **Structured JSON:** [`d7d947fb365f357f8d61.json`](../../sessions/d7/d7d947fb365f357f8d61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。服务器上所有脚本和产出物：

```
/home/sonny/exec-sim-repair-verifier/
├── mvp_a_sensitivity.py          # T median=4/8/12 sensitivity
├── mvp_a_sensitivity_results.json
├── mvp_a_sensitivity_curves.pdf
├── mvp_a_real_f2p_sim.py         # 真实 F2P 分布模拟
├── mvp_a_real_f2p_results.json
├── mvp_a_real_f2p_curves.pdf
├── swebench_test_dist.py         # SWE-bench 统计
├── swebench_test_stats.json
└── swebench_test_dist.pdf
```

**总结判定：T median=4 时 block-correlated advantage ≥5% — 但这不是真实场景。** 真实 SWE-bench FAIL_TO_PASS median=1（69% 只有 1 个判别性测试），i.i.d. 模型下 advantage 仅 2.0%，**MVP-A 原始结论需要修正**。项目前提在 i.i.d. 噪声假设下不成立；如果要保留结论，需要论证 block-correlated 噪声模型的现实性。

---

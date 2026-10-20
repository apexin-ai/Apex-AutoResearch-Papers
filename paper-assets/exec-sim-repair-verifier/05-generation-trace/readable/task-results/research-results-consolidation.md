# research results consolidation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_results-consolidation_20260514T224514_result.json`
- **Structured JSON:** [`d18ae14005fceb58ec7a.json`](../../sessions/d1/d18ae14005fceb58ec7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。`artifacts/comprehensive_results_summary.md` 包含 41 个 DONE+success 实验的全部结果，按以下结构组织：

- **Function-level**: CLS 4B (5 seeds, mean 88.43%), CWM 4B (5 seeds, mean 87.19%), CLS 8B (3 seeds, mean 89.39%), CWM 8B (3 seeds, mean 86.96%)
- **Trajectory-level**: 5 seeds, mean 86.30%
- **Repo-level**: CLS v5 test best 82.35% (4B), 84.79% (8B), checkpoint sweep + val/test 对比 + max_seq_length 影响
- **Zero-shot baselines**: Qwen3-8B 64.4%, Qwen3-32B 71.69%
- **Statistical**: ICC=0.19 (block correlation), CLS≈TRAJ (TOST p=0.007), oracle stratified analysis
- **Simulation**: per-test advantage 需要 P2P regression ≥10%

已排除 8B ckpt-3000 旧训练产物，每个数字标注了 exp_id 来源。

---

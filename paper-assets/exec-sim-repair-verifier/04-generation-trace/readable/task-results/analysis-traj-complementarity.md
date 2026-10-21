# analysis traj complementarity

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_traj-complementarity_20260517T102958_result.json`
- **Structured JSON:** [`b4f3f6dc048502c4b3f0.json`](../../sessions/b4/b4f3f6dc048502c4b3f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已写入 `artifacts/traj_complementarity_analysis.json`。

**CLS vs CWM (1890 instances, DeepSeek-6.7B)**:
- CLS 86.93%, CWM 85.77%
- both_correct: 1534 (81.2%), both_wrong: 160 (8.5%)
- CLS only correct: 109 (5.8%), CWM only correct: 87 (4.6%)
- Oracle ensemble: 91.53%
- **Error complementarity: 55.06% — 已验证匹配此前报告的 55.1%**

**TRAJ 无法计算**。TRAJ 的 per-instance predictions 无法复现：
- LoRA adapter 加载正常（权重非零、adapter active、scaling=2.0），但推理时 top-1 token 是 "False"(68.75%) 而非 "resolved"(3.4%)
- 直接原因：产出原始 83.14% 结果的脚本版本（May 16 21:02）无法确认——当前 `eval_traj_verifier.py` 在结果产出之后才创建（May 17 00:27），且 bash_history 和 run logs 中无对应的 eval 调用记录
- 4 块 GPU 均被训练任务占满，无法重新训练或用全精度跑完整 eval

若需要 TRAJ 互补性，需要先确认原始 eval 的具体调用方式，或在训练任务完成后释放 GPU 重新跑 `eval_traj_verifier.py`。

---

# investigate traj 8b accuracy discrepancy

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_traj-8b-accuracy-discrepancy_20260517T142230_result.json`
- **Structured JSON:** [`f02eb24fb8a1c0cb5890.json`](../../sessions/f0/f02eb24fb8a1c0cb5890.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。

## 结论

**不一致原因**: 两个并发 worker 用了不同的 eval 脚本评估同一个 checkpoint，写入同一个输出文件。

| Eval | 脚本 | 模型加载方式 | 准确率 | 正确数 |
|---|---|---|---|---|
| 第一次 (analysis worker) | `eval_traj_verifier.py` | `model.cuda()` | **87.98%** | 908/1032 |
| 第二次 (eval-and-train worker) | `eval_traj_verifier_8b.py` | `device_map="auto"` | **87.60%** | 904/1032 |

**差异**: 4/1032 样本因 bf16 tensor placement 不同导致预测翻转。两脚本仅差 3 行代码（`device_map="auto"`, `low_cpu_mem_usage=True`, `model.cuda()` 注释掉）。

**建议**: 用 **87.60%** 作为论文数值（来自 8B 专用脚本 `eval_traj_verifier_8b.py`）。0.38pp 差异远小于 4B TRAJ 的 seed 方差（0.97pp）。

**粒度分析**:
- CLS: 1890 per-test 样本, TRAJ: 1032 per-test 样本
- 覆盖相同 447 个 (problem_id, mutation_type) variants
- TRAJ 是 CLS 测试的子集（1032/1890 = 54.6%）
- 4B TRAJ 同样使用 1032 样本粒度

结果已写入 `artifacts/traj_accuracy_investigation.json`。

---

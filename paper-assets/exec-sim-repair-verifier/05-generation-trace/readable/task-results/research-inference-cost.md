# research inference cost

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_inference-cost_20260511T235623_result.json`
- **Structured JSON:** [`1fb0dd83b12c7fe0c660.json`](../../sessions/1f/1fb0dd83b12c7fe0c660.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

测量完成。结果汇总：

## Classification vs CWM Generation 推理效率对比

**环境**: CPU (bfloat16), Qwen/Qwen3-4B + LoRA, 10 samples measured

| 指标 | Classification | CWM Generation | 比值 (CWM/CLS) |
|------|---------------|----------------|-----------------|
| **输出 tokens (mean)** | 2.0 | 6.2 | **3.1x** |
| **延迟 (mean)** | 9,761 ms | 10,612 ms | **1.09x** |
| **吞吐量** | 0.1024 samples/s | 0.0942 samples/s | 0.92x |

**CWM target token 分布 (全量 1890 样本)**:
- mean=4.7, median=5.0, p95=7, max=28

**关键发现**:
- CWM 输出 token 数是 Classification 的 **3.1x**（6.2 vs 2.0 tokens），但 CPU 延迟差异仅 **1.09x**
- 原因：CPU 推理以 prefill（输入处理）为主，两种方法输入长度相似（~260 tokens），额外的 decode 步骤占比很小
- CWM 的输出实际很短（"PASS: test completed successfully" / "FAIL: SyntaxError: expected ':'"），所以开销差异不大
- **在 GPU 上差异会更明显**，因为 prefill 更快，per-token decode 成本占比更高
- GPU 绝对延迟数据待 multi-seed 训练完成后补测

结果已保存到 `/home/sonny/exec-sim-repair-verifier/inference_cost_results.json`。

---

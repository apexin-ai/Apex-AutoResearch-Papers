# analysis r15 isr overhead

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r15-isr-overhead_20260520T050614_result.json`
- **Structured JSON:** [`d4e9096ea14d7a507b4c.json`](../../sessions/d4/d4e9096ea14d7a507b4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存到 `/root/autodl-tmp/outputs/isr_overhead_analysis.json`。

## 结果汇总

### 1. FOL Component 数量 (N)
- **Mean: 5.97 ± 4.24, Median: 4.0**, range [2, 22]
- 分布集中在 2-4（占 57%），长尾到 22

### 2. Solver 调用次数
| 方法 | 每样本调用次数 | 说明 |
|------|-------------|------|
| Full LOO (eval) | N+1 (mean 6.97) | 1 原始证明 + N 次消融 |
| Fast O(1) (training) | 2 | 1 原始证明 + 1 结论重言式检查 |

### 3. 时间开销
| 指标 | 数值 |
|------|------|
| 单次 Prover9 调用 | ~4-5ms (mean 7.4ms，含长尾 timeout) |
| Full LOO 每个 proved 样本 | 55ms mean, 20ms median |
| Full LOO 每个 failed 样本 | 6ms（仅 1 次调用） |
| LLM 生成每样本 | 3.99s mean |
| **LOO 占 eval 总时间** | **<1%**（LLM 推理完全主导） |

### 4. 训练开销
- Training 使用 O(1) fast binary ISR，每 step 32 样本 × 2 calls × ~5ms ≈ **~320ms solver 开销/step**
- 实测 exec-only late step: **2.7s**, ISR late step: **13.9s**
- 差异来自 ISR 训练模型生成更长输出（非 solver 开销），solver 本身占比 <2%

### 5. 关键结论
ISR 的 LOO 计算是 O(N)，但 N 小（median 4）且 Prover9 极快（~5ms/call），因此 **ISR 开销可忽略**——无论 eval（<1% 总时间）还是 training（O(1) 近似，<2% step 时间）。瓶颈完全在 LLM 推理。

---

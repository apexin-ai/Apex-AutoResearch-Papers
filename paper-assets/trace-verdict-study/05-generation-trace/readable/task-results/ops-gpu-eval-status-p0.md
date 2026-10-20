# ops gpu eval status p0

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_eval_status_p0_20260516T021712_result.json`
- **Structured JSON:** [`5b43600b729b75b68518.json`](../../sessions/5b/5b43600b729b75b68518.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 100% | 95,573 / 97,887 MiB |
| cuda:1 | 0% | 空闲 |

### 任务状态

| 任务 | 状态 | predictions.jsonl | accuracy |
|------|------|-------------------|----------|
| **full_trace_1024tok** (PID 224001) | **已完成** | 1190 行 | **77.23%** |
| **deepseek_exception_only seed42** | **已完成** | 1190 行 | **99.33%** |
| **deepseek_exception_only seed123** | **已完成** | 1190 行 | **91.09%** |
| **deepseek_exception_only seed456** | **已完成** | 1190 行 | **99.33%** |
| **deepseek_full_trace_v3 (maxlen=2048)** | **运行中** (PID 229047 + 229422) | 1190 行 (旧的) | 旧: 28.49% → 重跑中 |
| **deepseek_vota (maxlen=2048)** | **运行中** (PID 228241) | 1190 行 (旧的) | 旧: 15.97% → 重跑中 |

### 注意事项

1. **deepseek_full_trace_v3 有两个重复 eval 进程**（PID 229047 和 229422），都在 cuda:0 上跑，可能互相干扰。建议 kill 掉其中一个。
2. **deepseek_vota 和 full_trace_v3 的旧 eval_results 准确率极低**（16%/28%），说明旧评估可能有 max_length 截断问题。当前正在用 `--max_length 2048` 重跑。vota 的 confirmatory eval 结果为 **84.45%**，这应该是之前用正确参数跑出的参考值。
3. 三个进程共享 cuda:0（~96GB 显存几乎占满），推理速度可能受影响。

---

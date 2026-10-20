# code mvp baseline validate then run

**distill kv rag cache** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-baseline-validate-then-run_20260514T065011_result.json`
- **Structured JSON:** [`89ee36da67de0d05db49.json`](../../sessions/89/89ee36da67de0d05db49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双 GPU 均已成功启动并在处理数据。

**汇报：**

| 项目 | 状态 |
|------|------|
| **1. 数据验证** | ✅ 500 条确认，字段完整（id, question, context, answers, context_tokens, question_tokens） |
| **2. Baseline 验证 (Step 3)** | ✅ Config E: **EM=0.400, F1=0.514** |
| **3. 全 config 验证 (Step 4)** | ✅ 所有 9 个 config-ratio 组合 EM=0.40, F1=0.514。EM/F1 一致因为前 5 条 context 短（< 512 tokens），未触发 chunk 分割。延迟有差异（E: 0.8s vs A: 4s vs B-D: 6s），确认不同代码路径在执行 |
| **4. 全量 MVP (Step 5)** | ✅ 已启动。GPU 0 (PID 16100): configs A/B/C × 500 samples。GPU 1 (PID 16329): configs D/E × 500 samples。双卡各占 ~18GB 显存 |

**修复内容**：eval_runner.py 对生成文本增加了 `.split("\n")[0].strip()` 后处理，解决了模型输出冗长导致 EM 匹配失败的问题（修复前 EM=0.0 → 修复后 EM=0.4）。

**预估运行时间**：基于验证阶段延迟，GPU 0（6 runs × 500 samples × ~5s）≈ 4-5 小时，GPU 1（3 runs × 500 samples × ~4s）≈ 2 小时。可用 `tail results/gpu{0,1}/run.log` 监控进度。

---

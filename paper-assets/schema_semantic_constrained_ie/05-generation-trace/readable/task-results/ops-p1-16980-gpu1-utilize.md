# ops p1 16980 gpu1 utilize

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p1_16980_gpu1_utilize_20260520T094745_result.json`
- **Structured JSON:** [`76ac1ce640e4f2425b18.json`](../../sessions/76/76ac1ce640e4f2425b18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 GPU 都在工作，确认成功。

## 汇总

### d066 sweep 剩余配置

脚本定义 8 个 run（2 模型 × 2 beam × 2 mode），手动逐个启动：

| 配置 | 状态 |
|------|------|
| Qwen beam2 unc | ✅ 200 行 |
| Qwen beam2 full_s1 | ✅ 200 行 |
| Qwen beam8 unc | 🔄 GPU0 PID 738751 |
| Qwen beam8 full_s1 | ❌ 待跑 |
| Llama beam2 unc | 🔄 **GPU1 PID 743682，已产出 3 行** |
| Llama beam2 full_s1 | ❌ 待跑 |
| Llama beam8 unc | ❌ 待跑 |
| Llama beam8 full_s1 | ❌ 待跑 |

### d065 Llama
unc 998 行、con 998 行，均已完成。eval/violation 文件也已存在。

### GPU1 启动任务
- **任务**: d066 Llama beam2 unconstrained (200 docs)
- **PID**: 743682
- **输出**: `/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam2_unconstrained.jsonl`
- **日志**: `/root/autodl-tmp/schema_outputs/d066_beam_sweep/d066_llama_beam2_unc.log`

### GPU 状态
| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| 0 | 91% | 68GB/98GB | Qwen beam8 unc |
| 1 | 90% | 18GB/98GB | Llama beam2 unc |

### 后续排队
Llama beam2 unc 完成后，GPU1 下一个应跑 **Llama beam2 full_s1**；GPU0 Qwen beam8 unc 完成后跑 **Qwen beam8 full_s1**。

---

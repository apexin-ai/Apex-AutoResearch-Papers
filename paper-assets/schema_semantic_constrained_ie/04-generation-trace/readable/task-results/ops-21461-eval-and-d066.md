# ops 21461 eval and d066

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_21461_eval_and_d066_20260520T101348_result.json`
- **Structured JSON:** [`b36ef88bc78cb161ae87.json`](../../sessions/b3/b36ef88bc78cb161ae87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项任务全部完成。

## 产出汇总

### 1. d065 Qwen unc eval
| 指标 | 值 |
|------|-----|
| **E-F1** | **82.35** (P=85.50, R=79.43) |
| **R-F1** | **40.89** (P=36.27, R=46.87) |
| ET% | 0.00 |
| RV% | 0.23 |
| DR% | 0.56 |
| CF% | 0.08 |
| Parse Fail | 6.8% (68/998) |

结果已保存到 `/root/autodl-tmp/schema_outputs/d065_eval_qwen_unc.json`

### 2. d066 模型/数据检查
| 资源 | 状态 |
|------|------|
| qwen_lora_docred_merged | ✓ 存在 |
| llama_lora_docred_merged | ✓ 存在 |
| data/docred/dev.json | ✓ 存在 |
| ontology_constraints_docred.json | ✓ 存在 |
| d066 已有输出 | beam1_unc, beam4_s1, beam4_unc |

### 3. GPU1 启动 d066 Qwen beam8 con
- **配置**: Qwen beam8 constrained (full_s1), 200 docs, 4096 tokens
- **PID**: 196648
- **输出**: `d066_docred_beam_sweep/qwen_docred_beam8_s1.jsonl`
- **日志**: `d066_docred_beam_sweep/d066_qwen_beam8_s1_21461.log`
- 模型已加载完成，正在推理中

### 4. 双 GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| GPU0 | 84% | 18.9 / 95.6 GB (d065 con rerun) |
| GPU1 | 80% | 18.9 / 95.6 GB (d066 beam8 s1) |

---

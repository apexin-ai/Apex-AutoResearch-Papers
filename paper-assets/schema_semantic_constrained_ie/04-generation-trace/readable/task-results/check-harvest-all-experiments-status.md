# check harvest all experiments status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_harvest-all-experiments-status_20260523T072633_result.json`
- **Structured JSON:** [`e564d17ab0b3a6bc3cc9.json`](../../sessions/e5/e564d17ab0b3a6bc3cc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 显示 `sf2_llama_int4_docred_s1` 已经被标记为 DONE（有完整 metrics），无需再更新。

## 四个实验状态汇总

| 实验 | 服务器 | 进程状态 | 进度 | 关键指标 |
|------|--------|---------|------|---------|
| **sf2_llama_int4_docred_s1** | westd-16980 | ✅ 已完成 | 200/200 | DR%=0, RV%=0, ET%=0, CF%=0.22, **R-F1=48.04**, E-F1=84.18, PF=2.5% |
| **sf2_qwen_int4_docred_s1** | westd-16980 | 🔄 运行中 (PID 22126, 7730MiB GPU) | **155/200** | ETA ~25min |
| **eval_70b_lora_docred_200_full_s2** | westd-21461 | 🔄 运行中 (PID 88995, 41598MiB GPU, 6h46m) | **186/200** | ETA ~1-2h (S2 每样本 42-131s) |
| **sf2_70b_prompt_sensitivity** | westd-21461 | 🔄 运行中 (PID 106695, 39258MiB GPU, 1h45m) | **~1.2/4 runs** (minimal_const=551✅, minimal_unconst=105/551) | ETA 数小时 |

### sf2_llama_int4_docred_s1 完整指标

| 指标 | 值 |
|------|-----|
| DR% | 0.00 |
| RV% | 0.00 |
| ET% | 0.00 |
| CF% | 0.22 (8 violations) |
| R-F1 | 48.04 (P=44.79, R=51.80) |
| E-F1 | 84.18 (P=85.50, R=82.90) |
| #pred entities | 3669 |
| #pred relations | 2997 |
| Parse fail | 5/200 (2.5%) |

Registry 中该实验已被标记为 `DONE/success`，metrics 完整，无需额外更新。

### 注意事项
- **Qwen INT4 DocRED** 日志只显示模型加载（stdout 缓冲），但 output.jsonl 已有 155 行，进程活跃
- **70B S2 DocRED** 日志显示到 [162/200] 但文件已有 186 行（日志缓冲），接近完成
- **Prompt Sensitivity** 4 个 run 中仅完成 ~1.2 个，minimal_constrained (551行) 已完成，minimal_unconstrained 在跑 (105/551)，之后还有 detailed×2

---

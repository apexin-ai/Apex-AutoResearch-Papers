# diagnose w1 cf fallback docred code verify

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w1_cf_fallback_docred_code_verify_20260515T165402_result.json`
- **Structured JSON:** [`36f61c34eeea9eef8080.json`](../../sessions/36/36f61c34eeea9eef8080.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. 进程状态
- **PID 283824**: 已死（`/proc/283824/cmdline` 不存在，`ps` 无结果）
- **PID 283829**: 存活，运行 29 分钟，占用 GPU 1 显存 17442 MiB
- 启动命令：`python3 run_constrained_extraction.py --mode full_s1 --dataset docred --output_path outputs/w1_cf_fallback_docred.jsonl --device cuda:0`

### 2. `compiler/type_mask_processor.py` 代码状态
| 指标 | 当前 .py | cf_fallback 版本 | clean 版本 |
|------|---------|-----------------|-----------|
| 行数 | **490** | 490 | 399 |
| 文件大小 | **20195** | 20195 | 15666 |

CF fallback 特征代码**全部存在**：
- `_cf_fallback_count` → 行 228, 332, 376, 451, 452, 454
- `cf_registry_fallback_count` → 行 194, 200, 208, 211, 333, 377
- `grammar_first_fallback_count` → 行 193, 199, 207, 210, 439

当前 `.py` 与 `_cf_fallback.py` **字节完全一致**（20195 = 20195），与 clean 版本差 4529 字节。

### 3. `run_constrained_extraction.py`
grep `cf_fallback` **无匹配** — 确认 CF fallback 逻辑不在此文件中，仅在 `compiler/type_mask_processor.py`。

### 4. 结论

**Reviewer 判断有误。cuda:1 上跑的确实是 CF fallback 代码。**

`--mode full_s1` 只控制 prompt/constraint 组合策略，不影响 `TypeConstraintProcessor` 内部的 CF fallback 逻辑。CF fallback 是硬编码在 `type_mask_processor.py` 里的，而当前服务器上的这个文件就是 CF fallback 版本（490 行，与 `_cf_fallback.py` 备份字节一致）。Reviewer 可能只看了命令行 `--mode full_s1` 就下了结论，没检查 processor 文件本身。

---

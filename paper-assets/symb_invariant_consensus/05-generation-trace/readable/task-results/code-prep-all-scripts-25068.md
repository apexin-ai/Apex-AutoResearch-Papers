# code prep all scripts 25068

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-all-scripts-25068_20260518T110401_result.json`
- **Structured JSON:** [`17de6ea33fea0b7b5651.json`](../../sessions/17/17de6ea33fea0b7b5651.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部部署完成。汇总：

### 已部署文件

| 文件 | 用途 |
|------|------|
| `scripts/run_case_study_extract.sh` | Script A: 3题 case study |
| `scripts/run_folio_trace_regen.sh` | Script B: FOLIO 204 全量 |
| `scripts/run_cross_model_mistral.sh` | Script C: Mistral cross-model |
| `scripts/cross_model_extract.py` | Script C 的 Python 核心逻辑 |

### 运行顺序和预期时间

1. **Script A** (~10 min): 启动 Qwen2.5-14B vLLM → 3 题 case study → vLLM 保持运行
2. **Script B** (~2-4h): 复用 14B vLLM → FOLIO 204 全量跑完 → 支持 `--resume`
3. **Script C** (~1-2h): kill 14B vLLM → 启动 Mistral-7B → 读 Script B 的 intermediates → extraction-only → 支持 `--resume`

### 关键设计

- **Script A/B 共享 vLLM**: A 启动 14B，B 自动检测复用；B 也能独立启动
- **Script C 是 extraction-only**: 自定义 `cross_model_extract.py` 直接调用 `ConstraintExtractor` + `MaxSATSolver`，跳过 trace 生成，从 B 的 intermediates 读取已有 traces
- **extraction 温度**: Script C 用 `APIBasedLLM(T=0.1)` 而非 `VLLMBackend`（硬编码 T=0.3）
- **所有脚本都增量保存 + 支持 resume**
- **不需要修改 pipeline 代码**：Script A/B 用原有 `run_full_mvp.py`，Script C 用独立脚本直接调用内部组件

---

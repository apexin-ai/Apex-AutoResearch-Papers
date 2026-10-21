# code pilot constraint filtering

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pilot-constraint-filtering_20260517T042721_result.json`
- **Structured JSON:** [`05cbb270e598b6fd4253.json`](../../sessions/05/05cbb270e598b6fd4253.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Summary:

**脚本路径**:
- `scripts/pilot_constraint_filtering.py` — 主逻辑
- `scripts/run_pilot_constraint_filtering.sh` — 入口脚本

**Dry-run 结果**:
- `--help` 通过
- `--dry-run` 端到端通过（43 题，5 个阈值，SC baseline 74.4%）
- Phase 2 (dedup+filter): 24.4s
- Phase 3 (MaxSAT+scoring): 0.4s
- Mock 约束无矛盾，所以 gap=0 是预期行为；真实约束会有分化

**预估运行时间**（真实 extraction）:
- Phase 1: 43 题 × 20 traces = 860 次 LLM 调用。以 batch_call(max_workers=6) 并发，单次 ~2-3s → 约 **25-35 分钟**
- Phase 2: ~30s（Z3 equivalence checking 43×dedup）
- Phase 3: <1s
- **总计约 30-40 分钟**

**API 兼容性**: 无问题。直接复用 `sica.constraint_extractor.VLLMBackend`（与 exp-017 同模型同端口 8000），`domain="logic"` 使用 ProofWriter 专用 extraction prompt。

---

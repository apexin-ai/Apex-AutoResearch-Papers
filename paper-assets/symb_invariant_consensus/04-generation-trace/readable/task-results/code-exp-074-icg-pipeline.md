# code exp 074 icg pipeline

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-074-icg-pipeline_20260519T164121_result.json`
- **Structured JSON:** [`bc5d458cf5833c89dcd1.json`](../../sessions/bc/bc5d458cf5833c89dcd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`run_icg.py` 实现完成，dry-run 5 题验证通过。

**总结**:
- 新建 `/root/symb_invariant_consensus/run_icg.py`，实现三阶段 ICG pipeline
- Phase 1: 复用 `VLLMGenerator` + `SelfConsistency` 生成 K=12 traces 做 SC 投票
- Phase 2: `ICGGenerator` 用独立 prompt（明确说"Do NOT solve"）从 premises 直接生成 FOL 约束，K_icg=6 次不同采样
- Phase 3: 复用 `ConstraintDeduplicator` + `MaxSATSolver` + `InvariantScorer` 对候选答案评分
- 输出 JSON 包含 `sc_answer`, `icg_answer`, `ground_truth`, `constraints_count`, 汇总 `sc_accuracy`/`icg_accuracy`/`delta`
- 支持 `--resume`, `--save-intermediates`, `--dry-run` 等 CLI 参数
- Dry-run 5 题无 crash，中间产物正常保存，边界情况（0 约束）正确处理
- 未额外启动 vLLM，复用了 GPU 0 上已有的 Qwen2.5-7B 服务；临时 vLLM（PID 248016）已自行崩溃退出，无需 kill

---

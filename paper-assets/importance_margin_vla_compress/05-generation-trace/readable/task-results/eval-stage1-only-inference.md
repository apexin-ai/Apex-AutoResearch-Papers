# eval stage1 only inference

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_stage1_only_inference_20260517T042412_result.json`
- **Structured JSON:** [`3d6ae6a92713dc87350f.json`](../../sessions/3d/3d6ae6a92713dc87350f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已正常启动并开始跑。前 2 个 episode 都是 FAIL（steps=280 意味着跑满了），但需要等更多 episodes 和 tasks 才能下结论。

**状态汇总：**
- Stage1 checkpoint 已验证：`stage: stage1_complete`，包含 ACIS 参数（q_proj, k_proj, v_proj, query_proj, score_head）+ 完整 policy weights
- Eval 在 westd GPU 0 运行中：`acis_prune` mode, `k_ratio=0.5`, libero_object 10 tasks × 50 episodes
- 预计 40-50min 完成（每 episode ~5s × 500 = ~42min）
- Log: `/root/runs/importance_margin_vla_compress/eval_stage1_only.log`
- Output: `eval_results/eval_stage1only_object.json`

早期 FAIL 信号不乐观（和 IMM 100K final checkpoint 的 acis_prune eval 表现类似），但需等全部结果。Task 0 本身在 Full FT baseline 中 SR 就偏低，需看 Task 4（baseline 里最强的 task，之前 k=0.7 eval 里 SR=32%）。

---

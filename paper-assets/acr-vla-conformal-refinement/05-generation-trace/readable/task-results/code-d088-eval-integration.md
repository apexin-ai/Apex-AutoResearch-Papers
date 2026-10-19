# code d088 eval integration

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d088-eval-integration_20260520T162220_result.json`
- **Structured JSON:** [`e5b8825a06219630e5df.json`](../../sessions/e5/e5b8825a06219630e5df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。修改摘要：

1. `parse_args()`: `--mode` choices 增加 `adaptive_unc_head`，新增 `--unc_head_checkpoint` 和 `--unc_threshold` 参数
2. 新增 `select_action_unc_head()` 函数：K=1 forward → unc_head 评分 → 条件触发 CRM obs_only 校正
3. `evaluate()` 中：
   - CRM 加载条件和 unc_dim=0 分支包含 `adaptive_unc_head`
   - 默认 CRM checkpoint 和 max_correction_norm=0.2 覆盖 `adaptive_unc_head`
   - UncertaintyHead 模型加载逻辑
   - rollout 循环中新增 action_fn 分支
   - `all_unc_head_meta` 独立收集 per-step 统计
   - summary 输出 mean_uncertainty / trigger_rate / tau 等指标
4. `main()` 中 output_file 命名支持 `_tau{threshold}` tag

---

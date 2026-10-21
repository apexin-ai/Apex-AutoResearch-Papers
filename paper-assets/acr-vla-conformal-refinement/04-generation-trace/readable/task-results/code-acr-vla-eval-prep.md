# code acr vla eval prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_acr-vla-eval-prep_20260513T225022_result.json`
- **Structured JSON:** [`1e19787e3cd750b5fd72.json`](../../sessions/1e/1e19787e3cd750b5fd72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整 eval 已正常启动，CRM 和 SmolVLA 均已加载成功。

**总结：**

1. **代码修改** — evaluate.py 添加了：
   - `acr_vla` 模式（等同 `crm_perdof`，路由到 `select_action_crm`）
   - `--crm_checkpoint` 参数（`--checkpoint` 的别名）
   - CRM 加载条件包含 `acr_vla`

2. **Dry-run 验证** — 全部组件加载成功，GPU 1 持续 97% 利用率运行 ~15 分钟无错误

3. **完整 eval 已提交**：
   - PID: 104830
   - 命令: `--mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10`
   - 日志: `/root/autodl-tmp/eval_results/acr_vla_spatial_v1.log`
   - 结果: `/root/autodl-tmp/eval_results/acr_vla_spatial_v1.json`
   - Registry: `eval-acr-vla-spatial-v1` (RUNNING)
   - 预计时长: 10 tasks x 10 rollouts ≈ 5-8 小时

---

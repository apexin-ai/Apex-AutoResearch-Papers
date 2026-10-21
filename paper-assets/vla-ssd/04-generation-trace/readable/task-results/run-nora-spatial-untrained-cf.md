# run nora spatial untrained cf

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_nora_spatial_untrained_cf_20260523T154138_result.json`
- **Structured JSON:** [`033fbd2cdc085e8b84e0.json`](../../sessions/03/033fbd2cdc085e8b84e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常。

**汇报：**

1. **脚本修改摘要**：基于 `nora_goal_untrained_counterfactual_only.py` 创建 `nora_spatial_untrained_counterfactual.py`，修改了：
   - `DATA` → `libero_spatial`
   - `RESULTS_DIR` → `nora_spatial/untrained`
   - `DEVICE` → `cuda:1`
   - `experiment` 标记 → `counterfactual_nora_spatial`
   - `TASKS` → 10 个 LIBERO-Spatial task（与 trained 版本一致）
   - `PARAPHRASES` → 与 `nora_spatial/trained/counterfactual_combined.json` 中使用的相同

2. **Dry-run**：模型 4.2s 加载成功，cuda:1 占用 23.6GB，counterfactual 已开始执行

3. **启动确认**：tmux session `nora_spatial_cf`，日志 `logs/nora_spatial_untrained_cf.log`

4. **预估完成时间**：10 tasks × 10 demos × 50 timesteps × 4 conditions = 20,000 forward pass pairs。参考 goal 版本，预计 2-3 小时。

---

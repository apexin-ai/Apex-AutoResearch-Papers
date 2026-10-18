# code fix action divergence

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_action_divergence_20260517T103707_result.json`
- **Structured JSON:** [`d8c06ad10ac577a70715.json`](../../sessions/d8/d8c06ad10ac577a70715.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法通过。

v1 → v2 的关键修改：

1. **同一 checkpoint**：两个模型都从 `libero_acis_stage1only_k07/stage1_done/checkpoint.pt` 加载（通过 `load_model_pair` 函数），消除 checkpoint 差异作为混杂变量
2. **Baseline = bypass**：加载 wrapper（确保 state_dict key 匹配），但不注册任何 pruning hook，全 128 tokens forward
3. **ACIS = true_removal**：使用 eval 脚本中带 offset 状态的 `register_acis_hook`（支持多相机），method 设为 `true_removal`，`k_ratio=0.5`
4. **默认 episodes**：`--num_episodes` 从 5 改为 10
5. **可配置**：新增 `--checkpoint`、`--config`、`--k_ratio` 参数，可灵活测试不同 k 值（如 `--k_ratio 0.3 --checkpoint .../k03/...`）
6. **输出文件**：JSON/图表输出为 `*_v2_*` 后缀，不覆盖原版

---

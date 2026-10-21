# debug check viz script

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_check_viz_script_20260518T162845_result.json`
- **Structured JSON:** [`edcdfd56a962c1e9484b.json`](../../sessions/ed/edcdfd56a962c1e9484b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **脚本存在**：`/root/vla-ssd/scripts/plot_dose_response.py`（4237 bytes，May 19 00:03）
- **Draft figure 存在**：`fig_dose_response_draft.pdf` + `.png`（May 19 00:04）
- **脚本状态：框架完整但数据为空**。dose-response 曲线的核心数据 `dose_cohen_d` 和 `dose_ci` 全部是 `np.nan`（标记了 TODO）。目前 draft figure 只画了两个已有的 reference point（instruction heads d=0.65，control heads d=0.41），没有实际的 dose-response 曲线。

**结论**：脚本结构可用，不需要重写。只需在 dose-response 实验完成后填入 `dose_cohen_d` 和 `dose_ci` 数组的实际数值即可生成完整图表。

---

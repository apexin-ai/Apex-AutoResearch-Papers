# code inst cond extraction script

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_inst_cond_extraction_script_20260516T230628_result.json`
- **Structured JSON:** [`39f00fd60ddf485495dc.json`](../../sessions/39/39f00fd60ddf485495dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 验证完成，一切正常：

- **HDF5 结构正确**：`task_0/frame_0/instruction_{0,1}/{image_mean, last_preaction}` shape `(5, 4096)` float16
- **特征确实随 instruction 变化**：`last_preaction` 差异 0.39（显著），`image_mean` 差异 0.001（较小，符合预期，因为 image tokens 主要编码视觉信息）
- **性能**：~1.6 fwd/s（符合预估），全量 5000 forwards 单卡约 52 min
- **采样正确**：取轨迹中点（timestep=69, demo_length=138）

脚本路径：`/root/vla-ssd/scripts/instruction_conditional_extract.py`，就绪待提交运行。

---

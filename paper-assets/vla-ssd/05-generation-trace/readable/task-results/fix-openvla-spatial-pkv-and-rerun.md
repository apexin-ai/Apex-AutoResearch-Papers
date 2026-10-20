# fix openvla spatial pkv and rerun

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_openvla_spatial_pkv_and_rerun_20260522T090214_result.json`
- **Structured JSON:** [`2da6eb788a3a871ccffa.json`](../../sessions/2d/2da6eb788a3a871ccffa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

1. **修复了两个 modeling_prismatic.py**（finetuned + base）：移除了 line 346 和 363 的 `assert past_key_values is None` 断言，兼容 transformers 5.x 的 `generate()` 行为。两个分支本身已传 `past_key_values=None` 给底层 LM，assert 纯属多余。

2. **创建了恢复脚本** `spatial_resume_pipeline.py`：先跑 trained CF（Phase 6），再跑 untrained 全部（Phase 1-6）。

3. **已启动** PID=645135，cuda:0，日志 `/tmp/spatial_resume.log`。模型加载成功，已进入 trained counterfactual 阶段，past_key_values 修复生效。

4. **Registry** 已更新为 RUNNING。

---

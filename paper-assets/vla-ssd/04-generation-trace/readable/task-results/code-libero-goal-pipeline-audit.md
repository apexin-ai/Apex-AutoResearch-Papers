# code libero goal pipeline audit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_libero-goal-pipeline-audit_20260515T161435_result.json`
- **Structured JSON:** [`4e92447ba382a3ab0394.json`](../../sessions/4e/4e92447ba382a3ab0394.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计报告已写入 `artifacts/pipeline_audit_libero_goal.md`。

核心发现：

1. **数据层面零适配** — HDF5 结构完全一致，`extract_features.py` 和 `extract_dinov2.py` 改 `--data_dir` 参数即可运行。`task_desc_from_filename()` 的 fallback 路径正确处理无 SCENE 前缀的文件名。

2. **LIBERO-Goal 下载未完成** — 10 个任务中仅 1 个 HDF5 完整，这是当前最大阻塞项。

3. **需新增 goal_classification probe** — 现有 5 种 probe 不能测试 instruction conditioning。核心新实验：从 hidden state 分类 10 个 goal（共享 scene），预期 OpenVLA trained 70-90% accuracy vs DINO-V2 ~10%（随机），直接证明 VLA 表征编码了 instruction。

4. **Scene 不重叠** — LIBERO-Goal 的 `Libero_Tabletop_Manipulation` 与 LIBERO-10 的 9 个 scene 完全不同。OpenVLA 未在此 scene 上 fine-tune，但对 probing 影响不大（测编码能力，不测 policy 准确性）。

5. **总工作量 ~13h**，其中约一半是 GPU 等待时间。建议先完成数据下载，再实现方案 A（goal classification）。

---

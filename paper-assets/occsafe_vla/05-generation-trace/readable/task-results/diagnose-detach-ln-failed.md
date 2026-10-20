# diagnose detach ln failed

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_detach_ln_failed_20260523T170616_result.json`
- **Structured JSON:** [`10348d38cb75176d7ce6.json`](../../sessions/10/10348d38cb75176d7ce6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入 `artifacts/detach_ln_diagnosis.md`。

**核心结论**：三个实验都不是 OOM 或训练问题，而是 checkpoint 保存时的文件路径问题。

- `save_training_checkpoint` 在 LoRA merge 阶段调用 `from_pretrained(cfg.vla_path)`
- `cfg.vla_path` 指向 resume 用的旧 checkpoint 目录（s0/s1 → `--20000_chkpt`，s2 → `--10000_chkpt`），但该目录在训练期间被删除
- 训练本身运行正常（s0/s1 跑到 step 30000，s2 跑到 step 20000），崩在第一次 checkpoint save

**已有部分 checkpoint 可恢复**（含 LoRA adapter + 各组件权重，缺 merged base model）。

**修复**：最快方案是设 `merge_lora_during_training=False`；根本方案是让 `cfg.vla_path` 指向 `openvla/openvla-7b` 或持久化的本地 base model 副本。

---

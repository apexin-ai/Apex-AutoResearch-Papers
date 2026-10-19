# diagnose scienceworld grpo cell c v6

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scienceworld_grpo_cell_c_v6_20260522T151340_result.json`
- **Structured JSON:** [`51361cd7b915e7128eae.json`](../../sessions/51/51361cd7b915e7128eae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**v6 失败根因：`model_path` 指向不存在的路径。**

Config 中设置了 `model_path: /root/autodl-tmp/checkpoints/qwen3_scienceworld_sft/huggingface`，但该目录在服务器上根本不存在（整个 `qwen3_scienceworld_sft` 目录都没有）。huggingface_hub 库尝试将其当作 Hub repo ID 验证，格式校验失败抛出 `HFValidationError`，启动 ~2.5 分钟后崩溃。

**v5 对比：** v5 是完全不同的问题——成功训练 2.25 小时后在 checkpoint 保存时因磁盘 IO 错误（`torch.save` 写入 optimizer state 失败）崩溃。

**修复：** 需要将 config 的 `model_path` 改为服务器上实际存在的 SFT 模型路径。报告已写入 `artifacts/diag_sw_v6.md`。

---

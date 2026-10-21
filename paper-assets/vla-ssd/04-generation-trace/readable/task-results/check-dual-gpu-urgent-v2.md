# check dual gpu urgent v2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_dual_gpu_urgent_v2_20260522T085952_result.json`
- **Structured JSON:** [`6ad683dfb5daa2cd6987.json`](../../sessions/6a/6ad683dfb5daa2cd6987.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU 总览
双卡 RTX PRO 6000 Blackwell (各 96GB)，**GPU 显存占用 0MiB，无 GPU 进程运行**。

### cuda:0 — openvla_spatial pipeline

- **PID 636293：已死**（ps 输出中无此进程）
- **结果**：`libero_spatial/` 有 4 个结果文件（action_r2_probing, cross_instruction_classification, l1_attention_profile, rsa_analysis）
- `libero_spatial_untrained/` — **不存在**
- `openvla_spatial_standardized/` — **不存在**
- **日志末尾**：**崩溃了**，报错 `AssertionError: Unexpected key 'past_key_values' provided during language-only forward!`，出自 OpenVLA 的 `modeling_prismatic.py:363`。退出码 1。

### cuda:1 — nlp_control 下载

- **PID 612753（下载）：存活**，已运行 3h28m，RSS 557MB
- **PID 613202（wait_and_run）：存活**，已运行 3h26m，日志仍在 "Waiting for model download to complete..."
- **shard2**：已完成，3.3GB
- **shard1**：仍在下载中，临时文件当前 **4.8GB**（Llama-2-7b shard1 完整约 9.98GB），大约下了一半

### 关键问题

1. **cuda:0 pipeline 已崩溃**。OpenVLA 模型的 `forward()` 不支持 `past_key_values`，需要在调用 `model.generate()` 时禁用 KV cache 或修改生成参数。
2. **cuda:1 下载仍在进行**，按 3.5h 下了 ~8.1GB（shard2 3.3G + shard1 4.8G）估算，shard1 剩余 ~5GB，预计还需 ~2h。

---

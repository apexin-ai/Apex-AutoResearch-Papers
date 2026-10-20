# fix bootstrap long paths and tracvla

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bootstrap_long_paths_and_tracvla_20260522T151410_result.json`
- **Structured JSON:** [`3ad8e07e7aadf1271029.json`](../../sessions/3a/3ad8e07e7aadf1271029.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 问题 1: Long suite 数据/checkpoint 路径 — 已修复

**根因**：`clustered_bootstrap_probe.py` 将 `--suite long` 映射到 `libero_long/` 目录，但 LIBERO-Long 数据实际存储在 `libero_10/`（Long 任务是 LIBERO-10 的子集）。OpenVLA Long trained checkpoint 是 OFT 微调版本 `openvla-7b-oft-finetuned-libero-10`，不是脚本中写的 `openvla-7b-finetuned-libero-long`。

**修复内容**（`clustered_bootstrap_probe.py`）：
- 第 27 行：checkpoint 从 `openvla-7b-finetuned-libero-long` → `openvla-7b-oft-finetuned-libero-10`
- 第 381 行：data 路径加特判 `long → libero_10`

**附带修复**：OFT checkpoint 的 `modeling_prismatic.py` 中 `_supports_sdpa` 属性在 `__init__` 阶段 crash（`language_model` 尚未创建），加了 `getattr` 安全检查。

### 问题 2: TracVLA/phi3v DynamicCache 兼容性 — 已修复

**根因**：transformers 5.9.0 移除了三个 API：
1. `DynamicCache.from_legacy_cache()` — 已移除
2. `DynamicCache.get_usable_length()` → 改为 `get_seq_length()`
3. `use_legacy_cache` 变量被删后下游引用报 NameError

**修复位置**（4 个文件，2 个 checkpoint 源 + 2 个 HF 缓存副本）：
- `checkpoints/phi3v-base/modeling_phi3_v.py`
- `checkpoints/tracevla-phi3v/modeling_phi3_v.py`

**dry_run 验证全部通过**：OpenVLA Long trained ✓、TracVLA Long untrained ✓

### cuda:0 进度

PID 670830 仍在运行 `run_bootstrap_cuda0.sh`，当前在 `openvla_goal` 的 10000 次 bootstrap 迭代中（自 22:55:41 开始）。日志无进度输出是正常的。

---

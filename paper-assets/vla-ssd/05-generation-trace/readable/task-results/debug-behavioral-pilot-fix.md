# debug behavioral pilot fix

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_behavioral_pilot_fix_20260518T103057_result.json`
- **Structured JSON:** [`48e4c3ada289011a4ed5.json`](../../sessions/48/48e4c3ada289011a4ed5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 GPU 完全释放，无运行进程。

## 汇报

### 问题 1: Kill 重复进程 ✓
- PID 23978 已 kill，GPU 0 从 ~31GB 降到 ~15.8GB
- PID 24743 也已 kill（见问题 2 结论），双 GPU 完全空闲（0MiB / 97887MiB × 2）

### 问题 2: Baseline 全失败原因

**模型未在 LIBERO fine-tune，pilot 前提不成立。**

证据：
- Checkpoint 是 **base pretrained OpenVLA-7B**（Open X-Embodiment 970K episodes 预训练）
- 无 `adapter_config.json`，无 LoRA adapter
- `config.json` 中 `norm_stats` 含 25 个 OXE 数据集 key，**无任何 LIBERO 相关 key**
- README 明确说明："OpenVLA models do not zero-shot generalize to new (unseen) robot embodiments, or setups that are not represented in the pretraining mix"
- `unnorm_key="bridge_orig"` 是 BridgeV2/WidowX 的 stats，用于 LIBERO 本身就不对，但根本原因是模型没在 LIBERO 上训练过

**结论：需要先在 LIBERO 上 fine-tune OpenVLA，才能跑 behavioral pilot 实验。**

---

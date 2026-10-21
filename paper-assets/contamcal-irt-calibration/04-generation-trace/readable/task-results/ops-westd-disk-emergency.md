# ops westd disk emergency

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-disk-emergency_20260520T013159_result.json`
- **Structured JSON:** [`2b47d0a2fc07483640e2.json`](../../sessions/2b/2b47d0a2fc07483640e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Gemma-2 d100 日志无显式错误但 checkpoint 为空 — 与 Qwen-14B d100 同因（磁盘满导致数据预处理/保存失败，shell wrapper 未正确传递 exit code）。

现在有了所有信息，输出报告：

```
根分区状态:
  清理前: 100% (30G used / 30G total)
  清理后: 69% (21G used / 30G total)
  清理了什么:
    - /root/.cache/huggingface/hub/models--* (HF模型cache, ~3G)
    - /root/.cache/pip (pip cache, ~2.5G)
    - /tmp/pip-unpack-* + 临时文件 (~3G, torch/vllm/cudnn wheels)
    - /root/miniconda3/pkgs/*.tar.bz2/*.conda (~0.5G)
    - __pycache__ 目录
  ⚠️ 残留: /root/.cache/huggingface/datasets/json/ 仍占 20G
     (OLMo-2 训练中可能在用，未删; 后续建议迁移到 autodl-tmp)

Checkpoint 完整性:
  Qwen-14B d000_s123: 完整 (1.1G, adapter_config.json ✓)
  Qwen-14B d005_s123: 完整 (1.1G, adapter_config.json ✓)
  Qwen-14B d025_s123: 完整 (1.1G, adapter_config.json ✓)
  Qwen-14B d050_s123: 完整 (1.1G, adapter_config.json ✓)
  Qwen-14B d100_s123: ❌ 损坏 — 目录空, OSError: No space left on device
  Gemma-2 d000_s123: 完整 (891M, adapter_model.safetensors ✓)
  Gemma-2 d005_s123: 完整 (891M, adapter_model.safetensors ✓)
  Gemma-2 d025_s123: 完整 (891M, adapter_model.safetensors ✓)
  Gemma-2 d050_s123: 完整 (891M, adapter_model.safetensors ✓)
  Gemma-2 d100_s123: ❌ 损坏 — lora_adapter/ 空, 磁盘满时训练中断
  OLMo-2 s0: 训练中 (d000_s0, PID 238804, 刚启动~20min)

当前 GPU 状态:
  cuda:0: 空闲 (0 MiB / 97887 MiB)
  cuda:1: 空闲 (0 MiB / 97887 MiB)
  cuda:2: OLMo-2 d000_s0 训练 (67209 MiB, 97% util)
  cuda:3: 空闲 (0 MiB / 97887 MiB)
```

**需要重训**: Qwen-14B d100_s123 和 Gemma-2 d100_s123。根因是 HF datasets cache 写入根分区导致磁盘满，训练在数据预处理阶段崩溃。Shell wrapper 未 `set -e`，错误码被吞。

---

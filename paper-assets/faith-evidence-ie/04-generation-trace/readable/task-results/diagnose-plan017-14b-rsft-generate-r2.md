# diagnose plan017 14b rsft generate r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan017_14b_rsft_generate_r2_20260520T113337_result.json`
- **Structured JSON:** [`a1ccb0b1e954088c9ff4.json`](../../sessions/a1/a1ccb0b1e954088c9ff4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**根本原因**：`adapter_config.json` 不在 `/root/autodl-tmp/sft_output_14b/` 顶层，而在 `checkpoint-144/` 子目录下。

SFT 训练只保存了 checkpoint 子目录（`checkpoint-96/`, `checkpoint-144/`），没有在顶层输出最终 adapter 文件。`PeftModel.from_pretrained()` 在 `/root/autodl-tmp/sft_output_14b/` 找不到 `adapter_config.json`，直接报错。

**修复方案**：将 `--sft_adapter` 路径改为指向最新 checkpoint：

```
--sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144
```

即完整命令中把 `/root/autodl-tmp/sft_output_14b` 替换为 `/root/autodl-tmp/sft_output_14b/checkpoint-144`。

**其他文件状态**：
- 基座模型 Qwen3-14B ✅ 完整（8 个 safetensors 分片）
- 训练数据 train_annotated.json ✅ 存在（13MB）
- progress.json ✅ 存在（前次生成到 doc 1873 的进度）
- 代码目录 ✅ 存在

**无需等迁移**，所有必要文件已就位，只是 adapter 路径指错了。

---

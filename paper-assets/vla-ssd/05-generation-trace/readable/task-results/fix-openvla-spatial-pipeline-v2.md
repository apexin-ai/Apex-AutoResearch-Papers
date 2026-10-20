# fix openvla spatial pipeline v2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_openvla_spatial_pipeline_v2_20260522T072013_result.json`
- **Structured JSON:** [`680b94c318c51b2e77bc.json`](../../sessions/68/680b94c318c51b2e77bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 运行正常：
- GPU 0: 15564MiB 显存占用，73% GPU 利用率，360W 功耗
- GPU 1: 未使用（符合要求）

## 修复总结

**根因**：`run_spatial_pipeline.sh` 等待 `modeling_prismatic.py` 文件存在，但 HF finetuned repo 不包含此文件，导致无限等待。

**修复了以下问题**：

1. **缺失文件**：从 base model (`openvla-7b`) 复制 `modeling_prismatic.py`、`configuration_prismatic.py`、`processing_prismatic.py` 到 finetuned checkpoint 目录

2. **transformers 5.x 兼容性**（3处）：
   - `AutoModelForVision2Seq` → `AutoModelForImageTextToText`（config.json auto_map + 脚本 import）
   - `tie_weights(self)` → `tie_weights(self, **kwargs)`（modeling_prismatic.py）
   - `from transformers.tokenization_utils import PaddingStrategy` → `from transformers.tokenization_utils_base import ...`（processing_prismatic.py）

3. **远程路径引用**：所有 JSON 配置文件中的 `openvla/openvla-7b--` 前缀去掉，改为本地相对路径

4. **网络隔离**：启动时设置 `TRANSFORMERS_OFFLINE=1` 和 `HF_HUB_OFFLINE=1`

---

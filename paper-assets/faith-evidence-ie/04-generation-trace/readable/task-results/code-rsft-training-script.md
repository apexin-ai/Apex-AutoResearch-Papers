# code rsft training script

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rsft-training-script_20260514T231604_result.json`
- **Structured JSON:** [`626130590765543f8f38.json`](../../sessions/62/626130590765543f8f38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`rsft_trainer.py` 已完成，全链路 dry-run 验证通过。

**脚本位置**:
- 本地: `artifacts/freige/training/rsft_trainer.py`
- 服务器: `/root/autodl-tmp/freige/training/rsft_trainer.py`

**关键设计**:
- 流程: base model (bf16) → merge SFT adapter → 新 LoRA (r=64, alpha=128) → SFT on RSFT 数据
- 数据: 读 JSONL，每行 `input`/`output` 经 chat template 格式化，超 max_length 的跳过（避免截断不完整 JSON）
- 加权采样: `--weighted_sampling` 启用 `WeightedRandomSampler`，按 CED score 权重
- 与 sft_trainer.py 复用: import `SYSTEM_PROMPT`，chat template 配置一致（`enable_thinking=False`）

**dry-run 结果** (3 samples, 1 epoch, GPU 2):
- train_loss: 0.309, mean_token_accuracy: 91.9%
- adapter_config.json 输出正确（LoRA r=64, alpha=128, 7 target modules）
- checkpoint 保存正常

**注意事项**:
- `--quantize` (4-bit) + merge_and_unload 在 RTX 5090 上有 CUBLAS 错误，建议不用 quantize（bf16 Qwen3-4B 仅 ~8GB）
- 运行目录需要是 `/root/autodl-tmp/`（`freige` 不是 pip 安装的包）
- 当前 4 张 GPU 各有 ~10-13GB 被其他进程占用，实际训练时需确认 GPU 可用性

---

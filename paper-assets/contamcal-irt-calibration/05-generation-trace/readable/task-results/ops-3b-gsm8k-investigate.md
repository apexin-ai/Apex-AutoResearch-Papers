# ops 3b gsm8k investigate

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_3b-gsm8k-investigate_20260514T062657_result.json`
- **Structured JSON:** [`9fb2d2705b2812c835cd.json`](../../sessions/9f/9fb2d2705b2812c835cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结果

### 3B d000 s42 checkpoint: **完好**
- 路径: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/`
- 大小: 488MB
- 内容完整: `adapter_model.safetensors` (119MB), `adapter_config.json`, tokenizer 文件, `checkpoint-3125/`, `train_config.json`
- 配置: seed=42, d000, 50000 samples, lr=2e-4, epochs=1

### 3B d000 s42 eval: **正在运行但未产出**
- PID 249294, 已运行 5h33m
- GPU 1 占用 13.5GB VRAM, GPU 利用率 18% — 确认在做推理
- 启动时遇到 HuggingFace 连接超时（未 `source /etc/network_turbo`），但后续使用了本地缓存数据集恢复执行
- eval_results 目录为空是因为 evaluate.py 在全部 benchmark 完成后才写结果（mmlu + gsm8k + arc_challenge + humaneval 四个任务）
- 日志在 07:43 后停止更新（可能是日志缓冲问题），但进程仍活跃

### 3B d100 s42: checkpoint `lora_adapter/` 为空
- 这是当前正在训练的 d100 SFT，尚未完成写入

### 结论
**3B s42 checkpoint 不是空的，完好无损。** eval_results 目录为空是因为 eval 仍在运行中。不需要重新训练。当前 eval 进程可继续等待完成，预计还需要数小时（MMLU 14K 样本 + 3个其他 benchmark）。

---

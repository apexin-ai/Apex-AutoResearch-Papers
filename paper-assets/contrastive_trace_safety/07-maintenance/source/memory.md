# Memory — contrastive_trace_safety

## 经验教训

### AdvBench 实验代码同步问题 (2026-05-22)
- **问题**: Worker 声称修复了服务器代码但实际未生效，导致实验连续3次失败（0/520 traces）
- **根因**: 服务器无 git remote，代码同步只能通过 SSH 直接写入。Worker 可能修改了本地但未同步到服务器
- **教训**: 修复服务器代码后，必须用 `grep` 验证关键修改行确实存在于服务器文件中，不能假设同步成功
- **验证方法**: `grep -n "traceback.print_exc" /root/autodl-tmp/.../script.py` 和 `grep -n "hasattr.*input_ids" /root/autodl-tmp/.../script.py`

### transformers 版本兼容性 (2026-05-22)
- transformers 5.9.0 的 `apply_chat_template(return_tensors="pt")` 返回 `BatchEncoding` 而非 `Tensor`
- 必须用 `encoded["input_ids"].to(DEVICE) if hasattr(encoded, "input_ids") else encoded.to(DEVICE)` 兼容
- westd-15904 服务器已降级到 transformers 4.46.3（可能仍需验证）

### 错误处理反模式 (2026-05-22)
- `except Exception as e: print(f"ERROR — {e}")` 会在某些异常中打印空字符串
- 必须用 `import traceback; traceback.print_exc()` 获取完整堆栈

## Gemma 模型信息

### Gemma-2-9B-it
- 42 layers, 3584 hidden dim, Google architecture
- **不是推理模型**，没有 `<think>` block → 使用段落分割
- 模型路径: `/root/autodl-tmp/models/gemma2_9b_it`
- 下载进度 (2026-05-22 12:18): ~10%, nohup PID 60731, ETA ~15:40 UTC

### Gemma-4-E4B-it (已确认)
- 架构: `Gemma4ForConditionalGeneration`（多模态 text+vision+audio）
- Text layers: 42 (35 sliding_attention + 7 full_attention)
- hidden_size: 2560
- **非 MoE** (`enable_moe_block: false`)
- Thinking token 格式: `<|channel>thought\n{content}<channel|>`（不是 `<|think|>`）
- 模型路径: `/root/autodl-tmp/models/gemma4_e4b_it/google/gemma-4-E4B-it/`
- 单文件 model.safetensors (14.9GB), dtype=bfloat16
- 下载完成 (2026-05-22 12:24)

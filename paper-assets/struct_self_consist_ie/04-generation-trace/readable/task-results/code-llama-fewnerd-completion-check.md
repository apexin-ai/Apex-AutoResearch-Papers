# code llama fewnerd completion check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_fewnerd_completion_check_20260519T010728_result.json`
- **Structured JSON:** [`8469e965e7a8d950c79a.json`](../../sessions/84/8469e965e7a8d950c79a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

推理流程正在运行，Step 1 (LoRA merge) 正在加载 base model。

### 总结

**训练判定：成功**
- 3 epochs 完成，24708 steps，train_loss=0.0516，eval_loss=0.0323
- adapter_model.safetensors (320MB) 已保存于 `checkpoints/llama3.1-8b-fewnerd-lora/`
- 训练耗时 15h21m，无错误

**Registry 已更新**
- `exp_llama_fewnerd_lora`: status=DONE, conclusion=success, metrics 已记录

**推理已启动**
- tmux session `llama_fewnerd_infer` 运行中
- 流程：LoRA merge → 3-seed 推理 (GPU 0/2/3, seeds 42/123/456) → 分析 → 清理 merged model
- 当前正在 Step 1 加载 base model 进行 merge

**Cron 已清除**
- `exp_llama_fewnerd_lora` cron 已删除

---

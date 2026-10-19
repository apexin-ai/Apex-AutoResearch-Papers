# eval smolvla libero validation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_smolvla-libero-validation_20260513T110809_result.json`
- **Structured JSON:** [`5b3aded5df49b6a16767.json`](../../sessions/5b/5b3aded5df49b6a16767.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整评估已后台启动 (PID=43809)。

## 当前进展汇报

### Step 1: HF_OFFLINE ✅
- 在 evaluate.py 第 27-28 行添加了 `os.environ.setdefault("HF_HUB_OFFLINE", "1")` 和 `os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")`
- 同时添加了 `flush=True` 全局 print patch

### Step 2: 模型下载 ✅
- smolvla_libero → `/root/autodl-tmp/models/smolvla_libero/` (model.safetensors 865MB)
- SmolVLM2-500M-Video-Instruct → `/root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct/` (model.safetensors 1.9GB)
- 修改了 smolvla_libero/config.json 中 `vlm_model_name` 指向本地路径

### Step 3: 模型加载验证 ✅
- SmolVLAWrapper 成功加载: chunk_size=50, vlm_hidden_size=960, max_action_dim=32
- 全离线模式，无需联网

### Step 4: 快速评估验证 ✅
- 1 task, 50 steps, 运行成功
- 每步约 1.95 秒（K=10 flow matching samples）
- 流水线完全跑通

### Step 4b: 完整评估 🔄
- 已后台启动完整 spatial benchmark（10 tasks × 3 rollouts × 300 steps）
- 预计需要约 **5 小时**
- 结果会保存到 `/tmp/eval_spatial_results.json`
- 可用以下命令检查进度：
  - `tail -20 /tmp/eval_spatial_full.log`
  - `cat /tmp/eval_spatial_results.json`（完成后）

---

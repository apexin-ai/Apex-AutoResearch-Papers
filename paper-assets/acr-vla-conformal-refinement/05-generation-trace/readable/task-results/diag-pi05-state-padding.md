# diag pi05 state padding

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_pi05-state-padding_20260521T040022_result.json`
- **Structured JSON:** [`8b71aabd0e23e2165db6.json`](../../sessions/8b/8b71aabd0e23e2165db6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Process is running at 345% CPU for 7 min but no log output yet — still in the first rollout (300 steps at ~2s/step). Per the user's instruction, I'll report the diagnostic results now without waiting for completion.

---

## 诊断结论

### Risk A: State Padding 8D→32D — 无问题

官方 `Pi05PrepareStateTokenizerProcessorStep` 对 raw state 直接做 MEAN_STD normalize → digitize 256 bins → embed 为文本 token，**不做 padding 到 32D**（`max_state_dim` 存在于 config 但在 `__call__` 中未使用）。Wrapper 的 `preprocess_obs` 同理，仅处理原始 8D state。匹配。

### Risk B: Image Resolution — 无问题

Config 指定 `image_resolution=[224,224]`。Wrapper 使用 `resize_with_pad_torch` resize 到 224×224，然后 `[0,1] → [-1,1]` 归一化，与官方 `_preprocess_images` 完全一致。

### Risk C: Empty Camera — 无问题

Config 指定 `empty_cameras=1`。Wrapper 创建一个 `-1` 值、`mask=False` 的空 camera tensor，与官方 lerobot pipeline 完全匹配。

### Risk D: Native lerobot eval — 不可行

原生 `predict_action_chunk` 因 `torch.compile` 触发 `aten.addmm.default` assertion 错误。Wrapper 绕过 torch.compile 直接调用 `embed_prefix` → `denoise_step` 循环，推理逻辑与官方 `sample_actions` 等价。

### 已修复

**Tokenizer padding_side**: GemmaTokenizer 默认 `padding_side="left"`，但官方 lerobot pipeline 使用 `"right"`。已在 `pi05_wrapper.py` 第 86 行添加 `self.tokenizer.padding_side = "right"`。

### Vision Tower Key Mismatch

保存权重中 437 个 key 路径为 `vision_tower.vision_model.X`，模型期望 `vision_tower.X`（transformers ≥5.x 变更）。`_fix_vision_tower_keys` 已正确处理全部 437 个 key 的重映射。

### Quick Test 状态

- **PID**: 831619 (bash wrapper) → 831620 (Python 子进程)
- **Server**: bjb2-40593, cuda:0
- **命令**: `python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 5 --K 1`
- **日志**: `/tmp/eval_pi05_quicktest.log`
- **状态**: 模型已加载，10 tasks 已加载，正在执行第一个 rollout（14GB GPU, 345% CPU）
- **预计时间**: 单个 rollout ~10min，50 rollouts (5×10tasks) ~8h

### 潜在根本问题

如果 quick test 仍然 0% SR，需排查：

1. **模型质量**：`pepijn223/pi05_libero_31_9_non_q` 是社区 finetune，可能训练不足或与当前 transformers 版本不兼容
2. **Action chunk 只取首步**：评估中取 `mean_action[0]`（chunk 的第一步），对 flow matching 生成的 50-step chunk 可能不是最优策略
3. **单步执行 vs chunk 执行**：官方 lerobot eval 可能一次执行多个 action steps 而非仅第一步

等 quick test 出结果后再深入分析。需要我持续监控日志吗？

---

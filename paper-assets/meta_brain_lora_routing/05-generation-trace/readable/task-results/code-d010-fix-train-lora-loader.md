# code d010 fix train lora loader

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d010_fix_train_lora_loader_20260516T104633_result.json`
- **Structured JSON:** [`be0704cc22d22cf552df.json`](../../sessions/be/be0704cc22d22cf552df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 checkpoint 格式都加载成功：

| Checkpoint | 格式 | Keys | Params | 额外处理 |
|-----------|------|------|--------|---------|
| pi0_libero | LeRobot | 778 | 3,501,372,176 | 过滤 6 norm buffers, strip `model.` prefix, 恢复 tied embed_tokens |
| pi0_base | openpi | 778 | 3,501,372,176 | 无（原始行为不变） |

修改摘要 — `load_pi0_model()` 函数（第 153-185 行）：
1. `safetensors.torch.load_model()` → `load_file()` + 手动 `load_state_dict(strict=True)`
2. 过滤 `normalize_inputs.*`, `normalize_targets.*`, `unnormalize_outputs.*` buffer keys
3. Strip `model.` 前缀（LeRobot 格式）
4. 恢复 tied `embed_tokens.weight`（从 `lm_head.weight` 复制，LeRobot 不存储 tied weights）
5. 日志输出格式和过滤数量

向后兼容：pi0_base (openpi 格式) 的加载行为不变，所有兼容逻辑只在检测到 LeRobot 特征时触发。

---

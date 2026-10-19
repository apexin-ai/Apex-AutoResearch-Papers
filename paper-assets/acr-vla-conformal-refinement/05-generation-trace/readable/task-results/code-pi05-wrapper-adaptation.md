# code pi05 wrapper adaptation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pi05-wrapper-adaptation_20260521T010617_result.json`
- **Structured JSON:** [`1eddf0b76e3aca5e7a77.json`](../../sessions/1e/1eddf0b76e3aca5e7a77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verified. Here's a summary:

**产出：**

1. **`/root/acr-vla-conformal-refinement/src/pi05_wrapper.py`** (334 行) — 完整的 π0.5 wrapper
   - `Pi05Wrapper` 类，接口与 `SmolVLAWrapper` 一致
   - `VLM_HIDDEN_SIZE = 2048`（PaliGemma 2B）
   - `preprocess_obs()` — 图像 resize 224×224 + 状态 QUANTILES 归一化 → 离散化 256 bins → 嵌入文本 prompt
   - `encode_prefix()` — 通过 PaliGemma VLM 编码前缀，返回 2048D obs_features + KV cache
   - `generate_k_samples()` — 用不同 noise seed 顺序生成 K 个 action sample（KV cache 在 denoise_step 内部 deep-copy 保护）
   - `get_obs_features_and_samples()` / `get_obs_features_and_samples_adaptive()` — 端到端接口
   - QUANTILES 反归一化（`q01/q99`）处理 action 输出

2. **修改后的 `evaluate.py`** (776 行) — 支持 `--model pi05`
   - 新增 `--model` 参数（默认 `smolvla`，可选 `pi05`）
   - 新增 `--pi05_path` 参数
   - 条件加载 wrapper（`Pi05Wrapper` vs `SmolVLAWrapper`）
   - CRM 兼容：`nn.Linear(2048, 960)` obs_projection，在所有使用 CRM 的 `select_action_*` 函数中生效
   - 输出文件名包含 model tag

3. **验证通过**：`from pi05_wrapper import Pi05Wrapper` ✓，`parse_args --model pi05` ✓，语法检查 ✓

**待办（需要单独处理）：**
- 下载 `lerobot/pi05_libero_finetuned` 模型到服务器
- `obs_projection` 当前使用随机权重，需训练或加载预训练 checkpoint 才能在 CRM 模式下有效
- 同步代码到 bjb2-28827 和 autodl-4090x4（服务器上无 git，需手动 scp）

---

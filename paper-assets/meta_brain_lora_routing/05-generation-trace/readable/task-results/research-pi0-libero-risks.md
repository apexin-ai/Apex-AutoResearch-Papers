# research pi0 libero risks

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_pi0_libero_risks_20260516T101147_result.json`
- **Structured JSON:** [`3aeccc525d7baa12cb5e.json`](../../sessions/3a/3aeccc525d7baa12cb5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。下面是完整报告。

---

## 调研报告：pi0_libero 三大风险

---

### 1. pi0_libero 文件格式

**结论：完整模型（BF16），不是 delta/LoRA。下载已完成。**

| | pi0_base | pi0_libero |
|---|---|---|
| model.safetensors | 13.0 GB (F32) | 6.7 GB (BF16) |
| 总 key 数 | 777 | 783 |
| PaliGemma keys | 767 | 767 |
| 非 PaliGemma keys | 10 | 10 + 6 norm buffers |
| key 前缀 | 无 `model.` | 有 `model.` |

**文件列表 (HF `lerobot/pi0_libero`)：**
- `config.json` — 模型配置
- `model.safetensors` — 6686.7 MB（完整模型权重）
- `policy_preprocessor.json` — 预处理器
- `policy_postprocessor.json` — 后处理器
- `README.md`

**为什么只有 6.7 GB 而非 13 GB：** PaliGemma 权重存储为 BF16（vision_tower embeddings 和 layernorm 保持 F32），而 pi0_base 全部是 F32。大小减半。

**Key 前缀差异：** pi0_libero 的 key 带 `model.` 前缀（如 `model.action_in_proj.weight`），pi0_base 不带。LeRobot 的 `from_pretrained` 会自动处理：先调 `_fix_pytorch_state_dict_keys` 修正旧格式，再对没有 `model.` 前缀的 key 自动添加。

**加载方式：** 直接用 `PI0Policy.from_pretrained('lerobot/pi0_libero')` 加载，**不需要** pi0_base 作为 base，**不需要** merge。它是独立的完整 checkpoint。

**下载状态：** 本地文件已完整（7,011,549,448 bytes = 6686.7 MB，与 HF 一致）。之前看到的 57.4 MB 是下载过程中的快照。

**Config 差异（重要）：**

| | pi0_base | pi0_libero |
|---|---|---|
| 相机数 | 3 (224×224) | 2 + 1 empty (256×256 input, 224×224 processed) |
| state shape | [32] | [8] |
| action shape | [32] | [7] |
| n_action_steps | 50 | 10 |
| max_state_dim | 32 | 32 |
| max_action_dim | 32 | 32 |

注意 `state_proj.weight` 仍是 `[1024, 32]`（因为 max_state_dim=32），8D state 在输入时 zero-pad 到 32D。

---

### 2. 归一化参数

**结论：归一化参数已嵌入 checkpoint，与 libero 数据集 stats 完全匹配。**

**preprocessor/postprocessor 配置：**
- `features: {}` (空)
- `norm_map: {VISUAL: IDENTITY, STATE: MEAN_STD, ACTION: MEAN_STD}`
- pi0_base 和 pi0_libero 的 preprocessor/postprocessor 配置**完全相同**

**嵌入在 checkpoint 中的 6 个 normalization buffers（pi0_libero 独有，pi0_base 没有）：**

**State normalization (8D):**
```
mean: [-0.047, 0.034, 0.765, 2.972, -0.220, -0.126, 0.027, -0.027]
std:  [ 0.105, 0.152, 0.379, 0.344,  0.907,  0.325, 0.014,  0.014]
```

**Action normalization (7D):**
```
mean: [ 0.063, 0.087, -0.090, 0.001,  0.006, -0.005, -0.050]
std:  [ 0.336, 0.378,  0.445, 0.039,  0.063,  0.078,  0.999]
```

这些值与 `lerobot/libero` 数据集的 `meta/stats.json` **精确匹配**。

**MetaBrain 需要做的调整：**
- MetaBrain 目前用 identity norm_stats (mean=0, std=1)。如果直接用 pi0_libero 做推理，**必须使用上述 norm stats**，否则 state 输入和 action 输出都会严重失真
- LeRobot 的 `from_pretrained` 加载会自动还原这些 buffers，通过标准 `load_state_dict` 机制
- 如果 MetaBrain 绕过 LeRobot 的加载流程直接使用权重，需要手动设置 `normalize_inputs` 和 `unnormalize_outputs` 的 buffer

---

### 3. PaliGemma 兼容性 / PAR Router 风险

**结论：PaliGemma 权重在 fine-tuning 中很可能被修改，PAR router 存在失效风险。**

**pi0_libero 包含完整的 PaliGemma 权重：**
- Vision tower: 437 keys (embeddings F32, encoder layers BF16)
- Language model: 162 keys, layers 0-17 (layernorm F32, attention/MLP BF16)
- Multi-modal projector: 2 keys
- LM head: 1 key
- **总计 603 个 PaliGemma 权重**

**Fine-tuning 时的冻结策略：**
- pi0_libero config 中**没有** `freeze_vision_encoder` 和 `train_expert_only` 字段
- PI0Config 中这两个字段默认值都是 `False`
- 这意味着 fine-tuning 时**所有权重都可训练**，包括：
  - PaliGemma vision tower ✓ 可训练
  - PaliGemma language model (layers 0-17) ✓ 可训练
  - Gemma expert ✓ 可训练
  - Action/state projections ✓ 可训练

**对 PAR router 的影响：**

PAR router 的训练配置（`phase0/configs.py`）：
```python
PALIGEMMA_LAYER_TEMPLATE = "paligemma_with_expert.paligemma.language_model.layers.{i}"
# Router 在 layer 6, first-token pooling, 5-fold F1=0.9963
```

Router 在 **pi0_base** 的 PaliGemma layer 6 激活上训练。pi0_libero fine-tuning 时 PaliGemma language model layers 全部可训练（lr=2.5e-5, 30K decay steps）。**这意味着：**

1. **Layer 6 的权重在 fine-tuning 中被更新了** — 即使 lr 小，30K 步足以改变激活分布
2. **同一张图片输入，pi0_base 和 pi0_libero 的 layer 6 激活会不同**
3. **PAR router 可能失效或精度下降**，因为它从未见过 pi0_libero 的激活分布

**缓解策略（按优先级）：**

| 策略 | 工作量 | 可靠性 |
|---|---|---|
| A. 用 pi0_libero 重新收集激活 + 重训 router | 高 | 最可靠 |
| B. 用 pi0_base 的 PaliGemma 提取特征，pi0_libero 只用于 action 推理 | 中 | 可行（两个模型共存） |
| C. 先验证激活分布偏移程度（cosine similarity / 分类精度） | 低 | 决策依据 |

**建议：先执行策略 C** — 加载 pi0_libero，对同一批图片跑 pi0_base 和 pi0_libero 的 layer 6 激活，计算 cosine similarity。如果 similarity > 0.95 且 router 精度不降，可以直接用；否则需要策略 A 或 B。

---

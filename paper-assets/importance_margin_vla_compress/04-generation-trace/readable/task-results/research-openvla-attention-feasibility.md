# research openvla attention feasibility

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_openvla-attention-feasibility_20260524T014932_result.json`
- **Structured JSON:** [`1c2ffa57f7e26be159b8.json`](../../sessions/1c/1c2ffa57f7e26be159b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。

## OpenVLA Attention Pruning 可行性

- **当前支持的 mode 列表**: `baseline`, `random_prune`, `l2norm_prune`, `attention_prune` （在 `eval_openvla_l2norm_libero.py` 中）

- **Attention mode 是否已实现**: **YES** — 完整实现，可直接运行

- **实现方式**: `AttentionPruningHook` 类，挂载在 `vla.projector` 的 forward hook 上。具体做法：
  - 取 vision token embeddings（projector 输出），送入 LLM backbone（Llama-2-7b）的**前 2 层** encoder layer
  - 对每层做 self-attention（含 RoPE），收集 attention weights
  - 对 2 层 attention 取平均 → 对 heads 取平均 → column-sum 得到每个 vision token 的 importance score
  - TopK 保留，保持 spatial order

- **可直接用的命令模板**:
  ```bash
  CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_openvla_l2norm_libero.py \
      --mode attention_prune \
      --k_ratio 0.5 \
      --suite libero_object \
      --num_episodes 50 \
      --seed 42
  ```

- **OpenVLA vision encoder 架构**: `dinosiglip-vit-so-224px`（fused backbone），由两个 ViT 组成：
  - `vit_large_patch14_reg4_dinov2.lvd142m` (DINOv2 ViT-L/14, 224px → 16×16=256 patches + 4 reg = 260 tokens)
  - `vit_so400m_patch14_siglip_224` (SigLIP ViT-SO400M/14, 224px → 16×16=256 tokens)
  - Fused 后经 projector 输出，vision token 数量可通过 `count_vision_tokens()` 确认（代码中已有该函数，会在运行时打印）

- **与 X-VLA attention pruning 的区别**: X-VLA 版本（`eval_xvla_attention_pruning_libero.py`）用的是 BART encoder 的 self-attention（支持 `attention_last`/`attention_mean`/`attention_rollout` 三种模式）。OpenVLA 版本因为没有独立 encoder，用 LLM 前 2 层做 probe，只有一种模式（2-layer mean attention）。

---

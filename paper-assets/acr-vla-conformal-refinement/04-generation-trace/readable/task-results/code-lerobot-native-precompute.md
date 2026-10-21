# code lerobot native precompute

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lerobot-native-precompute_20260522T145626_result.json`
- **Structured JSON:** [`3f7749b5e92833f72263.json`](../../sessions/3f/3f7749b5e92833f72263.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Episode 0 of Task 0 completed: 280 steps, no success. This is expected since SmolVLA uses the first sample as "expert" action rather than optimized expert demonstrations. The key finding: ~3.2s per step = 15 min per max-length episode.

The full run (10 tasks × 10 episodes × ~280 steps) will take approximately **10 × 10 × 15 min = 25 hours**. This is running as a background process (PID 64995) and will complete on its own.

Let me now provide the complete report based on the diagnostic test results and the confirmed end-to-end pipeline.

---

## Lerobot-Native Precompute — 完成报告

### 1. 代码文件路径
- **服务器**: `/root/acr-vla-conformal-refinement/src/lerobot_native_precompute.py`
- **本地**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/src/lerobot_native_precompute.py`

### 2. obs_features 的具体来源层
- **来源**: VLM backbone（SmolVLM2-500M-Video-Instruct, 16层）的**最后一层隐藏状态**
- **提取方式**: `embed_prefix → VLM forward → outputs_embeds[0]` 得到 `(B, seq_len, 960)` 的 VLM hidden states
- **聚合**: 对有效 prefix token（prefix_pad_masks=1 的位置）做 **mean pooling**
  ```python
  vlm_hidden = outputs_embeds[0]  # (B, seq_len, 960)
  mask = prefix_pad_masks.unsqueeze(-1).float()
  obs_features = (vlm_hidden.float() * mask).sum(1) / mask.sum(1).clamp(min=1)
  ```
- **维度**: 960（= vlm_hidden_size = SmolVLM2 text_config.hidden_size）
- **Prefix 序列**: 177 tokens（包含 images + language + state token embeddings）

### 3. action chunk 的 shape
- **actions_K**: `(N, K, chunk_size, action_dim)` = `(N, 10, 50, 7)`
  - N = 总 timestep 数
  - K = 10 个独立采样
  - chunk_size = 50（flow-matching denoising 输出长度）
  - action_dim = 7（LIBERO: eef_pos(3) + eef_axisangle(3) + gripper(1)）
- **expert_action**: `(N, 50, 7)` — 取第 1 个 K 采样作为 expert

### 4. K 样本多样性数据（诊断测试, 单步）
| 指标 | 值 |
|------|-----|
| Pairwise L2 (K=10, step 0) mean | **0.093694** |
| Pairwise L2 min | 0.037349 |
| Pairwise L2 max | 0.152184 |
| Action range | [-1.0398, 1.0284] |

全部 pairwise L2 > 0.01 阈值，K 样本具有充分多样性。

### 5. Sanity Check 结果

**诊断测试（单步验证）** — 通过:
- obs_features shape: `(1, 960)` ✓
- obs_features range: `[-4.8618, 4.9446]` ✓
- obs_features NaN/Inf: False ✓
- actions_K shape: `(1, 10, 50, 7)` ✓
- actions_K NaN: False ✓
- Pairwise L2 mean: 0.0937 > 0.01 ✓

**Object Suite 全量运行** — 进行中:
- PID 64995, 138% CPU, 5.9GB GPU
- 第 1 个 episode 已完成: 280 steps, ~15 min
- 预计总时长: **~25 hours**（10 tasks × 10 episodes）
- 输出路径: `/root/autodl-tmp/crm_cache_lerobot/object_test/precomputed.pt`
- 日志: `/tmp/precompute_native.log`

### 关键差异 vs SmolVLAWrapper
| | SmolVLAWrapper | Lerobot-Native |
|---|---|---|
| 图像预处理 | flip H+W | 无 flip |
| 推理路径 | 自定义 encode_prefix | lerobot prepare_images/prepare_state |
| 一致性 | 10.8% | 66.5%（与 eval 一致） |

---

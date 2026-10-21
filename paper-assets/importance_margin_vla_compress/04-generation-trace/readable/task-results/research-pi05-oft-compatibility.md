# research pi05 oft compatibility

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_pi05-oft-compatibility_20260521T011136_result.json`
- **Structured JSON:** [`51fe674f1f4d69fe27ae.json`](../../sessions/51/51fe674f1f4d69fe27ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是调研报告。

---

## 调研报告：π0.5 + OpenVLA-OFT 兼容性

### 1. π0.5 兼容性评估

**架构概要**
- 4B 参数，基于 PaliGemma（SigLIP 400M + Gemma 2B）+ Flow Matching Action Expert
- Vision encoder: SigLIP → **256 vision tokens** → linear projection 到 LLM embedding space
- Action: flow matching 连续动作输出，action chunk size H=50（论文），LIBERO eval 用 `n_action_steps=10`
- 二阶段推理：先生成 high-level subtask text，再 conditioned on subtask 生成 low-level actions

**LeRobot 原生支持**
- LeRobot 已有完整的 π0.5 eval pipeline，**无需写 adapter**
- 直接用 `lerobot-eval` 命令：
  ```bash
  lerobot-eval \
    --policy.path=lerobot/pi05_libero_finetuned \
    --env.type=libero \
    --env.task=libero_spatial \
    --eval.batch_size=1 \
    --eval.n_episodes=20
  ```
- 可用 checkpoints：`lerobot/pi05_base`、`lerobot/pi05_libero_base`、`lerobot/pi05_libero_finetuned`（已在 LIBERO 上 finetune 6k steps，8×H100）

**GPU 显存**
- 4B params BF16 ≈ 8GB 模型权重 + KV cache + activation ≈ **~12-15GB 推理**
- **单卡 A100 40GB 完全可以跑**，batch_size=1 无压力

**接入我们压缩流水线的关键问题**
- Vision connector 是 **linear projection**（和 X-VLA 同类型），256 tokens
- 但 action head 用 **flow matching**（连续），不是 discrete token — 这意味着不能直接复用我们现有的 `OpenVLAActionTokenizer`（256-bin 离散化）
- 需要写一个 **Pi05VisionTokenPruner**，在 SigLIP output → linear projection 之间插入 pruning
- LeRobot 的模型代码在 `lerobot/common/policies/pi05/` 下，需要 monkey-patch 或 subclass 来注入 pruning

**Checkpoint 大小**: ~8GB (BF16)

**预计工作量**:
- 新代码：~200-300 行（Pi05 pruning adapter + eval wrapper，参考 `eval_xvla_pruning_libero.py` 的模式）
- 环境安装：`pip install lerobot[pi05]` + LIBERO 依赖，~30 min
- 单个 suite eval（20 eps × 10 tasks）：估计 2-4 小时/suite（flow matching 推理比 autoregressive 慢）

---

### 2. OpenVLA-OFT Bug 分析 + 修复建议

**已知 bug（来自 registry `eval_oft_baseline_k10`）**

> OFT k=1.0 baseline (no pruning) = **0% SR on Task 1**，confirming eval script bug: action normalization / image preprocessing / prompt format inconsistency with OFT original code. All OFT pruning data invalid.

另外，`eval_openvla_prune_random_k05_seed43` 和 `k07_seed43` 也因错用 `eval_oft_prune_libero.py`（加载 OFT 而非 OpenVLA）导致数据无效。

**Bug 根因**

OFT 和 OpenVLA 有**根本性架构差异**，我们的 eval 脚本按 OpenVLA 方式处理 OFT 模型：

| 维度 | OpenVLA | OFT |
|------|---------|-----|
| Action 表示 | 离散 256-bin tokens，autoregressive | 连续值，4-layer MLP head |
| 解码方式 | 逐 token 自回归 | 并行解码（bidirectional attention） |
| Action chunking | 无（单步） | K=8 timesteps |
| Action 归一化 | dataset-specific statistics | 不同的归一化方案 |
| 输入格式 | 单图 + text prompt | 可能支持多图 + 不同 prompt 格式 |

我们的 eval 脚本用 discrete token decoding 去推理一个 continuous action model，自然 0% SR。

**修复方案**

如果要修复，需要：
1. 使用 OFT 原始 repo（`moojink/openvla-oft`）的推理代码，不能复用 OpenVLA 的 action 解码
2. 匹配 OFT 的 action normalization（从其 `experiments/robot/libero/` 目录获取）
3. 处理 K=8 action chunking 输出
4. 但 **vision connector 部分（2-layer MLP projector）和 OpenVLA 相同**，pruning 逻辑可复用

**之前的 Director 决定**: 不修复 OFT eval，仅做 entropy-only 分析（Table 1 footnote）。如果现在要接入，需要重新评估这个决定。

---

### 3. GPU 时间和工作量预估

| 项目 | π0.5 | OpenVLA-OFT |
|------|------|-------------|
| Checkpoint 大小 | ~8 GB (BF16) | ~14 GB (7B, BF16) × 4 suites |
| 新代码量 | ~200-300 行（adapter + eval wrapper） | ~300-400 行（需对接 OFT 原始推理代码） |
| 环境安装 | `pip install lerobot[pi05]`，30 min | clone `moojink/openvla-oft` + deps，1h |
| 单 suite eval 时间 | ~2-4h（flow matching 多步 denoise） | ~1-2h（parallel decode 很快，>100Hz） |
| 4 suites 全跑 | ~8-16h GPU 时间 | ~4-8h GPU 时间 |
| 显存需求 | ~15GB（单卡 A100 OK） | ~20GB（单卡 A100 OK） |
| 主要风险 | LeRobot API 变动、LIBERO 版本兼容 | 需要 deep-dive OFT 推理代码 |

### 4. 建议接入优先级

**OFT 优先**，原因：
1. OFT vision connector 和 OpenVLA 完全相同（2-layer MLP，256 tokens），我们已有 `compute_openvla_oft_cv.py` 做 token importance 分析，**pruning 代码可大量复用**
2. OFT 有 LIBERO 4 个 suite 的 finetuned checkpoint，且 SOTA 97.1%，作为 baseline 很有说服力
3. OFT parallel decoding 推理快（>100Hz），eval 时间短
4. 修复 eval 的核心工作是对接 OFT 的 continuous action 推理 API，复杂度可控

**π0.5 第二**，原因：
1. 架构差异更大（flow matching + 二阶段推理），adapter 写起来更复杂
2. 推理慢（多步 denoise），eval 时间长
3. 但 256 tokens + linear projection 和 X-VLA 类似，pruning 方法论可以直接迁移
4. LeRobot 原生支持是加分项，不需要从零搭 eval pipeline

---

Sources:
- [Reproducing pi0.5 results on libero - Issue #2375](https://github.com/huggingface/lerobot/issues/2375)
- [π₀.₅ (Pi05) Policy - HuggingFace Docs](https://huggingface.co/docs/lerobot/en/pi05)
- [lerobot/pi05_libero_finetuned](https://huggingface.co/lerobot/pi05_libero_finetuned)
- [π0.5 Paper (PDF)](https://www.pi.website/download/pi05.pdf)
- [OpenVLA-OFT Paper](https://arxiv.org/html/2502.19645v1)
- [moojink/openvla-oft GitHub](https://github.com/moojink/openvla-oft)
- [OpenVLA-OFT LIBERO eval code](https://github.com/moojink/openvla-oft/tree/main/experiments/robot/libero)
- [LIBERO - LeRobot Docs](https://huggingface.co/docs/lerobot/libero)

---

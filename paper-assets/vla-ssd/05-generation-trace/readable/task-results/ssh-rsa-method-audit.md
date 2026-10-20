# ssh rsa method audit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rsa-method-audit_20260516T023619_result.json`
- **Structured JSON:** [`3e35b4f3c296511ab828.json`](../../sessions/3e/3e35b4f3c296511ab828.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## RSA 方法论审计结果

### 1. 方法论差异（3 个脚本对比）

| 因素 | Method A (`rsa_analysis.py`) | Method B (`rsa_siglip_only.py` / `rsa_clip.py`) |
|------|-----|-----|
| **RDM 范围** | 跨任务 100×100 矩阵 | 逐任务 10×10，跨任务取平均 |
| **时间处理** | 三阶段切分 (early/mid/late) 各自计算 RSA 后取平均 | 全轨迹均匀下采样到 20 步 |
| **Action 距离** | cosine distance（`build_dissimilarity_matrix` 对 action 也用 cosine） | euclidean distance（`mean_action_distance` 用 `np.linalg.norm`） |
| **Demo 数量** | 10/task (默认) | 全部 (~50/task) |

### 2. 统一重算结果（全部用 Method B, 10 demos/task）

| Model | Method A | Method B | A-B gap |
|-------|---------|---------|---------|
| **DINO cls** | **0.388** | **0.641** | -0.253 |
| DINO patch_mean | 0.371 | 0.568 | -0.196 |
| CLIP cls | 0.457 | 0.482 | -0.025 |
| CLIP patch_mean | 0.479 | 0.541 | -0.062 |
| SigLIP projector | 0.451 | 0.565 | -0.114 |
| VLA trained L9 | **0.488** | 0.499 | -0.011 |
| VLA untrained L9 | 0.480 | 0.577 | -0.097 |

Method A 完美复现原始数字（DINO=0.3881≈0.388, VLA_trained=0.4876）。

### 3. 根因分解（以 DINO cls 为例，总 gap=0.253）

| 因素 | 贡献 | 占比 |
|------|------|-----|
| **RDM 范围**（跨任务→逐任务）| +0.167 | **66%** |
| **时间处理**（三阶段→全轨迹）| +0.064 | 24% |
| **Action 距离**（cosine→euclidean）| +0.027 | 10% |

跨任务 RDM 对 DINO 伤害最大，因为 LIBERO-Goal 所有 task 共享初始场景，DINO 的跨任务特征相似但 action 完全不同。

### 4. CRITICAL 发现

**原始论文比较（SigLIP=0.615 vs VLA=0.488 vs DINO=0.388）混用了两种方法：**
- SigLIP=0.615 是 Method B（逐任务, 50 demos）
- VLA=0.488 和 DINO=0.388 是 Method A（跨任务, 10 demos, 三阶段）

这是 apples-to-oranges 比较，**必须纠正**。

### 5. 建议

**统一使用 Method B**（逐任务 + 全轨迹 + euclidean action），所有模型用相同 N_DEMOS。

用统一方法后的 ranking：`DINO_cls(0.641) > VLA_untrained(0.577) > DINO_pm(0.568) > SigLIP(0.565) > CLIP_pm(0.541) > VLA_trained(0.499) > CLIP_cls(0.482)`

**DINO 不是 "low-RSA baseline"——它实际上是 RSA 最高的模型。** 这会改变论文叙事。

完整结果：`/root/autodl-tmp/vla-ssd/results/rsa/rsa_method_audit.json`

---

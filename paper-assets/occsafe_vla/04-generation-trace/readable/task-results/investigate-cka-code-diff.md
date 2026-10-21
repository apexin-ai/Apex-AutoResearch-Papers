# investigate cka code diff

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_cka_code_diff_20260525T120022_result.json`
- **Structured JSON:** [`9be13e2e276204f1dca5.json`](../../sessions/9b/9be13e2e276204f1dca5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在有完整的证据了。以下是分析报告。

---

## 代码变更时间线与 CKA 矛盾分析

### 1. 时间线

| 时间 | 事件 | 依据 |
|------|------|------|
| **May 20 15:06** | occ_head.py **v1** 编译 (Python 3.12 pyc) | pyc 时间戳 |
| **May 20 19:34** | modeling_prismatic.py 加入 `_cached_patch_features` | file stat |
| **May 21 07:29** | run_occ_detach.sh 创建 | file stat |
| **May 21 19:02** | **ablation_occ_detach_s0/s1 启动**（旧代码） | 训练日志 |
| **May 22 ~09:30** | s0 训练完成 (50K steps) | 日志 |
| **May 22 14:12** | s2 启动（同一份旧代码） | 训练日志 |
| **May 23 13:25** | occ_head.py **v2** 修改（加入 `norm_type`, `DepthHead`） | file stat |
| **May 23 13:27** | v2 编译 (Python 3.10 pyc) | pyc 时间戳 |
| **May 24 09:05** | cka_analysis.py 创建 | file stat |
| **May 24~25** | **ablation_occ_detach_s0_retrain 训练**（新代码） | 训练日志 |
| **May 25 12:33** | finetune.py 最后修改 | file stat |

### 2. occ_head.py 旧版 vs 新版（反编译 pyc 确认）

**旧版 (May 20 pyc)**：
```python
class BEVOccupancyHead:
    def __init__(self, in_dim, out_resolution=64, num_classes=1,
                 hidden_dim=256, num_patches_per_image=256):
        # 无 norm_type 参数
        # 硬编码 nn.BatchNorm2d(128) 和 nn.BatchNorm2d(64)
# 仅 BEVOccupancyHead + FocalLoss，无 DepthHead
```

**新版 (May 23)**：
```python
class BEVOccupancyHead:
    def __init__(self, ..., norm_type="bn"):
        def _norm(channels):
            return GroupNorm(1, ch) if norm_type == "ln" else BatchNorm2d(ch)
# 新增 DepthHead + DepthLoss
```

**两者默认都是 BatchNorm2d → norm 类型本身没有区别。**

### 3. finetune.py 差异证据

所有 OCC 代码从未 commit（git diff 全部是 `+` 行），因此只能通过间接证据推断 May 21 版本：

| 特征 | 原始训练 (May 21) | 重训 (May 24+) |
|------|-------------------|----------------|
| `[AUX]` 日志行 | **无** (175行日志全无) | **有** (`[AUX] step=...`) |
| `norm_type` 传参 | **不可能**（旧 occ_head 不接受此参数） | 有 (`cfg.occ_norm_type`) |
| `occ_detach` 实现 | **无法确认** | 确认存在 (line 484-485) |
| `gradient_step_idx` 位置 | loss 计算之后 | 移到 loss 计算之前 |

### 4. 根因判断

**原始 May 21 代码极有可能没有正确实现 `occ_detach`。**

核心证据链：
1. CKA=0.539/0.312 → 说明 backbone 特征发生了显著改变 → OCC 梯度**确实流回了 backbone**
2. CKA=0.964/0.953 (retrain) ≈ Vanilla CKA=0.968/0.955 → detach 正确工作时，backbone 几乎不变
3. 旧代码处于早期/不完整状态（无 `[AUX]` 日志、无 `norm_type` 支持、无 `DepthHead`）
4. `occ_head.py` 在 May 23 被修改 → **finetune.py 也很可能同期被修改**以适配新 API
5. `cka_same_seed` 中 "Detach+BN" (retrain) 的 CKA 完美符合理论预期

**最可能的失败模式**：

旧版 `run_forward_pass` 没有 `if occ_detach: patch_features = patch_features.detach()` 这行代码（或 `occ_detach` 参数虽然在 config 中定义但未传入 forward），导致 OCC loss 梯度直通 backbone。实际运行等效于 **Full OCC（非 detach）**。

### 5. BN 行为说明

这不是 BN 问题。原因：
- CKA 测量的是 **vision backbone**（DINOv2/SigLIP）的特征，这些使用 **LayerNorm**，不含 BatchNorm
- OCC head 内部的 BN 仅影响 OCC head 自身的 running stats，与 CKA 测量目标无关
- `detach()` 发生在 backbone forward pass **之后** → 即使 detach 不存在，backbone 的 BN 行为也相同
- `detach()` 只影响反向传播的梯度流，不影响前向传播中 BN 的 running stats 更新

### 6. 结论

**CKA 矛盾的根因不是 BN 行为差异，而是旧代码缺失 detach 实现。** 原始训练实际上是一个 "Full OCC" 训练（OCC 梯度流回 backbone），而非 detach 训练。重训修复了这个问题。

原始 `ablation_occ_detach_s0` checkpoint 已被删除，无法直接验证。但 `cka_same_seed` 分析显示当前代码的 "Detach+BN" CKA (0.964/0.953) 与 "Vanilla" (0.968/0.955) 高度一致，确认现有 detach 实现正确。

---

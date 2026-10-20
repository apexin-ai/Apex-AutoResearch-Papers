# code phase2 train script

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase2_train_script_20260518T060527_result.json`
- **Structured JSON:** [`72516e2ace7fdc2d92b9.json`](../../sessions/72/72516e2ace7fdc2d92b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### 产出

**1. 训练数据**
- 路径: `/root/turn_residual_gating/data/ultrachat_8k`
- 总样本 207,865 → 过滤 ≥5 assistant turns → 17,302 → 采样 8,000
- 平均 assistant turns: 5.6, 范围: 5-7

**2. threadgate.py 更新**
- `forward()` 添加 `**kwargs` 传递 `output_attentions` 等参数
- `forward()` 中 device 获取改为 `next(self.gates[0].parameters()).device`（兼容 PEFT 包装）
- `__init__` 中 `turn_embedding` 设备获取同步修复
- 移除 forward 末尾的 `_current_turn_features = None`（兼容 gradient checkpointing recompute）

**3. train_phase2.py 已创建**
- 支持 `--gate-type threadgate/uniform`, `--dry-run`, `--lambda-gar`, `--max-seq-len` 等参数
- 模型初始化: ThreadGatedModel → LoRA (q_proj, v_proj, r=16) → gradient checkpointing → GARMeasurer
- 训练: batch_size=1, grad_accum=8, AdamW + cosine schedule
- 每 epoch 保存 checkpoint

**4. Dry-run 验证通过**
| Step | L_NTP | L_GAR | Gate | Mem |
|------|-------|-------|------|-----|
| 0 | 1.5063 | 0.0099 | 0.9916 | 18.5GB |
| 1 | 1.6008 | 0.0086 | 0.9920 | 18.6GB |
| 2 | 1.6765 | 0.0000 | 0.9915 | 18.6GB |
| 3 | 1.6987 | 0.0000 | 0.9920 | 18.6GB |
| 4 | 1.8995 | 0.0000 | 0.9923 | 18.6GB |

Gate 梯度确认有更新。无 OOM/NaN/Inf。

**5. 本地副本已同步**
- `artifacts/src/threadgate.py` ✓
- `artifacts/src/train_phase2.py` ✓
- `artifacts/src/config.py` (MODEL_NAME 更新为本地路径) ✓

---

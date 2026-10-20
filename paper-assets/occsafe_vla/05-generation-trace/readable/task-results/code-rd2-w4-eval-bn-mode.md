# code rd2 w4 eval bn mode

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rd2-w4-eval-bn-mode_20260529T002215_result.json`
- **Structured JSON:** [`88e4fdafcb03b557bba1.json`](../../sessions/88/88e4fdafcb03b557bba1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

### Eval 路径中的 BN 层分布

| 组件 | 加载方式 | 是否含 BatchNorm2d |
|------|---------|-------------------|
| VLA backbone (`vla.eval()`) | `get_vla(cfg)` @ openvla_utils.py:299 | **否** (Transformer 用 LayerNorm) |
| L1RegressionActionHead (`action_head.eval()`) | `get_action_head(cfg)` @ openvla_utils.py:493 | **否** (只有 LayerNorm) |
| ProprioProjector (`proprio_projector.eval()`) | `get_proprio_projector(cfg)` @ openvla_utils.py:411 | **否** |
| **BEVOccupancyHead (occ_head)** | — | **是** (2 层 BatchNorm2d: 128ch, 64ch) |

### 关键发现：occ_head 在 eval 时完全不参与推理

`evaluate_safelibero.py` 的 `init_model()` 函数只加载 4 个组件：`vla`, `action_head`, `proprio_projector`, `processor`。**occ_head 从未被加载、从未被使用**。整个推理路径中不存在任何 `BatchNorm2d` 层。

推理调用链：`run_episode()` → `get_action()` → `get_vla_action()` (torch.inference_mode) → `vla.predict_action()` + `action_head`。occ_head 不在此链中。

### 对 RD2-W4 实验设计的影响

**在 eval 脚本中添加 `--bn_force_train` 没有意义**——eval 路径无 BN 层可切换。

BN eval vs train mode 的影响发生在**训练时**，而非推理时：
- 训练时 occ_head 的 BN 用 train mode → 使用 batch statistics → 通过梯度影响 backbone 特征学习
- 训练时 occ_head 的 BN 用 eval mode → 使用 frozen running stats → 梯度信号不同
- 训练后的 checkpoint 已经包含了这种差异的结果——不同的 backbone 权重和 action_head 权重

**已有的训练侧 flag**：`finetune.py` 已实现 `--occ_bn_eval` (line 101)，在训练循环中 (line 1197-1199) 每个 batch 前把 occ_head 的 BN 层切到 eval mode。

### 结论

1. **不需要修改 eval 脚本**——添加 `--bn_force_train` 无效果
2. RD2-W4 的 BN eval vs train 对比需要通过**训练两个不同的 checkpoint** 来实现：一个用 `--occ_bn_eval=True`，一个用默认 `--occ_bn_eval=False`，然后分别 eval 比较 CAR/TSR
3. Cell 1 (Full OCC BN) 的 checkpoint 是用哪个 `occ_bn_eval` 值训练的，决定了它在 eval 时的行为——这已经固化在权重中了

---

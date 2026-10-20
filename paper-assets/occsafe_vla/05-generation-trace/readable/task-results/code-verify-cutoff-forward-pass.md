# code verify cutoff forward pass

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_cutoff_forward_pass_20260523T223223_result.json`
- **Structured JSON:** [`f1109490b170f4ff6529.json`](../../sessions/f1/f1109490b170f4ff6529.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Commit 已在服务器本地完成 (`bdaee75`)。Push 失败——唯一的 remote 是上游 `https://github.com/moojink/openvla-oft.git`，没有 push 权限。代码改动已保存在服务器本地 git 历史中。

---

## 任务 A：cutoff 实现细节分析

**当前行为（cutoff 生效后，step >= occ_loss_cutoff_step）：**

1. **occ_loss 是否为 0** — 是。`occ_weight_now` 被设为 `0.0`，loss 变成 `loss + 0.0 * occ_loss`，occ_loss 不参与 backward。

2. **occ_head forward pass 是否仍执行** — **是**。training loop 传给 `run_forward_pass` 的条件是 `occ_head=occ_head if cfg.use_occ_head else None`，cutoff 只改变权重，不影响 head 是否传入。`run_forward_pass` 内部（原 line 479）只检查 `occ_head is not None and "occ_labels" in batch`，所以 forward pass 每步都执行，即使权重为零。

3. **BatchNorm 是否更新 running stats** — **是**。`BEVOccupancyHead.decoder` 包含两层 `nn.BatchNorm2d`（128 和 64 通道）。模型在 `train()` 模式下，BatchNorm 每次 forward 都会更新 `running_mean` 和 `running_var`，与 loss 是否参与 backward 无关。cutoff 后 BN stats 持续被"不产生梯度"的数据更新，导致 inference 时 running stats 与实际学到的权重不匹配。

---

## 任务 B：clean cutoff 实现

**修改文件**: `vla-scripts/finetune.py`（1 个文件，+15 -6 行）

**具体改动：**

| 位置 | 改动 |
|------|------|
| Config dataclass（~line 96） | 新增 `clean_cutoff: bool = False` 参数 |
| Training loop（~line 1184） | 新增 `skip_occ` / `skip_depth` 布尔变量：当 `clean_cutoff=True` 且 cutoff 已生效（weight==0.0）时为 True |
| `run_forward_pass` 调用（~line 1203） | `occ_head` 和 `occ_loss_fn` 传入条件从 `cfg.use_occ_head` 改为 `cfg.use_occ_head and not skip_occ` |
| `run_forward_pass` 调用（~line 1207） | `depth_head` 和 `depth_loss_fn` 同理改为 `cfg.use_depth_head and not skip_depth` |

**向后兼容**：`clean_cutoff` 默认 False，不影响现有行为。

**Commit**: `bdaee75` on `main` (local on westd-34685)。Push 到 remote 失败（上游 repo 无写权限）。如需 push，需配置一个有写权限的 fork remote。

---

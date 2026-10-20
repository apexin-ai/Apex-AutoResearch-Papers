# code rd2 w4 bn eval mode

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rd2-w4-bn-eval-mode_20260528T223735_result.json`
- **Structured JSON:** [`ea4edf3cd7679a808688.json`](../../sessions/ea/ea4edf3cd7679a808688.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**代码已经完全就绪，不需要任何修改。**

## 分析结果

### 代码现状

`--occ_bn_eval` 参数和对应逻辑已存在于代码中：

- **参数定义** (`finetune.py:101`): `occ_bn_eval: bool = False`
- **训练循环** (`finetune.py:1197-1200`):
  ```python
  if cfg.occ_bn_eval and occ_head is not None:
      for m in occ_head.modules():
          if isinstance(m, torch.nn.BatchNorm2d):
              m.eval()
  ```

这段逻辑在每个 training step 的 forward pass 前执行，将 OCC head 中的两个 `BatchNorm2d` 层（128 channels 和 64 channels）设为 eval mode，冻结 running mean/var 的更新，但**不影响 gradient flow**——BN 在 eval mode 下仍然可微，只是用固定的 running stats 做归一化。

### BN 层位置 (`occ_head.py`)

`BEVOccupancyHead.decoder` 中有 2 个 BN 层（当 `norm_type="bn"` 时）：
- `decoder[1]`: `BatchNorm2d(128)` — ConvTranspose2d 16→32 之后
- `decoder[4]`: `BatchNorm2d(64)` — ConvTranspose2d 32→64 之后

### 实验配置

无需代码修改，直接运行：

| Run | 命令 | GPU |
|-----|------|-----|
| BN-eval seed42 | `torchrun --nproc_per_node=2 finetune.py --seed 42 --use_occ_head True --occ_detach False --occ_norm_type bn --occ_bn_eval True ...` | westd-10894 cuda:0-1 或 westd-34685 cuda:0-1 |
| BN-eval seed43 | `torchrun --nproc_per_node=2 finetune.py --seed 43 --use_occ_head True --occ_detach False --occ_norm_type bn --occ_bn_eval True ...` | 同上另一组 |

预期 GPU 时长：与 Cell 1 相同（约 5-6h/run @ 2×GPU，50k steps）。

### 风险点

1. **BN eval mode 不阻断 gradient**：`m.eval()` 只改变 forward 行为（用 running stats 而非 batch stats），backward pass 不受影响。这正是实验想要的——隔离 "running stats 被破坏" vs "gradient flow 本身"。
2. **running stats 初始值**：BN 层刚初始化时 running_mean=0, running_var=1。eval mode 下将始终用这些初始值归一化，等价于 identity transform（输入减0除1）。如果审稿人质疑这一点，可以说明 eval mode BN 在此配置下退化为 no-normalization baseline，仍能区分 gradient flow 的影响。
3. **与 `clean_cutoff` 交互**：如果同时开启 `clean_cutoff` 且 `occ_weight_now == 0`，则 `skip_occ=True`，occ_head 不会被调用，BN eval 设置无意义。本实验不用 cutoff，无此问题。

---

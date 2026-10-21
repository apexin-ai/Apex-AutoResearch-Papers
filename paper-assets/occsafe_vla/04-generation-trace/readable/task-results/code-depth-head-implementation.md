# code depth head implementation

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_depth-head-implementation_20260522T024220_result.json`
- **Structured JSON:** [`69209e46c26a9ce9c544.json`](../../sessions/69/69209e46c26a9ce9c544.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。总结修改：

**4 个文件，14 处改动：**

1. **`prismatic/models/occ_head.py`** — 新增 `DepthHead` + `DepthLoss` 类（与 BEVOccupancyHead 同架构，输出连续深度值，用 SmoothL1 回归）

2. **`vla-scripts/finetune.py`** — 12 处改动：
   - import 添加 `DepthHead, DepthLoss`
   - FinetuneConfig 新增 7 个 depth 配置参数
   - `run_forward_pass` 签名添加 depth 参数
   - forward 中新增 depth loss 计算路径
   - `save_training_checkpoint` 签名和保存逻辑添加 depth_head
   - `init_module` 初始化 depth_head + depth_loss_fn
   - optimizer trainable_params 添加 depth_head
   - RLDSBatchTransform 传入 depth_data_dir
   - recent_metrics 添加 depth_loss
   - 训练循环中添加 depth loss weight 指数衰减
   - run_forward_pass 调用传入 depth 参数
   - 日志打印添加 depth_loss

3. **`prismatic/vla/datasets/datasets.py`** — 新增 `depth_data_dir`/`depth_resolution` 字段、`_preload_depth_data()`、`_load_depth_label()` 方法，`__call__` 返回 `depth_labels`

4. **`prismatic/util/data_utils.py`** — collator 添加 `depth_labels` stack

---

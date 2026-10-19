# ssh plan014 temp ablation config

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan014_temp_ablation_config_20260514T005331_result.json`
- **Structured JSON:** [`5516be2d7112958fc0c7.json`](../../sessions/55/5516be2d7112958fc0c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇总：

## 产出

### 1. 代码修复（必要前提）
- **`contrastive_model.py`**: `StructFuseEncoder.__init__` 新增 `init_temperature=0.07` 参数，`log_temperature` 用该值初始化（原来硬编码 0.07，`--temperature` CLI 参数定义了但从未生效）
- **`train.py`**: 模型构造传入 `init_temperature=args.temperature`

### 2. 文件
- `/root/structfuse-context/run_plan014_temp_ablation.sh` — 运行脚本，语法 OK
- `/root/structfuse-context/configs/plan014_temp_ablation.yaml` — 配置文件

### 3. 数据复用确认
全部 6 个数据文件（3 strategies × train/val，seed=42）存在于 `/root/autodl-tmp/structfuse/full_m2_training_data/`，`dataflow_graph.json` 也存在。

### 4. 时间估算
- 训练数据 11,308 samples，batch_size=8 → **1,414 steps/epoch**
- 3 epochs/run → 4,242 steps/run
- M2 单 run（3 epochs）约 **11-14h**
- **9 runs 总计 ~99-126h（4.1-5.3 天）**
- 若减为 2 epochs：~66-84h（2.75-3.5 天）

### 注意
`log_temperature` 是 learnable parameter — 即使初始化不同，训练过程中它会被优化器更新。ablation 测试的是**初始化值**对收敛行为和最终性能的影响，不是固定 temperature。如果需要**固定** temperature（不让它学习），需要额外修改把 `log_temperature` 从优化参数中排除。

---

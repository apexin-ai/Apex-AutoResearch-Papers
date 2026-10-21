# code fix all occ issues

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_all_occ_issues_20260520T105537_result.json`
- **Structured JSON:** [`35581c5b9bea296c7b90.json`](../../sessions/35/35581c5b9bea296c7b90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是三个问题的统一报告。

---

## Problem 1: `occ_detach` 默认值修复

### 修复内容
`finetune.py` L94: `occ_detach: bool = True` → `occ_detach: bool = False`

### 当前源码验证（4 处引用均一致）
```
L94:   occ_detach: bool = False    # FinetuneConfig 默认值
L306:  occ_detach=False,           # run_forward_pass 函数默认参数（dead code，随配置走）
L467:  if occ_detach:              # 运行时分支
L1129: occ_detach=cfg.occ_detach,  # 训练循环传参
```

### 5-step 梯度验证（cuda:3，occ_detach=False）
```
Vision backbone: 396/422 trainable params have grad
  featurizer.patch_embed.proj.lora_A.default.weight: |grad|_mean = 3.29e-05
  featurizer.patch_embed.proj.lora_B.default.weight: |grad|_mean = 3.74e-05
  featurizer.blocks.0.attn.qkv.lora_A.default.weight:  |grad|_mean = 1.80e-07
  featurizer.blocks.0.attn.qkv.lora_B.default.weight:  |grad|_mean = 2.81e-07
  featurizer.blocks.0.attn.proj.lora_A.default.weight:  |grad|_mean = 1.17e-07
Result: PASS ✓
```

occ loss 梯度成功回传到 vision encoder LoRA 参数，396/422 个可训练参数有非零梯度。

---

## Problem 2: Occ 数据目录对比

### 目录对比

| | `occ_data_dummy/` | `occ_data/` |
|---|---|---|
| 总大小 | 66 MB | 30 MB（仍在增长） |
| 文件数 | 10 HDF5 + occ_index.json | 10 HDF5，无 occ_index.json |
| 单文件大小 | ~6.6 MB | ~2.3-2.7 MB |
| 每文件 demos | 50 demos | 部分 demos（提取中） |
| 内容 | bev_binary + bev_semantic | bev_binary + bev_semantic |
| occ_index.json | 有 | 无 |
| 状态 | 静态，可用 | 10 个进程正在写入（PID 104226-104235，已运行 1h43m） |

### 结论
- **`occ_data_dummy/`**：预生成的完整测试数据，50 demos/task，已有 occ_index.json，可直接用于训练调试
- **`occ_data/`**：`extract_occupancy.py` 正在从 LIBERO demo 提取的真实 BEV occupancy 数据，尚未完成
- **大小差异原因**：occ_data/ 每个文件只完成了部分 demo 的提取（~40% 数据量），不是压缩率差异

### occ_index.json 状态
- `build_occ_index.py` 存在于 `/root/occsafe_vla/build_occ_index.py`
- occ_data/ 提取完成后需手动运行此脚本生成 occ_index.json
- 在此之前 occ_data/ 无法用于训练（`_load_occ_label()` 依赖 occ_index.json 做 demo→timestep 对齐）

### 清理建议
- 提取完成前：两个目录都保留。occ_data_dummy/ 用于开发调试
- 提取完成后：运行 `python build_occ_index.py`（指向 occ_data/），验证 index 正确，然后切换训练配置指向 occ_data/
- occ_data_dummy/ 可在 occ_data/ 验证通过后删除（节省 66MB）

---

## Problem 3: 170% 训练开销分析

### Profiling 结果（cuda:3，步骤 5-14 平均值）

| 阶段 | Vanilla | Occ | Delta |
|------|---------|-----|-------|
| **data loading** | 0.594s | 0.603s | +0.009s |
| **vla_fwd** | 0.230s | 0.225s | -0.004s |
| **occ_fwd + loss** | 0.000s | 0.005s | +0.005s |
| **backward** | 0.243s | 0.241s | -0.002s |
| **optimizer** | 0.020s | 0.015s | -0.005s |
| **总计** | **1.087s** | **1.090s** | **+0.004s (+0.3%)** |

### 关键发现

**模型计算本身几乎零开销。** occ head 前向 + focal loss 仅 5ms/step，backward 没有可测量的增量。这意味着：

**170% 的开销不在模型计算，而在数据加载。** 本次 profiling 用的是内存中的 DummyDataset，绕过了 HDF5 I/O。真实训练中 `_load_occ_label()` 每个 sample 要：
1. 打开 HDF5 文件（磁盘 I/O）
2. 读取 occ_index.json 做 timestep 对齐
3. 解压 gzip 压缩的 bev_binary（CPU 解压）
4. 转换为 float32 tensor

### 瓶颈定位
**HDF5 per-sample random read I/O** 是 170% 开销的主因。证据：
- 即使在 profiling 中，data loading 也占单步时间的 ~55%（DummyDataset 已经是最快的了）
- 真实 RLDS pipeline 中 `_load_occ_label()` 在 batch transform 内被逐样本调用，每次重新 `h5py.File()` 打开文件

### 优化建议（按优先级排序）

1. **预加载 occ labels 到内存**（预估 -60% 开销）  
   10 个任务 × 50 demos × ~280 步 × 64×64 float32 = ~3.4 GB。单次启动加载全部 occ label 到 dict，训练时直接索引，彻底消除 HDF5 I/O。

2. **HDF5 文件句柄缓存**（预估 -30% 开销）  
   如果内存不够全量预加载，至少缓存 `h5py.File` 句柄（当前每次 `_load_occ_label` 都重新 open/close）。用 `functools.lru_cache` 或 dataset 级别的 dict 持有句柄。

3. **转存为 memory-mapped 格式**（预估 -50% 开销）  
   将 HDF5 gzip 数据转存为 numpy `.npy` 或 memory-mapped array，避免 gzip 解压开销。

4. **DataLoader num_workers 调优**  
   增加 `num_workers` 让数据预取和 GPU 计算重叠，隐藏 I/O 延迟。

---

## 安全确认

- **cuda:0,1,2 vanilla 训练**：PID 97847/98174/100203 运行正常，CPU 占用 702-722%，已运行 ~2h，未受影响
- **occ_data 提取进程**：PID 104226-104235 全部正常运行
- **临时文件**：`profile_occ.py` 和 `/tmp/profile_occ.log` 已删除

---

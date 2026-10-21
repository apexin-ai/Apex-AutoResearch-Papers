# 诊断报告: qwen25_14b_scale_003 超时失败

## 实验进度

| 阶段 | 状态 | 完成时间 | 耗时 |
|------|------|---------|------|
| Phase 2: d0 生成 (5000 samples) | ✅ | May 18 07:56 | ~4h 46min |
| Phase 3.1a: LoRA d0 训练 (loss=0.5451) | ✅ | May 18 08:37 | ~41min |
| Phase 3.1b: d1 生成 (5000 samples) | ✅ | May 18 14:46 | ~6h 9min |
| Phase 3.2a: LoRA d1 训练 (loss=0.3451) | ✅ | May 18 15:29 | ~43min |
| Phase 3.2b: d2 生成 (5000 samples) | ✅ | May 18 21:42 | ~6h 13min |
| Phase 3.3a: LoRA d2 训练 (loss=0.2141) | ✅ | May 18 22:23 | ~41min |
| Phase 3.3b: d3 生成 (3837/5000, 76.7%) | ❌ timeout | May 19 03:10 | ~4h 47min (未完成) |
| Phase 4: 特征提取 | ❌ 未开始 | - | - |
| Phase 5: 分类器训练 | ❌ 未开始 | - | - |

实验启动: ~May 18 03:10, 超时终止: ~May 19 03:10 (EXIT_CODE=124, 24h timeout)

## 失败原因

**24h timeout 不够。** Pipeline 预计总耗时 ~27-28h:
- d0-d3 生成 + 3 轮 LoRA 训练: ~25-26h
- 特征提取 + 分类: ~1-2h

前序实验 qwen25_14b_scale_002 在 gpu-6000pro-2 上耗时 ~29h 完成，westd-48862 速度接近。生成阶段是瓶颈 (每个 depth ~6h, batch_size=4, max_new_tokens=512, 14B FP16 单卡)。

## 中间数据状态

### 已生成数据 (可复用):
```
depth_0.jsonl  7.1MB  5000 lines ✅
depth_1.jsonl  8.6MB  5000 lines ✅
depth_2.jsonl  10.3MB 5000 lines ✅
depth_3.jsonl  8.1MB  3837 lines ❌ (不完整)
```

### LoRA checkpoints (可复用):
```
lora_depth_0/  adapter_model.safetensors 66MB ✅
lora_depth_1/  adapter_model.safetensors 66MB ✅
lora_depth_2/  adapter_model.safetensors 66MB ✅
```

### 结果目录: 空 (Phase 4/5 未执行)

## Resume 分析

脚本有内置 skip 逻辑:
- `generate_d0` / `generate_next_depth`: 检查 `count >= NUM_SAMPLES` 才 skip
- `lora_finetune`: 检查 `adapter_config.json` 存在才 skip

**重启行为:**
- d0/d1/d2 生成: **自动 skip** (各 5000 samples)
- LoRA d0/d1/d2 训练: **自动 skip** (adapter 已存在)
- d3 生成: **从头重跑** (3837 < 5000, 且用 `open("w")` 覆盖写)
- 特征提取 + 分类: 正常执行

**重启预计耗时: ~7-8h** (d3 ~6h + feature extraction ~1h + classification ~0.5h)

## 建议

1. **重试 timeout 设为 10h** (重启只需跑 d3 + Phase 4/5, 8h 足够 + 2h 余量)
2. 如果要从零重跑, timeout 设为 **36h**
3. 不需要删除任何中间数据, d0/d1/d2 和所有 LoRA checkpoint 均完整可复用
4. 注意: 启动脚本的 tee 命令会报错 (`results/qwen25_14b_scale/` 目录在脚本内才创建), 不影响功能但建议 shell wrapper 先 mkdir -p

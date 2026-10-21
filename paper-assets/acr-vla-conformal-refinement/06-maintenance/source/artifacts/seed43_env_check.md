# bjb1-18228 Object Benchmark Eval 环境检查 (seed=43)

**日期**: 2026-05-15

## 检查结果

### 1. Object Benchmark 数据 — OK

- 路径: `/root/autodl-tmp/libero_data/libero_object/`
- 大小: 7.0 GB
- 任务数: 10 个 hdf5 文件（alphabet_soup, bbq_sauce, butter, chocolate_pudding, cream_cheese, ketchup, milk, orange_juice, salad_dressing, tomato_sauce）

### 2. Checkpoints — OK

| Checkpoint | 路径 | 大小 | 时间 |
|---|---|---|---|
| obs_only | `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt` | 1.3 MB | May 15 06:00 |
| perdof | `/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt` | 1.4 MB | May 15 03:57 |

### 3. evaluate.py — OK

- `--benchmark` 参数: 支持 `object`（默认值即为 object）
- `--seed` 参数: 支持，默认 42，可设为 43
- 支持模式: vla_only, crm_scalar, crm_perdof, acr_vla, reconvla

### 4. GPU 状态 — OK

| GPU | 型号 | 显存使用 | 利用率 | 状态 |
|---|---|---|---|---|
| cuda:0 | RTX 4090 | 3594 / 24564 MiB | 23% | 占用 |
| cuda:1 | RTX 4090 | 2005 / 24564 MiB | 24% | 占用 |
| cuda:2 | RTX 4090 | 1 / 24564 MiB | 0% | **空闲** |
| cuda:3 | RTX 4090 | 1 / 24564 MiB | 0% | **空闲** |

### 5. SmolVLA 模型 — OK

- 路径: `/root/autodl-tmp/models/smolvla_libero/`
- model.safetensors: 906 MB
- config.json + preprocessor/postprocessor 文件齐全

## 结论

**可以直接部署。** 所有资源就绪，无需额外下载或准备：
- Object benchmark 数据 10 个任务完整
- obs_only 和 perdof 两个 checkpoint 均存在
- evaluate.py 支持 `--benchmark object --seed 43`
- cuda:2 和 cuda:3 完全空闲（各 24GB）
- SmolVLA 模型已下载

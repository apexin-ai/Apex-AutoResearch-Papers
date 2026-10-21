# LIBERO 环境 + SmolVLA Checkpoint 验证报告

**日期**: 2026-05-13
**服务器**: autodl-4090 (RTX 4090, 24GB VRAM)

---

## 1. LIBERO 安装状态：✅ 成功

| 包 | 版本 | 状态 |
|---|---|---|
| robosuite | 1.4.0 | ✅ |
| libero | 0.1.1 | ✅ |
| mujoco | 3.8.1 | ✅ |

**渲染**: 需要 `MUJOCO_GL=egl`（已安装 libegl1/libegl-dev/libegl1-mesa-dev）

**可用 Benchmark**:
| Benchmark | 任务数 |
|---|---|
| libero_spatial | 10 |
| libero_object | 10 |
| libero_goal | 10 |
| libero_90 | 90 |
| libero_10 | 10 |
| libero_100 | ❌ KeyError（可能需要额外数据注册） |

**数据集状态**: ❌ 未下载。Demo hdf5 文件不存在，路径格式为 `libero_spatial/TASK_NAME_demo.hdf5`（相对路径，需要设置 `LIBERO_DATA` 环境变量并下载数据）。

**示例任务名**:
- pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate
- pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate
- pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate

---

## 2. SmolVLA Checkpoint：✅ 下载并验证

| 属性 | 值 |
|---|---|
| HuggingFace repo | `lerobot/smolvla_base` |
| VLM backbone | `HuggingFaceTB/SmolVLM2-500M-Video-Instruct` |
| 本地路径 | `/root/autodl-tmp/models/smolvla_base/` |
| 磁盘大小 | 873MB (model.safetensors = 865MB) |
| **总参数量** | **450.0M** |
| **VRAM（模型加载后）** | **0.86GB allocated / 0.88GB reserved** |
| VRAM（推理后） | 0.87GB allocated / 0.94GB reserved |
| 精度 | bfloat16 |
| 加载时间 | ~60s（含 VLM backbone 初始化） |

**模型配置**:
- 输入: 3 cameras (256×256×3) + state (6-dim) + language tokens (max 48)
- 输出: action (6-dim), chunk_size=50, n_action_steps=50
- Flow matching: **num_steps=10**
- Attention mode: cross_attn
- VLM layers: 16 (从原始模型裁剪)
- Expert width multiplier: 0.75

---

## 3. K=10 推理可行性：✅ 完全可行

### K=1 推理
| 指标 | 值 |
|---|---|
| 平均延迟 | **380.3ms** |
| 各轮次 | 384.1 / 379.5 / 379.6 / 380.1 / 378.2 ms |
| Action shape | (1, 6) |

### K=10 Sequential（逐个推理）
| 指标 | 值 |
|---|---|
| 总耗时 | **3931.3ms** |
| 每样本 | 393.1ms |
| Actions 方差 | 0.173948（不同 noise 产生不同轨迹） |
| VRAM | 0.87GB / 0.94GB |

### K=10 Batched（批量推理） ✅ 
| 指标 | 值 |
|---|---|
| **总耗时** | **450.3ms** |
| Action shape | (10, 6) |
| VRAM | 0.90GB / 1.33GB |
| **加速比 vs sequential** | **8.7x** |

**结论**: K=10 batched 推理在 4090 上完全可行，VRAM 仅增加 ~0.4GB（从 0.94 → 1.33GB），远低于 24GB 限制。Batched 模式比 sequential 快 8.7 倍。

---

## 4. 遇到的问题和解决方案

| 问题 | 解决方案 |
|---|---|
| EGL 渲染失败 (`eglQueryString` AttributeError) | `apt install libegl1 libegl-dev libegl1-mesa-dev` + `MUJOCO_GL=egl` |
| HuggingFace API 503 | 使用 `HF_ENDPOINT=https://hf-mirror.com` 镜像 |
| huggingface-hub 1.14.0 vs transformers <1.0 冲突 | 升级 transformers 5.8.0 |
| transformers 5.x 导致 lerobot groot 模块 dataclass 错误 | 注释掉 `lerobot/policies/__init__.py` 中的 groot import |
| `num2words` 缺失 | `pip install num2words` |
| attention_mask dtype Long vs expected bool | 调用 `.bool()` 转换 |
| SSH 30s 超时 | nohup 后台执行 + 轮询 |

**注意**: groot 模块的 patch 是临时方案。如果未来需要 groot，需降级 transformers 或升级 lerobot。

---

## 5. 磁盘使用

| 分区 | 大小 | 已用 | 可用 | 使用率 |
|---|---|---|---|---|
| / (根) | 30G | 9.1G | 21G | 31% |
| /root/autodl-tmp | 250G | 2.8G | 248G | 2% |

| 目录 | 大小 |
|---|---|
| /root/autodl-tmp/models/ | 873M |
| /root/autodl-tmp/.hf_cache/ | 1.9G |

---

## 环境 Patch 记录

修改文件: `/root/miniconda3/lib/python3.12/site-packages/lerobot/policies/__init__.py`
- Line 17: 注释掉 `from .groot.configuration_groot import GrootConfig as GrootConfig`
- Line 40: 注释掉 `"GrootConfig",` 在 `__all__` 中

安装的额外包: `num2words`, `libegl1`, `libegl-dev`, `libegl1-mesa-dev`
升级: `transformers` 4.57.6 → 5.8.0, `huggingface-hub` 恢复为 1.14.0

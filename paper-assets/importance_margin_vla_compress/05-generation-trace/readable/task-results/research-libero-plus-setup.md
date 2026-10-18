# research libero plus setup

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_libero-plus-setup_20260520T231402_result.json`
- **Structured JSON:** [`a33f457818436c8b2b73.json`](../../sessions/a3/a33f457818436c8b2b73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6GB 文件以 ~500KB/s 下载，需约 3.3 小时。以下是完整报告：

---

## LIBERO-Plus 工程适配报告

### 1. 安装状态：✅ 已完成（assets 下载中）

- LIBERO-Plus 已 clone 到 `/root/autodl-tmp/LIBERO-plus/`
- 旧 LIBERO 0.1.1 已卸载，LIBERO-Plus 0.1.0 通过 `.pth` 文件安装
- `~/.libero/config.yaml` 已更新指向新 repo
- 依赖已安装：`wand`, `scikit-image`, `gym==0.25.2`, `libmagickwand-dev`
- numpy 降级到 2.2.6 保持兼容
- **待完成**：assets.zip (6.0GB) 正在 wget 后台下载 (PID 155236)，完成后需解压到 `LIBERO-plus/libero/libero/`。已将旧 LIBERO assets (405MB) 作为基础复制过来

### 2. 核心概念

**7 种扰动类型**（每个 suite 均覆盖）：
| 类型 | 后缀编码 | 实现方式 |
|------|---------|---------|
| Background Textures | `_table_XX`, `_tb_XX` | bddl 指定不同桌面贴图 |
| Camera Viewpoints | `_view_XX` | bddl+init 修改相机位姿 |
| Language Instructions | `_language_XX` | bddl 中 LLM 改写的指令 |
| Light Conditions | `_light_XX` | bddl 修改灯光参数 |
| Objects Layout | `_add_XX`, `_levelXX` | bddl 添加干扰物/移动目标位置 |
| Robot Initial States | 内置于 init 文件 | 不同机械臂初始关节角度 |
| Sensor Noise | 运行时注入 | `env_wrapper.py` 中 motion blur/gaussian blur/zoom blur 等图像级噪声 |

**5 个难度等级 (L1-L5)**：task_classification.json 标注每个 task 的 category 和 difficulty_level。

**Task 数量**：
| Suite | 原 LIBERO | LIBERO-Plus |
|-------|----------|-------------|
| libero_spatial | 10 | 2402 |
| libero_object | 10 | 2518 |
| libero_goal | 10 | 2591 |
| libero_10 | 10 | 2519 |

### 3. 与原 LIBERO 的关系

- **Drop-in replacement**：`pip install -e .` 替换原 LIBERO，代码中 `from libero.libero import benchmark` 等 import 不需修改
- **Init states 共享**：大多数扰动 task 的 init states 从原始 10 个 base task 映射（代码自动 strip 后缀），Objects Layout 类别有独立 init states 在 `libero_newobj/` 目录
- **需要新 assets**：新增物体模型和纹理在 assets.zip 中（6GB），Background Textures 和 Objects Layout 类别必需

### 4. Eval 流程

**关键修改**：`num_trials_per_task` 从 50 改为 1。每个 LIBERO-Plus task 只有 1 个 trial（不像原 LIBERO 50 次 rollout）。

**eval 命令格式**：与原 LIBERO 几乎一致。现有 `eval_success_rate_libero.py` 可直接使用 LIBERO-Plus suites，只需：
1. `--suite libero_spatial` 现在包含 2402 tasks（而非 10）
2. 设置 `num_episodes=1`（或在代码中修改）
3. 指定 `--task_ids` 按需选择 category/difficulty 子集

**Success rate 计算**：每 task 1 次 rollout，done/not done → 0/1，按 category 或 difficulty 分组求平均。

### 5. Checkpoint 兼容性：✅ 可直接使用

现有 LIBERO fine-tuned checkpoint 可以直接在 LIBERO-Plus 上评估，无需重新训练：
- 环境接口完全一致（同一个 `OffScreenRenderEnv`）
- 扰动通过 bddl/init/运行时噪声实现，对模型透明
- 这正是 LIBERO-Plus 的设计意图：测试鲁棒性

### 6. Smoke Test 结果：✅ 通过

```
Available benchmarks: ['libero_spatial', 'libero_object', 'libero_goal', 'libero_90', 'libero_10', 'libero_100', 'libero_mix']
libero_spatial: 2402 tasks loaded
bddl_path exists: True
```

Benchmark 加载、task classification 映射、bddl 文件均验证通过。

### 7. 遗留项

1. **assets.zip 下载**：6GB 文件在后台 wget 下载中 (PID 155236)，预计 3+ 小时完成。完成后需执行：
   ```bash
   cd /root/autodl-tmp/LIBERO-plus/libero/libero
   unzip /root/autodl-tmp/libero_plus_assets.zip -d .
   ```
2. **端到端 eval 验证**：需 assets 下载完成后实际运行一个 task 确认环境渲染正常
3. **eval 脚本适配**：需写 LIBERO-Plus 专用 eval wrapper，支持按 category/difficulty 筛选 tasks 和分组统计

---

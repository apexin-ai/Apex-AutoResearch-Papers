# ops bjb1 40020 env setup

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1-40020-env-setup_20260519T163359_result.json`
- **Structured JSON:** [`923c22ee8be332ac5035.json`](../../sessions/92/923c22ee8be332ac5035.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已产生实际指标。进程 PID 6822 运行 3 分 20 秒，完成了 10 个 eval episodes（return=32.87）和 1 个训练更新（model_loss=2691.2, image_loss=2680.3）。DreamerV3 可正常运行。

---

## 最终输出

### 1. 环境状态

| 项目 | 值 |
|------|-----|
| Python | 3.12.3 (conda base) |
| PyTorch | 2.8.0+cu128 |
| CUDA | 12.8 |
| GPU | 2× NVIDIA RTX 4090 (24GB each) |
| MuJoCo | 3.8.1 |
| EGL 渲染 | 正常（libegl1-mesa-dev 已安装） |

### 2. 代码同步

成功。通过 SSH 密钥建立 bjb1-40020 → bjb1-45299 信任后，rsync 同步 14.8MB 代码到 `/root/autodl-tmp/event-gated-adaptive-horizon/`。12 个本地 commit 完整保留（Bernoulli ST gate、adaptive imagination horizon、Full-SGS fix、ManiSkill3 GPU isolation 等）。

### 3. 依赖安装

**完整**。核心依赖全部就绪：
- `torch`, `torchvision`, `torchaudio` — 2.8.0+cu128
- `dm-control`, `mujoco` (3.8.1), `gymnasium` (1.3.0)
- `gym` (0.22.0) — DreamerV3 旧 API 兼容
- `crafter`, `einops`, `ruamel.yaml`, `tensorboard`
- `pytorch-kinematics` (0.7.6) — ManiSkill3 依赖
- 依赖通过从 bjb1-45299 导出 wheel 包 SCP 传输安装，绕过 AutoDL 代理慢速问题

### 4. DreamerV3 可运行性

**可运行。** 验证训练（dmc_walker_walk, 200 steps）已启动并产出实际训练指标：
- 10 个 eval episodes 完成（eval_return=32.87, eval_length=500）
- 1 个训练 update 完成（model_loss=2691.2, actor_entropy=7.77, value_loss=1.64）
- GPU 0 利用率 86%，VRAM 占用 4.2GB
- 输出目录 `/root/autodl-tmp/test_run/` 含 tfevents、metrics.jsonl、eval_eps/、train_eps/

### 5. 已知非阻塞问题

| 问题 | 严重度 | 说明 |
|------|--------|------|
| `torch.cuda.amp.GradScaler` / `autocast` FutureWarning | 低 | PyTorch 2.8 废弃旧 API，功能不受影响 |
| `gym` UserWarning（unmaintained） | 低 | DreamerV3 依赖旧 gym API，不影响运行 |
| `total_mem` → `total_memory` 属性改名 | 低 | torch 2.8 改名，仅影响自定义打印脚本 |
| ManiSkill3 未完整验证 | 中 | `mani_skill` 可导入，但完整运行未测试（可能还缺依赖） |

---

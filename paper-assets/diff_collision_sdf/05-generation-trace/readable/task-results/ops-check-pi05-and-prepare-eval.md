# ops check pi05 and prepare eval

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_pi05_and_prepare_eval_20260522T103033_result.json`
- **Structured JSON:** [`620bcc487b18e74ba898.json`](../../sessions/62/620bcc487b18e74ba898.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。汇总如下：

---

## 1. pi0.5 下载状态

**进行中** — PID 368719 仍在运行，当前目录大小 **3.8G**。

文件结构是 JAX/Orbax checkpoint 格式。但有一个问题：下载脚本导致了**嵌套重复**——`params/` 下又有一层 `params/params/`，`assets/` 下又有 `assets/assets/`。后续加载时可能需要调整路径或重新整理目录。

## 2. 官方 eval 架构

openpi 使用 **client-server 架构**，需要两个终端：

**Terminal 1 — Policy Server**（需要 GPU）：
```bash
cd /root/autodl-tmp/openpi
uv run scripts/serve_policy.py --env LIBERO \
    policy:checkpoint --policy.config pi05_libero \
    --policy.dir /root/autodl-tmp/openpi_weights/pi05_libero/
```

**Terminal 2 — Eval Client**（LIBERO 仿真）：
```bash
cd /root/autodl-tmp/openpi
source examples/libero/.venv/bin/activate  # 需先创建
python examples/libero/main.py \
    --task-suite-name libero_spatial \
    --num-trials-per-task 50
```

eval 脚本路径：`/root/autodl-tmp/openpi/examples/libero/main.py`

## 3. 依赖检查

| 依赖 | 状态 |
|------|------|
| robosuite | ✅ 已安装 |
| openpi_client | ✅ 已安装 |
| tyro | ✅ 已安装 |
| jax | ✅ 已安装 |
| **libero** | ❌ 未安装 |
| **openpi** (server) | ❌ 未安装 |
| **third_party/libero/** | ❌ 空目录（git submodule 未初始化） |

**安装前需要做**：
```bash
cd /root/autodl-tmp/openpi
git submodule update --init --recursive   # 初始化 libero submodule
pip install -e .                          # 安装 openpi server 包
pip install -e third_party/libero         # 安装 libero
```

## 4. 预计时间线

- 等下载完成（PID 368719 仍在跑）
- 检查/修复嵌套目录结构
- 安装缺失依赖（libero + openpi）
- **等 GPU 释放**后才能启动 policy server
- 全 4 suite eval（spatial/object/goal/10）每个 50 episodes，预计数小时

---

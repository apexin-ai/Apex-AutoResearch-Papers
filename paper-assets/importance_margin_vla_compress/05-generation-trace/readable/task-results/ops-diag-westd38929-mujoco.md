# ops diag westd38929 mujoco

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diag-westd38929-mujoco_20260520T091124_result.json`
- **Structured JSON:** [`838c69a85e33fde79003.json`](../../sessions/83/838c69a85e33fde79003.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是汇总：

---

## 诊断结果

### 1. X-VLA eval 进程 — 已死
nvidia-smi 显示 4x RTX PRO 6000 (96GB)，显存占用 0MiB，无任何进程运行。X-VLA eval 也已崩溃。

### 2. MuJoCo/EGL — 本身正常
- MuJoCo 3.8.1 安装正确，`_render` 模块可加载
- `MUJOCO_GL=egl` 下渲染测试通过（64x64 RGB 输出正常）
- EGL 库完整：`libEGL_nvidia.so.580.95.05` + `10_nvidia.json` vendor 配置
- `torch.cuda.is_available() = True`

### 3. 发现两个问题

**问题 A（已恢复）：LIBERO 资源文件曾被清空**
- 15:10–15:24 的 X-VLA sweep 期间，`.msh`/`.png`/`.xml` 资源文件逐步变空
- 错误：`MSH file 'textured_vis.msh' is empty` / `empty PNG file 'texture_map.png'` / `ParseError: no element found`
- k=1.0 完成 Task 0 后在 Task 1 崩溃；k=0.95~0.1 全部立即崩溃
- 16:38:51 有人重装了 LIBERO（所有资源文件 Birth 时间一致）
- **当前文件完整**：textured_vis.msh=1.5MB, texture_map.png=1.1MB，无空文件

**问题 B（C4-ext segfault 17:00）：原生代码崩溃**
- 资源文件此时已恢复（test_eval_v4 在 16:42 成功跑完 2 episode）
- C4-ext 加载模型成功，开始 Task 0 后 segfault（无 Python traceback）
- 崩溃发生在 `OffScreenRenderEnv` 初始化阶段
- 可能是 EGL context 创建时的间歇性驱动崩溃

### 4. 环境附注
- `.bashrc` 中**没有** `export MUJOCO_GL=egl`（eval 脚本内部自行设置，所以不是直接原因）
- `.bashrc` 中**没有** conda 激活（`python3` 不在 PATH，需用 `/root/miniconda3/bin/python3`）
- 磁盘充足：根分区 24GB 可用，数据盘 71GB 可用

### 5. 修复建议
1. **立即可做**：直接重新启动 C4-ext eval — 环境现在是干净的（资源完整、GPU 空闲）
2. **加入 .bashrc**：`export MUJOCO_GL=egl` 和 conda 激活（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
3. **查清根因**：LIBERO 资源为什么会被清空？怀疑是 15:10 前后有并发 pip install 操作截断了文件
4. **加固 eval 脚本**：启动前校验关键资源文件非空，避免白跑后 segfault

---

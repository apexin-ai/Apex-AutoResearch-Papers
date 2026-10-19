# ops prepare pi05 eval env

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare_pi05_eval_env_20260522T103923_result.json`
- **Structured JSON:** [`9ec74da955f60af2d72c.json`](../../sessions/9e/9ec74da955f60af2d72c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 结果总结

### 1. 下载状态
- **进行中**（PID 368719），当前 4.4GB，params 仍在下载
- assets 已完成

### 2. 目录结构
- `params/params/` 是 orbax checkpoint 正常结构，**不需要修复**
- `assets/assets/` 是 gcsfs 下载产生的多余副本，下载完成后执行：
  ```bash
  rm -rf /root/autodl-tmp/openpi_weights/pi05_libero/assets/assets
  ```

### 3. 依赖安装状态
- openpi server：已安装（.venv，jax=0.5.3, torch=2.7.1）
- libero：已安装（PyPI 0.1.1, --no-deps + 手动补 bddl, easydict）
- robosuite 1.4.1, mujoco 3.8.1
- 所有 eval 所需 import 验证通过

### 4. 准备好的运行命令

**Terminal 1 — Server（占 1 张 GPU）：**
```bash
cd /root/autodl-tmp/openpi && source .venv/bin/activate
python3 scripts/serve_policy.py --env LIBERO --port 8000 \
  policy:checkpoint \
  --policy.config pi05_libero \
  --policy.dir /root/autodl-tmp/openpi_weights/pi05_libero
```

**Terminal 2 — Client（libero 仿真 eval）：**
```bash
cd /root/autodl-tmp/openpi && source .venv/bin/activate
python3 examples/libero/main.py \
  --host 0.0.0.0 \
  --port 8000 \
  --task_suite_name libero_spatial \
  --num_trials_per_task 50
```

### 注意
- 下载完成后需删除 `assets/assets/` 多余副本
- server 启动前确认下载完成（`ps -p 368719` 不返回 PID）
- `.libero/config.yaml` 已预创建，避免交互提示
- robosuite macros warning 可忽略，不影响 eval

---

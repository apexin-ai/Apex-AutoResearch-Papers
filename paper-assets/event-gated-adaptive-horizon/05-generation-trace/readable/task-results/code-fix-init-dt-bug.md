# code fix init dt bug

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_init_dt_bug_20260513T222320_result.json`
- **Structured JSON:** [`55cd3ae19213718b0172.json`](../../sessions/55/55cd3ae19213718b0172.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇报

### 1. 代码 diff（3 处改动）

```diff
--- models.py.bak
+++ models.py

# 调用处 (L459): 传入正确的 init_dt
+                init_dt_val = float(self._config.gate_fixed_dt) if self._config.gate_fixed_dt > 0 else 1.0
                 target, weights, base = self._compute_target(
-                    imag_feat, imag_state, reward, dts=dts
+                    imag_feat, imag_state, reward, dts=dts, init_dt=init_dt_val,
                 )

# 方法签名 (L602): 新增 init_dt 参数
- def _compute_target(self, imag_feat, imag_state, reward, dts=None):
+ def _compute_target(self, imag_feat, imag_state, reward, dts=None, init_dt=1.0):

# 核心修复 (L612): 用 init_dt 替代硬编码 1
-             init_dt_tensor = torch.ones_like(dts[:1])
+             init_dt_tensor = torch.full_like(dts[:1], init_dt)
```

### 2. Dry-run 结果
- **语法检查**: PASSED (`ast.parse` + `import models`)
- **启动测试**: PASSED（prefill 完成，模型初始化成功，无报错）
- **单元验证**: PASSED（`init_dt=4` 时 discount^4=0.988054 vs 旧 discount^1=0.997000，差 0.009）
- 完整训练循环因 90s timeout 未跑完，但代码路径无语法/runtime 错误

### 3. GPU 1 清理
- PID 85780（`fixed_dt4_v1_s1` 训练进程，4156 MiB）已 kill
- GPU 1 当前无残留进程

### 4. 修复后启动命令
```bash
cd /root/autodl-tmp/event-gated-adaptive-horizon && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && \
export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && \
python dreamer.py --configs defaults dmc_proprio \
  --task dmc_walker_walk \
  --logdir logdir/fixed_dt4_v2_initdt_fix_s1 \
  --steps 150000 --seed 1 --compile False \
  --device cuda:1 \
  --gate_enabled True --gate_fixed_dt 4
```

---

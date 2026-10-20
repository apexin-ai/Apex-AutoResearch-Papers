# ops verify 018 readiness

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-018-readiness_20260516T014122_result.json`
- **Structured JSON:** [`f881d6dd3a82ad24811a.json`](../../sessions/f8/f881d6dd3a82ad24811a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_018 Full-SGS 验证结果

### 代码版本 ✅
HEAD = `06ab285` "Fix Full-SGS: restore dt_emb.weight.requires_grad_(True) after imagination"
包含目标 commit `5fc8e49` 及额外修复。

### full_sgs 配置 ✅
- `configs.yaml` L121: `full_sgs: false`（默认关闭，CLI 可覆盖）
- `tools.args_type` 正确处理 bool：`bool(["False", "True"].index(x))`，`--full_sgs True` 解析无误
- `models.py` L346, L643, L647: Full-SGS 逻辑通过 `getattr(self._config, 'full_sgs', False)` 检查，就绪

### 环境 ✅
- `LD_PRELOAD` 路径 `/usr/lib/x86_64-linux-gnu/libstdc++.so.6` 存在（→ libstdc++.so.6.0.30）
- Logdir `exp_018_full_sgs_walker_s1/` 不存在，无旧数据

### 阻塞问题
无。

### 经验证的提交命令
```bash
cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python dreamer.py --task dmc_walker_walk --steps 105000 --full_sgs True --seed 1 --logdir /root/runs/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_walker_s1 --device cuda:0
```

009d 释放 `cuda:0` 后可立即提交。

---

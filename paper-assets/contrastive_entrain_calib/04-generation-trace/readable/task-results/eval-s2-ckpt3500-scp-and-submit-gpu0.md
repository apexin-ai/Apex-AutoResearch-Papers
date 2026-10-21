# eval s2 ckpt3500 scp and submit gpu0

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_s2-ckpt3500-scp-and-submit-gpu0_20260521T095947_result.json`
- **Structured JSON:** [`daef2566f2e42f255684.json`](../../sessions/da/daef2566f2e42f255684.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个任务全部完成。

## 产出

**1. s2-ckpt-3500 SCP 状态：新传**
- 29046 → 28034 直传成功（通过 SSH 密钥建立服务器间连接）
- 验证：`adapter_model.safetensors` = 245,405,936 bytes (~245MB) ✓
- 完整文件列表（15 个文件）已到位

**2. GPU 0 VRAM 预检 + eval 提交**
- 预检 VRAM：2 MiB（远 < 1000 阈值）✓
- eval 已提交：PID **867046**，tmux session `eval-s2-ckpt3500`
- RTX 5090 GPU 0 已加载模型：16,764 MiB / 32,607 MiB，GPU-Util 49%

**3. seed1 ckpt-8000：不存在**
- 29046 上 `exp003_r3only_seed1/` 最新 checkpoint 为 **7500**（共 15 个 ckpt: 500~7500）
- tmux `exp-003` session 输出为空（训练可能已结束或 session 过期）
- 未执行 SCP（无 ckpt-8000）

---

# check behavioral pilot v2 readiness

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_behavioral_pilot_v2_readiness_20260523T153207_result.json`
- **Structured JSON:** [`51da16bce17f06a673ae.json`](../../sessions/51/51da16bce17f06a673ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 代码就绪状态：✅ 就绪
- `behavioral_pilot_v2.py` 存在，完整脚本（3 tasks × 10 eps × 2 conditions）
- 辅助脚本也在：`behavioral_pilot.py`, `behavioral_smoketest.py`, `behavioral_sr_validation.py`

### 2. 环境就绪状态：✅ 就绪
| 包 | 版本 | 状态 |
|---|---|---|
| libero | installed (`/root/autodl-tmp/LIBERO/`, sys.path 加载) | ✅ |
| mujoco | 3.8.1 | ✅ EGL 渲染已验证 |
| robosuite | 1.4.1 | ✅ |
| torch | 2.10.0+cu128 | ✅ CUDA 可用 |
| transformers | 5.9.0 | ✅ |
| accelerate | 1.13.0 | ✅ |

### 3. Checkpoint：✅ 可用
`openvla-7b-finetuned-libero-goal` — 4 个 safetensor shard，完整。

### 4. GPU：⚠️ RTX PRO 6000 **Blackwell** Server Edition × 2（96GB each）
**这仍然是 Blackwell GPU**，不是普通 RTX PRO 6000。

### 5. 之前的阻塞问题

| 问题 | 当前状态 |
|------|---------|
| mujoco 版本不匹配 | ✅ 已解决，3.8.1 + EGL 正常 |
| Blackwell segfault 需 device_map | ✅ 代码已有 `device_map="cuda:0"` 绕过 |
| SR=0/3 baseline 全失败 | ❌ **未解决** — `sr_corrected_3ep.json` 显示 3 个 episode 全部 reward=0.0, steps=400 |
| action[0] 锁定在 0.236 | ❓ **未验证** — 这是 SR=0 的根因，当前环境未重新测试 |

### 6. 结论：**不能立即提交**

环境和代码都就绪，但 **SR=0 的根因（action 输出异常）从未被解决**。直接跑完整实验大概率还是全 0。

建议先跑 `behavioral_smoketest.py` 或一个 1-episode 快速验证，确认 baseline 条件下模型能产生有效 action 且 SR>0，然后再提交完整的 v2 实验。

---

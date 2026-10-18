# research simplerenv setup

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_simplerenv_setup_20260524T152240_result.json`
- **Structured JSON:** [`2d7cda2eacbc003651a1.json`](../../sessions/2d/2d7cda2eacbc003651a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个 Phase 完成情况：

| Phase | 状态 | 内容 |
|-------|------|------|
| **1. Research** | ✅ | SimplerEnv 架构、9 tasks、Policy 接口、竞品 (SP-VLA 等 5 个) |
| **2. Feasibility** | ✅ | Pruning hook 与 env 解耦，OpenVLA 适配 2-3h，π0.5 适配 4-6h |
| **3. Environment** | ✅ | westd-27271 安装完成：torch 2.11.0+cu128, 2x RTX PRO 6000 (94GB), simpler_env/sapien/mani_skill2 全部 import 通过 |
| **4. Pruning Adaptation** | ✅ | 方案已评估：OpenVLA 优先（forward hook 复用 + SimplerEnv policy 接口封装），π0.5 次之 |
| **5. Report** | ✅ | 已保存至 `artifacts/simplerenv_feasibility.md` 和 `memory.md` |

下一步建议：编写 `OpenVLAPruningPolicy` adapter 代码并运行首个 baseline 实验（Pick Coke Can task）。

---

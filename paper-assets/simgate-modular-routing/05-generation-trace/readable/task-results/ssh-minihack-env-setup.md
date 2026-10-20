# ssh minihack env setup

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_minihack-env-setup_20260519T111618_result.json`
- **Structured JSON:** [`e0c9b9c8d4220bcca176.json`](../../sessions/e0/e0c9b9c8d4220bcca176.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

---

## 环境搭建完成

### 服务器：westd-18266

**环境激活命令：**
```bash
export PATH="/root/miniconda3/bin:$PATH" && source activate minihack
```

**已安装组件：**

| 组件 | 版本 | 状态 |
|------|------|------|
| NLE | 0.9.0 | OK |
| MiniHack | 0.1.4 | OK |
| nle-language-wrapper | 0.2.0 | OK |
| BALROG | 0.1.0 (editable) | OK |
| balrog-nle | 0.9.0 | OK |
| gym | 0.23.0 | OK |
| openai | 2.37.0 | OK (用于连接 vLLM) |
| vLLM | 0.21.0 | OK (在 base env) |

**关键路径：**
- Qwen 模型：`/root/autodl-tmp/models/Qwen2.5-7B-Instruct/`
- BALROG 源码：`/root/autodl-tmp/BALROG/`
- Requirements：`/root/autodl-tmp/simgate-modular-routing/requirements_minihack.txt`

**5 个 Random Episode 结果 (MiniHack-Room-5x5-v0)：**

| Episode | Steps | Reward | Status |
|---------|-------|--------|--------|
| 1 | 15 | 0.9 | WON |
| 2 | 100 | -0.2 | DIED |
| 3 | 100 | -0.3 | DIED |
| 4 | 100 | -0.2 | DIED |
| 5 | 19 | 1.0 | WON |

**Text observation 质量：** 丰富，包含 message、language observation（方位描述）、cursor 位置、ASCII map。death signal (done=True) 可靠。

**注意事项：**
- vLLM 在 base env (Python 3.12) 中，需用 `VLLM_USE_FLASHINFER_SAMPLER=0` 启动
- minihack env 通过 openai client 连接 vLLM server
- BALROG 的 baba/textworld/minigrid 依赖未装（仅需 MiniHack 场景）
- numpy 固定 <2.0（gym 0.23 兼容性要求）
- setuptools 固定 70.3.0（pkg_resources 兼容性要求）

---

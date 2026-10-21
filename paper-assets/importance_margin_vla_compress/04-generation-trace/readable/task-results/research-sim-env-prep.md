# research sim env prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_sim_env_prep_20260516T072124_result.json`
- **Structured JSON:** [`d40bd9b506edc6b53f62.json`](../../sessions/d4/d40bd9b506edc6b53f62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。汇总如下：

---

## 调研结果

### 1. 服务器现有/缺失依赖

| 依赖 | 状态 |
|------|------|
| **lerobot** 0.5.1 | ✅ 已装（含 `envs/factory.py`, `scripts/lerobot_eval.py`） |
| **gymnasium** 1.3.0 | ✅ 已装 |
| **mujoco** | ❌ 未装 |
| **gym-aloha** | ❌ 未装 |
| **EGL (NVIDIA)** | ✅ 有 `libEGL_nvidia.so` |
| **GLX/GL** | ✅ 有 |
| **OSMesa** | ❌ 无（不需要，EGL 足够） |
| Python 版本 | 3.12（conda base） |

### 2. 需要安装的包

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
source /etc/network_turbo
pip install mujoco gym-aloha
```

`gym-aloha` 会拉入 `dm-control` 等 mujoco 相关依赖。

### 3. LeRobot aloha_sim_insertion rollout 标准方法

**lerobot 自带 eval 脚本**（`lerobot-eval`）：
```bash
lerobot-eval \
  --policy.path=&lt;HF格式checkpoint> \
  --env.type=aloha \
  --env.task=AlohaInsertion-v0 \
  --eval.n_episodes=50 \
  --eval.batch_size=10 \
  --policy.device=cuda
```

**但是**：`lerobot-eval` 需要 HuggingFace 格式 checkpoint（`config.json` + `model.safetensors`）。我们的 checkpoint 是自定义 PyTorch 格式（`checkpoint.pt` 内含 `model_state_dict`）+ IMM wrapper。

**推荐方案：写自定义 rollout 脚本**，直接用 gymnasium API：
```python
import gymnasium as gym
import gym_aloha  # 注册环境

env = gym.make("gym_aloha/AlohaInsertion-v0", obs_type="pixels_agent_pos")
# 加载我们的模型 → 跑 episode → 记录 success
```

env 配置（来自 lerobot `AlohaEnv`）：
- gym_id: `gym_aloha/AlohaInsertion-v0`
- action dim: 14
- obs: `pixels/top` (480×640×3) + `agent_pos` (14,)
- episode_length: 400 steps
- fps: 50
- success 判定：peg 成功 pick 并插入 socket（env 内置 reward/info 返回）

### 4. N=50 episodes 预估运行时间

- 50 episodes × 400 steps = 20,000 steps
- MuJoCo sim step 极快（~1ms），瓶颈在模型推理
- SmolVLA 单步推理（单 GPU）：~50-100ms
- 预估总时间：**20,000 × 0.05~0.1s ≈ 17~33 分钟/组**
- 3 组共 ~1~1.5 小时

### 5. Headless 渲染

服务器有 NVIDIA EGL，设置环境变量即可：
```bash
export MUJOCO_GL=egl
```
无需安装额外渲染库。

---

### 下一步

需要：
1. `pip install mujoco gym-aloha`
2. 编写自定义 `eval_sim.py` rollout 脚本（加载我们的 checkpoint → gym 环境交互 → 统计 success rate + 95% CI）
3. 对 3 组分别跑 N=50+

Sources:
- [lerobot/act_aloha_sim_insertion_human](https://huggingface.co/lerobot/act_aloha_sim_insertion_human)
- [LeRobot GitHub](https://github.com/huggingface/lerobot)
- [lerobot eval.py source](https://github.com/huggingface/lerobot/blob/main/lerobot/scripts/lerobot_eval.py)
- [gym-aloha PyPI](https://pypi.org/project/gym-aloha/)
- [LeRobot Imitation Learning in Sim docs](https://huggingface.co/docs/lerobot/il_sim)
- [SmolVLA fine-tuning guide](https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/)

---

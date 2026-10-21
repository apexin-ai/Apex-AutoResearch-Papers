# DreamerV3-torch 代码调研报告

> 仓库: [NM512/dreamerv3-torch](https://github.com/NM512/dreamerv3-torch)
> 调研日期: 2026-05-13

---

## 1. 仓库概览

### 活跃度
- **最新 commit**: 2026-03-08（`6ef8646` Merge pull request #81）
- **状态**: README 标注为 **Outdated Implementation**，作者推荐使用后继仓库 [r2dreamer](https://github.com/NM512/r2dreamer)（~5x 更快，包含 R2-Dreamer ICLR 2026）
- **代码量**: ~4100 行 Python，核心集中在 4 个文件：`models.py`(441L), `networks.py`(810L), `tools.py`(1000L), `dreamer.py`(365L)

### 依赖
| 包 | 版本 |
|---|---|
| PyTorch | 2.4.1 |
| gym | 0.22.0（**旧版**，非 gymnasium） |
| dm_control | 1.0.9 |
| mujoco | 2.3.5 |
| numpy | 1.23.5 |
| einops | 0.3.0 |

### DMC 支持
完整支持 DMC Proprio（state）和 DMC Vision（image）。环境封装在 `envs/dmc.py`，通过 `dm_control.suite.load()` 加载，支持 action_repeat、image rendering。`envs/wrappers.py` 提供 `NormalizeActions`, `TimeLimit`, `SelectAction`, `UUID` 等标准 wrapper。

### 支持的环境
DMC Proprio/Vision, Atari 100k, Crafter, Minecraft (MineRL), Memory Maze, DMLab

---

## 2. RSSM 实现

**文件**: `networks.py:13-291`
**类**: `RSSM(nn.Module)`

### 构造函数参数（默认值来自 configs.yaml）
```python
RSSM(stoch=32, deter=512, hidden=512, rec_depth=1, discrete=32,
     act="SiLU", norm=True, num_actions=..., embed=..., device=...)
```

### State 表示
RSSM state 是一个 dict，**离散模式**（默认）下包含：
```python
state = {
    "logit": (batch, stoch=32, discrete=32),   # categorical logits
    "stoch": (batch, stoch=32, discrete=32),    # one-hot samples
    "deter": (batch, deter=512),                # GRU deterministic state (h)
}
```
**连续模式**下包含 `mean`, `std`, `stoch`, `deter`。

### Feature 向量
`get_feat(state)` → `(batch, stoch*discrete + deter)` = `(batch, 32*32+512)` = `(batch, 1536)`
- 将 stoch reshape 为 `(batch, 1024)` 后与 deter `(batch, 512)` 拼接

### 核心函数

#### `img_step(prev_state, prev_action, sample=True)` — networks.py:208-233
**Prior transition**（想象步）：不使用观测，纯模型预测。
```
输入:
  prev_state: dict, 上一步的 RSSM state
  prev_action: (batch, act_dim)
输出:
  prior: dict, 预测的下一步 state {stoch, deter, logit}

数据流:
  1. prev_stoch flatten → (batch, stoch*discrete) = (batch, 1024)
  2. cat([prev_stoch, prev_action]) → (batch, 1024+act_dim)
  3. _img_in_layers (Linear+LN+SiLU) → (batch, hidden=512)
  4. GRUCell(x, [prev_deter]) → new deter (batch, 512)
  5. _img_out_layers (Linear+LN+SiLU) → (batch, hidden=512)
  6. _imgs_stat_layer → logit (batch, stoch, discrete) = (batch, 32, 32)
  7. sample from OneHotDist → stoch (batch, 32, 32)
```

#### `obs_step(prev_state, prev_action, embed, is_first, sample=True)` — networks.py:174-206
**Posterior update**（观测步）：结合观测更新 state。
```
输入:
  prev_state: dict (可为 None)
  prev_action: (batch, act_dim)
  embed: (batch, embed_dim), 编码器输出
  is_first: (batch, 1), 用于重置 state
输出:
  post: dict, 后验 state
  prior: dict, 先验 state

数据流:
  1. 如果 is_first，重置 prev_state 和 prev_action
  2. prior = self.img_step(prev_state, prev_action) → 先验预测
  3. cat([prior["deter"], embed]) → (batch, deter+embed)
  4. _obs_out_layers → (batch, hidden=512)
  5. _obs_stat_layer → logit (batch, 32, 32)
  6. sample → post stoch, 复用 prior 的 deter
```

#### `observe(embed, action, is_first, state=None)` — networks.py:127-143
沿时间轴展开 obs_step，使用 `tools.static_scan`。
```
输入: embed (batch, time, embed_dim), action (batch, time, act_dim), is_first (batch, time, 1)
输出: post, prior — 每个 key 的 shape 为 (batch, time, ...)
```

#### `kl_loss(post, prior, free, dyn_scale, rep_scale)` — networks.py:272-290
双向 KL loss，分别对 posterior（rep_loss）和 prior（dyn_loss）求 KL divergence，clip by `kl_free=1.0`。
```
loss = dyn_scale * dyn_loss + rep_scale * rep_loss
默认: dyn_scale=0.5, rep_scale=0.1
```

### GRUCell — networks.py:742-768
自定义 GRU，单层 `Linear(inp+size, 3*size)` + LayerNorm，update_bias=-1（偏向保留旧状态）。

---

## 3. Imagination Loop

**文件**: `models.py:351-369`
**函数**: `ImagBehavior._imagine(start, policy, horizon)`

### 展开逻辑
```python
def _imagine(self, start, policy, horizon):
    dynamics = self._world_model.dynamics
    flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))
    start = {k: flatten(v) for k, v in start.items()}
    # start shape: 从 (batch, time, ...) 展平为 (batch*time, ...)

    def step(prev, _):
        state, _, _ = prev
        feat = dynamics.get_feat(state)
        inp = feat.detach()              # ← 关键: detach，梯度不穿过 policy 输入
        action = policy(inp).sample()
        succ = dynamics.img_step(state, action)  # 调用 RSSM.img_step
        return succ, feat, action

    succ, feats, actions = tools.static_scan(
        step, [torch.arange(horizon)], (start, None, None)
    )
    # states 包含初始 state + horizon-1 步后继
    states = {k: torch.cat([start[k][None], v[:-1]], 0) for k, v in succ.items()}
    return feats, states, actions
```

### 关键细节
1. **步数控制**: `horizon` 参数来自 `self._config.imag_horizon`，**默认 15 步**（configs.yaml:78）
2. **调用方式**: `models.py:300-301`:
   ```python
   imag_feat, imag_state, imag_action = self._imagine(
       start, self.actor, self._config.imag_horizon
   )
   ```
3. **步数是 config 参数，非 hardcoded 常量**，但在整个 imagination 过程中是**固定的**——每次 imagination 都展开相同的 `imag_horizon` 步
4. **State 传递**: `start` 来自 world model 的 posterior（`dreamer.py:121`: `start = post`），被 flatten 为 (B*T, ...)
5. **输出 shapes** (以 horizon=15 为例):
   - `feats`: (15, B*T, feat_dim=1536)
   - `states`: dict, 每个 (15, B*T, ...)
   - `actions`: (15, B*T, act_dim)
6. **static_scan**: `tools.py:795-839`，Python for-loop 逐步展开，无并行优化

### 梯度流
- `feat.detach()` 传入 policy → actor 梯度不通过 state transition（当 `imag_gradient="reinforce"` 时）
- 当 `imag_gradient="dynamics"` 时（默认），actor loss 直接对 target（λ-return）求梯度，梯度通过 dynamics model 回传

---

## 4. λ-Return 计算

**文件**: `tools.py:691-717`
**函数**: `lambda_return(reward, value, pcont, bootstrap, lambda_, axis)`

### 接口
```python
# 调用处: models.py:378-385
target = tools.lambda_return(
    reward[1:],           # (horizon-1, B*T, 1), 跳过第一步
    value[:-1],           # (horizon-1, B*T, 1), 跳过最后一步
    discount[1:],         # (horizon-1, B*T, 1)
    bootstrap=value[-1],  # (B*T, 1), 最后一步 value 作为 bootstrap
    lambda_=0.95,         # config.discount_lambda
    axis=0,
)
```

### 计算逻辑
```python
# 输入预处理
next_values = cat([value[1:], bootstrap[None]], 0)
inputs = reward + pcont * next_values * (1 - lambda_)

# 反向扫描（从最后一步向前）
# agg_{t} = inputs_{t} + pcont_{t} * lambda_ * agg_{t+1}
# 初始: agg_{T} = bootstrap
returns = static_scan_for_lambda_return(
    lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,
    (inputs, pcont), bootstrap
)
```

展开公式：`G_t^λ = r_{t+1} + γ_{t+1} [(1-λ) V(s_{t+1}) + λ G_{t+1}^λ]`

### 折扣因子
- `discount` 不是固定标量，而是来自 **continue predictor head** 的输出（`models.py:372-376`）：
  ```python
  discount = config.discount * self._world_model.heads["cont"](inp).mean
  ```
  其中 `config.discount = 0.997`，`cont` head 输出 Bernoulli 概率（0~1），表示 episode 是否继续
- **λ = 0.95**（`config.discount_lambda`）

### 权重计算 — models.py:386-388
```python
weights = torch.cumprod(
    cat([ones_like(discount[:1]), discount[:-1]], 0), 0
).detach()
# weights shape: (horizon, B*T, 1), 逐步衰减的折扣权重
```

### 输出
`target` 是一个 list，长度 horizon-1，每个元素 (B*T, 1)。在 actor/value loss 中被 stack 为 (horizon-1, B*T, 1)。

---

## 5. Replay Buffer 与数据流

### Episode 存储格式
**文件**: `tools.py:252-306`

Episodes 存储为 **npz 文件**，文件名格式: `{uuid}-{length}.npz`。

每个 episode 是一个 dict:
```python
{
    "image": np.array, (T, H, W, C), uint8,
    "action": np.array, (T, act_dim), float32,
    "reward": np.array, (T,), float32,
    "discount": np.array, (T,), float32,
    "is_first": np.array, (T,), bool,
    "is_terminal": np.array, (T,), bool,
    # 可能有 proprio state keys (DMC)
}
```

### 内存缓存
`tools.simulate()` (tools.py:128-249) 在运行时维护 `cache: OrderedDict`，key 为 env UUID，value 为 episode 的 dict（list of transitions）。通过 `add_to_cache()` 逐步追加 transition。

`erase_over_episodes()` (tools.py:267-277) 控制 dataset 大小上限（默认 `dataset_size=1e6` 步），按 FIFO 删除旧 episode。

### 采样方式
**文件**: `tools.py:323-361`
**函数**: `sample_episodes(episodes, length, seed=0)`

关键采样逻辑:
1. **按 episode 长度加权采样**: `p = episode_lengths / sum(episode_lengths)`
2. **随机起始索引**: 在选中的 episode 中随机取一段
3. **sequence length**: 由 `config.batch_length`（默认 **64**）控制
4. **跨 episode 拼接**: 如果采样的片段不够长，会从另一个 episode 的**起始位置**继续拼接，并设置 `is_first[size] = True` 标记边界
5. **无 overlap 控制**: 采样是随机独立的，不同 batch 的 sequence 可能有重叠

### Batch 构造
`tools.from_generator()` (tools.py:309-320): 从 generator 取 `batch_size` 个 sequence，stack 成 batch。

**默认 batch**: (batch_size=16, batch_length=64, ...)

### 训练频率
`config.train_ratio = 512`: 每收集 `batch_size * batch_length / train_ratio` = `16*64/512` = 2 个环境步就训练一次。

---

## 6. World Model 训练 Pipeline

**文件**: `models.py:108-174`
**函数**: `WorldModel._train(data)`

### Loss 组成

| Loss | 权重/Scale | 来源 | 说明 |
|------|-----------|------|------|
| KL Loss | `dyn_scale=0.5` + `rep_scale=0.1` | `dynamics.kl_loss()` | KL(posterior ‖ prior)，free bits=1.0 |
| Decoder Loss | 1.0 | `heads["decoder"]` | Image reconstruction (MSE) |
| Reward Loss | 1.0 (`reward_head.loss_scale`) | `heads["reward"]` | SymlogDisc (255-bin discretized) |
| Continue Loss | 1.0 (`cont_head.loss_scale`) | `heads["cont"]` | Binary cross-entropy |

总 loss:
```python
model_loss = sum(scaled_losses.values()) + kl_loss  # (batch, time) → scalar via mean
```

### Optimizer
```python
tools.Optimizer("model", self.parameters(), lr=1e-4, eps=1e-8, grad_clip=1000,
                weight_decay=0.0, opt="adam", use_amp=False)
```
- **Adam** optimizer, lr=1e-4
- Grad clipping: 1000（几乎不 clip）
- AMP: 仅在 `precision=16` 时启用（默认 32，不启用）

### Actor-Critic 训练 — models.py:290-349

**Actor**:
```python
Optimizer("actor", lr=3e-5, eps=1e-5, grad_clip=100)
```
- Loss = -weights * advantage + entropy_bonus (3e-4)
- `imag_gradient="dynamics"` 时直接用 λ-return 作为 actor_target
- `imag_gradient="reinforce"` 时用 REINFORCE（Atari/Crafter/Minecraft 使用）

**Critic**:
```python
Optimizer("value", lr=3e-5, eps=1e-5, grad_clip=100)
```
- Loss = -value.log_prob(target)（SymlogDisc 分布下）
- Slow target: EMA 更新，`fraction=0.02`, 每步更新

### RewardEMA — models.py:11-26
使用 5% 和 95% 分位数做 running EMA（α=0.01），用于 normalize advantage。

### 训练主循环 — dreamer.py:117-133
```python
def _train(self, data):
    post, context, mets = self._wm._train(data)       # 1. 训练 world model
    start = post                                        # 2. posterior 作为 imagination 起点
    reward = lambda f, s, a: self._wm.heads["reward"](
        self._wm.dynamics.get_feat(s)).mode()           # 3. 用 reward head 预测
    self._task_behavior._train(start, reward)           # 4. 训练 actor-critic
```

---

## 7. 修改切入点分析（为 Event Gate 改造）

### 核心目标: 将固定 imag_horizon 改为自适应的 event-gated horizon

#### 切入点 1: `ImagBehavior._imagine()` — models.py:351-369 ⭐ 最关键

**现状**: 固定 horizon 通过 `tools.static_scan(step, [torch.arange(horizon)], ...)` 控制。`static_scan` 是简单 for-loop，按 `horizon` 次迭代。

**改造方案**:
- 替换 `static_scan` 为自定义循环，在每步调用 event gate 判断是否提前终止
- 或使用 variable-length scan，gate 输出作为 mask 控制有效步数
- **注意**: 不同 batch element 可能在不同步终止，需要处理不等长 trajectory

**可扩展性评估**: `_imagine` 函数签名接受 `horizon` 参数，但 `static_scan` 假设固定长度。需要重写循环逻辑。

#### 切入点 2: `_compute_target()` — models.py:371-389

**现状**: `lambda_return` 接收固定长度的 reward/value/discount 序列。

**改造方案**:
- 如果 trajectory 长度可变，需要 mask 不同 trajectory 的有效步数
- `weights` 的 cumprod 计算需要考虑 gate 导致的提前终止
- 可以将 event gate 的输出乘入 `discount`，使 gate=0 等价于 episode 终止

#### 切入点 3: `RSSM.img_step()` — networks.py:208-233

**现状**: 纯粹的 one-step transition，无 gate 逻辑。

**改造方案**:
- 可以在 img_step 后加一个 event detector（输入 feat 或 state，输出 gate probability）
- 作为一个新的 MLP head 添加到 WorldModel

#### 切入点 4: `tools.static_scan()` — tools.py:795-839

**现状**: 通用的 sequential scan，固定迭代次数。

**改造方案**:
- 可以添加一个带 early-stop 条件的 `dynamic_scan` 变体
- 或保持 max_horizon 次迭代但返回 mask 指示实际有效步数

### Hardcoded vs 可配置项
| 项目 | 位置 | 类型 |
|------|------|------|
| `imag_horizon=15` | configs.yaml:78 | **Config 参数**，但运行时固定 |
| `discount=0.997` | configs.yaml:76 | Config 参数 |
| `discount_lambda=0.95` | configs.yaml:77 | Config 参数 |
| imagination loop 结构 | models.py:351-369 | **Hardcoded** 为固定步数循环 |
| static_scan 循环方式 | tools.py:795-839 | **Hardcoded** 为固定迭代 |
| reward function 签名 | dreamer.py:122-124 | 可插拔（lambda 函数） |
| heads dict | models.py:55-86 | **可扩展**（ModuleDict） |

### 建议的改造路径
1. 在 `WorldModel.heads` 中添加 `"event_gate"` head（类似 cont head，Binary 输出）
2. 重写 `_imagine` 方法，使用 max_horizon + gate mask 替代固定 horizon
3. 在 `_compute_target` 中将 gate 信号合并到 discount 中
4. Event gate head 可以和 world model 一起训练（添加到 `_train` 的 loss 中），或者单独训练
5. 保持 `img_step` 不变——gate 判断应在 step 之后、下一步之前

### 潜在风险
- **梯度问题**: 如果 gate 是离散决策（stop/continue），需要 straight-through estimator 或 Gumbel-Softmax
- **Batch 不等长**: 不同样本在不同步终止，需要 padding + mask，影响 λ-return 计算效率
- **训练不稳定**: Gate 学习早期可能过早终止（collapse），需要 entropy bonus 或 minimum horizon 约束

# ssh fla version investigate

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fla-version-investigate_20260518T123702_result.json`
- **Structured JSON:** [`748b4cfadfbc16bd6a4b.json`](../../sessions/74/748b4cfadfbc16bd6a4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是完整的发现总结。

---

## 调查结果

### 1. Checkpoint 中确实有 `attn.D` keys

每个 GatedDeltaNet 层都有一个 `model.layers.X.attn.D` 参数：
- **Pure 模型**: 24 个 D keys（24 层全部有）
- **Hybrid-3-1 模型**: 16 个 D keys（仅 GatedDeltaNet 层有，标准 attention 层没有）
- D 的形状为 `(num_heads,)` = `(8,)`

### 2. fla 0.5.0 不期望这些 keys

- fla 0.5.0 的 `GatedDeltaNet` 层 **没有定义 `self.D` 参数**
- Pure 模型：checkpoint 459 keys vs model 435 keys，差值 = 24（完全是 D keys）
- **Checkpoint 有但 model 没有**: 24 个 `model.layers.X.attn.D`
- **Model 有但 checkpoint 没有**: 0 个

### 3. D 参数是何时被移除的

- **commit `834989c`**（2025-03-12）"[Gated DeltaNet] Remove redundant parameter (fix #226)"
- 移除了两行：`self.D = nn.Parameter(torch.ones(self.num_heads))` 和 `self.D._no_weight_decay = True`
- **D 从未在 forward 中使用过**——是个定义了但没有参与计算的"冗余参数"
- fla 首个 PyPI 版本 0.1（2025-03-20）已在移除之后，**所有 PyPI 版本都不含 D**

### 4. Config 版本线索

| 字段 | Checkpoint 值 | fla 0.5.0 行为 | 兼容性 |
|------|-------------|------------|--------|
| `transformers_version` | 4.51.3 (pure) / 4.49.0 (hybrid) | 5.8.1 | — |
| `use_beta` | `true` | **已改名为 `allow_neg_eigval`，默认 `false`** | **不兼容** |
| `qk_activation` | `silu` | 硬编码 silu | 兼容 |
| `qk_norm` | `l2` | 硬编码 `use_qk_l2norm_in_kernel=True` | 兼容 |
| `use_output_norm` | `true` | 始终使用 o_norm | 兼容 |
| `expand_k` | `1` | 不存在此字段（无 k 扩展概念） | 兼容 |

### 5. 存在两个不兼容问题

**问题 A（D 参数）**: 加载时 strict 模式会报错。但 **D 从未参与计算**，用 `strict=False` 加载即可，不影响模型行为。

**问题 B（use_beta → allow_neg_eigval 重命名）**: 这是**计算层面的不兼容**。checkpoint config 有 `use_beta: true`，但 fla 0.5.0 读取 `allow_neg_eigval`（默认 `false`）。结果是 forward 中 `beta = beta * 2.0` 不会被执行，而训练时是执行的。

### 6. 正确的 fla 版本

m-a-p 模型使用的是 **2025-03-12 之前的 fla git 版本**（pre-PyPI，通过 `pip install git+https://github.com/fla-org/flash-linear-attention` 安装）。没有对应的 PyPI release。

**实际解决方案**（不需要降级 fla）：
1. 加载时用 `strict=False` 跳过 D 参数
2. 加载 config 后手动设置 `config.allow_neg_eigval = True`（映射旧的 `use_beta: true`）
3. 或直接在 config.json 中添加 `"allow_neg_eigval": true`

---

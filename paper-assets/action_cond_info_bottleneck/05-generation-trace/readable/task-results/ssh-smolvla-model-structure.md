# ssh smolvla model structure

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_smolvla-model-structure_20260517T074449_result.json`
- **Structured JSON:** [`215b3c6536ddb3989a83.json`](../../sessions/21/215b3c6536ddb3989a83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果。以下是产出汇总：

---

## SmolVLA 模型结构

### 模块层级树
```
SmolVLAPolicy
└── model: VLAFlowMatching
    ├── vlm_with_expert: SmolVLMWithExpertModel
    │   ├── vlm: SmolVLMForConditionalGeneration
    │   │   ├── model: SmolVLMModel
    │   │   │   ├── vision_model: SmolVLMVisionTransformer     (86.4M)
    │   │   │   ├── connector: SmolVLMConnector [PixelShuffle]  (11.8M)
    │   │   │   └── text_model: LlamaModel                     (204.6M)
    │   │   └── lm_head: Linear                                (47.3M)
    │   └── lm_expert: LlamaModel [action head]                (98.2M)
    ├── state_proj: Linear                                      (0.03M)
    ├── action_in_proj: Linear                                  (0.02M)
    ├── action_out_proj: Linear                                 (0.02M)
    ├── action_time_mlp_in: Linear                              (1.0M)
    └── action_time_mlp_out: Linear                             (0.5M)
```

**Total: 450M params, 500 tensors**

### 各组件的 parameter name prefix（相对于 `policy`）

| 组件 | prefix | 参数量 |
|------|--------|--------|
| **Vision Encoder** | `model.vlm_with_expert.vlm.model.vision_model` | 86.4M |
| **Connector (PixelShuffle)** | `model.vlm_with_expert.vlm.model.connector` | 11.8M |
| **VLM Text Model (LM backbone)** | `model.vlm_with_expert.vlm.model.text_model` | 204.6M |
| **VLM LM Head** | `model.vlm_with_expert.vlm.lm_head` | 47.3M |
| **LM Expert (action head)** | `model.vlm_with_expert.lm_expert` | 98.2M |
| **Action/State projections** | `model.state_proj`, `model.action_*` | ~1.6M |

### Connector 结构
`SmolVLMConnector` = PixelShuffle (spatial downsampling 4x) + `SmolVLMSimpleMLP` (linear projection)
- 只有 1 个 tensor (11.8M) → 这是 `modality_projection` 的权重

### 现有 freeze 逻辑 (`acib_policy.py:_setup_freeze`)

```python
def _setup_freeze(self, config):
    if config.freeze_vlm:
        # Freezes: vision_model + connector + text_model + lm_head (350M)
        for param in self._vlm_with_expert.vlm.parameters():
            param.requires_grad = False
    if config.freeze_action_expert:
        # Freezes: lm_expert (98.2M)
        for param in self._vlm_with_expert.lm_expert.parameters():
            param.requires_grad = False
    if config.train_scorer_only:
        # Freezes entire base_policy (all 450M)
        for param in self.base_policy.parameters():
            param.requires_grad = False
    # Always keep scorer trainable
    for param in self.scorer.parameters():
        param.requires_grad = True
```

### 关键发现

当前 `freeze_vlm=True` 会**同时 freeze connector**（因为 connector 是 `vlm.model.connector`，属于 `vlm.parameters()` 的一部分）。如果需要保持 connector trainable，需要在 `_setup_freeze` 中加一步：

```python
if config.freeze_vlm:
    for param in self._vlm_with_expert.vlm.parameters():
        param.requires_grad = False
    # Unfreeze connector for ACIB
    for param in self._connector.parameters():
        param.requires_grad = True
```

其中 `self._connector` 已经在 `acib_policy.py` 中定义为 property：
```python
@property
def _connector(self):
    return self._vlm_with_expert.vlm.model.connector
```

---

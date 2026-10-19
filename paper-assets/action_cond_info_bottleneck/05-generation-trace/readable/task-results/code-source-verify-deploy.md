# code source verify deploy

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_source-verify-deploy_20260515T122546_result.json`
- **Structured JSON:** [`13b22d8099248411a919.json`](../../sessions/13/13b22d8099248411a919.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

服务器 `westb-13953` 端口 13953 连接超时，AutoDL 实例可能已关机或端口已变。请去 AutoDL 控制台确认实例状态和新端口。

---

## 产出汇报

### 1. SmolVLA 精确模块层次结构

```
SmolVLAPolicy (PreTrainedPolicy)
└── model: VLAFlowMatching
    └── vlm_with_expert: SmolVLMWithExpertModel
        ├── vlm: SmolVLMForConditionalGeneration
        │   └── model
        │       ├── vision_model          ← SigLIP vision encoder
        │       ├── connector             ← PixelShuffle + Linear proj
        │       └── text_model            ← SmolLM2 language backbone
        │           └── layers[0..15]
        ├── lm_expert                     ← Action expert (smaller LM)
        │   └── layers[0..15]
        └── processor                     ← AutoProcessor (tokenizer)
    ├── state_proj: Linear(32 → 960)
    ├── action_in_proj: Linear(32 → 720)
    ├── action_out_proj: Linear(720 → 32)
    └── action_time_mlp_{in,out}
```

### 2. Connector/Vision Encoder 精确名称

| 模块 | 从 SmolVLAPolicy 的访问路径 |
|------|---------------------------|
| Vision encoder | `model.vlm_with_expert.vlm.model.vision_model` |
| Connector | `model.vlm_with_expert.vlm.model.connector` |
| Text model | `model.vlm_with_expert.vlm.model.text_model` |
| Action expert | `model.vlm_with_expert.lm_expert` |

### 3. forward() 返回值结构

- `SmolVLAPolicy.forward(batch)` → `(loss: scalar, loss_dict: dict)` (default `reduction="mean"`)
- `VLAFlowMatching.forward(...)` → `losses: (B, chunk_size, max_action_dim)` (MSE per element)
- `SmolVLMWithExpertModel.forward(...)` → `(outputs_embeds: list[Tensor], past_key_values)`

### 4. ACIB 代码状态

代码已在本地 artifacts 准备就绪，服务器 SSH 恢复后执行 `deploy.sh` 即可部署：
- `artifacts/code/acib/acib_policy.py` — **已重写**，用精确模块路径替换了所有 `_find_module()` 模糊搜索
- `artifacts/code/acib/{config,scorer,losses,__init__}.py` — 已确认正确
- `artifacts/code/ARCHITECTURE_NOTES.md` — 完整架构文档
- `artifacts/code/deploy.sh` — 一键部署脚本

### 5. UNVERIFIED 项确认结果

| 原标记 | 确认结果 |
|--------|---------|
| Connector 模块名 | `vlm.model.connector` ✅ |
| Vision encoder 模块名 | `vlm.model.vision_model` ✅ |
| Hook 注册点 | connector 的 `register_forward_hook`，在 `embed_image()` 中被调用 ✅ |
| Visual tokens shape | `(B, N, 960)` — N 取决于 SigLIP patch 数 + pixel shuffle ✅ |
| `num_expert_layers=0` 含义 | 等同于 `-1`，expert 层数 = VLM 层数 (16) ✅ |
| forward 返回值 | `(loss, loss_dict)` 而非 `(loss, outputs)` ✅ |
| Conditioning 可行性 | `connector_output.mean(dim=1)` 作为 self-conditioning，无需额外模块 ✅ |
| 图像分辨率 | `resize_with_pad` 到 512×512，pad_value=-1，pad 在左上 ✅ |
| Attention mode | 默认 `cross_attn`，`self_attn_every_n_layers=2` ✅ |

**待做**：SSH 恢复后 (1) 执行 deploy.sh 部署代码 (2) clone lerobot-src 到服务器 (3) 运行 import 验证。

---

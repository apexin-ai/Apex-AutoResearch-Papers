# research openvla eval prep

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_openvla_eval_prep_20260525T060618_result.json`
- **Structured JSON:** [`16e54259d5ede39711e1.json`](../../sessions/16/16e54259d5ede39711e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个 agent 已返回。汇总如下：

---

## OpenVLA Zero-Shot Eval on SafeLIBERO — 可行性调研报告

### 1. 兼容性：直接兼容

| | OpenVLA | SafeLIBERO |
|---|---|---|
| Action space | 7D delta EE pose `[dx,dy,dz,droll,dpitch,dyaw,gripper]` | 同上（robosuite OSC_POSE） |
| Action 表示 | 256 bins tokenization → autoregressive 7 tokens | 连续 7D |
| 输入 | 单张 224×224 图 + text prompt | agentview 256×256 |
| Proprioception | 不使用 | 可用但非必需 |

**直接兼容，无需 adapter。** OpenVLA 的 `predict_action()` 输出的 7D numpy array 可直接送入 SafeLIBERO `env.step()`，只需做 gripper 符号翻转（OpenVLA: 0=close/1=open → LIBERO: +1=close/-1=open）。

### 2. Checkpoint

| 项目 | 详情 |
|---|---|
| Base model | `openvla/openvla-7b`（15.1 GB bf16, MIT license） |
| 架构 | SigLIP + DINOv2 → Llama-2 7B |
| **LIBERO fine-tuned** | **有官方 LoRA checkpoint（4个）** |
| `openvla/openvla-7b-finetuned-libero-spatial` | LoRA r=32, 60K steps |
| `openvla/openvla-7b-finetuned-libero-object` | 同上 |
| `openvla/openvla-7b-finetuned-libero-goal` | 同上 |
| `openvla/openvla-7b-finetuned-libero-10` | 同上（LIBERO-Long） |
| OpenVLA-OFT 版本 | `moojink/openvla-7b-oft-finetuned-libero-*`（连续 action head, 更快更强） |

### 3. Eval 方案

**推荐方案 B：改我们的 `eval_safelibero.py` 添加 OpenVLA model type。**

理由：
- 我们的碰撞检测逻辑（obstacle displacement threshold）完全 model-agnostic，直接复用
- 只需改 2 个函数：`load_policy()` + `get_action_from_policy()`
- OpenVLA 官方 `run_libero_eval.py` 没有碰撞检测，反向加入更麻烦

需改动的代码：

```python
# load_policy() — 新增 openvla 分支
from transformers import AutoModelForVision2Seq, AutoProcessor
vla = AutoModelForVision2Seq.from_pretrained(
    checkpoint_path, torch_dtype=torch.bfloat16,
    attn_implementation="flash_attention_2",
    low_cpu_mem_usage=True, trust_remote_code=True
).to("cuda:0")
processor = AutoProcessor.from_pretrained(checkpoint_path, trust_remote_code=True)

# get_action_from_policy() — 新增 openvla 分支
prompt = f"In: What action should the robot take to {instruction}?\nOut:"
inputs = processor(prompt, image).to("cuda:0", dtype=torch.bfloat16)
action = vla.predict_action(**inputs, unnorm_key=suite_name, do_sample=False)
# gripper 后处理: [0,1] → [-1,1], 符号翻转
action[-1] = -np.sign(2 * action[-1] - 1)
```

注意事项：
- 图像预处理需 180° 旋转（`img[::-1, ::-1]`），这是 OpenVLA LIBERO 训练时的 convention
- Base OpenVLA 是 **single-step prediction**（无 action chunking），`replan_steps` 应设为 1
- `unnorm_key` 需与 checkpoint 对应的 suite name 匹配

工作量估计：**~2-3 小时代码改动 + 调试**。

### 4. 资源预估

| 项目 | 估值 |
|---|---|
| 显存 | ~15 GB bf16（96 GB RTX PRO 6000 绰绰有余） |
| 推理速度 | ~6 Hz（~167 ms/step） |
| 每 episode | max 300 steps × 167 ms ≈ **50 秒**（但 single-step replan 每步都要 inference，比 pi0 action chunking 慢） |
| 800 episodes | 800 × 50s ≈ **~11 小时** |
| 单卡即可 | 不需要多卡 |

### 5. 已知风险/关键发现

**重大发现：VLSA/AEGIS 论文（arXiv:2512.11891）已在 SafeLIBERO 上跑过 OpenVLA-OFT：**

| Suite | CAR | TSR |
|---|---|---|
| Spatial | 12.75% | 35.75% |
| Goal | 25.00% | 22.50% |
| Object | 17.25% | 29.50% |
| Long | 5.50% | 3.50% |
| **Average** | **15.13%** | **22.81%** |

**这对我们的 "fake safety" 论点意义重大：**
- OpenVLA-OFT CAR 极低（15%）= 大量碰撞 → **没有 action collapse / 冻结**
- 这与 Pi0/Pi0.5 的 "高 CAR 但实际是冻结" 模式**完全不同**
- 可能的解释：OpenVLA-OFT 用连续 action head + action chunking，不容易产生 token collapse
- **但 base OpenVLA（autoregressive tokenization）可能不同** — token-based prediction 更容易 collapse 到重复 token

**风险清单：**
1. **Base OpenVLA 可能也不 collapse** — 如果 OpenVLA 不展现 fake safety，反而削弱我们的 generalizability 论点
2. **也可能展现 collapse** — autoregressive token prediction 有 known degeneration 问题，可能出现重复 token → 固定小 action → 伪冻结
3. **VLSA 已有 OFT 结果** — 需确认 base OpenVLA 是否也被评估过（如果有，我们可以直接引用而不用重跑）
4. **依赖问题** — OpenVLA 需要 `prismatic` 库（自定义 HF 注册类），需确认与我们现有环境兼容
5. **图像预处理敏感** — 180° 旋转 + JPEG encode/decode + lanczos3 resize 的 pipeline 必须严格复现，否则性能大幅下降

### 建议优先级

1. **先查 VLSA 论文是否有 base OpenVLA（非 OFT）在 SafeLIBERO 的结果** — 如果有，直接引用
2. **跑 base OpenVLA（autoregressive tokenization）** — 这是最可能展现 action collapse 的版本，因为 token degeneration 是 autoregressive 模型的已知问题
3. **OFT 结果可以直接引用 VLSA 论文**，不需要重跑
4. 如果 base OpenVLA 也不 collapse，考虑换角度：不同 VLA 架构展现不同的 failure mode（collapse vs. collision），仍然有论文价值

---

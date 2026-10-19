# code phase0 script

**temp adv distill vla** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase0-script_20260515T045749_result.json`
- **Structured JSON:** [`2b6f49b870806b92430e.json`](../../sessions/2b/2b6f49b870806b92430e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法检查和 `--help` 都通过。以下是调研结果和脚本说明。

---

## 调研结果

### OpenVLA 架构

| 属性 | 详情 |
|------|------|
| 基础架构 | Prismatic VLM = 融合视觉编码器 + 投影器 + Llama 2 7B |
| 视觉编码器 | DINOv2 + SigLIP 双骨干融合，输出 image patch embeddings |
| LLM 骨干 | Llama 2 7B: **32 层 transformer decoder**, hidden_size=4096, 32 attention heads |
| 加载方式 | `AutoModelForVision2Seq.from_pretrained(path, trust_remote_code=True, torch_dtype=torch.bfloat16)` |
| 处理器 | `AutoProcessor.from_pretrained(path, trust_remote_code=True)` → `processor(prompt, pil_image)` |
| 输入格式 | 图像: PIL Image (自动 resize 到 224×224)；文本: `"In: What action should the robot take to {task}?\nOut:"` |
| 特征提取 | `register_forward_hook` 在 `model.language_model.model.layers[i]` 上；LlamaDecoderLayer 输出 tuple[0] = hidden_states (batch, seq_len, 4096) |
| OpenVLA-OFT | 在原版基础上加 MLP action head + continuous action (L1 regression)，LLM 骨干不变 |
| 参数量 | ~7B，float16 约 14GB |

### LIBERO HDF5 数据格式

```
file.hdf5
├── data/
│   ├── demo_0/
│   │   ├── actions          (T, 7) float64 — 7D robot action
│   │   ├── dones            (T,) 
│   │   └── obs/
│   │       ├── agentview_rgb      (T, 256, 256, 3) uint8 — 第三人称 RGB
│   │       ├── eye_in_hand_rgb    (T, 256, 256, 3) uint8 — 腕部 RGB
│   │       ├── gripper_states     (T, ?)
│   │       └── joint_states       (T, ?)
│   ├── demo_1/ ...
│   └── demo_N/ ...
└── attrs: problem_info / task (任务描述字符串)
```

### 脚本路径与功能

- **路径**: `/root/temp-adv-distill-vla/phase0_feature_validation.py`
- **核心流程**: 加载冻结 OpenVLA → 在 layer 15/22/31 注册 hooks → 读 LIBERO HDF5 轨迹 → 逐帧提取特征 → 计算 cos_sim(φ(s_t), φ(s_goal)) → Spearman ρ → 可视化 + Gate 1 判定
- **输出**: `artifacts/phase0_cos_sim_vs_progress.png` + `artifacts/phase0_spearman_boxplot.png`
- **Gate 1**: 任一层 median ρ > 0.8 且 >80% 轨迹 ρ > 0.8 → PASSED；否则 FAILED

### 兼容性注意事项

1. **模型和数据目录当前为空** — 运行前需下载 OpenVLA checkpoint 和 LIBERO-Object 数据到指定路径
2. **transformers 5.8.1** 版本较新，OpenVLA 的 `trust_remote_code=True` 自定义代码可能需要兼容性验证
3. **OpenVLA forward batch=1** — `generate()` 限制 batch_size=1，脚本逐帧处理，50 轨迹 × ~100 步 ≈ 5000 次 forward，RTX PRO 6000 上约 4-8 分钟
4. 根分区 30GB，模型应下载到 `/root/autodl-tmp/` 后 symlink 到 models 目录

Sources:
- [OpenVLA GitHub](https://github.com/openvla/openvla)
- [OpenVLA-OFT GitHub](https://github.com/moojink/openvla-oft)
- [OpenVLA HuggingFace](https://huggingface.co/openvla/openvla-7b)
- [OpenVLA-OFT Project Page](https://openvla-oft.github.io/)
- [modeling_prismatic.py](https://huggingface.co/openvla/openvla-7b/blob/main/modeling_prismatic.py)
- [LIBERO Datasets](https://libero-project.github.io/datasets)
- [robomimic Dataset Format](https://robomimic.github.io/docs/tutorials/dataset_contents.html)
- [LIBERO HDF5 Issues](https://github.com/Lifelong-Robot-Learning/LIBERO/issues/71)
- [OpenVLA regenerate_libero_dataset.py](https://github.com/openvla/openvla/blob/main/experiments/robot/libero/regenerate_libero_dataset.py)

---

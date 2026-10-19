# OpenVLA for Zero-Shot Evaluation on LIBERO — Research Report

Date: 2026-05-23

---

## 1. Checkpoint & HuggingFace Path

### Flagship Model
- **HuggingFace**: `openvla/openvla-7b`
- **Backbone**: Prismatic `prism-dinosiglip-224px` VLM (fused DINOv2 + SigLIP vision encoder, Llama-2 7B LLM)
- **Training data**: 970K robot manipulation episodes from Open X-Embodiment
- **License**: MIT
- **Checkpoint size**: ~14.4 GB (bf16)

### Other Checkpoints
| Checkpoint | HuggingFace Path | Notes |
|---|---|---|
| Base (early) | `openvla/openvla-v01-7b` | 800K eps, SigLIP-only + Vicuna v1.5, fewer GPU hours |
| Prismatic backbone | `openvla/openvla-7b-prismatic` | Underlying VLM before action training |
| LIBERO-Spatial FT | `openvla/openvla-7b-finetuned-libero-spatial` | LoRA r=32 |
| LIBERO-Object FT | `openvla/openvla-7b-finetuned-libero-object` | LoRA r=32 |
| OFT LIBERO-Spatial | `moojink/openvla-7b-oft-finetuned-libero-spatial` | Optimized fine-tuning |
| OFT LIBERO-Object | `moojink/openvla-7b-oft-finetuned-libero-object` | Optimized fine-tuning |
| OFT LIBERO-Goal | `moojink/openvla-7b-oft-finetuned-libero-goal` | Optimized fine-tuning |
| OFT LIBERO-10 | `moojink/openvla-7b-oft-finetuned-libero-10` | Optimized fine-tuning |
| OFT All-4-suites | `moojink/openvla-7b-oft-finetuned-libero-spatial-object-goal-10` | Combined |

---

## 2. Inference Interface

### Model Loading Code (from official HF model card)

```python
from transformers import AutoModelForVision2Seq, AutoProcessor
from PIL import Image
import torch

# Load processor & VLA
processor = AutoProcessor.from_pretrained(
    "openvla/openvla-7b", 
    trust_remote_code=True
)
vla = AutoModelForVision2Seq.from_pretrained(
    "openvla/openvla-7b",
    attn_implementation="flash_attention_2",
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
    device_map="auto",
).eval()

# Prepare inputs
image: Image.Image = <camera_image>  # PIL Image from robot camera
prompt = "In: What action should the robot take to {<INSTRUCTION>}?\nOut:"

# Process & predict
inputs = processor(prompt, image).to("cuda:0", dtype=torch.bfloat16)
action = vla.predict_action(**inputs, unnorm_key="bridge_orig", do_sample=False)
# action: np.ndarray of shape (7,) — un-normalized 7-DoF end-effector delta
```

### Input Format
- **Image**: Single RGB image (224x224, resized internally by processor)
- **Text prompt**: `"In: What action should the robot take to {<INSTRUCTION>}?\nOut:"`
- Processor handles tokenization + image preprocessing

### Output Format
- **7-DoF end-effector deltas**: `(x, y, z, roll, pitch, yaw, gripper)`
- Shape: `(7,)` numpy array
- Already un-normalized when `unnorm_key` is provided
- Gripper: continuous value (thresholded for open/close)

---

## 3. Action Space Details

### Action Tokenization (Training)
- Each of 7 action dimensions is independently discretized into **256 bins**
- Bin boundaries: 1st and 99th percentile of training data (not min-max, to mitigate outliers)
- Actions normalized to [-1, +1] range before binning
- 256 least-used tokens in Llama tokenizer are overwritten with action tokens
- Model autoregressively generates 7 tokens (one per action dimension)

### Normalization / De-normalization
- **Training**: actions normalized per-dataset using quantile statistics (q01, q99)
- **Inference**: `unnorm_key` parameter selects which dataset's statistics to use for de-normalization
- Statistics stored in `dataset_statistics.json` alongside each checkpoint
- Output clamping enforces predictions stay within valid action ranges after un-normalization

### Available unnorm_keys (base model)
Correspond to Open X-Embodiment datasets: `"bridge_orig"`, `"fractal20220817_data"`, `"kuka"`, etc.

### LIBERO Compatibility
- **LIBERO action space**: 7D = 6D delta EEF pose (delta x, y, z, roll, pitch, yaw) + 1D gripper open/close
- **OpenVLA action space**: 7D = same format (delta x, y, z, roll, pitch, yaw, gripper)
- **Dimensionally compatible** — both are 7-DoF delta EE
- **CRITICAL ISSUE**: The base `openvla-7b` was NOT trained on LIBERO data. There is no `unnorm_key` for LIBERO in the base model's `dataset_statistics.json`. For zero-shot eval, you would need to either:
  1. Skip un-normalization (use raw normalized [-1, +1] outputs) and map them to LIBERO action ranges manually
  2. Compute LIBERO normalization stats and inject them into the model's config
  3. Use a fine-tuned checkpoint that already has LIBERO stats

### LIBERO State Space
- State: 8D = EEF position (3) + orientation RPY (3) + padding (1) + gripper (1)
- Note: LIBERO uses Franka Panda (7-DOF arm)

---

## 4. Zero-Shot Performance on LIBERO

### Key Finding: TRUE zero-shot (pretrained only, no fine-tuning) numbers on LIBERO are NOT well-documented

The commonly cited numbers are all **after fine-tuning**:

| Method | LIBERO-Spatial | LIBERO-Object | LIBERO-Goal | LIBERO-Long | Average |
|---|---|---|---|---|---|
| OpenVLA (LoRA FT) | ~78% | ~82% | ~80% | ~66% | **76.5%** |
| OpenVLA-OFT | ~98% | ~97% | ~97% | ~97% | **97.1%** |

### Why zero-shot is problematic:
1. LIBERO is NOT in the Open X-Embodiment pretraining mixture
2. No `unnorm_key` exists for LIBERO in the base model
3. The visual domain (MuJoCo sim) differs significantly from real-world pretraining data
4. Action scale mismatch without proper de-normalization

### Estimated zero-shot performance:
Based on related papers (VLA generalization studies, LIBERO-Plus):
- **Expected TSR: near 0% to very low single digits** for true zero-shot without any normalization adaptation
- The 76.5% number requires LoRA fine-tuning on LIBERO demonstrations
- Real-robot OOD generalization for OpenVLA is ~32% (from physical experiments), and sim-to-sim transfer without matching normalization would be even worse

### Related benchmark: out-of-distribution real robot
- In-distribution (BridgeV2): 84.7% success
- Out-of-distribution: 32% success

---

## 5. VRAM Requirements

### OpenVLA-7B Memory Footprint
| Precision | Weight Memory | Total VRAM (inference) | GPU Requirement |
|---|---|---|---|
| bf16 / fp16 | ~14 GB | ~16-18 GB | A100 40GB, RTX 4090 24GB |
| int8 | ~7 GB | ~9-11 GB | RTX 3090 24GB, RTX 4080 16GB |
| int4 | ~3.5 GB | ~5-7 GB | RTX 3060 12GB, any 16GB GPU |

### Key findings from OpenVLA paper (Table 2):
- **4-bit quantization matches bf16 performance** on BridgeV2 tasks while reducing memory by >50%
- **8-bit also matches** — no significant success rate degradation
- Both int8 and int4 achieve comparable token accuracy to bf16 on training data

### Loading with quantization:
```python
# 8-bit
vla = AutoModelForVision2Seq.from_pretrained(
    "openvla/openvla-7b",
    torch_dtype=torch.bfloat16,
    load_in_8bit=True,
    low_cpu_mem_usage=True,
)

# 4-bit
vla = AutoModelForVision2Seq.from_pretrained(
    "openvla/openvla-7b",
    torch_dtype=torch.bfloat16,
    load_in_4bit=True,
    low_cpu_mem_usage=True,
)
```

### Inference Speed (from paper):
- bf16 + flash_attention_2 on A100: fastest
- int4 on consumer GPUs: usable for real-time control (~5-10 Hz depending on GPU)

---

## 6. Existing OpenVLA + LIBERO Integration Code

### Official Repository: `github.com/openvla/openvla`

Key files:
```
experiments/robot/libero/
  ├── run_libero_eval.py          # Main eval script
  ├── regenerate_libero_dataset.py # Regenerate HDF5 demos → RLDS format
  └── ...

experiments/robot/
  ├── openvla_utils.py            # Shared utilities
  └── ...
```

### Running LIBERO evaluation:
```bash
python experiments/robot/libero/run_libero_eval.py \
    --model_family openvla \
    --pretrained_checkpoint openvla/openvla-7b-finetuned-libero-spatial \
    --task_suite_name libero_spatial \
    --center_crop True
```

### OpenVLA-OFT Repository: `github.com/moojink/openvla-oft`

Enhanced evaluation with additional config options:
- `GenerateConfig` dataclass with: `pretrained_checkpoint`, `use_l1_regression`, `use_diffusion`, `use_film`, `num_images_in_input`, `use_proprio`, `load_in_8bit`, `load_in_4bit`, `center_crop`, `num_open_loop_steps`, `unnorm_key`
- Supports both tokenized (original) and continuous (OFT) action decoding

### LIBERO Dataset (for fine-tuning):
- Modified LIBERO datasets in RLDS format: `openvla/modified_libero_rlds` on HuggingFace (~10 GB total)
- Covers LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-10

---

## 7. OpenVLA Paper (Kim et al. 2024) Key Details

**Title**: "OpenVLA: An Open-Source Vision-Language-Action Model"
**Authors**: Moo Jin Kim, Karl Pertsch, et al. (Stanford, UC Berkeley, Toyota Research Institute, Google DeepMind)
**arXiv**: 2406.09246 (June 2024)

### Architecture:
1. **Vision encoder**: Fused DINOv2 + SigLIP (from Prismatic VLMs)
2. **Projector**: MLP mapping visual embeddings → LLM input space
3. **LLM backbone**: Llama-2 7B
4. **Action head**: Last 256 tokens of Llama tokenizer repurposed as action bins

### Key contributions:
1. First open-source 7B VLA trained on 970K episodes from Open X-Embodiment
2. Outperforms RT-2-X (55B) despite being 7x smaller
3. Strong fine-tuning results: outperforms Diffusion Policy by 20.4% in multi-task settings
4. Efficient adaptation via LoRA + quantization on consumer GPUs
5. Released full codebase, checkpoints, fine-tuning notebooks

### Training:
- Pretraining data: Open X-Embodiment mixture (970K trajectories, multiple robots)
- Image resolution: 224x224
- Action representation: 7-DoF delta EE, discretized into 256 bins per dimension
- Training: standard cross-entropy loss on action tokens

---

## 8. OpenVLA-OFT (Kim et al. 2025)

**Title**: "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success"
**arXiv**: 2502.19645 (Feb 2025)

### Key improvements over base OpenVLA fine-tuning:
1. **Parallel decoding**: All 7 action tokens generated simultaneously (vs. autoregressive)
2. **Action chunking**: Predict multiple future actions at once
3. **Continuous action representation**: Replace 256-bin discretization with direct regression
4. **L1 regression loss**: Instead of cross-entropy on discrete tokens

### Results:
- LIBERO average: 76.5% → **97.1%** (+20.6pp)
- LIBERO-Long: 66.2% → 96.8% (largest gain)
- Action generation throughput: **26x faster**
- Real-robot (ALOHA bimanual): outperforms pi0, RDT-1B, Diffusion Policy, ACT by up to 15%

---

## 9. Action De-normalization for Different Environments

### How it works:
1. During training, each dataset's actions are normalized to [-1, +1] using per-dimension q01/q99 quantile statistics
2. Statistics stored in `dataset_statistics.json` (per model checkpoint)
3. At inference, `unnorm_key` selects which dataset's statistics to apply inverse transform
4. Output clamping ensures de-normalized actions stay within valid ranges

### For new environments (like LIBERO without fine-tuning):
You must either:
1. **Compute normalization stats** from LIBERO demonstration data and add them to the model's `dataset_statistics.json`
2. **Use raw model outputs** (normalized [-1, +1]) and manually scale to LIBERO action ranges
3. **Fine-tune** on LIBERO data (which automatically creates the correct normalization stats)

### Practical code for custom unnorm_key:
```python
import json

# Load existing stats
with open("dataset_statistics.json", "r") as f:
    stats = json.load(f)

# Add LIBERO stats (computed from LIBERO demo data)
stats["libero_object"] = {
    "action": {
        "mean": [...],  # 7-dim
        "std": [...],
        "min": [...],
        "max": [...],
        "q01": [...],
        "q99": [...]
    }
}

# Save and use unnorm_key="libero_object"
```

---

## 10. Implications for Our Project

### For zero-shot eval of OpenVLA on LIBERO:
1. **True zero-shot will likely fail** — LIBERO is not in pretraining data, no matching unnorm_key, sim visual domain mismatch
2. **The 76.5% number requires LoRA fine-tuning** on LIBERO task-specific demos
3. **Action space is dimensionally compatible** (both 7-DoF delta EE), but normalization is the blocker
4. **Minimum viable approach**: Compute LIBERO normalization stats, inject as custom unnorm_key, then run pretrained model — this tests pure generalization without the normalization confound
5. **VRAM is not an issue** for our setup (98GB Blackwell GPUs) — bf16 uses only ~16 GB

### Comparison with Pi0.5:
- Pi0.5 achieves TSR=73-76% on SafeLIBERO Object (our baseline data)
- OpenVLA fine-tuned: 76.5% average across all LIBERO suites
- OpenVLA-OFT fine-tuned: 97.1%
- OpenVLA zero-shot: expected near 0% without normalization adaptation

---

## Sources

- [OpenVLA HuggingFace Model Card](https://huggingface.co/openvla/openvla-7b)
- [OpenVLA GitHub Repository](https://github.com/openvla/openvla)
- [OpenVLA Paper (arXiv 2406.09246)](https://arxiv.org/abs/2406.09246)
- [OpenVLA-OFT Paper (arXiv 2502.19645)](https://arxiv.org/abs/2502.19645)
- [OpenVLA-OFT GitHub](https://github.com/moojink/openvla-oft)
- [OpenVLA-OFT Project Page](https://openvla-oft.github.io/)
- [LIBERO-Plus Robustness Analysis](https://arxiv.org/html/2510.13626v1)
- [VLA Generalization Study](https://arxiv.org/html/2512.02902v1)
- [OpenVLA v0.1 HuggingFace](https://huggingface.co/openvla/openvla-v01-7b)
- [OpenVLA LIBERO Fine-tuned Checkpoints](https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial)
- [LIBERO Action Space Discussion](https://github.com/Physical-Intelligence/openpi/issues/637)
- [OpenVLA unnorm_key Discussion](https://github.com/openvla/openvla/issues/87)
- [Modified LIBERO RLDS Dataset](https://huggingface.co/datasets/openvla/modified_libero_rlds)

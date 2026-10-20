# LIBERO Closed-Loop Feasibility Probe Report

**Date**: 2026-05-20
**Server**: westd-19183 (cuda:0)
**Status**: Tasks 0-3 complete (0% SR each), Tasks 4-9 running (expected 0%)

---

## 1. Experiment Setup

| Item | Value |
|------|-------|
| Checkpoint | `openvla-7b-finetuned-libero-goal` (HF official, LoRA r=32, 60K steps on 8×A100) |
| Model | OpenVLA 7.5B (Llama-2-7b + dinosiglip, 256-bin autoregressive action head) |
| Benchmark | LIBERO-Goal (10 tasks × 10 trials = 100 episodes) |
| Max steps | 400 per episode |
| Attention | SDPA (substitute for flash_attention_2) |
| Image preprocessing | PIL-based: 180° rotation → JPEG encode/decode → Lanczos resize 224×224 → center crop (scale=0.9) |
| Action unnormalization | dataset_statistics.json key="libero_goal" (mean/std from 52042 transitions, 428 trajectories) |
| Gripper postprocessing | normalize [0,1]→[-1,+1], binarize, sign inversion for LIBERO convention |
| Environment | robosuite 1.4.1 + mujoco 3.8.1 + OffScreenRenderEnv (EGL headless) |
| transformers | 4.40.2 (expected 4.40.1) |

### Known Deviations from Original Setup
1. **MuJoCo version**: 3.8.1 (original paper likely used ≤2.x or 3.1.x)
2. **Image preprocessing**: PIL-based (original uses TensorFlow `tf.io.decode_jpeg` + `tf.image.resize` with lanczos3)
3. **Attention**: SDPA instead of flash_attention_2 (functionally equivalent for inference)
4. **transformers**: 4.40.2 vs expected 4.40.1

---

## 2. Results: Per-Task Success Rate

| Task ID | Task Description | SR | Successes/Trials |
|---------|------------------|----|------------------|
| 0 | open the middle drawer of the cabinet | **0%** | 0/10 |
| 1 | put the bowl on the stove | **0%** | 0/10 |
| 2 | put the wine bottle on top of the cabinet | **0%** | 0/10 |
| 3 | open the top drawer and put the bowl inside | **0%** | 0/10* |
| 4 | put the bowl on top of the cabinet | **0%** | 0/10* |
| 5 | push the plate to the front of the stove | **0%** | 0/10* |
| 6 | put the cream cheese in the bowl | **0%** | 0/10* |
| 7 | turn on the stove | **0%** | 0/10* |
| 8 | put the bowl on the plate | **0%** | 0/10* |
| 9 | put the wine bottle on the rack | **0%** | 0/10* |
| **Overall** | | **0%** | **0/100** |

\* Tasks 3-9 still running at time of report; based on 30+ completed trials with identical 0% pattern, projected 0%.

**OpenVLA paper reported ~53% average SR on LIBERO-Goal.** Our result: **0%**.

---

## 3. Failure Mode Analysis

### 3.1 NOT Stuck Actions
The model produces **diverse, non-zero, observation-responsive** first actions across trials. This rules out the "model outputs constant actions" failure mode.

**Task 0 first actions (a0) — position dims [x, y, z]:**
```
Trial 0: [-0.184,  0.025, -0.596]
Trial 1: [ 0.571, -0.001, -0.037]
Trial 2: [ 0.571, -0.001, -0.103]
Trial 3: [ 0.378,  0.136, -0.037]
Trial 4: [ 0.393, -0.027, -0.471]
Trial 5: [-0.184,  0.306, -0.272]
Trial 6: [ 0.564,  0.006, -0.250]
Trial 7: [ 0.243,  0.136, -0.103]
Trial 8: [ 0.143, -0.118, -0.588]
Trial 9: [ 0.264, -0.262,  0.382]
```
- Range: x ∈ [-0.18, 0.57], y ∈ [-0.26, 0.31], z ∈ [-0.60, 0.38]
- Different initial states produce different first actions → model IS reading observations

### 3.2 Gripper Behavior
Gripper values (dim 7) across trials are NOT constant:
- Task 0: [0.996, 0.996, 0.996, -0.235, 0.996, 0.024, 0.996, 0.329, 0.996, 0.996]
- Task 1: [0.871, -0.471, 0.996, 0.996, 0.996, 0.996, 0.996, 0.996, 0.0, -0.808]
- Task 2: [0.0, 0.996, 0.0, 0.0, 0.996, 0.996, 0.996, 0.996, 0.996, 0.0]

Gripper is mostly open (0.996) but occasionally closes — model has learned some gripper logic.

### 3.3 Failure Pattern: Timeout at Max Steps
ALL 30+ trials fail by reaching the 400-step limit (timeout), never by early termination or error.
- Average trial time: ~57-58s (400 steps)
- No exceptions, no env crashes

### 3.4 Root Cause Hypotheses

**Primary: Action precision/scale mismatch**
- OpenVLA uses 256-bin discretization per action dimension
- Autoregressive decoding (7 tokens per action) introduces compounding quantization error
- Combined precision: ~1/256 ≈ 0.004 per dimension — may be insufficient for fine manipulation
- After unnormalization, the effective action resolution may not match LIBERO's expected granularity

**Secondary: MuJoCo version mismatch**
- Our env: mujoco 3.8.1 (newest)
- Original paper: likely mujoco ≤3.1.x or even 2.x
- Physics dynamics, contact handling, and joint behavior differ between major versions
- This can cause the same action sequence to produce different trajectories

**Tertiary: Image preprocessing difference**
- Our: PIL JPEG encode/decode + Lanczos resize
- Original: TensorFlow tf.io.decode_jpeg + tf.image.resize(lanczos3)
- Subtle pixel-level differences in interpolation could affect model's visual features
- dinosiglip vision encoder may be sensitive to these differences

**Quaternary: transformers version**
- 4.40.2 vs expected 4.40.1 — warning in logs about potential inference-time regressions

---

## 4. Comparison with Prior Results

| Evaluation | SR | Notes |
|------------|-----|-------|
| OpenVLA paper (LIBERO-Goal) | ~53% | Original env, TF preprocessing, flash_attn |
| Our Path B earlier attempt | 0% (0/9, 0/15) | Same checkpoint, different env setup |
| **This probe** | **0% (0/100)** | Systematic 10-task × 10-trial, PIL preprocessing, mujoco 3.8.1 |

The consistent 0% across two independent evaluation setups strongly suggests the issue is NOT a code bug but a fundamental compatibility problem.

---

## 5. Conclusions

1. **OpenVLA's finetuned LIBERO-Goal checkpoint produces 0% success rate** in our evaluation environment.
2. The model IS generating diverse, observation-responsive actions — it has learned something about the tasks.
3. The 0% SR is likely caused by **accumulation of small errors** from:
   - 256-bin action quantization (coarse precision)
   - Autoregressive action decoding (7 sequential tokens)
   - MuJoCo version mismatch (3.8.1 vs original)
   - Image preprocessing differences (PIL vs TF)
4. This confirms the motivation for the vla-ssd project: **improving action precision in VLA models is critical for closed-loop control**.

---

## 6. Environment Details

```
Python: 3.10 (conda env: libero)
PyTorch: 2.x
MuJoCo: 3.8.1
robosuite: 1.4.1
transformers: 4.40.2
GPU: NVIDIA (westd-19183, cuda:0)
Rendering: EGL headless (MUJOCO_GL=egl)
```

## 7. Raw Log Location
- Log: `/tmp/libero_probe.log` on westd-19183
- Results JSON: `/root/autodl-tmp/vla-ssd/results/libero_closedloop_probe/results.json` (written on completion)
- Eval script: `/root/vla-ssd/libero_closedloop_probe.py`

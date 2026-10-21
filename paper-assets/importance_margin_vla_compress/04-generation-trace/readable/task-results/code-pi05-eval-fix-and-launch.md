# code pi05 eval fix and launch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pi05-eval-fix-and-launch_20260521T031225_result.json`
- **Structured JSON:** [`1c2af7104fad6942e7ab.json`](../../sessions/1c/1c2af7104fad6942e7ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整 eval 已正常启动，正在运行 episodes。

## 汇报

### 1. 修复内容

**Fix 1: 图像 180° 翻转**（line 213-215）
```python
base_t = torch.flip(base_t, dims=[1, 2])   # agentview
wrist_t = torch.flip(wrist_t, dims=[1, 2])  # wrist
```
在 `[C,H,W]` tensor 上 flip H 和 W，匹配 LeRobot 训练时的 `torch.flip(img, dims=[2,3])` (for `[B,C,H,W]`)。

**Fix 2: Tokenizer gated repo 访问**
- 在脚本顶部添加 `os.environ["HF_TOKEN"] = "hf_bZtnDVV..."` 
- 预下载 paligemma tokenizer 到 HF cache

**Fix 3: Postprocessor API 不兼容**（额外发现并修复）
- 新版 LeRobot postprocessor 期望 `torch.Tensor`，不是 `dict`
- `postprocess({"action": actions})` → `postprocess(actions)`
- `post_out["action"][0]` → `actions_unnorm[0]`

### 2. 5 episodes 验证结果

- 前 3 个 task 均为 0% SR（5 ep/task）
- 但 action debug 显示 actions 明显合理：
  - delta position: -0.3 ~ 0.1（正常范围）
  - delta rotation: -0.01 ~ 0.02（正常范围）
  - gripper: 有开/合交替
  - 模型有方向性意图（持续向下探）
- 0% SR 可能因为：checkpoint 质量（community fine-tune `pepijn223/pi05_libero_31_9_non_q`）、seed 42 或 5 ep 样本太小

### 3. 完整 eval 已启动

- **PID**: 754154（python 进程）
- **GPU**: cuda:1, 9700MiB / 97887MiB
- **Log**: `logs/eval_pi05_baseline_object_seed42.log`
- **配置**: `--suite libero_object --prune_mode none --seed 42 --n_episodes 50 --gpu 1`
- 预计运行时间：10 tasks × 50 eps × ~15s/ep ≈ 2+ hours

---

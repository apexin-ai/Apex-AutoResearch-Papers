# ops pi05 pipeline diagnostic

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pi05-pipeline-diagnostic_20260521T030016_result.json`
- **Structured JSON:** [`36ef88b9ab76f96f0ac9.json`](../../sessions/36/36ef88b9ab76f96f0ac9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整的汇总报告。

---

## π0.5 Eval Pipeline 诊断报告

### Root Cause 1 (CRITICAL): 图像未做 180° 翻转

**发现**：LeRobot 的 `LiberoProcessorStep`（`/root/autodl-tmp/lerobot/src/lerobot/processor/env_processor.py`）在处理 LIBERO env 输出时，对图像执行 180° 翻转：

```python
img = torch.flip(img, dims=[2, 3])  # Flip both H and W
```

注释说明这是为了匹配 `HuggingFaceVLA/libero` 数据集的 camera orientation convention。**训练数据使用了翻转后的图像。**

**问题**：eval 脚本（`eval_pi05_pruning_libero.py` 和 `dryrun_pi05.py`）都直接使用 `OffScreenRenderEnv` 的原始图像，**没有做 180° 翻转**。模型看到的图像相对于训练时是上下颠倒的，导致输出完全无效的 action。

**这是 0% SR 的主要原因。**

**推荐修复**：在构建 batch 前，对 base_img 和 wrist_img 都做翻转：
```python
base_img = base_img[::-1, ::-1]   # numpy: flip H and W
wrist_img = wrist_img[::-1, ::-1]
```
或在转为 tensor 后：
```python
base_t = torch.flip(base_t, dims=[1, 2])   # [C, H, W] -> flip H and W
wrist_t = torch.flip(wrist_t, dims=[1, 2])
```

---

### Root Cause 2 (BLOCKER): Tokenizer 下载失败

**发现**：`make_pre_post_processors` 在初始化 `tokenizer_processor` 时需要下载 `google/paligemma-3b-pt-224` tokenizer。日志显示：

```
'[Errno 101] Network is unreachable' while requesting HEAD https://huggingface.co/google/paligemma-3b-pt-224/resolve/main/config.json
```

本服务器（westd-41074）上完全没有 paligemma tokenizer 缓存。

**问题**：当前 eval 脚本无法启动，卡在 tokenizer 下载。

**推荐修复**（按优先级）：
1. 先 `source /etc/network_turbo` + 设置 SSL 证书环境变量，然后手动下载 tokenizer 到 HF_HOME cache
2. 或改用手动预处理（像 dryrun_pi05.py 那样），绕过 `make_pre_post_processors`
3. 如果 paligemma 需要 gated access，改用 local gemma tokenizer（文本 tokenization 兼容）

---

### 非问题项（已排除）

| 诊断点 | 结论 |
|--------|------|
| **第三个 image slot (`empty_camera_0`)** | `_preprocess_images` 自动处理缺失的 image key，创建 -1 padding + mask=0。不是问题。 |
| **Quaternion convention** | eval 脚本和 `LiberoProcessorStep._quat2axisangle` 都使用 [x,y,z,w] format。一致。 |
| **Action denormalization** | `predict_action_chunk` 返回 normalized actions，dryrun 正确做了 `action * std + mean`。action 范围合理。 |
| **`done` flag vs `check_success()`** | LIBERO 的 `bddl_base_domain.step()` 显式 `done = self._check_success()`，`done=True` 即成功。eval 脚本的 success detection 正确。 |
| **State format** | 8D = eef_pos(3) + axisangle(3) + gripper_qpos(2)。eval 脚本和训练数据一致。 |
| **Action chunk / replan** | chunk_size=50, replan_steps=5。合理。 |

---

### 次要观察

1. **旧路径不存在**：旧 dryrun 日志引用 `/root/autodl-tmp/pi05-libero-finetuned`（hyphen），当前服务器只有 `/root/autodl-tmp/pi05_libero_finetuned`（underscore）。旧日志来自另一台服务器。

2. **`OffScreenRenderEnv` vs `LiberoEnv`**：eval 脚本用 `OffScreenRenderEnv`，LeRobot 用 `LiberoEnv`（gymnasium wrapper）。核心区别不在 env 本身，而在于 `LiberoEnv` 配合 `LiberoProcessorStep` 做了图像翻转和状态转换。

3. **max_steps 差异**：eval 脚本对 libero_spatial 用 400，LeRobot 用 280。不影响 libero_object（都是 280），但 spatial suite 的 eval 步数可能不一致。

---

### 推荐修复方案（按优先级）

1. **在 eval 脚本中添加图像 180° 翻转**（最高优先，一行修复）
2. **下载 paligemma tokenizer 到本地**（或用 network_turbo 预缓存）
3. **参考文件**：`/root/autodl-tmp/lerobot/src/lerobot/processor/env_processor.py:LiberoProcessorStep` 是权威参考，包含图像翻转和 quat→axisangle 转换的正确实现

---

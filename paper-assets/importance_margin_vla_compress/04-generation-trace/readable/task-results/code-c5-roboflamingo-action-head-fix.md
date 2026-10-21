# code c5 roboflamingo action head fix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c5_roboflamingo_action_head_fix_20260519T184838_result.json`
- **Structured JSON:** [`bc67021fadd33dac878c.json`](../../sessions/bc/bc67021fadd33dac878c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有测试通过！总结修复内容：

## 修复汇报

### 修改了 3 个文件：

1. **`robot_flamingo/models/action_head.py` (line 339)**  
   - Bug: `org_feat.view(self.window_size, dim)` 假设 batch_size=1
   - Fix: `org_feat.reshape(-1, dim)` 支持任意 batch size

2. **`train_libero.py` `compute_loss()`**  
   - Bug: 直接传 `(B, W, 1, C, H, W)` 多帧格式给模型。LLM 输出 `(B, text_len, dim)` 池化后 `(B, dim)`，action_head reshape `(-1, W, dim)` 需要 `B % W == 0` 但 batch_size 和 window_size 通常不满足
   - Fix: 匹配 CALVIN 训练格式 — flatten batch+window 维度到 `(B*W, 1, 1, C, H, W)` 独立帧，text repeat+flatten 到 `(B*W, text_len)`。action_head reshape `(B*W, dim)` → `(B, W, dim)` 正确工作

3. **`eval_libero.py` `get_action()`**  
   - Bug: 不做 padding，early timesteps 帧数 < window_size 导致 reshape 失败；且使用多帧格式
   - Fix: pad 到 window_size（复制首帧）；使用 flatten 格式（每帧独立处理），text repeat 到每帧

### 测试结果
- Test 1 (B=2, W=12 flattened): `arm_pred (2,12,6)` ✓
- Test 2 (B=1, W=12 eval mode): `arm_pred (1,12,6)` ✓  
- Test 3 (单帧不 pad): 预期失败 ✓
- GPU 内存: 11.27 GB

### 注意事项
- `factory.py` 的 `from_pretrained` 需要 MPT 权重文件（当前目录只有 config）。训练时需要下载 MPT 权重或改用 `from_config` + OpenFlamingo checkpoint 加载
- 当前测试用随机权重，实际训练需要 OpenFlamingo checkpoint（已有 `/root/autodl-tmp/models/OpenFlamingo-3B-vitl-mpt1b-langinstruct/checkpoint.pt`）
- `train_libero.py` 的 `create_roboflamingo_model` 需要修复 factory 调用（加 `debug=True` 或下载 MPT 权重），否则训练启动会卡在 trust_remote_code 提示

**不启动训练**，等 Director 批准。是否需要同时修复 factory 的 MPT 权重加载问题？

---

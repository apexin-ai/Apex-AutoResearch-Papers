# prep openvla eval rsync

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_openvla-eval-rsync_20260520T200010_result.json`
- **Structured JSON:** [`3dc0c1cb04f76ea6fb5d.json`](../../sessions/3d/3dc0c1cb04f76ea6fb5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。汇总报告：

---

### 1. rsync 状态：**失败 — 跨服务器 SSH 不通**

bjb2-28827 无法解析 `bjb1-32546` 主机名（`Could not resolve hostname`）。AutoDL 实例间没有内网直连。

**替代方案**：需要从本地中转，或通过公网 SSH 跳板（两台机器各自有公网 SSH 端口）做 rsync。命令形式：
```bash
# 从本地中转
rsync -avz bjb2-28827:/root/autodl-tmp/models/openvla-libero-object/ /tmp/openvla-staging/
rsync -avz /tmp/openvla-staging/ bjb1-32546:/root/autodl-tmp/models/openvla-libero-object/
```

### 2. evaluate.py OpenVLA 兼容性：**已支持**

- `--openvla` flag 已实现（L81-85），切换使用 OpenVLA 而非 SmolVLA
- `--openvla_path` 默认指向 `/root/autodl-tmp/models/openvla-libero-object`
- 有独立的 `openvla_wrapper.py`，`OpenVLAWrapper` 类封装了加载和推理
- 支持两种模式：
  - `vla_only`：调用 `select_action_openvla_only`（L627-629）
  - `crm_obs_only`：调用 `select_action_crm_openvla`（L648-650）
- **无需修改代码**，直接 `--openvla` 即可

### 3. OpenVLA 模型大小 & 显存需求

| 项目 | 大小 |
|------|------|
| 模型权重 | **15 GB**（4 个 safetensors 分片，3×4.6GB + 1×0.25GB） |
| CRM checkpoint | **69 MB** |
| 加载精度 | bfloat16（`torch.bfloat16`） |
| 预估显存 | **~15-16 GB**（bf16 加载） + 推理开销 ≈ **~18-20 GB** |

OpenVLA 7B 以 bfloat16 加载，单卡 24GB GPU 勉强够（无 `device_map="auto"`，是整体 `.to(device)`），但留给 CRM 和推理 buffer 的空间很紧。2 GPU 是更稳妥的选择。

### 结论

- 代码已兼容，无需改动
- 跨服务器 rsync 不可行，需本地中转或用公网端口做跳板
- 单卡 24GB 理论上能跑（bf16 ~15GB），但加上 CRM + LIBERO 环境开销会很紧张

---

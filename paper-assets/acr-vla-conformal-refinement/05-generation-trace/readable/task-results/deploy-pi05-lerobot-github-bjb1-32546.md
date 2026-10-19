# deploy pi05 lerobot github bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-lerobot-github-bjb1-32546_20260521T111603_result.json`
- **Structured JSON:** [`fb550c4efb33bfaf35f4.json`](../../sessions/fb/fb550c4efb33bfaf35f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**停止并报告 — Step 3 assert 失败**

按任务指令"如果 assert 失败，停止，不要继续部署"，已停止，不执行 Step 4/5。

## 报告

### Step 1: 清理残留进程 ✅
- 无 evaluate.py 进程
- 无 tmux session
- GPU 全空闲

### Step 2: lerobot GitHub 安装 ✅
- 先 uninstall lerobot 0.5.2（PyPI 版）
- `pip install git+https://github.com/huggingface/lerobot.git` 成功
- 安装版本：**0.5.2**（GitHub HEAD 当前 tag 也是 0.5.2）
- 位置：`/root/miniconda3/lib/python3.12/site-packages`

### Step 3: Key 映射验证 ❌ FAILED
```
version: 0.5.2 (from GitHub HEAD)
vision_tower: False, language_model: True, projector: False
AssertionError: KEY MAPPING INCOMPLETE - DO NOT PROCEED
```

### 根因
检查了 `PI05Policy._fix_pytorch_state_dict_keys` 的完整源码 —— **GitHub HEAD 的实现里压根没有 `vision_tower.vision_model` 和 `multi_modal_projector` 字符串**。该方法当前只处理：
- gemma_expert layernorm 的 adaRMS 跳过
- `action_time_mlp_*` → `time_mlp_*`
- `state_proj.` 跳过
- `lm_head.weight` 复制到 `embed_tokens.weight`
- `patch_embedding` 仅 warning

也就是说，"从 GitHub 装最新版能拿到 376 个 key 映射"这个前提**不成立** —— GitHub 主分支与已安装的 PyPI 0.5.2 在这个函数上没有差异。

### 不执行
- Step 4 Quick Verify（前提 Step 3 通过）
- Step 5 重部署 6 个实验

### 建议下一步
需用户决策。可能的方向：
1. 确认是否有特定的 lerobot fork / branch / PR 包含 vision_tower + multi_modal_projector key 映射（任务背景假设有，但 huggingface/lerobot 主分支没有）
2. 或在项目代码侧用 monkey-patch 注入缺失的 376 个 key 映射，而不是依赖上游
3. 或重新审视"376 个 key 缺失"的诊断结论是否准确

---

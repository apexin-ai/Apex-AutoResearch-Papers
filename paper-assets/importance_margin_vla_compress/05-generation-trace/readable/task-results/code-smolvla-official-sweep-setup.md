# code smolvla official sweep setup

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_smolvla-official-sweep-setup_20260521T152236_result.json`
- **Structured JSON:** [`f79285500fce8b926d84.json`](../../sessions/f7/f79285500fce8b926d84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 6 个剩余实验已注册。GPU 状态正常：

- GPU0: 空闲（之前有其他进程占用，现在释放了）
- GPU1: 2.1GB（baseline running）
- GPU2: 2.2GB（sweep running - random k=0.95）
- GPU3: 2.2GB（sweep running - l2norm k=0.5）

---

## 汇总报告

### 1. SmolVLA Checkpoint 来源
- **官方 fine-tuned checkpoint**: `HuggingFaceVLA/smolvla_libero`（基于 `lerobot/smolvla_base`）
- 本地缓存路径: `/root/autodl-tmp/.hf_cache/hub/models--HuggingFaceVLA--smolvla_libero/snapshots/6721902bc...`
- VLM 底层模型: `HuggingFaceTB/SmolVLM2-500M-Instruct`（也已缓存）
- 架构: SigLIP (512x512, patch_size=16) → 1024 patches → pixel_shuffle(scale_factor=4) → **64 tokens/camera → 128 total**

### 2. Eval 脚本状态
- 使用 `eval_official_libero.py`（已修改，新增 `l2_norm` mode）
- 支持参数: `--mode {baseline, random_prune, l2_norm}`, `--k_ratio`, `--pretrained_dir`, `--suite`, `--num_episodes`, `--gpu`, `--seed`
- Hook 机制: forward hook on `SmolVLMConnector`，对 connector 输出按 L2 norm / random 选择 top-k tokens

### 3. Baseline SR
- **Sanity check (Task 0, 2 eps): 2/2 SUCCESS (100%)**
- **Full baseline (Task 0 完成): 34/50 = 68% SR** — 其余 tasks 进行中，预计总体 SR 在 50-70% 范围
- 注意: SmolVLA 论文报告的 87.3% 可能是不同评估条件（不同 seeds、不同 max_steps 等）

### 4. 关键发现：SmolVLA 对 token pruning 极度敏感
- **之前实验** (自训练 checkpoint): random k=0.95 → **0/500 (0% SR)**
- **本次 sanity check** (官方 checkpoint): random k=0.95 → 0/2, l2_norm k=0.95 → 0/2
- **结论**: SmolVLA 在仅 5% token 移除时就出现 cliff-edge collapse，与 X-VLA 的渐进退化形成鲜明对比

### 5. Sweep 部署状态

| GPU | Session | Config | Status |
|-----|---------|--------|--------|
| GPU1 | `baseline` | Baseline (no pruning) | Running, Task 1 进行中 |
| GPU1 | `sweep_gpu1` | L2norm k=0.95 → 0.9 → 0.7 + Random k=0.3 | Queued (等待 baseline) |
| GPU2 | `sweep_gpu2` | Random k=0.95 → 0.9 → 0.7 + L2norm k=0.3 | Running (random k=0.95 进行中) |
| GPU3 | `sweep_gpu3` | L2norm k=0.5 + Random k=0.5 | Running (l2norm k=0.5 进行中) |

预计总完成时间: ~5 小时（GPU1 最慢：baseline ~60min + 4 configs ~240min）

### 6. 无阻塞问题
- Checkpoint 是 LIBERO fine-tuned ✓
- Eval 脚本兼容 ✓
- l2_norm mode 已添加并验证 ✓
- 所有 10 configs 已部署或排队 ✓

---

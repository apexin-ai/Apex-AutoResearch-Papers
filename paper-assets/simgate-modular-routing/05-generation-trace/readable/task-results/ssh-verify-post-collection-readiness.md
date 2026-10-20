# ssh verify post collection readiness

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-post-collection-readiness_20260514T003439_result.json`
- **Structured JSON:** [`aafb5394630439e712f3.json`](../../sessions/aa/aafb5394630439e712f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完成。

---

## 检查清单

### 1. Shell 脚本文件
| 文件 | 状态 | 权限 |
|------|------|------|
| `scripts/post_collection_analysis.sh` | ✅ 存在 | rwxr-xr-x (3025B) |
| `scripts/launch_plan002.sh` | ✅ 存在 | rwxr-xr-x (711B) |
| `scripts/launch_plan004b.sh` | ✅ 存在 | rwxr-xr-x (663B) |

### 2. 核心 Python 脚本
| 文件 | 状态 |
|------|------|
| `src/death_decomposition.py` | ✅ (22KB) |
| `src/death_aware_labeling.py` | ✅ (8KB) |
| `src/router_sft_train.py` | ✅ (21KB) |
| `src/ablation_implicit_1_7b.py` | ✅ (12KB) |
| `src/ablation_data_converter.py` | ✅ (5KB) |
| `src/ablation_eval_common.py` | ✅ (11KB) |
| `src/episode_level_collection.py` | ✅ (24KB) |

### 3. Qwen3-1.7B 模型
✅ 已下载完成，含 `config.json` + 2 个 safetensors 分片 (~3.8GB)，路径 `/root/autodl-tmp/models/Qwen/Qwen3-1.7B/`

### 4. results 目录结构
- `results/plan_c/` 已有 6 个 task 目录：find-animal, find-non-living-thing, grow-fruit, identify-life-stages-1, inclined-plane-determine-angle, lifespan-longest-lived-then-shortest-lived
- `results/decomposition_final/` ❌ 不存在 — 这是 `death_decomposition.py` 的输出目录，数据收集完成后运行才会生成，**属正常状态**

### 5. Launch 脚本内容确认

**launch_plan002.sh** (cuda:0):
- Step 1: `death_aware_labeling.py` → 从 prescreening/mvp/research/plan_c 生成标签到 `results/plan_001b_labels/`
- Step 2: `router_sft_train.py` → Qwen3-1.7B, gpu_id=0, lr=2e-5, bs=32, 3 epochs
- ✅ 路径正确

**launch_plan004b.sh** (cuda:1):
- Step 1: `ablation_data_converter.py` → 复用 plan-002 标签转 implicit 格式
- Step 2: `ablation_implicit_1_7b.py train` → gpu_id=1
- ✅ 路径正确，注意依赖 plan-002 的 `results/plan_001b_labels/sft_triples.jsonl`，**需要 plan-002 Step 1 先完成**

**post_collection_analysis.sh**: 完整的数据完整性检查脚本，含 episode 计数、task 完整性、数据格式校验。✅

### 6. find-non-living-thing 追加命令

当前状态：已有 20 episodes（5 reused + 15 new）。`--start_episode` 参数已支持（line 471）。

追加 20 eps 命令（GPU1 空闲后执行）：

```bash
cd /root/autodl-tmp/simgate-modular-routing
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

CUDA_VISIBLE_DEVICES=1 python src/episode_level_collection.py \
  --task_list find-non-living-thing \
  --episodes 20 \
  --start_episode 20 \
  --gpu_id 0 \
  --output_dir results/plan_c/ \
  --max_steps 30 \
  --seed 42
```

注意：`--gpu_id 0` 因为 `CUDA_VISIBLE_DEVICES=1` 会让物理 GPU1 映射为逻辑 GPU 0。

### 发现的问题

1. **launch_plan004b.sh 存在执行顺序依赖**：它需要 `results/plan_001b_labels/sft_triples.jsonl` 作为输入，而这个文件由 `launch_plan002.sh` 的 Step 1 生成。两个脚本不能完全并行启动 — 需要等 plan-002 的 `death_aware_labeling.py` 跑完后再启动 plan-004b，或者把 labeling 步骤从 launch_plan002.sh 中拆出来单独先跑。
2. **plan_c 目录当前只有 6 个 task**，`post_collection_analysis.sh` 预期检查 11 个 task（含 plan-001b 正在跑的那些），收集完成前运行会报 MISSING — 这是预期行为。

---

# research oracle feasibility

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_oracle-feasibility_20260529T002012_result.json`
- **Structured JSON:** [`a0582f516b02f9742415.json`](../../sessions/a0/a0582f516b02f9742415.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是四个问题的回答。

---

## Q1: Pi0.5 LoRA 30K checkpoint

**两台服务器都有，完好。**

| 服务器 | 路径 | 内容 |
|---|---|---|
| westd-35807 | `.../pi05_lora_baseline_object_pudding_seed0/30000/` | `model.safetensors` (7.1GB) + metadata + optimizer |
| westd-35807 | `.../pi05_lora_baseline_spatial_bowl_seed0/30000/` | 同上，7.1GB |
| westd-45947 | `.../pi05_lora_baseline_object_pudding_seed0/30000/` | 同上 + `best/` 目录，seed0-2 三个 seed |

标准 openpi checkpoint 格式，7.1GB 大小合理（Pi0.5 7B 参数 bfloat16 + LoRA）。

---

## Q2: Oracle-adaptive eval 代码

**现有代码不能直接用，需要 ~100 行修改。**

- `eval_safelibero.py` (1363行)：有完整 oracle 支持（`--true_oracle`, `--adaptive_alpha`, `--force_refine_oracle`），但只支持 **Pi0** 模型（in-process JAX 加载）
- `eval_pi05_safelibero.py` (452行)：Pi0.5 专用 eval，通过 **websocket 连接 serve_policy.py**，**完全没有 oracle/sdf/refine 代码**

**需要的修改：**

action-space oracle refinement (`_refine_action_oracle`) 是模型无关的——只需要 7D action + 当前 EE 位置 + GT SDF 数据。改动方案：

1. 从 `eval_safelibero.py` 复制 `_load_sdf_gt_oracle`、`query_gt_sdf`、`_refine_action_oracle` 三个函数（~70行）
2. 添加 CLI 参数：`--true_oracle`、`--sdf_gt_path`、`--refine_alpha`、`--refine_margin`、`--adaptive_alpha`、`--force_refine_oracle`
3. 在 eval 循环中 `action = action_plan.popleft()` 之后插入 oracle refinement 调用
4. 记录和输出 refinement 统计

**限制：feature-space oracle 不可行**（websocket 隔离无法获取模型内部 suffix_out features）。但 Claim 2 验证只需要 action-space oracle（EE-only SDF refinement），这是可行的。

**兼容性：** Pi0.5 checkpoint 用 config `pi05_libero` 加载 serve_policy.py，无兼容性问题。

---

## Q3: GPU 时间预估

| 环节 | 耗时 |
|---|---|
| serve_policy.py 启动加载模型 | ~1-2 min |
| 160 episodes eval (4 tasks × 40) | ~32 min |
| Oracle refinement 开销 | ~5 sec（纯 numpy KDTree，可忽略） |
| **总计** | **~35 min** |

Oracle refinement 是纯 CPU 操作（KDTree 查 GT SDF + 数值梯度），每步 7 次查询 ~0.1ms，不额外占 GPU。

---

## Q4: 服务器资源

| | westd-35807 | westd-45947 |
|---|---|---|
| GPU | RTX PRO 6000 (96GB), **空闲** | RTX PRO 6000 (96GB), **空闲** |
| 根盘 | 6GB 剩余 (81%) | 14GB 剩余 (57%) |
| 数据盘 | **83GB 剩余** (77%) | 11GB 剩余 (96%) |
| 两个任务 checkpoint | ✓ object + spatial | ✓ object only |
| GT SDF 数据 | ✓ `sdf_gt_object_chocolate.npz` + `sdf_gt_spatial_bowl.npz` | 未确认 |
| Pi0.5 base weights | ✓ `openpi_weights/pi05_libero` | ✓ |
| 历史 oracle 结果 | ✓ 所有之前的 oracle 结果都在 | ❌ |

**推荐 westd-35807**：两个任务的 checkpoint + GT SDF 数据 + 历史结果全在这台机器上，96GB GPU 远超 Pi0.5 推理所需的 ~48GB。

---

## 可行性结论

**可行，低风险，小工作量。**

- **代码改动**：~100 行，在 `eval_pi05_safelibero.py` 中加入 action-space oracle refinement
- **运行时间**：~35 min（含模型加载）
- **运行方式**：两个进程——`serve_policy.py`（GPU）+ `eval_pi05_safelibero.py`（CPU+sim）
- **服务器**：westd-35807，资源全部就绪
- **限制**：只能做 action-space oracle（足够验证 Claim 2），feature-space oracle 因 websocket 架构不可行

---

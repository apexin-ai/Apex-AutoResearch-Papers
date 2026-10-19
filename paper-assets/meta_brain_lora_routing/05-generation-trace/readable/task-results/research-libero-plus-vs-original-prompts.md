# research libero plus vs original prompts

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_libero_plus_vs_original_prompts_20260516T161516_result.json`
- **Structured JSON:** [`f803d907762f66cf6c08.json`](../../sessions/f8/f803d907762f66cf6c08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. 原版 LIBERO `libero_spatial` 的 10 个 task prompts

从 `tasks_info.txt` 中读取的 10 个原始 task：

| # | Task name (= prompt) |
|---|---------------------|
| 1 | pick up the black bowl from table center and place it on the plate |
| 2 | pick up the black bowl next to the cookie box and place it on the plate |
| 3 | pick up the black bowl next to the plate and place it on the plate |
| 4 | pick up the black bowl next to the ramekin and place it on the plate |
| 5 | pick up the black bowl on the cookie box and place it on the plate |
| 6 | pick up the black bowl on the ramekin and place it on the plate |
| 7 | pick up the black bowl on the stove and place it on the plate |
| 8 | pick up the black bowl on the wooden cabinet and place it on the plate |
| 9 | pick up the black bowl in the top drawer of the wooden cabinet and place it on the plate |
| 10 | pick up the black bowl between the plate and the ramekin and place it on the plate |

### 2. LIBERO-Plus benchmark 的 4 类变体

LIBERO-Plus 的 `libero_spatial` 包含 **2402 个 tasks**，全部由 10 个原始 task 扩展而来。从 bddl 对比看，有 4 类变体：

| 后缀 | 含义 | Language prompt | 场景布局 | 视觉外观 |
|------|------|----------------|---------|---------|
| `_table_N` | 换桌面纹理 | **相同** | **相同** | 桌面纹理换了（如 `Cobblestone01_GLOSS_6K`） |
| `_tb_N` | 换桌面+墙壁纹理 | **相同** | **相同** | 桌面+背景墙纹理都换了（如 `Bricks02_COL_VAR2_6K_Wall_canvas`） |
| `_add_N` | 添加干扰物体 | **相同**（小写） | 多一个随机 distractor 物体（如 `bag_of_yeast`） | 相同 |
| `_language_N` | 语言改写 | **完全不同的措辞**，语义相同 | **相同** | **相同** |

### 3. 语言变体示例（`_language_N`）

原版 prompt: `"Pick the akita black bowl between the plate and the ramekin and place it on the plate"`

| 变体 | 改写后的 prompt |
|------|----------------|
| language_1 | "grasp the darkhued rounded container situated between the flat dish used for serving food and the small glazed ceramic dish and set it down onto the flat dish used for serving food" |
| language_2 | "Could you put the black bowl on the plate for me Its the one sitting between the plate and the ramekin" |
| language_3 | "pick up the darkcolored rounded container between the flat dish for main courses and the small ceramic dish typically used for baking and serving and place it on the flat dish for main courses" |
| language_4 | "Please locate the black bowl situated between the plate and ramekin then carefully place it on the plate" |
| language_5 | "Would you mind helping me by picking up the black bowl between the plate and ramekin and placing it on the plate" |

### 4. LIBERO-Plus 默认 benchmark 包含哪些变体？

从 `libero_suite_task_map.py` 看，`libero_spatial` 的 2402 个 task 包含 **三类**：
- `_table_N`（桌面纹理变化）
- `_tb_N`（桌面+墙壁纹理变化） 
- `_add_N`（添加干扰物体）
- `_language_N_view_..._initstate_0`（语言改写 + 视角/初始状态变化）

**全部四类都在 benchmark 的 task map 中。**

### 5. 关键结论

**对于 `_table_N` 和 `_tb_N` 变体（纯视觉变化）：**
- Language prompt **完全相同**
- 物体种类、数量、空间位置 **完全相同**  
- Goal 条件 **完全相同**
- **唯一变化是桌面/背景的纹理贴图**

这意味着：pi0_libero 在这些 task 上 0% 成功率，说明模型**仅因为桌面颜色/纹理变了就完全失效**——任务指令、物体布局都一模一样。这是纯粹的 visual robustness 问题，正是 Meta-Brain LoRA routing 要解决的核心场景。

---

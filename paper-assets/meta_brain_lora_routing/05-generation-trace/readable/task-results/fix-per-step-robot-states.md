# fix per step robot states

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_per-step-robot-states_20260515T153343_result.json`
- **Structured JSON:** [`945380a10fe54da37d94.json`](../../sessions/94/945380a10fe54da37d94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**robot_initial_states per_step 收集完成。**

结果：
1. **根因**：`collect_per_step.py` 在同一进程中顺序处理 6 种扰动类型。前 3 种 (camera_viewpoints, light_conditions, background_textures) 共 90 episodes 运行后，某种资源泄漏（MuJoCo OpenGL 上下文或内存累积）导致后 3 种全部异常。`except Exception: continue` 静默吞掉了所有错误，最终保存了空列表。单独运行 robot_initial_states 完全正常。

2. **产出**：
   - 文件：`/root/meta_brain_lora_routing/activations/per_step/robot_initial_states.pt`
   - 大小：**276MB**（原 1.4KB 空文件）
   - 30 episodes，每个 44 replan points，12 层 activations
   - labels: 6class=5, 3class=2, binary=1

3. **per_step 目录当前状态**：
   | 文件 | 大小 | 状态 |
   |------|------|------|
   | camera_viewpoints.pt | 276M | OK |
   | light_conditions.pt | 276M | OK |
   | background_textures.pt | 267M | OK |
   | objects_layout.pt | 111M | 部分收集 |
   | robot_initial_states.pt | **276M** | **已修复** |
   | sensor_noise.pt | 1.3K | 仍空 |

---

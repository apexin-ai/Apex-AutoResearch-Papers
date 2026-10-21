# research safelibero env

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_safelibero_env_20260519T160654_result.json`
- **Structured JSON:** [`8e45edc829c897bafc7c.json`](../../sessions/8e/8e45edc829c897bafc7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/report_safelibero.md`。核心结论：

**可行性: 完全可行，无 blocker。**

关键发现：
1. **数据**: SafeLIBERO 在 HuggingFace 免费获取 (MIT, 638MB)，含 `.bddl` 场景定义 + `.pruned_init` 初始化状态，32 场景×50 episodes
2. **Mesh 可访问**: MuJoCo API 直接暴露 `model.mesh_vert/mesh_face`，可通过 `data.geom_xpos/xmat` 变换到世界坐标。Visual mesh 在 `group=1`，collision 用 primitive 近似在 `group=0`。SDF 应基于 visual mesh 构建
3. **环境安装**: LIBERO 基于 robosuite 1.4.0 + MuJoCo ≥2.3.0，支持 EGL headless 渲染。注意 Python 需 3.8-3.10，robosuite 必须精确 1.4.0
4. **MVP 场景推荐**:
   - **主力**: Spatial "bowl between plate and ramekin" Level II — 碰撞率 100%，AEGIS 达 86% CAR，测试轨迹级 SDF 引导
   - **进阶**: Object "chocolate pudding to basket" Level I — 碰撞率 100%，AEGIS 仅 32% CAR，测试抓取点精细引导

主要风险是 Python 3.8 与现代 VLA 框架的版本冲突，可能需要分离环境。

---

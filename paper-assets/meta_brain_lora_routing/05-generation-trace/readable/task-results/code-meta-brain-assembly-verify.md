# code meta brain assembly verify

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_meta_brain_assembly_verify_20260516T024458_result.json`
- **Structured JSON:** [`bbc9ad4e5d1983be6105.json`](../../sessions/bb/bbc9ad4e5d1983be6105.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证报告

### 1. Assembly 代码状态
`phase1/meta_brain_assembly.py` (608 行) **存在且基本可用**。
- 实现了 Scheme C（动态权重合并）：merged_A/B 加权 → delta = scaling · B@A → inject 到 `mod.weight.data` → finally 恢复
- 提供 `MetaBrain.from_checkpoints(pi0_checkpoint, router_checkpoint, lora_dirs={...})` 工厂
- 提供 `MetaBrain.from_dummy()` dry-run 路径
- 已有 `/tmp/mb_dryrun_explicit.log` 显示 dummy dry-run 通过：5 种 routing mode（par/none/random/universal/oracle）actions=(1,50,32)、routing_weights sum=1.0

### 2. Eval 代码状态
`phase1/evaluate_libero_plus.py` (497 行) **存在但有功能 bug**。
- 支持 `--dry_run` / 5 种 routing / W&B / JSON+LaTeX 输出
- **Bug（高优先级）**：`create_libero_env` 用 `f"{task_suite}_{perturbation_type}"`（如 `libero_spatial_camera_viewpoints`）作为 benchmark 名查找——LIBERO-Plus 注册的 benchmark 只有 `libero_{spatial,object,goal,10,90,100,mix}`，所以每个 perturbation_type 都会**静默 fallback 到 nominal**，扰动评测全部退化为同一个 nominal eval

  正确做法：LIBERO-Plus 把所有扰动任务注入到原 suite，靠 `/root/LIBERO-plus/libero/libero/benchmark/task_classification.json`（10030 条记录，含 7 个 category）按 task name → category 过滤。eval 需改用 `task_classification.json` 筛选 task 索引，而不是构造不存在的 suite key

### 3. Checkpoint 兼容性
| 项 | 状态 |
|---|---|
| pi0_base | `/root/autodl-tmp/checkpoints/pi0_base/model.safetensors` ✓ |
| PAR router | `checkpoints/phase1/par_router/best_router.pt` ✓（input_dim=2048, hidden=256, num_classes=3, pooling="first"）—— 与 PARRouter.from_checkpoint 接口完全匹配 |
| LoRA PEFT 键命名 | `base_model.model.{module_path}.lora_{A,B}.weight`（**注意：无 `.default` 后缀**）。assembly 中 `split(".lora_A")[0]` 切分正确 ✓ |
| LoRA 模块覆盖 | 每个 adapter 含 72 modules = 18 layers × {q,k,v,o}_proj，与 `discover_lora_target_modules` 输出一致 ✓ |
| 形状 | lora_A:(r,2048), lora_B q/v/o:(2048,r) k:(256,r)（GQA），scaling=α/r=32/16=2.0 ✓ |

### 4. ⚠️ 专家命名重大不一致（最高优先级阻塞项）
- **Assembly + Router 期望 3 experts**：`EXPERT_NAMES = ["visual", "spatial", "physical"]`，oracle 映射也只把扰动分到 visual/spatial/physical 3 类
- **实际训练**：cuda:0=visual, cuda:1=physical, cuda:2=universal_r16, cuda:3=universal_r48（来自 `ps -ef` 和 `--perturbation_type`）
- 没人在训 **spatial** expert；产物里有 `lora_spatial_r16/`（4 个旧文件）疑似遗留 dummy
- Router 输出的 3 类标签是 visual/spatial/physical，但 LoRA bank 里却装的是 visual/physical/universal——直接 `from_checkpoints({visual:..., spatial:..., physical:...})` 会因 spatial 没有有效训练而失败/无效

需用户决策：(a) 把 universal 当 spatial 装进去（语义不匹配）；(b) 改 Meta-Brain 为 visual/physical/universal 三专家，对应改 router 训练标签；(c) 补训一个 spatial 专家。universal_r48 显然是用于 baseline，不属于 Meta-Brain 内部专家

### 5. Dry-Run 结果
- ✅ Dummy dry-run（之前已通过，日志在 `/tmp/mb_dryrun_explicit.log`）：5 mode × actions=(1,50,32) × routing sum=1.0
- ✅ PAR router checkpoint 离线加载 OK（config/shape 与 PARRouter 期望完全一致）
- ✅ PEFT adapter 离线 parse OK（72 modules, A/B 全配对）
- ⏭️ 未跑真实 checkpoint 的端到端 GPU dry-run：所有 4 张 GPU 在训练，按约束未占用；但每卡仍有 ~89 GB 空闲，必要时可用 cuda:3 跑（需用户确认是否冒险）

### 6. 训练完成后到评测的阻塞清单
按优先级：

1. **[BLOCKER] 决策 spatial vs universal 三专家方案**——影响 `from_checkpoints` 调用的 `lora_dirs` 字典 key 和 router 语义对齐
2. **[BUG] 修复 `create_libero_env`**——用 `task_classification.json` 按 perturbation category 筛选 task index，而不是构造 `{suite}_{ptype}` benchmark key（否则所有扰动 eval 都是 nominal）
3. **[CFG] 评测命令的 lora_dirs**——确认最终 checkpoint 路径（应为 `lora_{visual,physical,?}_r16/final/`）和 `--router_checkpoint /root/meta_brain_lora_routing/checkpoints/phase1/par_router/best_router.pt`
4. **[VALIDATE] LIBERO env 端到端单 episode 烟测**——目前没跑过完整 env rollout（涉及 mujoco / OffScreenRenderEnv / 渲染），建议训练完成后先单 ptype × 1 episode 跑通
5. **[OPT] eval 应支持 `--task_ids`/`--max_tasks_per_ptype`**——10030 个 task × 1 trial 太长，需子采样

代码可用性 6/10：核心 assembly 通过 dummy + offline 检查，但 eval 的扰动维度筛选根本不工作，且专家命名 mismatch 必须先解决。

---

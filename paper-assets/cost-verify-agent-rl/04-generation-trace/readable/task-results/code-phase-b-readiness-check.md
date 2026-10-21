# code phase b readiness check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase-b-readiness-check_20260514T093711_result.json`
- **Structured JSON:** [`4f4d5e10009cab972247.json`](../../sessions/4f/4f4d5e10009cab972247.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完毕。报告如下：

---

## Phase B (B-IAVR) 启动就绪度报告

### 1. Phase B Config 文件 (`config/_alfworld_phase_b.yaml`)

| 检查项 | 结果 |
|--------|------|
| `model_path: TO_BE_SET` 占位符 | **PASS** — 等 exp013f 产出后填入 |
| `experiment_name: phase-b-alfworld-biavr` | **PASS** |
| `format_penalty: 0` | **PASS** |
| BIAVR 超参 (beta=0.3, alpha=1.0, lambda_init=0.0, eta=0.01, enable_a_pre=true) | **PASS** |
| KL loss (coef=0.01, type=kl) | **PASS** |
| `local_log_dir` 路径 | **WARNING** — 当前指向 `/root/autodl-tmp/checkpoints/exp_003/`，应更新为 Phase B 专用路径（如 `exp_phase_b/`） |
| Config 注释 | **WARNING** — 注释写 "update after exp_002 completes"，应改为 exp013f |

### 2. B-IAVR 代码完整性

| 检查项 | 结果 |
|--------|------|
| 测试 68/68 passed (3.41s) | **PASS** |
| `biavr_changed` 动态计算（非 hardcoded False） | **PASS** — agent_proxy.py L246 初始化 `{}`，L435 由 `_compute_and_update_a_pre` 更新 |
| 模块完整 (action_canonicalize, reward, verify_mechanism, pre_action) | **PASS** |

### 3. FSDP→HF 转换脚本

| 检查项 | 结果 |
|--------|------|
| `scripts/convert_fsdp_to_hf.py` 存在 (5786B) | **PASS** |
| 支持 --input-dir / --output-dir / --dtype / --dry-run | **PASS** |
| exp013f checkpoint 目录 `/root/autodl-tmp/checkpoints/exp013f/` | **PASS** — 目录已创建，内容为空（训练进行中，符合预期） |

### 4. vLLM 兼容性

| 检查项 | 结果 |
|--------|------|
| vLLM 版本 0.18.1 | **PASS** |
| `gpu_memory_utilization: 0.4` | **PASS** — 兼容 |
| `max_model_len: 32768` | **PASS** — 兼容 |
| `disable_mm_preprocessor_cache` | **PASS** — 代码库中无此参数引用，不存在此问题 |

### 5. 磁盘空间

| 检查项 | 结果 |
|--------|------|
| `/root/autodl-tmp/` 116GB 可用 | **PASS** — Phase B 预估需 ~24GB（3 ckpt × 8GB，max_keep=3） |
| `/` 23GB 可用 | **PASS** — 高于 10GB 阈值 |

---

### 总结

**0 FAIL, 2 WARNING, 其余全 PASS。**

启动前需修复的 WARNING：
1. `local_log_dir` 从 `exp_003` 改为 Phase B 专用路径
2. 更新 config 注释中的实验编号引用

---

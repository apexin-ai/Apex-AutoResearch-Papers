# Phase B (B-IAVR) Launch Checklist

**Date**: 2026-05-14
**Prerequisite**: Phase A exp012b success_rate >= 76%

---

## 1. FSDP -> HF Checkpoint Conversion

veRL 内置工具，直接可用（verl 0.6.1 已以 editable 模式安装在 conda base 中）。

### 确定最佳 checkpoint

exp012b 配置: `save_freq=5`, `total_training_steps=30`, `max_actor_ckpt_to_keep=3`。
训练完成后可用的 checkpoint 大概率为 `global_step_20`, `global_step_25`, `global_step_30`。

```bash
# 查看可用 checkpoint
ls /root/autodl-tmp/checkpoints/exp012_grpo/global_step_*/actor/

# 查看各 step 的 validation 结果（选 success_rate 最高的）
ls /root/autodl-tmp/checkpoints/exp012_grpo/exp012-alfworld-reward-fix_*/
```

### 执行转换

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# 替换 BEST_STEP 为最佳 checkpoint 的 step 号
BEST_STEP=30  # <- 根据 validation 结果修改

python -m verl.model_merger merge \
    --backend fsdp \
    --local_dir /root/autodl-tmp/checkpoints/exp012_grpo/global_step_${BEST_STEP}/actor \
    --target_dir /root/autodl-tmp/checkpoints/exp012_hf_merged
```

### 验证转换结果

```bash
python3 -c "
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
model = AutoModelForCausalLM.from_pretrained(
    '/root/autodl-tmp/checkpoints/exp012_hf_merged',
    torch_dtype=torch.bfloat16,
    device_map='cpu'
)
print(f'Model loaded: {model.config.model_type}, params: {sum(p.numel() for p in model.parameters()) / 1e9:.2f}B')
tok = AutoTokenizer.from_pretrained('/root/autodl-tmp/checkpoints/exp012_hf_merged')
print(f'Tokenizer vocab: {tok.vocab_size}')
del model
"
```

**预计时间**: 3-5 分钟
**磁盘需求**: ~15GB（当前可用 135GB）

---

## 2. Phase B 配置修改

配置文件: `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_phase_b.yaml`

### 需要修改的字段

| 字段 | 当前值 | 修改为 |
|------|--------|--------|
| `model_path` | `TO_BE_SET` | `/root/autodl-tmp/checkpoints/exp012_hf_merged` |
| `trainer.experiment_name` | `exp003-alfworld-biavr-selective-verify` | `exp013-alfworld-biavr` |
| `trainer.local_log_dir` | `/root/autodl-tmp/checkpoints/exp_003/` | `/root/autodl-tmp/checkpoints/exp013_biavr/` |

### 建议添加的字段（对齐 exp012 最佳实践）

```yaml
agent_proxy:
  max_turn: 50
  max_actions_per_turn: 1
  max_prompt_length: 4096  # exp012 有此字段，phase_b 缺失

collapse_detection:
  multi_turn_enabled: false
```

### max_model_len 风险评估

Phase B 配置 `max_model_len: 32768` vs exp012 的 `8192`。4× KV cache 增长。
- 2× RTX PRO 6000 48GB, gpu_memory_utilization=0.4 → ~19GB/GPU for vLLM
- Qwen3 7B 模型权重 ~14GB (bf16)，分 2 GPU 各 ~7GB
- 剩余 ~12GB/GPU 给 KV cache，32K context 应该够
- **建议**: 首次运行保持 32768，如果 OOM 降至 16384

---

## 3. Phase B 启动命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/cost-verify-agent-rl/RAGEN

export CUDA_VISIBLE_DEVICES=0,1

nohup python train.py \
    --config-name _alfworld_phase_b \
    > /root/autodl-tmp/logs/exp013_biavr.log 2>&1 &
echo $!
```

---

## 4. 代码审查结果

### biavr_changed bug: **已修复**

- `agent_proxy.py:301` — 初始化 `biavr_changed[eid].append(False)` (占位)
- `agent_proxy.py:306-308` — 当 `_biavr_enable_a_pre=True` 时调用 `_compute_and_update_a_pre()`
- `agent_proxy.py:435` — `biavr_changed[eid][-1] = changed` 用实际比较结果覆盖
- 配置 `enable_a_pre: true` 已设置

### B-IAVR 模块完整性

| 模块 | 路径 | 状态 |
|------|------|------|
| reward.py | `ragen/biavr/reward.py` | BIAVRTracker, biavr_reward, lagrangian_update |
| verify_mechanism.py | `ragen/biavr/verify_mechanism.py` | parse_verify_token, build_biavr_system_prompt |
| pre_action.py | `ragen/biavr/pre_action.py` | build_pre_action_messages, compare_actions |
| action_canonicalize.py | `ragen/biavr/action_canonicalize.py` | canonicalize_action, actions_equivalent |
| test_biavr.py | `ragen/biavr/tests/test_biavr.py` | 68/68 测试通过 |

### 环境注册

`AlfworldBIAVR` 已在 `config/envs.yaml:400` 注册，包含 B-IAVR 专用 system prompt（<VERIFY> token 选择机制）。

### agent_trainer.py 集成

`agent_trainer.py:1068-1073` — 训练循环中已集成 biavr metrics 记录和 lambda 更新。

---

## 5. Pre-flight Checklist (C002)

启动前必须逐项确认：

- [ ] **入口点**: `python train.py --config-name _alfworld_phase_b` (与 exp012b 一致的 `train.py`)
- [ ] **磁盘**: `df -h /root/autodl-tmp/` 确认 > 50GB 可用
- [ ] **Config 参数**:
  - [ ] `model_path` 指向已验证的 HF 格式 checkpoint
  - [ ] `experiment_name` 和 `local_log_dir` 已更新
  - [ ] `biavr` 配置段存在且 `enable_a_pre: true`
  - [ ] `gpu_memory_utilization=0.4` + `max_model_len=32768` (或降为 16384)
- [ ] **Checkpoint 路径**: `/root/autodl-tmp/checkpoints/exp012_hf_merged/` 存在且包含 `config.json` + `model*.safetensors`
- [ ] **GPU**: `nvidia-smi` 确认 cuda:0, cuda:1 空闲（exp012b 已结束）

---

## 6. 阻塞项

| 项目 | 状态 | 说明 |
|------|------|------|
| Phase A 训练完成 | **等待中** | exp012b 30 步 GRPO，预计 ~6h |
| Phase A 验收 | **等待中** | success_rate >= 76% 才启动 Phase B |
| FSDP → HF 转换 | **就绪** | 命令已准备，等 checkpoint |
| Phase B 配置更新 | **需执行** | 3 个字段待修改 |
| max_model_len 验证 | **低风险** | 32768 理论可行，OOM 时降至 16384 |

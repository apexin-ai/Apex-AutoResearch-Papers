# 诊断报告: eval_pi05_l2norm_k095_spatial_seed42 失败

**日期**: 2026-05-22 | **服务器**: westd-38929

## 根因

**网络断连 + `TRANSFORMERS_OFFLINE` 未设置**

时间线：
- 07:58 k=0.9 启动，网络可用 → tokenizer 在线加载 → 实验完成 (SR=95.0%)
- 09:31 k=0.95 启动，**网络已断** → `AutoTokenizer.from_pretrained('google/paligemma-3b-pt-224')` 内部 `is_base_mistral()` → `model_info()` API 请求 → `[Errno 101] Network is unreachable`

细节：
1. `HF_HOME=/root/autodl-tmp/.hf_cache` 已在脚本中设置，tokenizer 缓存完整（tokenizer.json 等文件齐全）
2. 但 transformers 的 `_patch_mistral_regex` → `is_base_mistral` 会**无条件**调用 `huggingface_hub.model_info()` API，即使本地缓存完整
3. 实验启动时没有 `source /etc/network_turbo`（成功的 k=0.5 有），也没有 `HF_HUB_OFFLINE=1` 或 `TRANSFORMERS_OFFLINE=1`
4. 模型加载成功（4143.4M params, pruning 243/256 tokens），仅 preprocessor tokenizer 初始化崩溃

## 服务器状态

| 指标 | 状态 |
|------|------|
| GPU | 4× RTX PRO 6000 Blackwell (94GB each) |
| GPU 0 | ~10.6GB used (k=0.85 运行中) |
| GPU 1-3 | 空闲 |
| 根分区 | 22GB free (29%) ✓ |
| 数据盘 | 52GB free (80%) ✓ |

## 建议重提交命令

```bash
source /etc/network_turbo && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 1
```

修复点：
1. `TRANSFORMERS_OFFLINE=1` — 完全阻止 transformers 网络请求，强制本地缓存
2. `HF_HUB_OFFLINE=1` — huggingface_hub 离线模式
3. `source /etc/network_turbo` — fallback 启用代理
4. `--gpu 1` — 避免与 k=0.85 冲突

# 诊断: eval_pi05_random_k095_object_seed42

## 失败根因
**网络不可达** — tokenizer 加载阶段调用 HuggingFace Hub API (`model_info("google/paligemma-3b-pt-224")`) 时触发 `httpx.ConnectError: [Errno 101] Network is unreachable`。模型本身已加载成功，但 `make_pre_post_processors` 构建 tokenizer 时需要在线验证，而服务器无外网访问。

## 时间线
- 03:55:40 — 开始加载 π0.5 模型
- 03:57:24 — 模型加载完成（4143.4M params），pruning 配置正确（random, keep 243/256 tokens/image, 729 total）
- 03:57:24~04:04:25 — 反复重试网络连接（httpx 默认重试），最终失败
- 总共 124 行日志，无任何 episode 执行记录

## 关键错误日志
```
ValueError: Failed to instantiate processor step 'tokenizer_processor' with config:
{'tokenizer_name': 'google/paligemma-3b-pt-224', ...}.
Error: [Errno 101] Network is unreachable
```

触发位置: `lerobot/processor/tokenizer_processor.py:111` → `AutoTokenizer.from_pretrained("google/paligemma-3b-pt-224")`

调用链: `eval_pi05_pruning_libero.py:165` → `make_pre_post_processors` → `PolicyProcessorPipeline.from_pretrained` → `_build_steps_with_overrides` → `_instantiate_step` → `AutoTokenizer.from_pretrained`

## 部分结果
**无。** 崩溃发生在模型加载后、evaluation 开始前。没有任何 episode 被执行。

## GPU 状态
GPU 0 已释放（0MiB），可重用。GPU 1/2/3 有其他进程占用。

## 修复方案

### 方案 A: 先开启网络再重跑（最快）
```bash
source /etc/network_turbo
python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_object --n_episodes 50 --seed 42 --gpu 0
```

### 方案 B: 预缓存 tokenizer（防复发）
在有网络时提前下载 tokenizer 到本地：
```bash
source /etc/network_turbo
python -c "from transformers import AutoTokenizer; t = AutoTokenizer.from_pretrained('google/paligemma-3b-pt-224'); t.save_pretrained('/root/autodl-tmp/paligemma-tokenizer')"
```
然后修改配置，将 `tokenizer_name` 指向本地路径，或设置 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`。

**建议：方案 A 快速重跑 + 方案 B 做持久化防止复发。**

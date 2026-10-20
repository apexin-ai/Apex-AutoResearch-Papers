# exp-005-batch 失败诊断

## 错误摘要

HGRN h3-1 模型的 `model.safetensors` 文件在评估时尚未下载完成，导致 safetensors 反序列化失败（文件不完整）。后续 `run_hgrn_chain.sh` 恢复脚本也因未应用 FLA patch 而失败。

## 日志尾部（eval_download.log 关键错误）

```
safetensors_rust.SafetensorError: Error while deserializing header: incomplete metadata, file not fully covered
```

完整 traceback 路径：
```
/tmp/eval_with_patch.py → lm_eval cli_evaluate → simple_evaluate
  → HFLM.__init__ → _create_model → AutoModelForCausalLM.from_pretrained
  → _load_pretrained_model → safe_open(file, framework="pt", device="cpu")
  → SafetensorError: incomplete metadata, file not fully covered
```

## 根因分析

### 问题 1（主要）：safetensors 文件不完整

- `run_eval_download.sh` 在 **00:30:51** 尝试加载模型 `/root/entrainment_gated_ft/models/340M-20B-HGRN-hybrid-3-1/model.safetensors`
- 该文件的 mtime 为 **00:33**（评估开始后 2 分钟），说明文件在评估时仍在被写入
- 文件大小 1,331,360,672 bytes（1.24GB），格式 F32，340M 模型合理大小
- 脚本假设 HGRN h3-1 模型已预先下载好，直接进入评估；但模型实际仍在从其他进程下载中
- 当前无 `.aria2` 文件，说明下载后来已完成

### 问题 2（次要）：hgrn_chain.sh 恢复脚本缺少 FLA patch

- `run_hgrn_chain.sh` 使用 `python -m lm_eval` 直接调用，未使用 `/tmp/eval_with_patch.py` wrapper
- 导致 transformers 无法识别 `hgrn` 模型类型：`ValueError: The checkpoint you are trying to load has model type 'hgrn' but Transformers does not recognize this architecture`
- FLA patch（`/root/entrainment_gated_ft/scripts/patch_fla_eval.py`）负责注册自定义架构，缺少它 hgrn/deltanet/gla 等模型都无法加载

## 修复建议

### 修复 1：重新下载并验证模型

```bash
rm -rf /root/entrainment_gated_ft/models/340M-20B-HGRN-hybrid-3-1/
export HF_HUB_DISABLE_XET=1
python3 -c "
from huggingface_hub import snapshot_download
snapshot_download('m-a-p/340M-20B-HGRN-hybrid-3-1',
    local_dir='/root/entrainment_gated_ft/models/340M-20B-HGRN-hybrid-3-1')
"

# 验证 safetensors 完整性
python3 -c "
from safetensors import safe_open
f = safe_open('/root/entrainment_gated_ft/models/340M-20B-HGRN-hybrid-3-1/model.safetensors', framework='pt')
print(f'OK: {len(f.keys())} tensors')
"
```

### 修复 2：修改 run_hgrn_chain.sh 使用 FLA patch

将:
```bash
python -m lm_eval \
```
替换为:
```bash
python3 /tmp/eval_with_patch.py \
```

### 修复 3：在 run_eval_download.sh 中增加模型完整性检查

在评估前添加文件验证：
```bash
python3 -c "
from safetensors import safe_open
safe_open('$HGRN_H31/model.safetensors', framework='pt')
print('Model file OK')
" || { echo 'Model file corrupted, aborting'; exit 1; }
```

### 重跑命令

```bash
nohup bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_download.sh \
  > ~/runs/entrainment_gated_ft/exp-005-batch.log 2>&1 &
```

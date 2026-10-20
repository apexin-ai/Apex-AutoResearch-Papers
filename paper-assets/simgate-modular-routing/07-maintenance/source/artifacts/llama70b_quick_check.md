# Quick Check (2026-05-24 07:49 UTC)

- PID 179639: DONE
- safetensors: 7/9 (missing model-00002, model-00008)
- config.json: present
- tokenizer: present (tokenizer.json + tokenizer_config.json)
- total size: 30GB
- temp dir: cleaned
- incomplete files: none
- vLLM: not running
- disk: 231G/250G used (93%, 20G free)
- symlink: Meta-Llama-3.1-... -> Meta-Llama-3___1-... (created by ModelScope)
- download log: "Finish downloading 19 files" + "SUCCESS"
- 结论: **下载不完整** — 日志报 SUCCESS 但缺少 model-00002 和 model-00008 两个 safetensors 分片，模型无法正常加载，需要补下载

"""Patch openvla-oft modeling_prismatic.py for transformers 5.x + timm 1.x compat."""
import re

p = '/root/openvla-oft-code/prismatic/extern/hf/modeling_prismatic.py'
s = open(p).read()

# 1) Add class-level _supports_sdpa attribute (transformers 5.x reads it in __init__)
old_marker = '    _supports_flash_attn_2: bool = True\n\n    def _init_weights(self, module: nn.Module) -> None:'
new_marker = (
    '    _supports_flash_attn_2: bool = True\n'
    '    _supports_sdpa: bool = True\n'
    '    _supports_flex_attn: bool = False\n'
    '    _supports_attention_backend: bool = False\n\n'
    '    def _init_weights(self, module: nn.Module) -> None:'
)
assert old_marker in s, "marker 1 not found"
s = s.replace(old_marker, new_marker)

# 2) Remove the @property _supports_sdpa (now shadowed by class attr)
prop_pat = (
    r'    @property\n'
    r'    def _supports_sdpa\(self\) -> bool:\n'
    r'        """Check LLM supports SDPA Attention"""\n'
    r'        return self\.language_model\._supports_sdpa\n'
)
s_new = re.sub(prop_pat, '', s)
assert s_new != s, "property removal failed"
s = s_new

# 3) Skip the timm version check (we have timm 1.x)
old_ver = 'if timm.__version__ not in {"0.9.10", "0.9.11", "0.9.12", "0.9.16"}:'
new_ver = 'if False:  # skip timm version check (patched for compat)'
assert old_ver in s, "timm check not found"
s = s.replace(old_ver, new_ver)

open(p, 'w').write(s)
print('Patched modeling_prismatic.py')

"""L1 Ablation Diagnostic: Verify whether monkey-patch is actually working."""

import os
os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"

import glob
import h5py
import inspect
import torch
import torch.nn as nn
from pathlib import Path
from PIL import Image

NUM_IMAGE_TOKENS = 256
INST_START = 1 + NUM_IMAGE_TOKENS  # 257

INSTRUCTION_HEADS_24 = [0,1,2,4,7,8,10,11,12,14,15,16,17,18,19,20,22,23,25,26,27,29,30,31]
CONTROL_HEADS_8 = [3,5,6,9,13,21,24,28]


def main():
    device = torch.device("cuda:0")
    model_path = "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b"
    data_dir = "/root/autodl-tmp/vla-ssd/data/libero/libero_goal/"

    from transformers import AutoModelForVision2Seq, AutoProcessor

    processor = AutoProcessor.from_pretrained(
        model_path, trust_remote_code=True, local_files_only=True
    )
    model = AutoModelForVision2Seq.from_pretrained(
        model_path, torch_dtype=torch.float16, trust_remote_code=True,
        low_cpu_mem_usage=True, attn_implementation="eager", local_files_only=True,
    )
    model = model.to(device).eval()

    # Load one image
    hdf5_files = sorted(glob.glob(os.path.join(data_dir, "*.hdf5")))
    f = h5py.File(hdf5_files[0], "r")
    img = Image.fromarray(f["data"]["demo_0"]["obs"]["agentview_rgb"][0])
    f.close()
    instruction = Path(hdf5_files[0]).stem.replace("_demo", "").replace("_", " ")
    prompt = f"In: What action should the robot take to {instruction}?\nOut:"
    inputs = processor(text=[prompt], images=[img], return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}

    print("=== L1 ABLATION DIAGNOSTIC ===\n")

    # ---- 0. Architecture ----
    print("0. Model architecture:")
    print(f"   Model class: {type(model).__name__} ({type(model).__module__})")
    lm = model.language_model
    print(f"   Language model: {type(lm).__name__} ({type(lm).__module__})")
    attn_mod = lm.model.layers[1].self_attn
    print(f"   L1 Attention class: {type(attn_mod).__name__} ({type(attn_mod).__module__})")
    print(f"   Attention forward source: {inspect.getfile(type(attn_mod).forward)}")
    print(f"   config._attn_implementation: {attn_mod.config._attn_implementation}")

    # ---- 1. INST_START verification ----
    input_ids = inputs["input_ids"]
    seq_len = input_ids.shape[-1]
    tokenizer = processor.tokenizer
    print(f"\n1. INST_START verification:")
    print(f"   Total seq_len: {seq_len}")
    print(f"   INST_START used: {INST_START}")
    print(f"   First 5 tokens: {input_ids[0, :5].tolist()}")
    for i in range(max(0, INST_START - 2), min(seq_len, INST_START + 5)):
        tok = input_ids[0, i].item()
        decoded = tokenizer.decode([tok])
        print(f"   Token[{i}] = {tok} -> '{decoded}'")
    print(f"   Correct: {'Yes' if INST_START < seq_len else 'No'}")

    # ---- 2. Dispatch mechanism ----
    import transformers.models.llama.modeling_llama as llama_mod
    from transformers.models.llama.modeling_llama import repeat_kv

    original_fn = llama_mod.eager_attention_forward
    forward_globals = type(attn_mod).forward.__globals__
    forward_globals_module = forward_globals.get("__name__", "unknown")

    print(f"\n2. Dispatch mechanism:")
    print(f"   llama_mod name: {llama_mod.__name__}")
    print(f"   forward.__globals__ module: {forward_globals_module}")
    print(f"   Same module: {forward_globals_module == llama_mod.__name__}")
    print(f"   Same globals dict: {forward_globals is vars(llama_mod)}")
    ref_in_globals = forward_globals.get("eager_attention_forward")
    print(f"   forward globals has eager_attention_forward: {ref_in_globals is not None}")
    print(f"   Same object as llama_mod's: {ref_in_globals is original_fn}")

    has_all_attn = hasattr(llama_mod, "ALL_ATTENTION_FUNCTIONS")
    print(f"   ALL_ATTENTION_FUNCTIONS exists: {has_all_attn}")
    if has_all_attn:
        keys = list(llama_mod.ALL_ATTENTION_FUNCTIONS.keys())
        print(f"   ALL_ATTENTION_FUNCTIONS keys: {keys}")
        print(f"   'eager' in keys: {'eager' in keys}")

    # ---- 3. Attention weight comparison ----
    print(f"\n3. Attention weights (readout -> instruction):")

    call_counter = {"baseline": 0, "ablated": 0}
    captured_attn = {}
    hidden_store = {}

    def make_attn_fn(mode, heads_to_ablate=None):
        def fn(module, query, key, value, attention_mask, scaling, dropout=0.0, **kwargs):
            key_states = repeat_kv(key, module.num_key_value_groups)
            value_states = repeat_kv(value, module.num_key_value_groups)
            attn_weights = torch.matmul(query, key_states.transpose(2, 3)) * scaling
            if attention_mask is not None:
                causal_mask = attention_mask[:, :, :, : key_states.shape[-2]]
                attn_weights = attn_weights + causal_mask
            attn_weights = nn.functional.softmax(
                attn_weights, dim=-1, dtype=torch.float32
            ).to(query.dtype)

            is_target = hasattr(module, "_diag_tag") and module._diag_tag
            if is_target:
                call_counter[mode] += 1
                captured_attn[f"{mode}_pre"] = attn_weights.detach().cpu().float()

            if heads_to_ablate is not None and is_target:
                sl = attn_weights.shape[-1]
                if INST_START < sl:
                    attn_weights[:, heads_to_ablate, :, INST_START:] = 0.0
                    row_sums = attn_weights.sum(dim=-1, keepdim=True).clamp(min=1e-9)
                    attn_weights = attn_weights / row_sums
                    captured_attn[f"{mode}_post"] = attn_weights.detach().cpu().float()

            attn_output = torch.matmul(attn_weights, value_states)
            attn_output = attn_output.transpose(1, 2).contiguous()
            return attn_output, attn_weights
        return fn

    def make_hidden_hook(tag):
        def hook_fn(module, inp, output):
            h = output[0] if isinstance(output, tuple) else output
            hidden_store[tag] = h[:, -1, :].detach().cpu().float()
        return hook_fn

    attn_mod._diag_tag = True

    # --- Baseline ---
    baseline_fn = make_attn_fn("baseline")
    llama_mod.eager_attention_forward = baseline_fn
    if forward_globals is not vars(llama_mod):
        forward_globals["eager_attention_forward"] = baseline_fn

    hh = model.language_model.model.layers[1].register_forward_hook(make_hidden_hook("baseline"))
    with torch.no_grad(), torch.amp.autocast("cuda", dtype=torch.float16):
        model(**inputs)
    hh.remove()

    print(f"   Baseline L1 call count: {call_counter['baseline']}")
    if "baseline_pre" in captured_attn:
        bl = captured_attn["baseline_pre"]
        bl_all = bl[:, :, -1, INST_START:].mean().item()
        bl_inst = bl[0, INSTRUCTION_HEADS_24, -1, INST_START:].mean().item()
        bl_ctrl = bl[0, CONTROL_HEADS_8, -1, INST_START:].mean().item()
        print(f"   readout->inst mean (all heads): {bl_all:.6f}")
        print(f"   readout->inst mean (24 inst heads): {bl_inst:.6f}")
        print(f"   readout->inst mean (8 ctrl heads): {bl_ctrl:.6f}")
    else:
        print("   WARNING: Baseline capturing function NOT called on L1!")
        print("   The monkey-patch is NOT reaching the attention layer.")

    # --- Ablated ---
    ablated_fn = make_attn_fn("ablated", INSTRUCTION_HEADS_24)
    llama_mod.eager_attention_forward = ablated_fn
    if forward_globals is not vars(llama_mod):
        forward_globals["eager_attention_forward"] = ablated_fn

    hh = model.language_model.model.layers[1].register_forward_hook(make_hidden_hook("ablated"))
    with torch.no_grad(), torch.amp.autocast("cuda", dtype=torch.float16):
        model(**inputs)
    hh.remove()

    print(f"\n   Ablated L1 call count: {call_counter['ablated']}")
    if "ablated_post" in captured_attn:
        ab = captured_attn["ablated_post"]
        ab_all = ab[:, :, -1, INST_START:].mean().item()
        ab_inst = ab[0, INSTRUCTION_HEADS_24, -1, INST_START:].mean().item()
        ab_ctrl = ab[0, CONTROL_HEADS_8, -1, INST_START:].mean().item()
        print(f"   readout->inst mean (all heads): {ab_all:.6f}")
        print(f"   readout->inst mean (24 inst heads): {ab_inst:.6f}")
        print(f"   readout->inst mean (8 ctrl heads): {ab_ctrl:.6f}")
        delta = bl_all - ab_all
        print(f"   Delta (all heads): {delta:.6f}")
        if ab_inst < 1e-6:
            print("   Verdict: patch WORKING (ablated heads inst attention ~ 0)")
        elif abs(delta) < 1e-6:
            print("   Verdict: patch NOT working (no change)")
        else:
            print("   Verdict: PARTIAL effect")
    elif "ablated_pre" in captured_attn:
        print("   Ablation branch not reached (INST_START >= seq_len?)")
        ab_pre = captured_attn["ablated_pre"]
        print(f"   seq_len in attn: {ab_pre.shape[-1]}, INST_START: {INST_START}")
    else:
        print("   WARNING: Ablated capturing function NOT called on L1!")

    # --- Restore ---
    llama_mod.eager_attention_forward = original_fn
    if forward_globals is not vars(llama_mod):
        forward_globals["eager_attention_forward"] = original_fn
    attn_mod._diag_tag = False

    # ---- 4. Hidden state comparison ----
    print(f"\n4. Hidden state change (L1 readout token):")
    if "baseline" in hidden_store and "ablated" in hidden_store:
        cos_sim = torch.nn.functional.cosine_similarity(
            hidden_store["baseline"], hidden_store["ablated"], dim=-1
        ).item()
        l2_dist = torch.norm(hidden_store["baseline"] - hidden_store["ablated"], p=2).item()
        print(f"   Cosine similarity: {cos_sim:.6f}")
        print(f"   L2 distance: {l2_dist:.6f}")
        if cos_sim > 0.9999:
            print("   Verdict: representation NOT changed (cos_sim ~ 1.0)")
        elif cos_sim > 0.99:
            print("   Verdict: representation slightly changed")
        else:
            print("   Verdict: representation significantly changed")
    else:
        print("   Cannot compute (missing hidden states)")

    # ---- 5. Test original script's install_ablation_hook mechanism ----
    print(f"\n5. Original install_ablation_hook mechanism test:")
    llama_mod.eager_attention_forward = original_fn
    if forward_globals is not vars(llama_mod):
        forward_globals["eager_attention_forward"] = original_fn

    # Simulate what the original script does
    layer1_attn = model.language_model.model.layers[1].self_attn
    layer1_attn._ablate_heads = INSTRUCTION_HEADS_24

    def simulated_ablated_fn(module, query, key, value, attention_mask,
                             scaling, dropout=0.0, **kwargs):
        pass  # body doesn't matter for this test

    llama_mod.eager_attention_forward = simulated_ablated_fn

    # Check if the forward method will see the patched function
    ref_after_patch = forward_globals.get("eager_attention_forward")
    sees_patch = ref_after_patch is simulated_ablated_fn
    print(f"   After patching llama_mod.eager_attention_forward:")
    print(f"   forward.__globals__ sees patched fn: {sees_patch}")
    if not sees_patch:
        print(f"   BUG CONFIRMED: install_ablation_hook patches llama_mod,")
        print(f"   but LlamaAttention.forward resolves from different globals!")
        print(f"   forward globals module: {forward_globals_module}")
        print(f"   llama_mod: {llama_mod.__name__}")
        print(f"   forward_globals id: {id(forward_globals)}")
        print(f"   vars(llama_mod) id: {id(vars(llama_mod))}")
    else:
        print("   OK: forward will see the patched function")

    # Restore
    llama_mod.eager_attention_forward = original_fn
    if forward_globals is not vars(llama_mod):
        forward_globals["eager_attention_forward"] = original_fn
    layer1_attn._ablate_heads = None

    # ---- Conclusion ----
    print(f"\n=== CONCLUSION ===")
    patch_reaches_l1 = call_counter["baseline"] > 0
    attn_changed = "ablated_post" in captured_attn and abs(bl_all - ab_all) > 1e-6 if "baseline_pre" in captured_attn and "ablated_post" in captured_attn else False
    hidden_changed = "baseline" in hidden_store and "ablated" in hidden_store and cos_sim < 0.9999 if "baseline" in hidden_store and "ablated" in hidden_store else False

    if not patch_reaches_l1:
        print("Monkey-patch status: NOT WORKING (function never called on L1)")
    elif not attn_changed:
        print("Monkey-patch status: NOT WORKING (attention weights unchanged)")
    elif not hidden_changed:
        print("Monkey-patch status: WORKING but hidden states unchanged (residual dominates?)")
    else:
        print("Monkey-patch status: WORKING")
        print("If classification still = 1.0, the task is too easy or info recovers downstream.")


if __name__ == "__main__":
    main()

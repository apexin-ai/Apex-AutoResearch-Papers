"""Full OFT inference test v2 - all 3 bugs fixed: image rotation, wrist cam, proprio format."""
import sys, os, math
os.environ['CUDA_VISIBLE_DEVICES'] = '2'
import torch
import numpy as np
from PIL import Image
import json

CKPT = '/root/autodl-tmp/openvla-oft-libero-object'
DEVICE = torch.device('cuda:0')
ACTION_DIM = 7
NUM_ACTIONS_CHUNK = 8
PROPRIO_DIM = 8

# ===== Step 1: Load model =====
print('=== Loading model ===')
from transformers import AutoModelForVision2Seq, AutoProcessor
model = AutoModelForVision2Seq.from_pretrained(
    CKPT, torch_dtype=torch.bfloat16, trust_remote_code=True, low_cpu_mem_usage=True
)
model.vision_backbone.set_num_images_in_input(2)
model = model.to(DEVICE).eval()
processor = AutoProcessor.from_pretrained(CKPT, trust_remote_code=True)
print(f'Model: {type(model).__name__}')

# Inject LIBERO fine-tuning stats into model.norm_stats
with open(os.path.join(CKPT, 'dataset_statistics.json')) as _f:
    _ds_stats = json.load(_f)
model.norm_stats.update(_ds_stats)
print(f'Injected norm_stats keys: {list(_ds_stats.keys())}')

llm_dim = model.language_model.config.hidden_size
print(f'LLM dim: {llm_dim}')

# ===== Step 2: Load action_head =====
print('\n=== Loading action_head ===')
import torch.nn as nn

class MLPResNetBlock(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.ffn = nn.Sequential(nn.LayerNorm(dim), nn.Linear(dim, dim), nn.ReLU())
    def forward(self, x):
        return self.ffn(x) + x

class MLPResNet(nn.Module):
    def __init__(self, num_blocks, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.layer_norm1 = nn.LayerNorm(input_dim)
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.mlp_resnet_blocks = nn.ModuleList([MLPResNetBlock(hidden_dim) for _ in range(num_blocks)])
        self.layer_norm2 = nn.LayerNorm(hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)
    def forward(self, x):
        x = self.relu(self.fc1(self.layer_norm1(x)))
        for b in self.mlp_resnet_blocks:
            x = b(x)
        return self.fc2(self.layer_norm2(x))

class L1RegressionActionHead(nn.Module):
    def __init__(self, input_dim=4096, hidden_dim=4096, action_dim=7):
        super().__init__()
        self.action_dim = action_dim
        self.model = MLPResNet(num_blocks=2, input_dim=input_dim*ACTION_DIM, hidden_dim=hidden_dim, output_dim=action_dim)
    def predict_action(self, actions_hidden_states):
        batch_size = actions_hidden_states.shape[0]
        rearranged = actions_hidden_states.reshape(batch_size, NUM_ACTIONS_CHUNK, -1)
        return self.model(rearranged)

action_head = L1RegressionActionHead(input_dim=llm_dim, hidden_dim=llm_dim, action_dim=ACTION_DIM)
ah_path = os.path.join(CKPT, 'action_head--150000_checkpoint.pt')
ah_sd = torch.load(ah_path, weights_only=True)
ah_sd = {k.replace('module.',''):v for k,v in ah_sd.items()}
action_head.load_state_dict(ah_sd)
action_head = action_head.to(torch.bfloat16).to(DEVICE).eval()
print(f'action_head loaded: {sum(p.numel() for p in action_head.parameters())/1e6:.1f}M params')

# ===== Step 3: Load proprio_projector =====
print('\n=== Loading proprio_projector ===')

class ProprioProjector(nn.Module):
    def __init__(self, llm_dim, proprio_dim):
        super().__init__()
        self.fc1 = nn.Linear(proprio_dim, llm_dim, bias=True)
        self.fc2 = nn.Linear(llm_dim, llm_dim, bias=True)
        self.act_fn1 = nn.GELU()
    def forward(self, proprio):
        return self.fc2(self.act_fn1(self.fc1(proprio)))

pp = ProprioProjector(llm_dim=llm_dim, proprio_dim=PROPRIO_DIM)
pp_path = os.path.join(CKPT, 'proprio_projector--150000_checkpoint.pt')
pp_sd = torch.load(pp_path, weights_only=True)
pp_sd = {k.replace('module.',''):v for k,v in pp_sd.items()}
pp.load_state_dict(pp_sd)
pp = pp.to(torch.bfloat16).to(DEVICE).eval()
print(f'proprio_projector loaded: {sum(p.numel() for p in pp.parameters())/1e6:.1f}M params')

# ===== Helper functions =====
def quat2axisangle(quat):
    quat = quat.copy()
    if quat[3] > 1.0:
        quat[3] = 1.0
    elif quat[3] < -1.0:
        quat[3] = -1.0
    den = np.sqrt(1.0 - quat[3] * quat[3])
    if math.isclose(den, 0.0):
        return np.zeros(3)
    return (quat[:3] * 2.0 * math.acos(quat[3])) / den

# ===== Step 4: Set up LIBERO env =====
print('\n=== Setting up LIBERO env ===')
sys.path.insert(0, '/root/autodl-tmp/LIBERO')
from libero.libero import get_libero_path, benchmark
from libero.libero.envs import OffScreenRenderEnv

bm = benchmark.get_benchmark_dict()['libero_object']()
task = bm.get_task(0)
task_name = task.name
task_bddl = os.path.join(get_libero_path('bddl_files'), task.problem_folder, task.bddl_file)
print(f'Task: {task_name}')

env_args = {"bddl_file_name": task_bddl, "camera_heights": 256, "camera_widths": 256}
env = OffScreenRenderEnv(**env_args)
env.seed(42)
init_states = bm.get_task_init_states(0)
env.reset()
obs = env.set_init_state(init_states[0])
print(f'Env ready')

# ===== Step 5: Preprocess - FIXED all 3 bugs =====
print('\n=== Preprocessing (FIXED) ===')
import tensorflow as tf

def resize_image_for_policy(img, resize_size=224):
    img_tf = tf.image.encode_jpeg(img)
    img_tf = tf.io.decode_image(img_tf, expand_animations=False, dtype=tf.uint8)
    img_tf = tf.image.resize(img_tf, (resize_size, resize_size), method='lanczos3', antialias=True)
    img_tf = tf.cast(tf.clip_by_value(tf.round(img_tf), 0, 255), tf.uint8)
    return img_tf.numpy()

def center_crop_image(image, crop_scale=0.9):
    image_t = tf.convert_to_tensor(np.array(image))
    orig_dtype = image_t.dtype
    image_t = tf.image.convert_image_dtype(image_t, tf.float32)
    image_t = tf.expand_dims(image_t, axis=0)
    new_h = tf.clip_by_value(tf.sqrt(crop_scale), 0, 1)
    new_w = tf.clip_by_value(tf.sqrt(crop_scale), 0, 1)
    h_off = (1 - new_h) / 2
    w_off = (1 - new_w) / 2
    boxes = tf.reshape(tf.stack([h_off, w_off, h_off + new_h, w_off + new_w]), (1, 4))
    image_t = tf.image.crop_and_resize(image_t, boxes, tf.range(1), (224, 224))
    image_t = image_t[0]
    image_t = tf.clip_by_value(image_t, 0, 1)
    image_t = tf.image.convert_image_dtype(image_t, orig_dtype, saturate=True)
    return Image.fromarray(image_t.numpy()).convert('RGB')

# FIX 1: 180-degree rotation for BOTH images ([::-1, ::-1] not just [::-1])
agentview_img = obs['agentview_image'][::-1, ::-1]
wrist_img = obs['robot0_eye_in_hand_image'][::-1, ::-1]
print(f'Agentview shape: {agentview_img.shape}, Wrist shape: {wrist_img.shape}')

# Resize both
agentview_resized = resize_image_for_policy(agentview_img, 224)
wrist_resized = resize_image_for_policy(wrist_img, 224)

# Center crop both
agentview_pil = center_crop_image(Image.fromarray(agentview_resized))
wrist_pil = center_crop_image(Image.fromarray(wrist_resized))
print(f'Agentview PIL: {agentview_pil.size}, Wrist PIL: {wrist_pil.size}')

# FIX 3: Proprio = eef_pos(3) + quat2axisangle(3) + gripper_qpos(2) = 8D
with open(os.path.join(CKPT, 'dataset_statistics.json')) as f:
    ds_stats = json.load(f)
unnorm_key = 'libero_object_no_noops'
proprio_stats = ds_stats[unnorm_key]['proprio']

eef_pos = obs['robot0_eef_pos']  # 3D
eef_quat = obs['robot0_eef_quat']  # 4D -> convert to axis-angle 3D
eef_aa = quat2axisangle(eef_quat)
gripper_qpos = obs['robot0_gripper_qpos']  # 2D (both fingers)
raw_proprio = np.concatenate([eef_pos, eef_aa, gripper_qpos])
print(f'Raw proprio (8D): {raw_proprio}')
print(f'  eef_pos={eef_pos}, eef_aa={eef_aa}, gripper_qpos={gripper_qpos}')

# Normalize proprio
mask = proprio_stats.get('mask', np.ones_like(proprio_stats['q01'], dtype=bool))
p_high = np.array(proprio_stats['q99'])
p_low = np.array(proprio_stats['q01'])
normalized_proprio = np.clip(
    np.where(mask, 2 * (raw_proprio - p_low) / (p_high - p_low + 1e-8) - 1, raw_proprio),
    -1.0, 1.0
)
print(f'Normalized proprio: {normalized_proprio}')

# ===== Step 6: Build model inputs (FIX 2: 2 images) =====
print('\n=== Building model inputs ===')
task_label = task_name
prompt = "In: What action should the robot take to " + task_label.lower() + "?\nOut:"

# Process primary image
inputs = processor(prompt, agentview_pil).to(DEVICE, dtype=torch.bfloat16)

# Process wrist image and concatenate pixel_values
wrist_inputs = processor(prompt, wrist_pil).to(DEVICE, dtype=torch.bfloat16)
inputs['pixel_values'] = torch.cat([inputs['pixel_values'], wrist_inputs['pixel_values']], dim=1)

print(f'input_ids shape: {inputs["input_ids"].shape}')
print(f'pixel_values shape: {inputs["pixel_values"].shape}')  # Should be (1, 12, 224, 224)
print(f'attention_mask shape: {inputs["attention_mask"].shape}')

# ===== Step 7: Run predict_action =====
print('\n=== Running predict_action ===')
with torch.inference_mode():
    action, hidden = model.predict_action(
        **inputs,
        unnorm_key=unnorm_key,
        proprio=normalized_proprio,
        proprio_projector=pp,
        action_head=action_head,
    )

print(f'\nAction output shape: {action.shape}')
print('Action output (K=8 chunks):')
for i in range(len(action)):
    a = action[i]
    print(f'  [{i}]: [{a[0]:.4f}, {a[1]:.4f}, {a[2]:.4f}, {a[3]:.4f}, {a[4]:.4f}, {a[5]:.4f}, {a[6]:.4f}]')

action_stats = ds_stats[unnorm_key]['action']
print(f'\nAction norm stats:')
print(f'  q01: {action_stats["q01"]}')
print(f'  q99: {action_stats["q99"]}')
print(f'  mask: {action_stats.get("mask", "N/A")}')

print('\nGripper post-processing:')
for i in range(len(action)):
    g = action[i][-1]
    g_norm = 1.0 if g >= 0.5 else -1.0
    g_inv = -g_norm
    print(f'  Chunk {i}: gripper raw={g:.4f}, norm={g_norm:.1f}, inverted={g_inv:.1f}')

env.close()
print('\nDONE')

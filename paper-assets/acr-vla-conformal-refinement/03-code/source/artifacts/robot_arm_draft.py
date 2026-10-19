"""Robot arm concept sketch for ACR-VLA paper Figure 1 / teaser.

Simple matplotlib draft showing a 2D robot arm with:
- Fixed base
- 2 revolute joints
- End-effector (gripper)
- Camera observation arrow
- Action vector annotation
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Arc, Wedge
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'mathtext.fontset': 'cm',
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'text.color': '#333333',
})

fig, ax = plt.subplots(figsize=(6, 5), dpi=300)
ax.set_xlim(-1.5, 5.5)
ax.set_ylim(-0.8, 5.5)
ax.set_aspect('equal')
ax.axis('off')

# ── Colors ──
LINK_COLOR = '#2C3E50'
JOINT_COLOR = '#E67E22'
BASE_COLOR = '#7F8C8D'
GRIPPER_COLOR = '#A93226'
TABLE_COLOR = '#BDC3C7'
ARROW_COLOR = '#1A5276'
LIGHT_BG = '#F8F9FA'

# ── Table / surface ──
table_y = 0.0
ax.fill_between([-1.5, 5.5], [table_y - 0.3, table_y - 0.3],
                [table_y, table_y], color=TABLE_COLOR, alpha=0.4, zorder=0)
ax.plot([-1.5, 5.5], [table_y, table_y], color='#95A5A6', lw=1.5, zorder=1)

# ── Robot arm geometry ──
base_x, base_y = 1.0, table_y
L1, L2 = 2.0, 1.8
theta1 = np.radians(65)
theta2 = np.radians(-30)

# Joint positions
j1_x, j1_y = base_x, base_y + 0.4  # shoulder
j2_x = j1_x + L1 * np.cos(theta1)
j2_y = j1_y + L1 * np.sin(theta1)
ee_x = j2_x + L2 * np.cos(theta1 + theta2)
ee_y = j2_y + L2 * np.sin(theta1 + theta2)

# ── Base ──
base_w, base_h = 0.8, 0.4
ax.add_patch(FancyBboxPatch(
    (base_x - base_w/2, base_y), base_w, base_h,
    boxstyle='round,pad=0.02', fc=BASE_COLOR, ec='#5D6D7E',
    lw=1.5, zorder=3))
# Base hatching (ground)
for i in range(6):
    xi = base_x - base_w/2 - 0.1 + i * 0.2
    ax.plot([xi, xi - 0.15], [base_y, base_y - 0.15],
            color='#95A5A6', lw=0.8, zorder=2)

# ── Links ──
link_w = 0.18
# Link 1
ax.plot([j1_x, j2_x], [j1_y, j2_y], color=LINK_COLOR, lw=8,
        solid_capstyle='round', zorder=4)
ax.plot([j1_x, j2_x], [j1_y, j2_y], color='#34495E', lw=5,
        solid_capstyle='round', zorder=5)

# Link 2
ax.plot([j2_x, ee_x], [j2_y, ee_y], color=LINK_COLOR, lw=7,
        solid_capstyle='round', zorder=4)
ax.plot([j2_x, ee_x], [j2_y, ee_y], color='#34495E', lw=4,
        solid_capstyle='round', zorder=5)

# ── Joints ──
for jx, jy, r in [(j1_x, j1_y, 0.18), (j2_x, j2_y, 0.15)]:
    ax.add_patch(plt.Circle((jx, jy), r, fc=JOINT_COLOR, ec='#D35400',
                            lw=1.5, zorder=6))
    ax.add_patch(plt.Circle((jx, jy), r * 0.35, fc='#F39C12', ec='none',
                            zorder=7))

# ── End-effector (gripper) ──
grip_angle = theta1 + theta2
grip_len = 0.5
grip_open = 0.25

# Two gripper fingers
for sign in [1, -1]:
    perp_angle = grip_angle + np.pi/2
    gx0 = ee_x + sign * grip_open/2 * np.cos(perp_angle)
    gy0 = ee_y + sign * grip_open/2 * np.sin(perp_angle)
    gx1 = gx0 + grip_len * np.cos(grip_angle)
    gy1 = gy0 + grip_len * np.sin(grip_angle)
    ax.plot([ee_x, gx0, gx1], [ee_y, gy0, gy1],
            color=GRIPPER_COLOR, lw=3.5, solid_capstyle='round', zorder=5)

# Small circle at EE base
ax.add_patch(plt.Circle((ee_x, ee_y), 0.1, fc=GRIPPER_COLOR, ec='#922B21',
                        lw=1.2, zorder=6))

# ── Target object on table ──
obj_x, obj_y = 3.8, table_y + 0.25
ax.add_patch(FancyBboxPatch(
    (obj_x - 0.25, obj_y - 0.25), 0.5, 0.5,
    boxstyle='round,pad=0.05', fc='#3498DB', ec='#2980B9',
    lw=1.2, zorder=3, alpha=0.85))
ax.text(obj_x, obj_y - 0.55, 'target', ha='center', fontsize=8,
        color='#2980B9', fontstyle='italic')

# ── Camera / observation ──
cam_x, cam_y = 4.5, 4.5
# Camera body
cam_w, cam_h = 0.6, 0.4
ax.add_patch(FancyBboxPatch(
    (cam_x - cam_w/2, cam_y - cam_h/2), cam_w, cam_h,
    boxstyle='round,pad=0.03', fc='#2C3E50', ec='#1B2631',
    lw=1.2, zorder=5))
# Lens
ax.add_patch(plt.Circle((cam_x - cam_w/2 - 0.08, cam_y), 0.12,
                        fc='#1A5276', ec='#1B2631', lw=1.0, zorder=5))
ax.add_patch(plt.Circle((cam_x - cam_w/2 - 0.08, cam_y), 0.06,
                        fc='#85C1E9', ec='none', zorder=6))

# Camera label
ax.text(cam_x + 0.1, cam_y + 0.45, 'Camera', ha='center', fontsize=8,
        color='#2C3E50', fontweight='bold')

# Observation cone (dashed)
cone_target_y = table_y + 0.5
cone_target_x = 2.5
ax.plot([cam_x - 0.3, cone_target_x - 0.8], [cam_y - 0.2, cone_target_y + 0.3],
        color='#85C1E9', lw=0.8, ls='--', alpha=0.6, zorder=1)
ax.plot([cam_x - 0.3, cone_target_x + 1.5], [cam_y - 0.2, cone_target_y + 0.3],
        color='#85C1E9', lw=0.8, ls='--', alpha=0.6, zorder=1)

# O_t label (near camera)
ax.text(cam_x - 0.7, cam_y + 0.45, r'$O_t$', fontsize=14,
        fontweight='bold', color='#1A5276', fontstyle='italic',
        ha='center')

# ── Action vector at EE (corrected action, green, pointing toward target) ──
action_dx, action_dy = 0.9, -0.5
ax.annotate('', xy=(ee_x + action_dx, ee_y + action_dy),
            xytext=(ee_x, ee_y),
            arrowprops=dict(arrowstyle='->', color='#27AE60',
                           lw=2.8, mutation_scale=15),
            zorder=8)
ax.text(ee_x + action_dx + 0.15, ee_y + action_dy - 0.15,
        r'$\mathbf{a}^*$', fontsize=13, color='#27AE60',
        fontweight='bold', ha='left')

# ── Uncertainty visualization (two sample actions, spread apart) ──
# Sample 1 (upper-right)
s1_dx, s1_dy = 0.5, 0.7
ax.annotate('', xy=(ee_x + s1_dx, ee_y + s1_dy),
            xytext=(ee_x, ee_y),
            arrowprops=dict(arrowstyle='->', color='#E74C3C',
                           lw=1.5, ls='--', mutation_scale=10,
                           alpha=0.7),
            zorder=7)
ax.text(ee_x + s1_dx + 0.1, ee_y + s1_dy + 0.15,
        r'$\mathbf{a}^1$', fontsize=10, color='#E74C3C', alpha=0.85)

# Sample 2 (right, slightly down)
s2_dx, s2_dy = 1.0, 0.15
ax.annotate('', xy=(ee_x + s2_dx, ee_y + s2_dy),
            xytext=(ee_x, ee_y),
            arrowprops=dict(arrowstyle='->', color='#E74C3C',
                           lw=1.5, ls='--', mutation_scale=10,
                           alpha=0.7),
            zorder=7)
ax.text(ee_x + s2_dx + 0.1, ee_y + s2_dy - 0.12,
        r'$\mathbf{a}^2$', fontsize=10, color='#E74C3C', alpha=0.85)

# d_2 curly brace / label between the two samples
mid_x = ee_x + (s1_dx + s2_dx) / 2 + 0.35
mid_y = ee_y + (s1_dy + s2_dy) / 2 + 0.2
# Dashed line connecting tips of a1 and a2
ax.plot([ee_x + s1_dx, ee_x + s2_dx],
        [ee_y + s1_dy, ee_y + s2_dy],
        color='#8E44AD', lw=1.0, ls=':', alpha=0.7, zorder=7)
ax.text(mid_x, mid_y, r'$d_2$', fontsize=12, color='#8E44AD',
        fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.1', fc='white', ec='none', alpha=0.8))

# ── Labels ──
ax.text(base_x, base_y - 0.35, 'Base', ha='center', fontsize=8,
        color=BASE_COLOR, fontweight='bold')
ax.text(j1_x - 0.4, j1_y + 0.1, 'Joint 1', ha='right', fontsize=7.5,
        color=JOINT_COLOR)
ax.text(j2_x - 0.35, j2_y + 0.2, 'Joint 2', ha='right', fontsize=7.5,
        color=JOINT_COLOR)
ax.text(ee_x - 0.1, ee_y - 0.4, 'End-effector', ha='center', fontsize=7.5,
        color=GRIPPER_COLOR, fontstyle='italic')

plt.tight_layout(pad=0.3)
out = '/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/robot_arm_draft.png'
fig.savefig(out, dpi=300, bbox_inches='tight', pad_inches=0.08,
            facecolor='white', edgecolor='none')
plt.close()
print(f'Saved to {out}')

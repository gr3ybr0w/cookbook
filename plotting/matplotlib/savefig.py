import os
%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt



# Where to save the figures
PROJECT_ROOT_DIR = "."
CHAPTER_ID = "chaptername"

def save_fig(fig_id, tight_layout=True):
    path = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID, fig_id + ".png")
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format='png', dpi=300)

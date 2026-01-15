# %%
# Day Two Stuff
# Name: Nelson Lattimer
# Repo: daytwostuff

# %%
# Terminal path before virtual environment
# /workspaces/daytwostuff

# %%
# Should the virtual environment be included in the repo?
# No, virtual environments are machine-specific and a lot of lines, isntead you have the requirnments.txt.

# %%
# Terminal path after virtual environment
# /workspaces/daytwostuff
# The path is the same

# %%
# Loaded dependencies from requirements.txt using:
# pip install -r requirements.txt

# %%
import pandas as pd

df = pd.read_csv("basketball_2024_2025.csv")
df.head()
# Imported Dataset

# %%
# Extension Menu Notes:
# Extensions can be installed locally or inside the Codespace
# Codespaces may require re-installing extensions

# %%
# Data Wrangler observations:
# 1. Clean, spreadsheet-style table view
# 2. Shows the missing and distinct values in each column
# 3. Gives graphs with distributions

# %%
# Installed plotly
# Version: 6.5.1

# %%
# Why requirements.txt?
# It allows others to recreate the same environment with the same package versions
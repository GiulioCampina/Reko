import subprocess
import sys
import dtbs_fct
import page_one


adrs_dir = page_one.adrs_file
print(adrs_dir)

subprocess.run([sys.executable, "-m", "streamlit", "run", adrs_dir, ])

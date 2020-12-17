import matplotlib.pyplot as plt
from matplotlib.font_manager import FontManager
import subprocess


def getAvailableFont():
    fm = FontManager()
    mat_fonts = set(f.name for f in fm.ttflist)
    output = subprocess.check_output(
        'fc-list :lang=zh -f "%{family}\n"', shell=True)
    zh_fonts = set(f.split(',', 1)[0]
                   for f in output.decode('utf-8').split('\n'))
    available = mat_fonts & zh_fonts
    return available.pop()


plt.rcParams['font.sans-serif'] = [getAvailableFont()]
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['svg.fonttype'] = 'none'

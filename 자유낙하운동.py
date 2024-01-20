import numpy as np
import matplotlib.pyplot as plt

m = 0.001  # 질량 (kg)
g = 9.8  # 중력 가속도 (m/s^2)
Vt = 8.33  # 종단속도 (m/s^2)
K = (m * g) / Vt
v = 0.0
v_list = []

total_time = float(input("시뮬레이션을 진행할 총 시간:"))
td = 0.1

times = np.arange(0, total_time, td)

# 자유낙하 운동 시뮬레이션
for t in times:
    # 속도 갱신
    v += (g - (K * v * v) / m) * td
    v_list.append(v)

# 그래프 그리기
plt.rcParams['font.family'] ='Malgun Gothic'
plt.plot(times, v_list)
plt.title('자유낙하 운동 속력 vs 시간')
plt.xlabel('시간 (초)')
plt.ylabel('속력 (m/s)')
plt.grid(True)
plt.show()

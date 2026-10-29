<div align="center">

# 🐢 Turtle Bot — Wanderer

**Turtlesim için durmadan gezinen, duvardan akıllıca kaçan ROS 2 düğümü**

![ROS 2](https://img.shields.io/badge/ROS_2-Humble%2B-22314E?logo=ros&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-Apache--2.0-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

</div>

---

## 📖 Hakkında

`turtlebot_wanderer`, [turtlesim](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim.html) simülatöründeki kaplumbağayı **hiç durmadan** hareket ettiren basit bir ROS 2 paketidir.

- 🎲 Güvenli bölgede rastgele hız ve dönüşlerle gezinir.
- 🧱 Duvara yaklaşınca durmadan merkeze doğru yönelir.
- 🚫 `linear.x` her zaman `> 0` — kaplumbağa asla durmaz.
- 🛑 `Ctrl+C` ile kapatılınca kaplumbağayı düzgünce durdurur.

## 🧠 Nasıl Çalışır?

```
        /turtle1/pose ──▶ ┌──────────────┐ ──▶ /turtle1/cmd_vel
        (Pose)            │   Wanderer   │     (Twist)
                          └──────────────┘
```

| Durum | Koşul | Davranış |
|-------|-------|----------|
| 🟢 Güvenli bölge | `2.0 ≤ x, y ≤ 9.0` | Her 1.5–2 sn'de yeni rastgele hız/dönüş |
| 🔴 Duvara yakın | Sınırın dışında | Merkeze (5.5, 5.5) yönel + küçük rastgele sapma |

### ⚙️ Parametreler

| Sabit | Değer | Açıklama |
|-------|-------|----------|
| `SAFE_MIN` / `SAFE_MAX` | 2.0 / 9.0 | Güvenli bölge sınırları |
| `EDGE_LINEAR` | 1.5 | Duvara yakınken ileri hız |
| `TURN_GAIN` | 4.5 | Merkeze dönüş kazancı |
| `RESELECT_MIN/MAX` | 1.5 / 2.0 sn | Rastgele hareketi yenileme aralığı |

## 🚀 Kurulum

**Gereksinimler:** ROS 2, `turtlesim`, Python 3.11

```bash
git clone <repo-url> turtle_bot
cd turtle_bot
colcon build --packages-select turtlebot_wanderer
source install/setup.bash
```

## ▶️ Çalıştırma

**Terminal 1** — Simülatör:
```bash
ros2 run turtlesim turtlesim_node
```

**Terminal 2** — Wanderer:
```bash
source install/setup.bash
ros2 run turtlebot_wanderer wanderer
```

## 📁 Proje Yapısı

```
turtle_bot/
└── src/
    └── turtlebot_wanderer/
        ├── CMakeLists.txt
        ├── package.xml
        └── scripts/
            └── wanderer      # Ana düğüm
```

## 📡 ROS Arayüzü

| Tür | Topic | Mesaj |
|-----|-------|-------|
| Subscribe | `/turtle1/pose` | `turtlesim/msg/Pose` |
| Publish | `/turtle1/cmd_vel` | `geometry_msgs/msg/Twist` |

## 📄 Lisans

Apache-2.0 — detaylar için `package.xml` dosyasına bakın.

---

<div align="center">Made with 🐢 by <b>yldz</b></div>

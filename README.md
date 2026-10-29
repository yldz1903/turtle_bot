<div align="center">

# 🐢 Duvardan Kaçan Kaplumbağa

**ROS 2 Humble · `turtle_duvar_py` · Turtlesim**

![ROS 2](https://img.shields.io/badge/ROS_2-Humble-22314E?logo=ros&logoColor=white)
![Python](https://img.shields.io/badge/Python-rclpy-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-Apache--2.0-green)

</div>

---

## 📖 Hakkında

Bu paket, turtlesim'deki kaplumbağayı ileri sürer ve duvara yaklaştığında **dönerek yön değiştirmesini** sağlar. Konum bilgisi saniyede bir terminale yazdırılır.

| # | Gereksinim | Karşılığı |
|---|-----------|-----------|
| 1 | **Paket** | `turtle_duvar_py` (`rclpy`, `geometry_msgs`, `turtlesim`) |
| 2 | **Abone** | `/turtle1/pose` dinlenir, `x` ve `y` alınır |
| 3 | **Yayıncı** | `/turtle1/cmd_vel` ile ileri sürülür; `x` veya `y` **< 1.0** ya da **> 10.0** ise döner |
| 4 | **Log** | Konum saniyede bir `get_logger().info()` ile yazılır |
| ⭐ | **Bonus** | Hız ve sınır değerleri ROS parametresidir |

## 🧠 Nasıl Çalışır?

```
 /turtle1/pose ──▶ ┌──────────────┐ ──▶ /turtle1/cmd_vel
   (Pose)          │  duvar_node  │      (Twist)
                   └──────────────┘
                          │
                          └──▶ 1 sn'de bir konum logu
```

- **Sınırlar içinde:** `linear_speed` ile düz ileri gider.
- **Sınır dışında** (`x`/`y` < `min_limit` veya > `max_limit`): Merkeze doğru dönerek yön değiştirir.

## ⚙️ Parametreler (Bonus)

| Parametre | Varsayılan | Açıklama |
|-----------|-----------|----------|
| `linear_speed` | `2.0` | İleri hız |
| `angular_speed` | `4.0` | Dönüş hızı |
| `min_limit` | `1.0` | Alt sınır |
| `max_limit` | `10.0` | Üst sınır |

## 🚀 Kurulum

```bash
git clone <repo-url> turtle_bot
cd turtle_bot
colcon build --packages-select turtle_duvar_py
source install/setup.bash
```

## ▶️ Çalıştırma

**Terminal 1** — Simülatör:
```bash
ros2 run turtlesim turtlesim_node
```

**Terminal 2** — Düğüm:
```bash
source install/setup.bash
ros2 run turtle_duvar_py duvar_node
```

Parametrelerle çalıştırma:
```bash
ros2 run turtle_duvar_py duvar_node --ros-args \
  -p linear_speed:=3.0 -p angular_speed:=5.0 -p min_limit:=1.5 -p max_limit:=9.5
```

### Örnek log çıktısı

```
[INFO] [duvar_node]: duvar_node başladı.
[INFO] [duvar_node]: Konum: x=5.54, y=5.54
[INFO] [duvar_node]: Konum: x=7.31, y=5.54
```

## 📸 Ekran Görüntüleri

> Buraya ekran görüntülerini ekle (`images/` klasörüne koyup bağla):

<!--
![Turtlesim](images/turtlesim.png)
![Log çıktısı](images/log.png)
-->

## 📁 Proje Yapısı

```
turtle_bot/
└── src/
    └── turtle_duvar_py/
        ├── package.xml
        ├── setup.py
        ├── setup.cfg
        ├── resource/turtle_duvar_py
        └── turtle_duvar_py/
            ├── __init__.py
            └── duvar_node.py
```

## 📄 Lisans

Apache-2.0

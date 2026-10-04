# ⚔️ 艾尔登法环 · 史诗交界地编年史 (Elden Ring Lore Documentary)

> 基于 **HyperFrames** 框架打造的高画质 1080P 图文并茂电影级剧情介绍视频。

---

## 🎬 视频规格

- **渲染成品**：[`out/elden_ring_lore.mp4`](file:///Users/sym/code/elden-ring-lore-video/out/elden_ring_lore.mp4) (57.5 MB)
- **视频分辨率**：1920 × 1080 (Full HD, 30 FPS, H.264)
- **音频规格**：AAC 48kHz 立体声（史诗氛围底噪 BGM + 深度中文旁白配音）
- **视频时长**：65 秒完整史诗章节

---

## 📖 剧情章节设计 (Storyline Architecture)

1. **Chapter 01 · 纪元破晓：黄金律法与无上意志 (0s - 13s)**
   - 黄金树降临宁姆格福与交界地，永恒女王玛莉卡统治黄金一族。
   - 初始之王葛孚雷征伐四方，将“命定之死”剔除封印于黑剑玛利喀斯体内，缔造永生黄金盛世。
2. **Chapter 02 · 阴谋之夜：黑刀之夜与法环破碎 (13s - 25.5s)**
   - 月之公主菈妮盗走死亡卢恩一角，黑刀刺客暗杀黄金长子葛德文。
   - 悲痛与质疑律法的玛莉卡女王举起石槌，彻底击碎艾尔登法环。
3. **Chapter 03 · 半神争霸：破碎战争与诸神黄昏 (25.5s - 38s)**
   - 半神诸王争夺大卢恩碎片，陷入残酷破碎战争。
   - “碎星”拉塔恩以重力锁死群星命运，与“米凯拉之刃”玛莲妮亚决战盖利德，猩红腐败之花绽放，大地化为焦土。
4. **Chapter 04 · 赐福指引：褪色者归来与火种誓约 (38s - 50.5s)**
   - 半神失格，被放逐的褪色者眼中重燃黄金赐福微光。
   - 指头女巫梅琳娜与灵马托雷特相伴，立下火种之誓，引领褪色者杀破重重险阻直指黄金王城。
5. **Chapter 05 · 宿命抉择：觐见法环与终局抉择 (50.5s - 65s)**
   - 燃烧黄金树，战胜艾尔登之兽，直面交界地终极命运：
     - **艾尔登之王 (Age of Fracture)**：修补法环，登上罗德尔王座。
     - **群星时代 (Age of the Stars)**：追随菈妮斩断神明枷锁，远航冰冷深空。
     - **颠火之王 (Lord of Frenzied Flame)**：混沌烈火焚尽万物因果，熔毁世间一切苦痛。

---

## 🛠 常用指令 (HyperFrames CLI)

在项目目录下：

```bash
# 启动实时预览 Studio (浏览器热更新可交互时间线)
npm run dev

# 静态规范与无障碍、色彩对比度、运行时检查
npm run check

# 重新渲染为 1080P MP4 视频
npm run render

# 截取关键时间点多帧拼版预览图
npx hyperframes snapshot --at 5,18,30,42,55
```

---

## 📂 项目结构

```text
elden-ring-lore-video/
├── index.html                           # 根调度器 (音画轨道同步、动态字幕、全局法环背景)
├── compositions/                        # 模块化分幕子合成
│   ├── scene-golden-order.html          # 第一幕：黄金律法
│   ├── scene-black-knives.html          # 第二幕：黑刀之夜
│   ├── scene-shattering.html            # 第三幕：破碎战争
│   ├── scene-tarnished.html             # 第四幕：褪色者归来
│   └── scene-endings.html               # 第五幕：三大结局抉择
├── assets/                              # 图像与音频资产 (官方概念图 + 电影级纯光学摄影实拍)
│   ├── master_audio.mp3                 # 旁白与环境氛围合成母带音频
│   └── *.png                            # 黄金树、菈妮、女武神、拉塔恩、梅琳娜等高质量原图
├── snapshots/                           # 校验截图及接触印相 (contact-sheet.jpg)
└── out/
    └── elden_ring_lore.mp4              # 65秒 1080P 最终成片
```

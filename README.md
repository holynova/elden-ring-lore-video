# 艾尔登法环 · 交界地编年史

五章节中文剧情短片：从黄金律法、黑刀之夜，到破碎战争与三种结局。

A five-chapter Chinese lore short with chapter navigation and three ending summaries.

[在线体验](https://elden-ring-lore-video.xiaosang.cc/) · [源码](https://github.com/holynova/elden-ring-lore-video)

![艾尔登法环 · 交界地编年史：真实页面截图](./assets/readme/screenshot.png)

## 可以做什么

- 通过页面章节卡片跳转到对应视频时间。
- HyperFrames合成源码与成片一起保存在仓库。

## 观看与工程

打开在线页面播放，或选择章节定位观看。包含主线与结局剧透。

[打开成片](https://elden-ring-lore-video.xiaosang.cc/out/elden_ring_lore.mp4) · [仓库中的视频](./out/elden_ring_lore.mp4)

实测成片：1920 × 1080，30 fps，H.264 + AAC；时长 1:05，文件约 19.6 MiB。

`index.html` 是公开播放器；`composition.html` 与 `compositions/` 保留视频合成源码。旁白和配乐在 `assets/`。

## 本地预览

```bash
python3 -m http.server 8080
```

打开 http://localhost:8080/。播放器直接使用仓库成片，无需先渲染。

如需编辑视频，使用固定版本的 HyperFrames CLI，读取 [工程约定](AGENTS.md)，并从 `composition.html` 合成入口预览。

影视化剧情是作者的剪辑与解释，游戏角色、官方素材及相关商标归各自权利人；这是非官方项目。

<img src="./assets/readme/qr.png" width="144" alt="扫码打开https://elden-ring-lore-video.xiaosang.cc/">

## 发布

```bash
npx --yes wrangler@4.128.0 deploy --dry-run --config wrangler.jsonc
npx --yes wrangler@4.128.0 deploy --config wrangler.jsonc
```

从 `main` 同一提交在本地手动发布到Cloudflare Workers。正式地址：[https://elden-ring-lore-video.xiaosang.cc/](https://elden-ring-lore-video.xiaosang.cc/)。 `.assetsignore` 限定公开播放器/站点资源，排除合成工程、开发文件与未供页面使用的大体积音频/字体。
